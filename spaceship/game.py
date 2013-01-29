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
from ball import *

def catchUserInput(game):
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      pygame.quit()
      exit()
    elif e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()
      elif e.key == pygame.K_DOWN:
        game["ball"].decreaseSpeed()
      elif e.key == pygame.K_UP:
        game["ball"].increaseSpeed()
      elif e.key == pygame.K_LEFT:
        game["ball"].moveLeft()
      elif e.key == pygame.K_RIGHT:
        game["ball"].moveRight()
        
def updateGameState(game):
  game["ball"].updateState() 

def updateDisplay(game):
  game["screen"].fill((0,0,0))
  game["screen"].blit(game["ball"].image, game["ball"].rect)
  if __debug__:
    #print "Debug mode: Draw sprite's rects"
    pygame.draw.rect(game["screen"], (255,255,255), game["ball"].rect, 1)
  pygame.display.flip()
  pygame.time.wait(1000 / 60)

def buildGame():
  pygame.init()
  pygame.key.set_repeat(10,10)
  res = (640, 480)
  game = dict()
  game["screen"] = pygame.display.set_mode(res, pygame.DOUBLEBUF)
  game["ball"] = Ball()
  return game
  
def main():
  game = buildGame()
  while True:
    catchUserInput(game)
    updateGameState(game)
    updateDisplay(game)
    
main()
