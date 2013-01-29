#  ball.py
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
from pygame.locals import *
import os

def load_image(filename, transparent=False):
  try: 
    image = pygame.image.load(os.path.join('images', filename))
    #image = image.convert()
    #if transparent:
    #  color = image.get_at((0,0))
    #  image.set_colorkey(color, RLEACCEL)
    return image
  except pygame.error, message:
    print "Fallo la carga de una imagen"
    raise SystemExit, message
  
# Resolutions
HEIGHT = 480
WIDTH = 640
  
class Ball(pygame.sprite.Sprite):
  '''
  Ball class (sprite)
  '''
  
  def __init__ (self):
    pygame.sprite.Sprite.__init__(self)
    self.image = load_image("ship.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = HEIGHT / 2
    self.rect.centery = WIDTH / 2
    self.speed = 10
    self.dir = "UP"

  def increaseSpeed(self):
    self.speed += 1
    
  def decreaseSpeed(self):
    self.speed -= 1

  def moveLeft(self):
    if self.rect.centerx > 0:
      self.rect.centerx -= 5
      
  def moveRight(self):
    if self.rect.centerx < WIDTH:
      self.rect.centerx += 5

  def updateState(self):
    if self.dir == "UP":
      if self.rect.centery > 0:
        self.rect.centery -= self.speed
      else:
        #change direction
        self.dir = "DOWN"
        self.rect.centery += self.speed
    else:
      if self.rect.centery < HEIGHT:
        self.rect.centery += self.speed
      else:
        #change direction
        self.dir = "UP"
        self.rect.centery -= self.speed
       
