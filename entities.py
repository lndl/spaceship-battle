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
from circle import Circle

class PlayerShip(EventListener):
  '''
  Player ship class (entity)
  '''
  
  ratioSize = 50
  
  def __init__(self, game, xPos, yPos):
    self.game = game
    self.center = Vector2D(xPos, yPos)
    self.direction = Vector2D(0,7) #Heading to 90 degrees
    self.body = Circle(self.center, PlayerShip.ratioSize)
    self.game.evManager.suscribe(PlayerMoveEvent, self)
    self.game.evManager.suscribe(PlayerRotateEvent, self)
    self.game.evManager.suscribe(PlayerLaserShootEvent, self)

  def moveForward(self):
    self.center += self.direction

  def moveBackward(self):
    self.center -= self.direction
    
  def rotateLeft(self):
    self.direction = self.direction.rotate(10)
    
  def rotateRight(self):
    self.direction = self.direction.rotate(-10)

  def update(self):
    pass

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
  
  def processPlayerLaserShootEvent(self, event):
    self.game.goManager.addLaserObject(self)
    
class EnemyShip:
  '''
  Enemy ship (entity class)
  '''
  
  ratioSize = 50
  
  def __init__(self, game, xPos, yPos):
    self.game      = game
    self.center    = Vector2D(xPos, yPos)
    self.direction = Vector2D(0,-7) #Heading to 270 degrees
    self.body = Circle(self.center, EnemyShip.ratioSize)
    self.laserTimer = 0

  def update(self):
    if self.laserTimer > 100:
      self.game.goManager.addLaserObject(self)
      self.laserTimer  = 0
    else:
      self.laserTimer += 1

class Laser():

  def __init__(self, game, origin, direction):
    self.game      = game
    self.center    = copy(origin)
    self.direction = copy(direction) * 2

  def update(self):
    self.center += self.direction
