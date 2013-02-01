#  vector.py
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

import math

class Vector2D:
  '''
  A 2D math vector to represental several geometrics and physics
  concepts 
  '''
  
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    
  @classmethod
  def fromPoint(clz, pointTuple):
    return Vector2D(pointTuple[0], pointTuple[1])
  
  def toPoint(self):
    ''' 
    Returns a built-in tuple representation of vector
    '''
    return (self.x, self.y)
    
  def __add__(self, other):
    ''' 
    + operator 
    '''
    return Vector2D(self.x + other.x, self.y + other.y)
    
  def __sub__(self, other):
    ''' 
    - operator 
    '''
    return Vector2D(self.x - other.x, self.y - other.y)
    
  def __iadd__(self, other):
    ''' 
    += operator 
    '''
    self.x += other.x
    self.y += other.y
    return self
    
  def __isub__(self, other):
    ''' 
    -= operator 
    '''
    self.x -= other.x
    self.y -= other.y
    return self
    
  def magnitude(self):
    ''' 
    Length or magnitude
    '''
    return math.sqrt((self.x ** 2) + (self.y ** 2))
  
  def rotate(self, angle):
    ''' 
    Returns a new rotated vector with certain angle
    '''
    radAngle = angle * math.pi / 180
    rotX = math.cos(radAngle) * self.x - math.sin(radAngle) * self.y
    rotY = math.sin(radAngle) * self.x + math.cos(radAngle) * self.y
    return Vector2D(rotX, rotY) 
  
  def invX(self):
    ''' 
    Return a new vector with x coordinate inverted 
    '''
    return Vector2D(-self.x, self.y)
    
  def __str__(self):
    ''' 
    String representation
    '''
    return "Vector2D: " + "( " + str(self.x) + " , " + str(self.y) + " )"
