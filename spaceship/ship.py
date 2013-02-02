#  ship.py
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

from config import ConfigManager
from utils import *
from vector import Vector2D

WIDTH, HEIGHT = ConfigManager.get("resolution")  
    
class Ship(pygame.sprite.Sprite):
  '''
  Ship class (sprite)
  '''
  
  def __init__ (self):
    pygame.sprite.Sprite.__init__(self)
    self.image = load_image("ship.png")
    self.rect = self.image.get_rect()
    self.center = Vector2D(HEIGHT / 2, WIDTH / 2)
    self.rect.center = self.center.toPoint()
    self.direction = Vector2D(0,5) #Heading to 90 degrees
    self.iImage = 90 / 10
    self.__initImageCache()
    
  def __initImageCache(self):
    ''' 
    This fragments initialize all the spaceship rotation images
    in order to speed up the performance when driving the ship.
    '''
    self.cachedImages = []
    for angle in range(0,360,10):
      self.cachedImages += \
      [pygame.transform.rotate(self.image, (angle - 90))]

  def moveForward(self):
    self.center += self.direction.invY()
    self.rect.center = self.center.toPoint()

  def moveBackward(self):
    self.center -= self.direction.invY()
    self.rect.center = self.center.toPoint()
    
  def rotateLeft(self):
    self.iImage = (self.iImage + 1) % (360 / 10)
    self.direction = self.direction.rotate(10)
    self.image = self.cachedImages[self.iImage]
    
  def rotateRight(self):
    self.iImage = (self.iImage - 1) % (360 / 10)
    self.direction = self.direction.rotate(-10)
    self.image = self.cachedImages[self.iImage]
