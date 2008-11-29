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
from threading import Thread

class IOF_HwMouse(Thread, ioflow.THardware):    
    def __init__(self):
        Thread.__init__(self)
        ioflow.THardware.__init__(self, "mouse", "Mouse")
        self.init_buttons()
        self.running = 1
        
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
    
    
    def run(self):
        screen = pygame.display.set_mode((640, 480))
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
                # sys.stdout.write(".")
                x, y = event.pos
        
            screen.fill((0, 0, 0))
            pygame.display.flip()
            
            
#---------------------------------------------------
def _test_classes():
    iof_hw_mouse = IOF_HwMouse()
    iof_hw_mouse.start()
    
    while iof_hw_mouse.running:
        sys.stdout.write("X")
        time.sleep(5)


if __name__ == "__main__":
    _test_classes()    





