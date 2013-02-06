#  entities.py
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

import pygame

from copy   import copy
from events import *
from utils  import *
from vector import Vector2D

class PlayerShip(EventListener):
  '''
  Player ship class (entity)
  '''
  
  def __init__(self, xPos, yPos):
    self.center = Vector2D(xPos, yPos)
    self.direction = Vector2D(0,5) #Heading to 90 degrees

  def moveForward(self):
    self.center += self.direction

  def moveBackward(self):
    self.center -= self.direction
    
  def rotateLeft(self):
    self.direction = self.direction.rotate(10)
    
  def rotateRight(self):
    self.direction = self.direction.rotate(-10)

  # Event Listener: interface implementation

  def processPlayerMoveEvent(self, event):
    if event.isForward():
      self.moveForward()
    elif event.isBackward():
      self.moveBackward()

  def processPlayerRotateEvent(self, event):
    if event.isLeft():
      self.rotateLeft()
    elif event.isRight():
      self.rotateRight()
  
class Laser():
  
  def __init__(self, origin, direction):
    self.center    = copy(origin)
    self.direction = copy(direction)

  def update(self):
    self.center += self.direction
