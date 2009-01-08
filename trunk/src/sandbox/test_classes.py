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
__version__ = '0.15 - january 7th, 2009 - 22:40'
__author__ = 'Peter Bubestinger (pb@das-werkstatt.com)'

import logging
from threading import Thread
import thread    # TODO: threading & thread: ok?
import time

log = logging.getLogger("ioflow")



#----------------------------------------------------------------------------
class TIoFlowObject:
    """Mother of all ioFlow objects.
    
    This class contains fields and methods that all or most ioflow objects
    have in common. The most default fields are "name" and "label".

    fields:
      name -- (string) name handle
      label -- (string) human readable name
      parent -- (TIoFlowObject) parent of this object
      index -- (integer) index count within scope of this object
    
    """
    _instances = 0
    _by_name = {}
    
    
    def __init__(self, name="ioflow_object", label="ioFlow Object", 
                 parent=None, index=None):
        TIoFlowObject._instances += 1    # count ioflow instances.
        
        self.name = name
        self.label = label
        self.parent = parent
        
        if index == None:
            self.__class__._instances += 1
            index = self.__class__._instances
        self.index = index
        
        log.debug("created [%s]: %s, %s, %d", self.__class__.__name__, self.name, self.label, self.index)
        
        
    def welcome(self, parent, siblings):
        """Introduces this ioflow object into a certain hierarchical structure.
        
        This method assigns the object's parent and a useful index, based
        on the number of existing items in 'siblings'.
        
        arguments:
          parent -- parent object
          siblings -- list of entities of same class type in same hierarchy.
        
        """
        self.parent = parent
        self.index = len(siblings) + 1
        log.info("Added '%s'[%s] as '%s' to %s", 
                 self.label, self.__class__.__name__, self.get_name(level=0), 
                 parent.get_name(labeled=True))


    def get_name(self, level=30, labeled=False, typed=False):
        """Returns naming information for this object.
        
        arguments:
          level -- (integer) max. levels of hierarchy to display.
          labeled -- (boolean) include label
          typed -- (boolean) include class name
        
        """
        name = "%s_%d" % (self.name, self.index)
        if labeled:
            name = "%s(%s)" % (name, self.label)
        if typed:
            name = "%s[%s]" % (name, self.__class__.__name__)
        
        if (level > 0) and (self.parent != None):
            name = "%s.%s" % (self.parent.get_name(level=level-1, labeled=labeled), name)
        return name



#----------------------------------------------------------------------------
class TIoFlowHandler(TIoFlowObject):
    """Container for dynamically created ioFlow objects.
    
    Mainly intended to provide an access method by name.
    TODO: Is this really a clever thing to have? 
    Only works for the first hierarchy level. What about the others?
    alternatives: 
    - "byname()" method per object: is even more uncomfortable.
    - global "byname(xxx.get_name())" function that accepts a full tree string. hm....?
    
    """
    def __init__(self):
        pass
    
    
    def add(self, object):
        if isinstance(object, TIoFlowObject):
            # naming method 1:
            setattr(self, object.get_name(level=0), object)    
            log.info("Added object %s", object.get_name(level=0))
            
            # naming method 2:
            classname = object.__class__.__name__
            try:
                classgroup = getattr(self, classname)
            except AttributeError:
                setattr(self, classname, [])
                classgroup = getattr(self, classname)
            classgroup.append(object)
            
            
    def by_name(self, fullname):
        """Return instance of object, matching given name."""
        names = fullname.split('.')
        level = 0
        object = None
        
        for name in names:
            level += 1
            # TODO: implement this.
            print "(%d) %s" % (level, name)
            
        return object


#----------------------------------------------------------------------------
class TPadFilter(TIoFlowObject):
    """Simple flow control and value filtering mechanism."""
    def __init__(self, name="filter", label="Filter", 
                 parent=None, index=None, 
                 keep_old=0):
        TIoFlowObject.__init__(self, name, label, parent, index)

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
                 parent=None, index=None, 
                 min=0, max=100, type="midpass"):
        TPadFilter.__init__(self, name, label, parent, index)
        self.min = min        # (numeric)
        self.max = max        # (numeric)
        self.type = type      # (string) [lowpass|midpass|highpass]
        
        
    def apply(self, value):
        """Returns the value if it passes the gate, otherwise returns None."""
        TPadFilter.apply(self, value)
        
        # TODO: check value type
        if value == None:
            # log.debug("filter empty: %s", self.get_name())
            return None
        else:
            if (self.type == "lowpass") and (value <= self.min):
                log.debug("%s (%d)" % (self.type, value))
                return value
            elif (self.type == "midpass") and ((value >= self.min) and (value <= self.max)):
                log.debug("%s (%d)" % (self.type, value))
                return value
            elif (self.type == "highpass") and (value >= self.max):
                log.debug("%s (%d)" % (self.type, value))
                return value
            else:
                # print "blocked"
                return None



#----------------------------------------------------------------------------
class TDelay(TPadFilter):
    """Delays the output of a received value."""
    def __init__(self, name="filter_delay", label="Filter: Delay",
                 parent=None, index=None, 
                 duration=500):
        TPadFilter.__init__(self, name, label, parent, index)
        self.duration = duration        # (numeric) time in msec to wait until propagating the input value.



#----------------------------------------------------------------------------
class TPad(Thread, TIoFlowObject):
    _instances = 0
    
    
    def __init__(self, value, name="pad", label="Pad", 
                 parent=None, index=None, 
                 offset=0, 
                 connects=None, flow="out", type="numeric",
                 keepalive=0, ramping=0, calibrate=False,
                 filters_pre=None, filters_post=None, 
                 min=0, max=100, precision=2, listener=None):
        TIoFlowObject.__init__(self, name, label, parent, index)
        Thread.__init__(self, name=name)
        
        # initialize list and dict arguments:
        if connects == None: connects = []
        if filters_pre == None: filters_pre = []
        if filters_post == None: filters_post = []
        
        self.value = value                      # (variant) current value of data in pad
        self.offset = offset                    # (numeric) +/- offset to add to the value before sending
        self.connects = connects                # (list of TPad) existing connections
        self.flow = flow                        # ([in|out|duplex]) data flow of pad: "sink|source|both"
        self.type = type                        # (numeric|string|xxx) type 
        self.calibrate = calibrate              # (bool) auto calibration on/off
        self.min = min                          # (numeric) lower range limit
        self.max = max                          # (numeric) upper range limit
        self.precision = precision              # (numeric) number of digits after the comma. for floats.
        
        self.filters_pre = filters_pre          # (list of TPadFilter) Applied in order of list.
        self.filters_post = filters_post        # (list of TPadFilter) Applied in order of list.
        
        self.keepalive = keepalive -1           # initializing it with wrong value to trigger thread activation.
        self.set_keepalive(keepalive)           # (numeric) interval between re-sending of value (in msec)
        self.ramping = ramping                  # (numeric) time delay between 2 values (in msec)
        self._running = False                   # (boolean) used to start/stop a pad-thread.
        
        self.listeners = []                     # (list of function) functions to execute upon value change.
        self.add_listener(listener)
        
        self.update_connects()                  # make sure that connection lists are up to date.
        
        
    def run(self):
        """Thread routine. If necessary, a pad will start its own thread."""
        return
        # FIXME: find a way to control threading pads.
        # Currently, this thread will never stop.
        while self._running:
            # Take care of re-sending the current value:
            if self.keepalive > 0:
                self.send()
                time.sleep(self.keepalive / 1000)    # convert from msec to seconds.
        
    
    def copy(self, label=None):
        """Create a copy instance of this pad. 
        
        The following things are *not* copied, but initialized empty:
         - connects
         - listeners
        
        """
        connects = []      # do *not* copy connections
        listener = None    # do *not* copy listener assignments (good idea?)
        
        if label == None:
            label = self.label
    
        # TODO: take care of index and name for new instance.
        return TPad(self.value, self.name, label, self.parent, self.index,
                    self.offset, connects, self.flow, self.type, 
                    self.keepalive, self.ramping, self.calibrate,
                    self.filters_pre, self.filters_post, 
                    self.min, self.max, self.precision, listener)
    
        
    def set_ramping(self, delay):
        """Time delay (in msec) between 2 values. Used for interpolation."""
        # TODO: implement this
        # problem: Initial idea was to use "keepalive" for transmitting
        # intermediate values of ramping, but there might be a case where you don't want
        # to use keepalive, but *do* want ramping.
        pass
        
        
    def set_keepalive(self, delay):
        """Update the delay (in msec) between re-sending the current value."""
        if (delay > 0) and (delay != self.keepalive):
            self.keepalive = delay
            if not(self._running):
                self._running = True
                self.start()
        

    def add_listener(self, listener):
        """Add more listener functions to this pad."""
        if listener != None:
            self.listeners.append(listener)
            

    def update_connects(self):
        """Resets and fills local input/outputs lists based on flow of connected pads."""
        self.inputs  = []                       # (list of TPad) connections to listen to.
        self.outputs = []                       # (list of TPad) connections to send to.
        
        if len(self.connects) > 0:
            log.debug("connections of %s:" % self.get_name())
            
        for pad in self.connects:
            if pad.flow in ["in", "duplex"]:
                log.debug(" < output %s (%s)" % (pad.label, pad.name))
                self.outputs.append(pad)
            elif pad.flow in ["out", "duplex"]:
                log.debug(" > input %s (%s)" % (pad.label, pad.name))
                self.inputs.append(pad)
                
                
    def connect(self, pad):
        """Handle incoming connection requests."""
        
        log.info("connecting %s to %s...", self.get_name(), pad.get_name())
        if pad in self.connects:    # avoid double connects.
            return True             # but treat it like a successful connection.
        else:            
            if (self.flow == pad.flow) and (self.flow != ["duplex"]):
                # TODO: use ioflow-specific exception "ConnectionError"
                log.error("incompatible pad flow directions: %s, %s", self.flow, pad.flow)
                return False
            else:
                self.connects.append(pad)
                self.update_connects()
                pad.connects.append(self)
                pad.update_connects()
                return True
        
    
    def apply_filters(self, value, filters=None):
        """Apply the filter chain in order of 'filters' list."""
        if filters == None:
            filters = self.filters_post
        
        for filter in filters:
            value = filter.apply(value)
        return value
    
    
    def insert_filter(self, filter, filters=None, position=None):
        """Insert a filter at a certain position in a given filter chain."""
        if filters == None:
            filters = self.filters_post
            
        if filter != None:
            filter.welcome(self, filters)
            
            if position != None:
                filters.insert(position, filter)
            else:
                filters.append(filter)
                
    def insert_filter_pre(self, filter, position=None):
        self.insert_filter(filter, self.filters_pre, position)
        
    def insert_filter_post(self, filter, position=None):
        self.insert_filter(filter, self.filters_post, position)
        
        
    def auto_calibrate(self, value):
        """Update pads min/max range according to incoming values.
        
        Calibration is mutually exclusive to value conversion, because conversion
        would kick in and disguise exceeding range limits.
        
        A "TypeError" exception is raised if the incoming value has a 
        different datatype, in order to avoid unpredictable results.
        
        """
        if type(value) != type(self.value):
            raise TypeError("Value type changed during calibration!")
        
        if value < self.min:
            # print "new min: %d" % value
            self.min = value
        if value > self.max:
            # print "new max: %d" % value
            self.max = value
            

    def is_number(self):
        """Returns True if pad's value is numeric. False if otherwise."""
        try:
            return(self.value - 0)
        except:
            return False
    
            
    def convert(self, value, in_min=None, in_max=None):
        """take care of value range/type transformations."""
        # TODO: verify proper conversion. use pydoc-tests?
        # - value conversion (in:min/max > out:min/max)
        if (value != None):
            # - range conversion:
            if (in_min != None) and (in_max != None):
                try:
                    factor = float(self.max - self.min) / float(in_max - in_min)
                except ZeroDivisionError:
                    log.info("convert: Division by Zero. %d %d %d %d", self.max, self.min, in_max, in_min)
                    factor = float(0)
                except:
                    log.error("Conversion error in %s:",
                                self.get_name(level=5), exc_info=True)
                    
                else:
                    value = (value - in_min) * factor + self.min
            elif(self.is_number()):
                # We can only call calibration if there is *no* range given,
                # and if the value *is* numeric:
                if self.calibrate: 
                    self.auto_calibrate(value)
                
            # - type conversion (str, int, float, ...)
            if (type(value) != type(self.value)) and (self.value != None):
                try:        
                    value = type(self.value)(value)
                except ValueError:
                    log.warning("Automated value type conversion impossible between '%s' and '%s'",
                                type(self.value).__name__, type(value).__name__, exc_info=True)
            
        return value
        

    def send(self):
        """output current value to all connected sinks."""
        for pad in self.outputs:
            pad.recv(self.value, self)


    def recv(self, value, pad=None, min=None, max=None):
        """update current value (triggered by source pads).
        
        Note: min/max are only necessary if a non-pad calls it directly.
        
        """
        # pre-conversion filtering:
        value = self.apply_filters(value, filters=self.filters_pre)
        if value != None:
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
                
            # post-conversion filtering:
            value = self.apply_filters(value, filters=self.filters_post)
            if value != None:
                self.value = value     # If the value made it through, update it
                self.send()            # Propagate it to outputs
                for listener in self.listeners:
                    if listener != None:
                        thread.start_new_thread(listener, tuple([self]))    # trigger listener action
        

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
    def __init__(self, name="plug", label="Plug", 
                 parent=None, index=None, 
                 connects=None, pads=None, 
                 listener=None):
        TIoFlowObject.__init__(self, name, label, parent, index)
        
        self.active_pads = 0         # (int) number of pads connected.
        
        if connects == None: connects = []
        if pads == None: pads = []
        
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
        
            
    def add_pad(self, pad):
        """Add single new pad to this plug."""
        if isinstance(pad, TPad):
            pad.add_listener(self.on_change)    # tell this pad to notify us about its changes.
            # pad.welcome(self, self.pads)
            self.pads.append(pad)
            
            
    def add_pads(self, pads):
        """Adds more pads to this plug."""
        try:
            for pad in pads:
                self.add_pad(pad)
        except TypeError:
            log.error("argument 'pads' must be a list!")
        
            
    def on_change(self, pad):
        """listener function that acts upon changes in pads."""
        try:
            index = self.pads.index(pad)
        except ValueError:
            print "pad %s not in plug %s" % (pad.name, self.get_name())
            
        for listener in self.listeners:
                if listener != None:
                    # trigger listener action:
                    thread.start_new_thread(listener, tuple([self, index]))
            
        
    def connect(self, incoming):
        """Initiate connection to other plug.
        
        Returns number (int) of valid connections made.
        
        """
        log.debug("connecting plug '%s':", self.get_name())
        try:
            pads_in = incoming.pads
        except AttributeError:
            if type(incoming) == list:
                pads_in = incoming
            else:
                pads_in = [incoming]
           
        self.connects.append(incoming)
        # Currently just connects as many pads as possible by iteration.
        # TODO: Think about use cases that might break this.
        
        """
        Damn!! Plugs should be able to handle different types of incoming connections:
          - plug / [pad, pad, ...] / pad
        That's not the problem, but the behavior must be defined.
        Each new connection will spawn a new pad within the plug if necessary.
        Disconnecting a pad will also remove it from the plug.
        """ 
        
        diff = len(pads_in) - len(self.pads)
        for i in range(diff):
            # more pads coming in than we could handle. We must create some.
            # The first pad in our plug will be our "prototype":
            self.add_pad(self.pads[0].copy())
        
        for i in range(0, len(pads_in)):
            if type(pads_in[i]) == TPad:
                try:
                    if pads_in[i].connect(self.pads[i]):
                        self.active_pads += 1
                except:
                    # TODO: handle real ioflow exception.
                    print "incompatible plugs"
                    
        return self.active_pads



#----------------------------------------------------------------------------
class TGroup(TIoFlowObject):
    """Grouping ioflow objects to have a common handle."""
    def __init__(self, name, label, 
                 parent=None, index=None, contents=None):
        TIoFlowObject.__init__(self, name, label, parent, index)
        
        # initialize list and dict arguments:
        if contents == None: contents = []
        self.contents = contents           # could be any type: element, widget, pad, ...



#----------------------------------------------------------------------------
class TElement(TIoFlowObject):
    """Basic interaction elements of hardware devices.

    Notes:
    - "value" is stored in pad(s).
    - type (input/output) is determined by pad(s).

    """
    def __init__ (self, name=None, label=None, 
                  parent=None, index=None, pads=None):
        TIoFlowObject.__init__(self, name, label, parent, index)
        # initialize list and dict arguments:
        if pads == None: pads = []
        self.pads = pads               # (list of TPad) type "in/out" is defined by pads
    
    
    def set_value(self, value, pad_index=0):
        """Triggers a 'receive' event on the given pad and updates the value."""
        self.pads[pad_index].recv(value)
    
        
    def insert_filter_pre(self, filter, position=0, pad_index=0):
        self.pads[pad_index].insert_filter_pre(filter, position)
        
    def insert_filter_post(self, filter, position=0, pad_index=0):
        self.pads[pad_index].insert_filter_post(filter, position)
        
        
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
            pad.welcome(self, self.pads)
            self.pads.append(pad)



#----------------------------------------------------------------------------
class TButton(TElement):
    """Input element with 2 distinct states.

    Typical logical representation of these 2 states are:
    - 0 / 1
    - on / off
    - press / release

    """
    _instances = 0
    
    PAD_OUT = 0
    
    PRESS = 1
    RELEASE = 0
    
    
    def __init__(self, value=None, name="button", label="Button",
                 parent=None, index=None):
        TElement.__init__(self, name, label, parent, index, pads=[])
        
        if value == None:
            value = self.__class__.RELEASE
            
        # --- output pin/pad:        
        self.add_pad(TPad(value, name="output", label="Button state", offset=0,
                       connects=[], flow="out", type="numeric", 
                       keepalive=0, ramping=0, calibrate=False,
                       filters_pre=[], filters_post=[], 
                       min=0, max=1, precision=0))
        # TODO: currently no plug is used, but pads directly. check.
        # think about it and check/verify if it's ok.
        
        
    def press(self):
        self.set_value(TButton.PRESS, TButton.PAD_OUT)
        log.debug("btn %s (%s) press" % (self.label, self.get_name()))
    
    
    def release(self):
        self.set_value(TButton.RELEASE, TButton.PAD_OUT)
        log.debug("btn %s (%s) release" % (self.label, self.get_name()))



#----------------------------------------------------------------------------
class TPixel(TElement):
    """Single output element that can display different colors.

    Typical examples for pixel elements are:
    - LEDs
    - pixels

    """
    PAD_IN = 0
    
    BLACK = 0x000000
    RED = 0xFF0000
    GREEN = 0x00FF00
    BLUE = 0x0000FF
    WHITE = 0xFFFFFF
    
    
    def __init__(self, value=None, name="pixel", label="Pixel",
                 parent=None, index=None):
        TElement.__init__(self, name, label, parent, index, pads=[])
        
        if value == None:
            # (numeric) color value (24bit: 0xRRGGBB), default: black (0x000000)
            value = TPixel.BLACK
        
        self.add_pad(TPad(value, name="input", label="Pixel color", offset=0,
                      connects=[], flow="in", type="numeric", 
                      keepalive=0, ramping=0, calibration=False,
                      filters_pre=[], filters_post=[], 
                      min=0, max=0xFFFFFF, precision=0))



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
    
    
    def __init__(self, value=None, name="fader", label="Fader", 
                 parent=None, index=None, 
                 min=0, max=100, calibrate=False, precision=0):
        TElement.__init__(self, name, label, parent, index, pads=[])
        
        if value == None:
            value = 0
            
        self.add_pad(TPad(value, name="output", label="Fader value", offset=0,
                       connects=[], flow="out", type="numeric", 
                       keepalive=0, ramping=0, calibrate=calibrate,
                       filters_pre=[], filters_post=[], min=min, max=max, precision=precision))
        


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
    _instances = 0
    
    
    # TODO: Find a way for handling categories to avoid wild growth. e.g. dictionary?
    def __init__(self, name="widget", label="Widget", 
                 parent=None, index=None, 
                 pads=None, plugs=None, settings=None, category="all"):
        # initialize list and dict arguments:
        if pads == None: pads = []
        if plugs == None: plugs = []
        if settings == None: settings = {}
            
        TElement.__init__(self, name, label, parent, index, pads=pads)
        self.plugs = plugs                  # (list of TPlug) handling multi-value connections
        self.settings = settings            # (dictionary) used for configuration and settings
        self.category = category            # (string?) used for distinguishing and grouping different types of widgets


    def add_plug(self, plug):
        """Adds a new plug to this widget."""
        if isinstance(plug, TPlug):
            plug.welcome(self, self.plugs)
            self.plugs.append(plug)



#----------------------------------------------------------------------------
class THardware(Thread, TIoFlowObject):
    """This entity splits hardware devices into their elements."""
    
    _instances = 0
    
    def __init__(self, name="hardware", label="Hardware", 
                 parent=None, index=None):
        Thread.__init__(self)
        TIoFlowObject.__init__(self, name, label, parent, index)
        
        self.elements = []                      # (list of TElement) elements gear consists of
        self.groups = []                        # (list of TGroup) Grouping elements for massive assignments and/or better overview of elements
        self.settings = {}                      # (dictionary) contains name/value pairs for device-specific settings
        self.plugs = []                         # (list of TPlug)
        
        
    def add_element(self, element):
        """Assign element to hardware and create corresponding lists."""
        if not(isinstance(element, TElement)):
            log.warn("non-element passed to '%s.add_element()'." % self.get_name())
            return None
        else:
            elements = self.get_elements_by_type(element.__class__, create=True)
            element.welcome(self, elements)
            
            elements.append(element)
            self.elements.append(element)
            return element
        
        
    def add_elements(self, elements):
        """Assign multiple elements to hardware."""
        for element in elements:
            self.add_element(element)


    def get_elements_by_type(self, type, create=False):
        """(list of TElement) returns an list of elements of a given type (e.g. TButton)."""
        classname = type.__name__.lower()
        try:
            elements = getattr(self, classname)
        except:
            if not(create):
                log.info("No elements of type %s in %s." \
                          % (classname, self.get_name()))
                elements = None
            else:
                log.info("First element of type %s in %s." \
                          % (classname, self.get_name()))
                setattr(self, classname, [])           # initialize this attribute.
                elements = getattr(self, classname)    # and try again.
        return elements


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


if __name__ == "__main__":
    _test_classes()









