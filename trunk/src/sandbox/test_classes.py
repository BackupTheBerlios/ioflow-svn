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
__version__ = '0.7 - november 29th, 2008 - 15:18'
__author__ = 'Peter Bubestinger (pb@das-werkstatt.com)'

from random import randint
import logging


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
                print self.type
                return value
            elif (self.type == "midpass") and ((value >= self.min) and (value <= self.max)):
                print self.type
                return value
            elif (self.type == "highpass") and (value >= self.max):
                print self.type
                return value
            else:
                # print "blocked"
                return None



class TDelay(TPadFilter):
    """Delays the output of a received value."""
    def __init__(self, name="filter_delay", label="Filter: Delay",
                 duration=500):
        TPadFilter.__init__(self, name, label)
        self.duration = duration        # (numeric) time in msec to wait until propagating the input value.



class TPad(TIoFlowObject):
    def __init__(self, name="pad", label="Pad", value=None, offset=0, 
                 connects=[], flow="out", type="numeric", 
                 keepalive=0, ramping=0, calibration=False,
                 filters=[], min=0, max=100, precision=2):
        TIoFlowObject.__init__(self, name, label)
        self.value = value                      # (variant) current value of data in pad
        self.offset = offset                    # (numeric) +/- offset to add to the value before sending
        self.connects = connects                # (list of TPad) existing connections
        self.flow = flow                        # ([in|out|duplex]) data flow of pad: "sink|source|both"
        self.type = type                        # (numeric|string|xxx) type 
        self.keepalive = keepalive              # (numeric) interval between re-sending of value (in msec)
        self.ramping = ramping                  # (numeric) time delay between 2 values (in msec)
        self.calibration = calibration          # (bool) auto calibration on/off
        self.filters = filters                  # (list of TPadFilter) Applied in order of list.
        self.min = min                          # (numeric) lower range limit
        self.max = max                          # (numeric) upper range limit
        self.precision = precision              # (numeric) number of digits after the comma. for floats.
        
        self.update_connects()
        


    def update_connects(self):
        """Resets and fills local input/outputs lists based on flow of connected pads."""
        self.inputs = []                        # (list of TPad) connections to listen to.
        self.outputs= []                        # (list of TPad) connections to send to.
        
        for pad in self.connects:
            if pad.flow in ["in", "duplex"]:
                self.inputs.append(pad)
            elif pad.flow in ["out", "duplex"]:
                self.outputs.append(pad)
                    
    
    def filters_apply(self, value):
        """Apply the filter chain in order of "self.filters" list."""
        for filter in self.filters:
            value = filter.apply(value)
        return value
        

    def send(self):
        """output current value to all connected sinks."""
        for pad in self.outputs:
            pad.recv(self.value)


    def recv(self, value):
        """update current value (triggered by source pads)."""        
        # TODO: run through conversion
        # Run it through filters:
        if self.filters_apply(value) != None:
            self.value = value # If the value made it through, update it
            self.send()    # Propagate it to outputs
        

    def bang(self):
        """trigger re-sending of currently stored value."""
        self.send()
    
    
    
class TPlug(TIoFlowObject):
    """A plug is a group of pads.

    Plugs are making it easier and less cluttered to handle multiple pads at once.

    """
    def __init__(self, name=None, label=None, connects=[], pads=[]):
        TIoFlowObject.__init__(name, label)
        self.connects = connects           # (list of TPlug) sockets this is plug is connected to.
        self.pads = pads                   # (list of TPad) all the pins in the plug



class TGroup(TIoFlowObject):
    """Grouping ioflow objects to have a common handle."""
    def __init__(self, name, label, contents=[]):
        self.contents = contents           # could be any type: element, widget, pad, ...



class TElement(TIoFlowObject):
    """Basic interaction elements of hardware devices.

    Notes:
    - "value" is stored in pad(s).
    - type (input/output) is determined by pad(s).

    """
    def __init__ (self, name=None, label=None, plugs=[]):
        TIoFlowObject.__init__(self, name, label)
        self.plugs = plugs                      # (list of TPlug) type "in/out" is defined by pads inside of plug.
        logging.debug("[TElement] created: \"%s\" (%s)" % (self.label, self.name))



class TButton(TElement):
    """Input element with 2 distinct states.

    Typical logical representation of these 2 states are:
    - 0 / 1
    - on / off
    - press / release

    """
    PRESS = 1
    RELEASE = 0
    
    def __init__(self, name="button", label="Button", value=0):
        TElement.__init__(self, name, label)
        self._init_plugs()

        
    def _init_plugs(self):
        """Initialize plugs and pads of the button.
        
        Called once by the __init__ function.
        
        """
        self.plugs = []    # start with an empty plug
        
        # --- output pin/pad:        
        pad_out = TPad(name="state", label="State", value=0, offset=0,
                       connects=[], flow="out", type="numeric", 
                       keepalive=0, ramping=0, calibration=False,
                       filters=[], min=0, max=1, precision=0)
        # TODO: currently no plug is used, but pads directly.
        self.plugs.append(pad_out)
        
    def press(self):
        self.plugs[0].recv(TButton.PRESS)
        print "btn %s (%s) press" % (self.label, self.name)
    
    def release(self):
        self.plugs[0].recv(TButton.RELEASE)
        print "btn %s (%s) release" % (self.label, self.name)


class TPixel(TElement):
    """Single output element that can display different colors.

    Typical examples for pixel elements are:
    - LEDs
    - pixels

    """
    def __init__(self, name="pixel", label="Pixel", value=0x000000):
        self.value = value                # (numeric) color value (24bit: 0xRRGGBB), default: black (0x000000)
        self.plugs = []


class TFader(TElement):
    """Input element with a certain value range.

    Typical example for fader elements are:
    - faders, knobs (potentiometers)
    - piano key
    - touch stripes
    - ADC output

    """
    def __init__(self, name="fader", label="Fader", value=0, min=0, max=100):
        self.value = value                       # (numeric) value of fader
        # TODO: set min/max in pads within plug:
        self.plugs = []




class TWidget(TIoFlowObject):
    """Contain semantic information and specialized functionalities.

    Widgets are the most important part of ioflow. They are small blocks
    that contain closed pieces of logical behavior, making it possible
    to add semantic meaning to ioflow entities.

    Typical example would be:
    - group several leds together to form a VU-meter.
    - group several buttons together to act as a radiogroup.

    """
    def __init__(self, name=None, label=None, plugs=[], settings={}, category="all"):
        self.plugs = plugs
        self.settings = settings            # (dictionary) used for configuration and settings
        self.category = category            # (string?) used for distinguishing and grouping different types of widgets




class THardware(TIoFlowObject):
    """This entity splits hardware devices into their elements."""
    def __init__(self, name, label):
        TIoFlowObject.__init__(self, name, label)
        self.elements = []                      # (list of TElement) elements gear consists of
        self.groups = []                        # (list of TGroup) Grouping elements for massive assignments and/or better overview of elements
        self.settings = {}                      # (dictionary) contains name/value pairs for device-specific settings
        self.plugs = []                         # (list of TPlug)
        
        
    def add_button(self, label="Button", state=0):
        """Create a new button element and add it to this hardware.        
        """
        button = TButton("%s.button" % self.name, label)
        self.elements.append(button)
        return button
        

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









