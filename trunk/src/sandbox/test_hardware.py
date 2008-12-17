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

import test_classes as ioflow
import pygame
import sys
import time
import pypm
import logging


class IOF_WdMidi(ioflow.TWidget):
    """Prototype widget. Outputting MIDI signals."""
    def __init__(self, device_out=0, channel_out=1, device_in=0, channel_in=1):
        ioflow.TWidget.__init__(self, name="midi", label="Midi Widget", category="test")
        pypm.Initialize()
        
        self.device_out = int(device_out)
        self.channel_out = int(channel_out)
        self.device_in = int(device_in)
        self.channel_in = int(channel_in)
        
        self._midi_out = pypm.Output(self.device_out, 20)
        
        self.add_pad(ioflow.TPad(label="Midi Note", value=0, 
                                 flow="in", min=0, max=127,
                                 listener=self.play_note))
        
    def __dealloc__(self):
        pypm.Terminate()
        
    
    def note_on(self, channel, tone, velocity=127):
        cmd = 0x90 + (channel -1)
        self._midi_out.WriteShort(cmd, tone, velocity)

    def note_off(self, channel, tone, velocity=0):
        cmd = 0x80 + (channel -1)
        self._midi_out.WriteShort(cmd, tone, velocity)
    
    def play_note(self, pad=None):
        if isinstance(pad, ioflow.TPad):
            self.note_on(self.channel_out, pad.value)
            time.sleep(1)
            self.note_off(self.channel_out, pad.value)


class IOF_WdTextOut(ioflow.TWidget):
    """Prototype widget. Mainly outputting text to check functionality."""
    pass

    
class IOF_WdRadioBtnGroup(ioflow.TWidget):
    """Prototype widget. Groups buttons together in a radiogroup.
    
    input: several buttons
    output: a value between min/max of output pad
    
    """
    
    def __init__(self, min=0, max=100):
        ioflow.TWidget.__init__(self, name="btnradiogroup", label="Button radio group", category="test")
        # input pads (TODO: create dynamically, on demand of connection. *ouch*)
        # hint: copy objects?
        pad_1 = ioflow.TPad(label="W Btn 1", value=0, flow="in", min=0, max=1)
        pad_2 = ioflow.TPad(label="W Btn 2", value=0, flow="in", min=0, max=1)
        pad_3 = ioflow.TPad(label="W Btn 3", value=0, flow="in", min=0, max=1)
        pad_4 = ioflow.TPad(label="W Btn 4", value=0, flow="in", min=0, max=1)
        pad_5 = ioflow.TPad(label="W Btn 5", value=0, flow="in", min=0, max=1)
        
        # group input pads together in a plug:
        self.add_plug(ioflow.TPlug(name="buttons_in", label="W btn inputs", 
                                   pads=[pad_1, pad_2, pad_3, pad_4, pad_5], 
                                   listener=self.on_change))
        # output pads               
        self.add_pad(ioflow.TPad(label="Value output", flow="out", value=0, 
                                 min=min, max=max, listener=self.print_value))
        
    
    def on_change(self, pad=None, index=None):
        """Trigger action on incoming pad events inside a plug.
        
        This function defines the specific behavior of this widget.
        
        """
        # setting a "raw" value (from non-pad), requires to provide min/max information about source:
        # TODO: hardcoded indices are pure evil. find a better way!
        self.pads[0].recv(index, min=0, max=self.plugs[0].active_pads -1)
        
        
    def print_value(self, pad=None):
        """Dirty debugging function: prints pad values."""
        #TODO: Use IOF_TextOut widget for this!
        print pad.value
    
        

class IOF_HwMouse(ioflow.THardware):
    """Prototype ioflow hardware, using mouse as input device"""
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    
    
    def __init__(self):
        ioflow.THardware.__init__(self, "mouse", "Mouse")
        self.init_buttons()
        self.init_faders()
        self.running = True
        
        # - show off some filtering action (filter_gate):
        gate1 = ioflow.TGate(name="filter_gate", label="X-gate", min=100, type="lowpass")
        gate2 = ioflow.TGate(name="filter_gate", label="Y-gate", min=100, max=200, type="midpass")
        
        self.tfader[self.X_AXIS].insert_filter(gate1)
        self.tfader[self.Y_AXIS].insert_filter(gate2)
        
        self.start()    # run itself as a thread.
        
        
    def init_buttons(self):       
        self.add_elements([ioflow.TButton(label="Left"), 
                           ioflow.TButton(label="Middle"), 
                           ioflow.TButton(label="Right"), 
                           ioflow.TButton(label="Wheel up"), 
                           ioflow.TButton(label="Wheel down")])
        
        self.BTN_LEFT = 1
        self.BTN_RIGHT = 2
        self.BTN_MIDDLE = 3
        self.SCROLL_UP = 4
        self.SCROLL_DOWN = 5
    
        
    def init_faders(self):
        # Note: assigning weird min/max to test auto_calibration.
        self.add_elements([ioflow.TFader(value=0, label="X-axis", min=100, max=0, calibrate=True),
                           ioflow.TFader(value=0, label="Y-axis", min=100, max=0, calibrate=True)])
        
        self.X_AXIS = 0
        self.Y_AXIS = 1
    
    
    def run(self):
        screen = pygame.display.set_mode((IOF_HwMouse.SCREEN_WIDTH, IOF_HwMouse.SCREEN_HEIGHT))
        event = pygame.event.poll() # do this once to init pygame events
        
        while self.running:
            event = pygame.event.wait()
        
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.tbutton[event.button-1].press()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.tbutton[event.button-1].release()
                if event.button == 5:
                    print "good bye!"
                    self.running = False    # QUIT
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                self.tfader[self.X_AXIS].set_value(x)
                self.tfader[self.Y_AXIS].set_value(y)
        
            screen.fill((0, 0, 0))
            pygame.display.flip()
            
            
#---------------------------------------------------
def _test_classes():
    log = logging.getLogger("ioflow")
    log.setLevel(logging.DEBUG)
    # Logging configuration, to stdout in this case
    console = logging.StreamHandler()
    log.addHandler(console)
    
    iof_hw_mouse = IOF_HwMouse()
    iof_wd_radio = IOF_WdRadioBtnGroup(min=0, max=100)
    iof_wd_midi = IOF_WdMidi(device_out=4, channel_out=1)
    
    iof_wd_radio.pads[0].connect(iof_wd_midi.pads[0])
    iof_wd_midi.pads[0].connect(iof_hw_mouse.tfader[0].pads[0])
    iof_wd_midi.pads[0].connect(iof_hw_mouse.tfader[1].pads[0])
    #iof_wd_midi.pads[0].connect(iof_hw_mouse.tbutton[0].pads[0])
    
    mouse_btns = ioflow.TPlug(name="mouse_buttons", label="Mouse buttons")
    # fill plug with pads:
    for i in range(0, 4):
        mouse_btns.add_pad(iof_hw_mouse.tbutton[i].pads[0])
    iof_wd_radio.plugs[0].connect(mouse_btns)
    
    # thread testing:
    while iof_hw_mouse.running:
        sys.stdout.write("X")
        time.sleep(5)


if __name__ == "__main__":
    _test_classes()    





