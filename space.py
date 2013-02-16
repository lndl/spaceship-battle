#  space.py
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
from utils import *

class Space(pygame.Surface):
  '''
  Space class creates the space background
  '''
  
  def __init__ (self, resolution):
    pygame.Surface.__init__(self, resolution)
    self.starsSprites =  []
    # self.starsSprites += [load_image("star1.png")] #ugly image
    self.starsSprites += [load_image("star2.png")]
    self.rect = self.get_rect()
    self.__populateSpace()
    
  def __populateSpace (self):
    ''' 
    Fills space with random stars sprites
    !!! Future improves: Implements a slot-based randomize mechanism to
    prevent stars sprites overlapping
    '''
    import random
    xStarsCoord = random.sample(range(0,self.rect.w), 20)
    yStarsCoord = random.sample(range(0,self.rect.h), 20)
    for xy in zip(xStarsCoord,yStarsCoord):
      iStar = random.randint(0, len(self.starsSprites)-1)
      self.blit(self.starsSprites[iStar], xy)
