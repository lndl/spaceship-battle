#  shapes.py
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

from vector import Vector2D

class Shape:
  
  def isCollidingWith(self, aShape):
    raise NotImplementedError("Missing dispatching collision shape method")
  
  def isCollidingWithCircle(self, aCircle):
    raise NotImplementedError("Missing circle-colliding shape method")
  
  def isCollidingWithLine(self, aLine):
    raise NotImplementedError("Missing line-colliding shape method")

class Circle(Shape):
  '''
  A circle class with collision-detection support
  '''
  
  def __init__(self, center, radius):
    '''
    Initializes a circle with a ratio (double type)
    and a center (vector type)
    '''
    self.radius  = radius
    self.center = center
  
  def __str__(self):
    ''' 
    String representation
    '''
    return "Circle: (Center = %s, Radius = %.2f)" % (self.center, self.radius)
  
  def isCollidingWith(self, aShape):
    return aShape.isCollidingWithCircle(self)
  
  def isCollidingWithCircle(self, aCircle):
    '''
    Test if this circle and other are in collision
    '''
    cA = self.center
    rA = self.radius
    cB = aCircle.center
    rB = aCircle.radius
    return cA.distanceFrom(cB) < (rA + rB)

  def isCollidingWithLine(self, aLine):
    '''
    Test if this circle and a line are in collision
    FIXME: This is a fast and naive collision detection method, but not
    very acurate. May be add a discriminant mechanism or something... 
    '''
    return ( (aLine.start.distanceFrom(self.center) < self.radius) or
              (aLine.start.distanceFrom(self.center) < self.radius) ) 

class Line(Shape):
  
  def __init__(self, start, end):
    self.start = start
    self.end   = end
  
  def slope(self):
    return (float(self.end.y - self.start.y) / 
            float(self.end.x - self.start.x))

  def yOrigin(self):
    return (self.start.y - self.slope() * self.start.x)

  def isCollidingWith(self, aShape):
    return aShape.isCollidingWithLine(self)

  def isCollidingWithCircle(self, aCircle):
    # Calling back to circle detection system
    return aCircle.isCollidingWithLine(self)
    
  def isCollidingWithLine(self, aLine):
    return False
