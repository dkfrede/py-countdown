import time
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
  
def start():
  start = input("Type start to start the countdown \n")
  countdownTime = int(input("What should the timer start to be? \n"))
  if start == "start":
    while True:
        if countdownTime != 0:
          cls()
          print(countdownTime)
          countdownTime = countdownTime -1
  
          time.sleep(1)
        else:
          cls()
          print("Times up!")
          input("Press any button to reset \n")
          cls()
          start()
start()
