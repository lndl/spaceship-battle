#  circle.py
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

class Circle:
  '''
  A circle class with collision-detection support
  '''
  
  def __init__(self, center, ratio):
    '''
    Initializes a circle with a ratio (double type)
    and a center (vector type)
    '''
    self.ratio  = ratio
    self.center = center
  
  def isCollidingWith(self, anotherCircle):
    '''
    Test if this circle and other are in collision
    '''
    cA = self.center
    rA = self.ratio
    cB = anotherCircle.center
    rB = anotherCircle.ratio
    return cA.distanceFrom(cB) < (rA + rB)
