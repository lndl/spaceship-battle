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

WIDTH, HEIGHT = ConfigManager.get("resolution")  
    
class Ship(pygame.sprite.Sprite):
  '''
  Ship class (sprite)
  '''
  
  def __init__ (self):
    pygame.sprite.Sprite.__init__(self)
    self.image = load_image("ship.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = HEIGHT / 2
    self.rect.centery = WIDTH / 2
    self.angle = 90
    self.__initImageCache()
    
  def __initImageCache(self):
    ''' 
    This fragments initialize all the spaceship rotation images
    in order to speed up the performance when driving the ship.
    '''
    self.cachedImages = []
    for angle in range(0,360,10):
      self.cachedImages += [pygame.transform.rotate(self.image, angle)]

  def moveBackward(self):
    # pass
    self.rect.centery += 5
    
  def moveForward(self):
    # pass
    self.rect.centery -= 5

  def __rotate(self, angle):
    old_self_rect_center  = self.rect.center
    old_image_rect_center = self.image.get_rect().center
    #if __debug__:
    #  try: rotated_image = self.cachedImages[angle / 10]
    #  except IndexError: print "Angle crash: %d" % angle
    rotated_image = self.cachedImages[angle / 10]
    new_image_rect_center = rotated_image.get_rect().center
    self.rect.center = (old_self_rect_center[0] + (old_image_rect_center[0] - new_image_rect_center[0]), old_self_rect_center[1] + (old_image_rect_center[1] - new_image_rect_center[1]))

    self.image = rotated_image

  def rotateLeft(self):
    if self.angle < 360 - 10: self.angle += 10
    else: self.angle = 0
    self.__rotate(self.angle)
      
  def rotateRight(self):
    if self.angle > 0: self.angle -= 10
    else: self.angle = 360 - 10
    self.__rotate(self.angle)
