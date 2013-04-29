#  game_object.py
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

class GameObject:
  '''
  Game object sums an entity -which manages the logic- 
  and a sprite -which manages the visual representation
  of an object and how it renderize-
  '''
  
  def __init__(self, entity, sprite):
    self.entity = entity
    self.sprite = sprite

  def collidedWith(self, anotherGO):
    ''' 
    Function doc 
    '''
    self.entity.collidedWith(anotherGO.entity)
    
  def isOnCollisionWith(self, anotherGO):
    return self.entity.isOnCollisionWith(anotherGO.entity)

  def update(self):
    self.entity.update()

  def render(self, surface):
    self.sprite.render(surface, self.entity)
