#  config.py
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

class ConfigManager:
  '''
  Loads configurations attributes and provides
  a global way to access them (Singleton)
  '''
  
  configurations = dict()
  
  #~ configurations["resolution"] = (1024, 600)
  configurations["resolution"] = (640, 480)
  #~ configurations["fullscreen"] = True
  configurations["fullscreen"] = False
  
  def __init__(self):
    pass
    
  @classmethod
  def get(self, attr):
    return ConfigManager.configurations[attr]
  
  @classmethod  
  def set(self, key, attr):
    ConfigManager.configurations[key] = attr
