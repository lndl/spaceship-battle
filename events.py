#  event.py
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

class EventListener:
  '''
  A event listener is an interface for all those entities who 
  wants to react to events generated in the game. 
  '''
  
  def processPlayerMoveEvent(self, event):
    pass
  
  def processPlayerRotateEvent(self, event):
    pass  

class Event:
  
  def dispatch(self, listener):
    raise NotImplementedError("Please, implement \"dispach\" method")

class PlayerMoveEvent(Event):
  
  FORWARD  = 1
  BACKWARD = 2
  
  def __init__(self, where):
    self.where = where
  
  def isForward(self):
    return self.where == PlayerMoveEvent.FORWARD
    
  def isBackward(self):
    return self.where == PlayerMoveEvent.BACKWARD
    
  def dispatch(self, listener):
    listener.processPlayerMoveEvent(self)
  
class PlayerRotateEvent(Event):

  LEFT  = 1
  RIGHT = 2
  
  def __init__(self, where):
    self.where = where
  
  def isLeft(self):
    return self.where == PlayerRotateEvent.LEFT
    
  def isRight(self):
    return self.where == PlayerRotateEvent.RIGHT

  def dispatch(self, listener):
    listener.processPlayerRotateEvent(self)

class LaserShootEvent(Event):
  
  def __init__(self, source):
    self.source = source
  
  def dispatch(self, listener):
    listener.processLaserShootEvent(self)
