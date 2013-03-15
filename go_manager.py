#  go_manager.py
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

from sprites       import *
from entities      import *
from event_manager import EventManager
from game_object   import GameObject

class GOManager:
  '''
  
  '''
  
  def __init__(self, game):
    self.game = game
    self.gameObjects = []
    self.__createGOs()
    
  def __createGOs(self):
    player = PlayerShip(self.game,100,100)
    enemy  = EnemyShip(self.game,600,400)
    ##TODO: Move out this event suscription
    pss = ShipSprite(load_image("shipP.png"))
    self.game.evManager.suscribe(PlayerRotateEvent, pss)
    self.addGameObject(GameObject(player, pss))
    self.addGameObject(GameObject(enemy,  ShipSprite(load_image("shipE1.png"))))
  
  def addLaserObject(self, source):
    l  = Laser(self.game, source.center, source.direction)
    ls = LaserSprite()
    self.addGameObject(GameObject(l, ls))

  def addGameObject(self, gameObject):
    self.gameObjects.append(gameObject)

  def removeGameObject(self, gameObject):
    self.gameObjects.remove(gameObject) 

  def updateAll(self):
    for go in self.gameObjects:
      go.update()

  def renderAll(self):
    for go in self.gameObjects:
      go.render(self.game.screen)
