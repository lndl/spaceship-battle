#  sprites.py
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
from vector import Vector2D
from utils  import *

WIDTH, HEIGHT = ConfigManager.get("resolution")  
    
class ShipSprite(pygame.sprite.Sprite):
  '''
  Ship class (sprite)
  '''  

  def __init__(self, entity, image):
    pygame.sprite.Sprite.__init__(self)
    self.entity = entity
    self.image = image
    self.rect  = self.image.get_rect()
    self.iImage = 90 / 10
    self.__initImageCache()
  
  def render(self, screen):
    renderCoord = (self.entity.center.x, 480 - self.entity.center.y)
    self.rect.center = renderCoord
    self.iImage = int(self.entity.direction.angle() / 10)
    self.image = self.cachedImages[self.iImage]
    pygame.draw.rect(screen, RED, self.rect, 2)
    pygame.draw.ellipse(screen, GREEN, self.rect, 2)
    screen.blit(self.image, self.rect)
  
  def __initImageCache(self):
    ''' 
    This fragments initialize all the spaceship rotation images
    in order to speed up the performance when driving the ship.
    '''
    originalRect = self.image.get_rect()
    self.cachedImages = []
    for angle in range(0,360,10):
      rotatedImage = pygame.transform.rotate(self.image, (angle - 90))
      rotatedRect  = rotatedImage.get_rect()
      
      # Derive a Rect that is the same size as the original, but offset just a tad
      # to compensate for the rotation.  Specifically, offset by half of the total
      # growth, because that growth is evenly distributed on both sides of the
      # rotated image.
      clippedRect = pygame.Rect(
        (rotatedRect.width - originalRect.width) / 2,
        (rotatedRect.height - originalRect.height) / 2,
        originalRect.width,
        originalRect.height,
      )
      
      rotatedImage = rotatedImage.subsurface(clippedRect)
      self.cachedImages += [rotatedImage]

class LaserSprite(pygame.sprite.Sprite):

  def __init__(self, entity):
    pygame.sprite.Sprite.__init__(self)
    self.entity = entity
  
  def render(self, screen):
    startLine = (self.entity.center.x, 480 - self.entity.center.y)
    endLine = (startLine[0] + 5, startLine[1] + 5)
    pygame.draw.aaline(screen, GREEN, startLine, endLine)  
  
