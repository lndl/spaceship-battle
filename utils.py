#  utils.py
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

#  Utils and misc functions. Map color

BLACK = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
GREEN = (0,255,0)
BLUE  = (0,0,255)

import pygame
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


