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

class EventManager:
  '''
  Handles all the event-messaging system
  '''
  
  def __init__ (self):
    self.eventMap = {}
    
  def connect(self, event, method):
    ''' 
    Creates a conection between an user-defined event
    and a method/function to be executed when that event
    be procesed
    '''
    if event not in self.eventMap:
      self.eventMap[event] = []
    self.eventMap[event] += [method]

  def notify(self, event):
    ''' 
    Notifies the ocurrence of an event, calling all the
    methods related to it 
    '''
    if event in self.eventMap:
      for method in self.eventMap[event]:
        method() #call method to handle the event
    else:
      pass #ignore unregistered events
      
