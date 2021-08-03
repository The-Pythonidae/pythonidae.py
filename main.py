import os
import time
import json
# Starter modules just in case

def clear(): # Prob won't need this ;)
  os.system('clear')
  
def cmd(command):
  try:
    os.system(str(command))
  except:
    exit()

# Pretty much an example function for module. 
