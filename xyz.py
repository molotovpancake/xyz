def main(): 
  import random
  import time
  from time import sleep
  from random import randint
  
  rn = randint(0, 9)
  
  ui = input("What is your name? ")
  sleep(0.1)
  print ("hi, "+ ui)
  sleep(0.5)
  print ("Let's play a game.")
  sleep(0.1)
  print ("I'll think of a number between zero and nine, inclusive.")
  sleep(0.1)
  print ("Your goal is to guess that number in three attempts.")
  print (rn)
  sleep(0.4)

  msg = ["Take a guess. ", "Guess again. ", "Take another guess. ", "Nope. "]

  end = False
  i = 0
  while end == False:
    sleep(0.1)
    ui = input (msg [i])
    i = randint(1, len(msg)-1)
    try:
      ui = int(ui)
      if rn == ui:
        print ("Correct! Goodbye.")
        sleep(0.1)
        break
      else:
        if ui < rn:
          print ("Less.")
        else:
          pass
    except:
      print ("That's not a number.")
main()
