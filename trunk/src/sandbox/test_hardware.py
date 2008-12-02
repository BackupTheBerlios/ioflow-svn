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


class IOF_WdTextOut(ioflow.TWidget):
    """Prototype widget. Mainly outputting text to check functionality."""
    pass
    
class IOF_WdRadioBtnGroup(ioflow.TWidget):
    """Prototype widget. Groups buttons together in a radiogroup.
    
    input: several buttons
    output: a value between min/max of output pad
    
    """
    
    def __init__(self, min=0, max=100):
        ioflow.TWidget.__init__(self, name="textout", label="Text output", category="test")
        # input pads (TODO: create dynamically, on demand of connection. *ouch*)
        # hint: copy objects?
        pad_1 = ioflow.TPad(label="W Btn 1", value=0, flow="in", min=0, max=1)
        pad_2 = ioflow.TPad(label="W Btn 2", value=0, flow="in", min=0, max=1)
        pad_3 = ioflow.TPad(label="W Btn 3", value=0, flow="in", min=0, max=1)
        pad_4 = ioflow.TPad(label="W Btn 4", value=0, flow="in", min=0, max=1)
        pad_5 = ioflow.TPad(label="W Btn 5", value=0, flow="in", min=0, max=1)
        
        # group input pads together in a plug:
        # FIXME: if pads in connected plugs don't match, conversion fails.
        # In this case, "pad5" is not connected later on, thus distorting the conversion.
        # possible solution: TSocket ?
        plug_in = ioflow.TPlug(name="buttons_in", label="W btn inputs", 
                               pads=[pad_1, pad_2, pad_3, pad_4, pad_5], 
                               listener=self.on_change)
        self.add_plug(plug_in)
        
        # output pads               
        pad_out = ioflow.TPad(label="Value output", flow="out", value=0, min=min, max=max, listener=self.print_value)
        self.add_pad(pad_out)
        
    
    def on_change(self, pad=None, index=None):
        """Trigger action on incoming pad events inside a plug.
        
        This function defines the specific behavior of this widget.
        
        """
        print "btn index: %d" % index # let us know that something happened.
        self.pads[0].recv(index, min=0, max=len(self.plugs[0].pads)-1)
        # TODO: find a way to input raw values into pads, but profit from their internal conversion
        # features without necessity for an intermediate pad (it's ugly).
        # idea: add a "recv_raw(value, min, max)" method to pads. should be sufficient?
        
    def print_value(self, pad=None):
        """Dirty debugging function: prints pad values."""
        print pad.value
    
        

class IOF_HwMouse(ioflow.THardware):
    """Prototype ioflow hardware, using mouse as input device"""
    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    
    def __init__(self):
        ioflow.THardware.__init__(self, "mouse", "Mouse")
        self.init_buttons()
        self.init_faders()
        self.running = 1
        
        # show off some filtering action:
        gate1 = ioflow.TGate(name="filter_gate", label="X-gate", min=100, type="lowpass")
        gate2 = ioflow.TGate(name="filter_gate", label="Y-gate", min=100, max=200, type="midpass")
        
        self.faders[self.X_AXIS].insert_filter(gate1)
        self.faders[self.Y_AXIS].insert_filter(gate2)
        
        self.start()    # run itself as a thread.
        
        
    def init_buttons(self):
        self.buttons = [self.add_button("Left"), 
                        self.add_button("Middle"), 
                        self.add_button("Right"), 
                        self.add_button("Wheel up"), 
                        self.add_button("Wheel down")]
        
        self.BTN_LEFT = 1
        self.BTN_RIGHT = 2
        self.BTN_MIDDLE = 3
        self.SCROLL_UP = 4
        self.SCROLL_DOWN = 5
    
        
    def init_faders(self):
        self.faders = [self.add_fader("X-axis", 0, min=0, max=IOF_HwMouse.SCREEN_WIDTH),
                       self.add_fader("Y-axis", 0, min=0, max=IOF_HwMouse.SCREEN_HEIGHT)]
        
        self.X_AXIS = 0
        self.Y_AXIS = 1
    
    
    def run(self):
        screen = pygame.display.set_mode((IOF_HwMouse.SCREEN_WIDTH, IOF_HwMouse.SCREEN_HEIGHT))
        event = pygame.event.poll() # do this once to init pygame events
        
        while self.running:
            event = pygame.event.wait()
        
            if event.type == pygame.QUIT:
                self.running = 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.buttons[event.button-1].press()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.buttons[event.button-1].release()
                if event.button == 5:
                    print "good bye!"
                    self.running = 0    # QUIT
            elif event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                self.faders[self.X_AXIS].set_value(x)
                self.faders[self.Y_AXIS].set_value(y)
        
            screen.fill((0, 0, 0))
            pygame.display.flip()
            
            
#---------------------------------------------------
def _test_classes():
    iof_hw_mouse = IOF_HwMouse()
    iof_wd_radio = IOF_WdRadioBtnGroup(min=0, max=100)
    
    mouse_btns = ioflow.TPlug(name="mouse_buttons", label="Mouse buttons")
    # fill plug with pads:
    for i in range(0, 4):
        mouse_btns.add_pad(iof_hw_mouse.buttons[i].pads[0])
    iof_wd_radio.plugs[0].connect(mouse_btns)
    
    # thread testing:
    while iof_hw_mouse.running:
        sys.stdout.write("X")
        time.sleep(5)


if __name__ == "__main__":
    _test_classes()    





