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
from ball import Ball
from config import ConfigManager
from space import Space
from utils import *

class Game:
  '''
  Main game class
  '''
  
  def __init__ (self):
    pygame.init()
    pygame.key.set_repeat(10,10)
    res = ConfigManager.get("resolution")
    self.screen = pygame.display.set_mode(res, pygame.DOUBLEBUF)
    self.ball = Ball()
    self.space = Space(res)
  
  def catchUserInput(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        pygame.quit()
        exit()
      elif e.type == pygame.KEYDOWN:
        if e.key == pygame.K_ESCAPE:
          pygame.quit()
          exit()
        elif e.key == pygame.K_DOWN:
          self.ball.decreaseSpeed()
        elif e.key == pygame.K_UP:
          self.ball.increaseSpeed()
        elif e.key == pygame.K_LEFT:
          self.ball.moveLeft()
        elif e.key == pygame.K_RIGHT:
          self.ball.moveRight()
          
  def updateGameState(self):
    self.ball.updateState() 
  
  def updateDisplay(self):
    self.screen.fill(BLACK)
    self.screen.blit(self.space, self.space.rect)
    self.screen.blit(self.ball.image, self.ball.rect)
    if __debug__:
      #print "Debug mode: Draw sprite's rects"
      pygame.draw.rect(self.screen, WHITE, self.ball.rect, 1)
      #print "Debug mode: Draw statistics"
      font = pygame.font.Font(None, 24)
      speedMsg = "Spaceship speed: " + str(self.ball.speed)
      posMsg = "Spaceship position: " + str(self.ball.rect)
      textS = font.render(speedMsg, 1, GREEN)
      textP = font.render(posMsg, 1, GREEN)
      self.screen.blit(textS, (10,10))
      self.screen.blit(textP, (10,25))
      
    pygame.display.flip()
    pygame.time.wait(1000 / 60)

  def run(self):
    while True:
      self.catchUserInput()
      self.updateGameState()
      self.updateDisplay()
    
if __name__ == "__main__":
  game = Game()
  game.run()
