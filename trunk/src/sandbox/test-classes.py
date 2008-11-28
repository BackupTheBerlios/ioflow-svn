#!/usr/bin/env python
"""ioflow class implementation draft."""
__version__ = '0.5 - november 28th, 2008 - 14:20'
__author__ = 'Peter Bubestinger (pb@das-werkstatt.com)'

from random import randint


class TIoFlowObject:
    """Mother of all ioFlow objects.
    
    This class contains fields and methods that all or most ioflow objects
    have in common. The most default fields are "name" and "label".

    fields:
      name -- (string) name handle
      label -- (string) human readable name
    
    """
    def __init__(self, name=None, label=None):                
        if (name == None):
            self.name = "IoFlowObject_" + random.randint()
        if (name == None):
            self.label = "Unknown_" + random.randint()
        


class TPadFilter(TIoFlowObject):
    """Simple flow control and value filtering mechanism."""
    def __init__(self, name=None, label=None, input=0, output=0, keep_old=0):
        
        self.name = name        # (string) name handle
        self.label = name        # (string) human readable name
        self.input = input        # (variant) input value
        self.output = output        # (variant) output value

        # store previous values. useful for differential filters:
        self.keep_old = keep_old    # (numeric) how many previous values to store.
        self.old = [input]        # (list of variant) previous values.



class TGate(TPadFilter):
    """Blocks numeric values outside a given range.
    
    Requires numeric values to work on. String values will always pass.
    
    """
    def __init__(self, name=None, label=None, input=0, output=0, min=0, max=100, type="midpass"):
        TPadFilter.__init__(name, label, input, output)
        self.min = min        # (numeric)
        self.max = max        # (numeric)
        self.type = type    # (string) [lowpass|midpass|highpass]



class TDelay(TPadFilter):
    """Delays the output of a received value."""
    def __init__(self, name=None, label=None, input=0, output=0, duration=500):
        TPadFilter.__init__(name, label, input, output)
        self.duration = duration        # (numeric) time in msec to wait until propagating the input value.



class TPad(TIoFlowObject):
    def __init__(self):
        self.name = "pad"                       # (string) name handle for pad
        self.label = "pad"                      # (string) human readable name of pad (useful for labeling "pins")
        self.value = None                       # (variant) current value of data in pad
        self.offset = 0                         # (numeric) +/- offset to add to the value before sending
        self.pads = []                          # (list of TPad) existing connections
        self.inputs = []                        # (list of TPad) connections to listen to (filled once at runtime from "self.pads")
        self.outputs= []                        # (list of TPad) connections to send to (filled once at runtime from "self.pads")
        self.flow = "in"                        # ([in|out|duplex]) data flow of pad: "sink|source|both"
        self.type = "numeric"                   # (numeric|string|xxx) type 
        self.keepalive = 0                      # (numeric) interval between re-sending of value (in msec)
        self.ramping = 0                        # (numeric) time delay between 2 values (in msec)
        self.calibration = False                # (bool) auto calibration on/off
        self.filters = []                       # (list of TPadFilter) Applied in order of list.
        self.min = 0                            # (numeric) lower range limit
        self.max = 100                          # (numeric) upper range limit
        self.precision = 2                      # (numeric) number of digits after the comma. for floats.

    def send(self):
        """output current value to all connected sinks."""
        pass

    def recv(self, value):
        """update current value (triggered by source pads)."""
        pass

    def bang(self):
        """trigger re-sending of currently stored value."""
        pass


class TElement(TIoFlowObject):
    """Basic interaction elements of hardware devices.

    Notes:
    - "value" is stored in pad(s).
    - type (input/output) is determined by pad(s).

    """
    def __init__ (self, name=None, label=None, plugs=[]):
        TIoFlowObject.__init__(name, label)
        self.plugs = plugs                      # (list of TPlug) type "in/out" is defined by pads inside of plug.


class TButton(TElement):
    """Input element with 2 distinct states.

    Typical logical representation of these 2 states are:
    - 0 / 1
    - on / off
    - press / release

    """
    def __init__(self, name="button", label="Button", value=0):
        self.value = value                       # state of button (0..off, 1..on)
        self.plugs = []


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


class THardware(TIoFlowObject):
    """This entity splits hardware devices into their elements."""
    def __init__(self, name, label):
        self.elements = []                      # (list of TElement) elements gear consists of
        self.groups = []                        # (list of TGroup) Grouping elements for massive assignments and/or better overview of elements
        self.settings = {}                      # (dictionary) contains name/value pairs for device-specific settings
        self.plugs = []                         # (list of TPlug)

    def get_elements_by_type():
        """(list of TElement) returns an list of elements of a given type (e.g. TButton)."""
        pass

    def get_elements_by_group(): 
        """(list of TElement) returns elements within a given group."""
        pass

    def get_all_groups():
        """(list of TGroup) returns all groups."""
        pass

    def get_all_elements():
        """(list of TElement) returns all elements regardless of their type."""
        pass












