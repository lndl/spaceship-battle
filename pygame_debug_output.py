#  pygame_debug_output.py
#  
#  Copyright 2013 Lautaro <laudleon@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from collections import deque
from utils       import *

import pygame.font

class PygameDebugOutput:
  '''
  Renders debug messages over the Pygame display
  '''
  
  __instance = None
  
  @classmethod
  def instance(cls):
    if cls.__instance is None:
      cls.__instance = PygameDebugOutput((10,10))
    return cls.__instance
  
  def __init__ (self, msgInitCoord):
    self.font     = pygame.font.Font(None, 18)
    self.msgQueue = deque()
    self.msgInit  = msgInitCoord 

  def log(self, msg):
    ''' 
    attach a message to output to pygame display
    '''
    text = self.font.render(msg, 1, RED)
    self.msgQueue.append(text)

  def render(self, screenToBlit):
    '''
    render the queues messages over a screen
    '''
    i = 0
    while self.msgQueue:
      msg = self.msgQueue.popleft()
      blitCoord = (self.msgInit[0], self.msgInit[1] + i)
      screenToBlit.blit(msg, blitCoord)
      i += 10
