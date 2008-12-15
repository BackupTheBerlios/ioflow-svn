#!/usr/bin/env python
"""  Copyright 2008, Peter Bubestinger and ioflow contributors.
     This file is part of "ioflow".

     Ioflow is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.

     Ioflow is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with Ioflow.  If not, see <http://www.gnu.org/licenses/>.
"""

"""ioflow class implementation draft."""
__version__ = '0.11 - december 3rd, 2008 - 20:00'
__author__ = 'Peter Bubestinger (pb@das-werkstatt.com)'

import logging
from threading import Thread


#----------------------------------------------------------------------------
class TIoFlowObject:
    """Mother of all ioFlow objects.
    
    This class contains fields and methods that all or most ioflow objects
    have in common. The most default fields are "name" and "label".

    fields:
      name -- (string) name handle
      label -- (string) human readable name
    
    """
    _counter = 0
    
    def __init__(self, name="ioflow_object", label="ioFlow Object"):                
        # TODO: have individual, meaningful counters per entitiy.
        # example: hardware_1.button_1, hardware_1.button_2
        TIoFlowObject._counter += 1

        
        logging.debug("[TIoFlowObject] args: %s, %s" % (name, label))
        self.name = "%s_%d" % (name, TIoFlowObject._counter)
        self.label = label
        logging.debug("[TIoFlowObject] fields: %s, %s" % (self.name, self.label))
        


#----------------------------------------------------------------------------
class TPadFilter(TIoFlowObject):
    """Simple flow control and value filtering mechanism."""
    def __init__(self, name="filter", label="Filter", keep_old=0):
        TIoFlowObject.__init__(self, name, label)

        # store previous values. useful for differential filters:
        self.keep_old = keep_old    # (numeric) how many previous values to store.
        self.old = []               # (list of variant) previous values.
 
        
        
    def apply(self, value):
        """(abstract) applies filter to given value.
        
        Default action is to simply return the value unchanged.
        Also stores 'keep_old' number of previous values in 'old' (list).
        
        """
        if self.keep_old > 0:
            # "append" is not used, to have new elements at beginning of list:
            self.old = [value] + self.old
            self.old = self.old[:self.keep_old]    # trim list to max. keep_old entries
        return value



#----------------------------------------------------------------------------
class TGate(TPadFilter):
    """Blocks numeric values outside a given range.
    
    Requires numeric values to work on. String values will always pass.
    
    """
    def __init__(self, name="filter_gate", label="Filter: Gate", 
                 min=0, max=100, type="midpass"):
        TPadFilter.__init__(self, name, label)
        self.min = min        # (numeric)
        self.max = max        # (numeric)
        self.type = type      # (string) [lowpass|midpass|highpass]
        
        
    def apply(self, value):
        """Returns the value if it passes the gate, otherwise returns None."""
        TPadFilter.apply(self, value)
        logging.debug("[TGate]: applying %s (%d %d) %d" % (self.type, self.min, self.max, value))
        
        # TODO: check value type
        if value == None:
            print "filter empty."
            return None
        else:
            if (self.type == "lowpass") and (value <= self.min):
                logging.debug("%s (%d)" % (self.type, value))
                return value
            elif (self.type == "midpass") and ((value >= self.min) and (value <= self.max)):
                logging.debug("%s (%d)" % (self.type, value))
                return value
            elif (self.type == "highpass") and (value >= self.max):
                logging.debug("%s (%d)" % (self.type, value))
                return value
            else:
                # print "blocked"
                return None



#----------------------------------------------------------------------------
class TDelay(TPadFilter):
    """Delays the output of a received value."""
    def __init__(self, name="filter_delay", label="Filter: Delay",
                 duration=500):
        TPadFilter.__init__(self, name, label)
        self.duration = duration        # (numeric) time in msec to wait until propagating the input value.



#----------------------------------------------------------------------------
class TPad(TIoFlowObject):
    def __init__(self, value, name="pad", label="Pad", offset=0, 
                 connects=[], flow="out", type="numeric",
                 keepalive=0, ramping=0, calibrate=False,
                 filters=[], min=0, max=100, precision=2, listener=None):
        TIoFlowObject.__init__(self, name, label)
        self.value = value                      # (variant) current value of data in pad
        self.offset = offset                    # (numeric) +/- offset to add to the value before sending
        self.connects = connects                # (list of TPad) existing connections
        self.flow = flow                        # ([in|out|duplex]) data flow of pad: "sink|source|both"
        self.type = type                        # (numeric|string|xxx) type 
        self.keepalive = keepalive              # (numeric) interval between re-sending of value (in msec)
        self.ramping = ramping                  # (numeric) time delay between 2 values (in msec)
        self.calibrate = calibrate              # (bool) auto calibration on/off
        self.filters = filters                  # (list of TPadFilter) Applied in order of list.
        self.min = min                          # (numeric) lower range limit
        self.max = max                          # (numeric) upper range limit
        self.precision = precision              # (numeric) number of digits after the comma. for floats.
        
        self.listeners = []                     # (list of function) functions to execute upon value change.
        self.add_listener(listener)
        
        self.update_connects()                  # make sure that connection lists are up to date.
        

    def add_listener(self, listener):
        """Add more listener functions to this pad."""
        if listener != None:
            self.listeners.append(listener)
            

    def update_connects(self):
        """Resets and fills local input/outputs lists based on flow of connected pads."""
        self.inputs = []                        # (list of TPad) connections to listen to.
        self.outputs= []                        # (list of TPad) connections to send to.
        
        print "connections of %s:" % self.name
        for pad in self.connects:
            if pad.flow in ["in", "duplex"]:
                print "output %s (%s)" % (pad.label, pad.name)
                self.outputs.append(pad)
            elif pad.flow in ["out", "duplex"]:
                print "input %s (%s)" % (pad.label, pad.name)
                self.inputs.append(pad)
                
    def connect(self, pad):
        """Handle incoming connection requests."""
        
        print "connecting %s to %s..." % (self.name, pad.name)
        if pad in self.connects:    # avoid double connects.
            return False
        else:            
            if (self.flow == pad.flow) and (self.flow != ["duplex"]):
                # TODO: use ioflow-specific exception "EConnectionMismatch"
                print "incompatible pad flow directions"
                return False
            else:
                self.connects.append(pad)
                pad.connects.append(self)
                self.update_connects()
                return True
        
    
    def apply_filters(self, value):
        """Apply the filter chain in order of "self.filters" list."""
        for filter in self.filters:
            value = filter.apply(value)
        return value
    
    def insert_filter(self, filter, position=None):
        if filter != None:
            if position != None:
                self.filters.insert(position, filter)
            else:
                self.filters.append(filter)
            
            
    def auto_calibrate(self, value):
        """Update pads min/max range according to incoming values.
        
        Calibration is mutually exclusive to value conversion, because conversion
        would kick in and disguise exceeding range limits.
        
        A "TypeError" exception is raised if the incoming value has a 
        different datatype, avoiding unpredictable results.
        
        """
        if type(value) != type(self.value):
            raise TypeError, "Value type changed during calibration!"
        
        if value < self.min:
            print "new min: %d" % value
            self.min = value
        if value > self.max:
            print "new max: %d" % value
            self.max = value
            
            
    def convert(self, value, in_min=None, in_max=None):
        """take care of value range/type transformations."""
        # TODO: verify proper conversion. use pydoc-tests?
        # - value conversion (in:min/max > out:min/max)
        if (value != None):
            # - range conversion:
            if (in_min != None) and (in_max != None):
                factor = float(self.max - self.min) / float(in_max - in_min)
                value = (value - in_min) * factor + self.min
            else:
                # We can only call calibration if there is *no* range given:
                if self.calibrate: 
                    self.auto_calibrate(value)
                
            # - type conversion (str, int, float, ...)
            if (type(value) != type(self.value)) and (self.value != None):            
                value = type(self.value)(value)
            
        return value
        

    def send(self):
        """output current value to all connected sinks."""
        for pad in self.outputs:
            pad.recv(self.value, self)


    def recv(self, value, pad=None, min=None, max=None):
        """update current value (triggered by source pads).
        
        Note: min/max are only necessary if a non-pad calls it directly.
        
        """
        # Adjust type, range, etc:
        if isinstance(pad, TPad):
            value = self.convert(value, pad.min, pad.max)
        else:
            if (min != None) and (max != None):
                # we're getting a value supplied from a non-pad:
                value = self.convert(value, min, max)
            else:
                # TODO: evaluate when this happens.
                value = self.convert(value)
            
        # Run it through filters:
        if self.apply_filters(value) != None:
            self.value = value     # If the value made it through, update it
            self.send()            # Propagate it to outputs
            for listener in self.listeners:
                if listener != None:
                    listener(self)    # trigger listener action
        

    def bang(self):
        """trigger re-sending of currently stored value."""
        self.send()
    
    
    
#----------------------------------------------------------------------------
class TPlug(TIoFlowObject):
    """A plug is a group of pads.

    Plugs are making it easier and less cluttered to handle multiple pads at once.
    Furthermore, they're keeping some track about pads they've connected, useful for
    multi-element behavior.

    """
    def __init__(self, name="plug", label="Plug", connects=[], pads=[], 
                 listener=None):
        TIoFlowObject.__init__(self, name, label)
        
        self.active_pads = 0         # (int) number of pads connected.
        
        self.connects = []           # (list of TPlug) sockets this is plug is connected to.
        for plug in connects:
            self.connect(plug)
        
        self.pads = []               # (list of TPad) all the pins in the plug
        self.add_pads(pads)                
        
        self.listeners = []          # (list of function) functions to execute upon value change.
        self.add_listener(listener)
        
        
    def add_listener(self, listener):
        """Add more listener functions to this pad."""
        if listener != None:
            self.listeners.append(listener)
        
    def add_pads(self, pads):
        """Adds more pads to this plug."""
        try:
            for pad in pads:
                self.add_pad(pad)
        except TypeError:
            print "argument 'pads' must be a list!"
            
    def add_pad(self, pad):
        """Add single new pad to this plug."""
        if isinstance(pad, TPad):
            pad.add_listener(self.on_change)    # tell this pad to notify us about its changes.
            self.pads.append(pad)
            
    def on_change(self, pad):
        """listener function that acts upon changes in pads."""
        try:
            index = self.pads.index(pad)
        except ValueError:
            print "pad %s not in plug %s" % (pad.name, self.name)
            
        for listener in self.listeners:
                if listener != None:
                    listener(pad=self, index=index)    # trigger listener action
            
        
    def connect(self, plug):
        """Initiate connection to other plug.
        
        Returns number (int) of valid connections made.
        
        """
        self.connects.append(plug)
        # Currently just connects as many pads as possible by iteration.
        # TODO: Think about use cases that might break this.
        for i in range(0, len(plug.pads)):
            if self.pads[i] != None:
                try:
                    if plug.pads[i].connect(self.pads[i]):
                        self.active_pads += 1
                except:
                    # TODO: handle real ioflow exception.
                    print "incompatible plugs"
                    
        return self.active_pads



#----------------------------------------------------------------------------
class TGroup(TIoFlowObject):
    """Grouping ioflow objects to have a common handle."""
    def __init__(self, name, label, contents=[]):
        self.contents = contents           # could be any type: element, widget, pad, ...



#----------------------------------------------------------------------------
class TElement(TIoFlowObject):
    """Basic interaction elements of hardware devices.

    Notes:
    - "value" is stored in pad(s).
    - type (input/output) is determined by pad(s).

    """
    def __init__ (self, name=None, label=None, pads=[]):
        TIoFlowObject.__init__(self, name, label)
        self.pads = pads               # (list of TPad) type "in/out" is defined by pads
        logging.debug("[TElement] created: \"%s\" (%s)" % (self.label, self.name))
    
    def set_value(self, value, pad_index=0):
        """Triggers a 'receive' event on the given pad and updates the value."""
        self.pads[pad_index].recv(value)
        
    def insert_filter(self, filter, position=0, pad_index=0):
        self.pads[pad_index].insert_filter(filter, position)
        
    def add_pads(self, pads):
        """Add more pads to this element."""
        try:
            for pad in pads:
                self.add_pad(pad)
        except TypeError:
            print "argument 'pads' must be a list!"
            
    def add_pad(self, pad):
        """Adds a single pad to this element (after verifying that it's a pad)."""
        if isinstance(pad, TPad):
            self.pads.append(pad)



#----------------------------------------------------------------------------
class TButton(TElement):
    """Input element with 2 distinct states.

    Typical logical representation of these 2 states are:
    - 0 / 1
    - on / off
    - press / release

    """
    PRESS = 1
    RELEASE = 0
    PAD_OUT = 0
    
    def __init__(self, name="button", label="Button", value=0):
        self.pads = []    # start with no pads
        # --- output pin/pad:        
        pad_out = TPad(value, name="output", label="Button state", offset=0,
                       connects=[], flow="out", type="numeric", 
                       keepalive=0, ramping=0, calibrate=False,
                       filters=[], min=0, max=1, precision=0)
        # TODO: currently no plug is used, but pads directly. check.
        # think about it and check/verify if it's ok.
        self.add_pad(pad_out)
        
        TElement.__init__(self, name, label, self.pads)
        
        
    def press(self):
        self.set_value(TButton.PRESS, TButton.PAD_OUT)
        logging.debug("btn %s (%s) press" % (self.label, self.name))
    
    def release(self):
        self.set_value(TButton.RELEASE, TButton.PAD_OUT)
        logging.debug("btn %s (%s) release" % (self.label, self.name))



#----------------------------------------------------------------------------
class TPixel(TElement):
    """Single output element that can display different colors.

    Typical examples for pixel elements are:
    - LEDs
    - pixels

    """
    PAD_IN = 0
    
    def __init__(self, name="pixel", label="Pixel", value=0x000000):
        #TODO: set pad to use "value" as default.
        # (numeric) color value (24bit: 0xRRGGBB), default: black (0x000000)
        self.pads = []
        pad_in = TPad(value, name="input", label="Pixel color", offset=0,
                      connects=[], flow="in", type="numeric", 
                      keepalive=0, ramping=0, calibration=False,
                      filters=[], min=0, max=0xFFFFFF, precision=0)
        self.add_pad(pad_in)



#----------------------------------------------------------------------------
class TFader(TElement):
    """Input element with a certain value range.

    Typical example for fader elements are:
    - faders, knobs (potentiometers)
    - piano key
    - touch stripes
    - ADC output

    """
    PAD_OUT = 0
    
    def __init__(self, name="fader", label="Fader", value=0, min=0, max=100, 
                 calibrate=False, precision=0):
        self.pads = []
        pad_out = TPad(value, name="output", label="Fader value", offset=0,
                       connects=[], flow="out", type="numeric", 
                       keepalive=0, ramping=0, calibrate=calibrate,
                       filters=[], min=min, max=max, precision=precision)
        self.add_pad(pad_out)
        


#----------------------------------------------------------------------------
class TWidget(TElement):
    """Contain semantic information and specialized functionalities.

    Widgets are the most important part of ioflow. They are small blocks
    that contain closed pieces of logical behavior, making it possible
    to add semantic meaning to ioflow entities.

    Typical example would be:
    - group several leds together to form a VU-meter.
    - group several buttons together to act as a radiogroup.

    """
    
    # TODO: Find a way for handling categories to avoid wild growth. e.g. dictionary?
    def __init__(self, name="widget", label="Widget", pads=[], plugs=[], settings={}, category="all"):
        self.pads = pads                    # (list of TPad) handling single-value connections
        self.plugs = plugs                  # (list of TPlug) handling multi-value connections
        self.settings = settings            # (dictionary) used for configuration and settings
        self.category = category            # (string?) used for distinguishing and grouping different types of widgets

    def add_plug(self, plug):
        """Adds a new plug to this widget."""
        if isinstance(plug, TPlug):
            self.plugs.append(plug)


#----------------------------------------------------------------------------
class THardware(Thread, TIoFlowObject):
    """This entity splits hardware devices into their elements."""
    def __init__(self, name="hardware", label="Hardware"):
        Thread.__init__(self)
        TIoFlowObject.__init__(self, name, label)
        
        self.elements = []                      # (list of TElement) elements gear consists of
        self.groups = []                        # (list of TGroup) Grouping elements for massive assignments and/or better overview of elements
        self.settings = {}                      # (dictionary) contains name/value pairs for device-specific settings
        self.plugs = []                         # (list of TPlug)
        
        
    # TODO: remove add_button/add_fader and use generic "add_element(type)" function.
    #       in order to preserve upwards compatibility with future elements.
    def add_button(self, label="Button", value=0):
        """Create a new button element and add it to this hardware."""
        button = TButton("%s.button" % self.name, label, value)
        self.elements.append(button)
        return button
    
    def add_fader(self, label="Fader", value=0, min=0, max=100, calibrate=False, precision=2):
        """Create a new fader element and add it to this hardware."""
        fader = TFader("%s.fader" % self.name, label=label, value=value, 
                       min=min, max=max, calibrate=calibrate, precision=precision)
        self.elements.append(fader)
        return fader
        

    def get_elements_by_type(self):
        """(list of TElement) returns an list of elements of a given type (e.g. TButton)."""
        pass

    def get_elements_by_group(self): 
        """(list of TElement) returns elements within a given group."""
        pass

    def get_all_groups(self):
        """(list of TGroup) returns all groups."""
        pass

    def get_all_elements(self):
        """(list of TElement) returns all elements regardless of their type."""
        pass
    
    
    
#---------------------------------------------------
def _test_classes():
    print "hello world"
    logging.basicConfig(level=logging.DEBUG)
    


if __name__ == "__main__":
    _test_classes()









