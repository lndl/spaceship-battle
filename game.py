#  game.py
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

import pygame

from events        import *
from sprites       import *
from entities      import *
from utils         import *

from event_manager import EventManager
from config        import ConfigManager
from space         import Space


class Game:
  '''
  Main game class
  '''
  
  RES  = ConfigManager.get("resolution")
  
  def __init__ (self):
    pygame.init()
    pygame.key.set_repeat(10,10)
    # Read and set fullscreen view
    isFS = ConfigManager.get("fullscreen")
    if isFS: FSFlag = pygame.HWSURFACE | pygame.FULLSCREEN
    else:    FSFlag = 0
    self.screen = pygame.display.set_mode(Game.RES, pygame.DOUBLEBUF | FSFlag)
    self.__createEntities()
    self.__setEventWireline()
    
  def __createEntities(self):
    self.ship = Ship()
    self.sprites = [ShipSprite(self.ship)]
    self.space = Space(Game.RES)
    
  def __setEventWireline(self):
    self.eventManager = EventManager()
    self.eventManager.connect(KeyPressedUp,    self.ship.moveForward)
    self.eventManager.connect(KeyPressedDown,  self.ship.moveBackward)
    self.eventManager.connect(KeyPressedLeft,  self.ship.rotateLeft)
    self.eventManager.connect(KeyPressedRight, self.ship.rotateRight)
    
  def catchUserInput(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()
        exit()
    keysPressedList = pygame.key.get_pressed()
    if keysPressedList[pygame.K_DOWN]:
      self.eventManager.notify(KeyPressedDown)
    if keysPressedList[pygame.K_UP]:
      self.eventManager.notify(KeyPressedUp) 
    if keysPressedList[pygame.K_LEFT]:
      self.eventManager.notify(KeyPressedLeft) 
    if keysPressedList[pygame.K_RIGHT]:
      self.eventManager.notify(KeyPressedRight)

  def updateGameState(self):
    pass
    
  def updateDisplay(self):
    self.screen.fill(BLACK)
    self.screen.blit(self.space, self.space.rect)
    for sprite in self.sprites:
      sprite.render(self.screen)
    pygame.display.flip()
    # pygame.display.update(self.ship.rect)
    pygame.time.wait(1000 / 60)

  def run(self):
    while True:
      self.catchUserInput()
      self.updateGameState()
      self.updateDisplay()
    
if __name__ == "__main__":
  game = Game()
  game.run()
