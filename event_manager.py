#  event_manager.py
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

from collections import deque

class EventManager:
  '''
  Handles all the event-messaging system
  '''
  
  def __init__ (self, game):
    self.game       = game
    self.eventQueue = deque()
    self.eventMap   = dict()
    
  def suscribe(self, eventClass, listener):
    ''' 
    Suscribes a listener (by default, an entity) to an
    event ocurrence.
    '''
    if eventClass.__name__ not in self.eventMap:
      self.eventMap[eventClass.__name__] = []
    self.eventMap[eventClass.__name__] += [listener]

  def unsuscribe(self, eventClass, listener):
    '''
    Unsuscribes an listener from an event. 
    '''
    try:
      if listener in self.eventMap[eventClass.__name__]:
        del self.eventMap[eventClass.__name__]
    except KeyError:
      print "WARNING: listener not found in event listener list"
      pass #Ignore the exception

  def notify(self, event):
    ''' 
    Notifies the ocurrence of an event
    '''
    self.eventQueue.append(event)
    
  def processEvents(self):
    ''' 
    Consume the event queue, dispatching all the events
    to the listeners, by using a double-dispatching mechanism
    '''
    while self.eventQueue: #queue is not empty
      e = self.eventQueue.popleft()
      if e.__class__.__name__ in self.eventMap:
        for listener in self.eventMap[e.__class__.__name__]:
          e.dispatch(listener)
      else:
        pass #Ignore no-mapped events (No suscribers for it)
