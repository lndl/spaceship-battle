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
from shapes import *

class GameEntity(EventListener):
  
  def __init__(self, game, center, direction, body):
    self.game = game
    self.center = center
    self.direction = direction
    self.body = body

  def isOnCollisionWith(self, anotherEntity):
    return self.body.isCollidingWith(anotherEntity.body)

  def collidedWith(self, anotherEntity):
    raise NotImplementedError("Missing collision action")

  def update(self):
    ''' 
    Not mandatory the entity update
    '''
    pass

class PlayerShip(GameEntity):
  '''
  Player ship class (entity)
  '''
  
  ratioSize = 50
  
  def __init__(self, game, xPos, yPos):
    super(PlayerShip, self).__init__(game, 
          Vector2D(xPos, yPos), Vector2D(0,5), 
          Circle(Vector2D(xPos, yPos), PlayerShip.ratioSize))
    
    self.game.evManager.suscribe(PlayerMoveEvent, self)
    self.game.evManager.suscribe(PlayerRotateEvent, self)
    self.game.evManager.suscribe(PlayerLaserShootEvent, self)
    self.game.evManager.suscribe(LaserCollisionEvent, self)
    self.game.evManager.suscribe(EnemyCollisionEvent, self)

  def moveForward(self):
    self.center += self.direction

  def moveBackward(self):
    self.center -= self.direction
    
  def rotateLeft(self):
    self.direction = self.direction.rotate(10)
    
  def rotateRight(self):
    self.direction = self.direction.rotate(-10)
    
  def collidedWith(self, anotherEntity):
    self.game.evManager.notify(PlayerCollisionEvent(self, anotherEntity))

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

class EnemyShip(GameEntity):
  '''
  Enemy ship (entity class)
  '''
  
  ratioSize = 50
  
  def __init__(self, game, xPos, yPos):
    super(EnemyShip, self).__init__(game, 
          Vector2D(xPos, yPos), Vector2D(0,-1),
          Circle(Vector2D(xPos, yPos), EnemyShip.ratioSize))
    self.game.evManager.suscribe(PlayerCollisionEvent, self)
    self.game.evManager.suscribe(LaserCollisionEvent,  self)
    self.laserTimer = 0

  def update(self):
    if self.laserTimer > 100:
      #self.game.goManager.addLaserObject(self)
      self.laserTimer  = 0
    else:
      self.laserTimer += 1
  
  def collidedWith(self, anotherEntity):
    self.game.evManager.notify(EnemyCollisionEvent(self, anotherEntity))
  
  def processLaserCollisionEvent(self, event):
    print "Un Laser choco contra el enemigo"
  
  def processPlayerCollisionEvent(self, event):
    print "El jugador humando choco contra el enemigo"
  
class Laser(GameEntity):

  def __init__(self, game, origin, direction):
    super(Laser, self).__init__(game, 
          copy(origin), copy(direction) * 2, 
          Line(origin, origin + direction))

  def update(self):
    self.center += self.direction
    
  def collidedWith(self, anotherEntity):
    self.game.evManager.notify(LaserCollisionEvent(self, anotherEntity))
