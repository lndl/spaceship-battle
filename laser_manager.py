#  laser_manager.py
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

from events   import *
from entities import * 
from sprites  import *

class LaserManager(EventListener):
  
  def __init__(self, game):
    self.game = game
    self.laserEntities = []
    self.laserSprites = []
    #Auto-suscribes to Laser Shoot Event
    self.game.eventManager.suscribe(LaserShootEvent, self)
    
  def createLaser(self, source):
    l  = Laser(source.center, source.direction)
    self.laserEntities += [l]
    ls = LaserSprite(l)
    self.laserSprites += [ls]
    
  def processLaserShootEvent(self, event):
    self.createLaser(event.source)

  def updateLasers(self):
    for l in self.laserEntities:
      l.update()
  
  def renderLasers(self):
    for l in self.laserSprites:
      l.render(self.game.screen)
