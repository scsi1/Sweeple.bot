import os, time, random


while True:
  time.sleep(60*60*24)
  file = os.remove(random.choice(os.chdir(f"{os.getcwd()}/uploads")))
  print(f"DEBUG: Removed {file}")