from random import randint
import logging
import os
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

################################################################################
# Classes 
################################################################################

class clArg:
  def __init__(self, argName, argSpec):
    self.argName = argName
    self.argSpec = argSpec

  def argHelp(self):
    name = self.argName
    spec = self.argSpec
  
    print(str(name), end='')
    lines = spec.split()
    lines = [' '.join(lines[i:i+wordLength]) \
             for i in range(0, len(lines), wordLength)] 

    for i in range(len(lines)): 
      print("\t" + lines[i])
    print() # Formatting.


################################################################################
# Functions
################################################################################

def check(calc, ans):
  # Type safety
  calc = int(calc)
  ans = int(ans)

  if calc == ans:
    print("Answer is {}. Correct!".format(ans))
    return True
  else:
    print("Answer is {}. Incorrect.".format(ans))
    return False
    

def askQuestion(a, b):
  os.system("clear")
  print("{} x {} = ".format(a,b))


def getFileDate():
  string = time.asctime()
  string = string.split(' ')[1:] # Get rid of the spaces and format
  string = '_'.join(string)
  string = string.split(':')
  string = '.'.join(string)
  string = string[0:3] + string[4:] # Format it prettier.
  return string


def main():
  progressIo = "progress.csv"
  f = open(progressIo, "a")

  # Question
  a = randint(1000, 9999)
  b = 2
  askQuestion(a,b)

  t0 = time.time()
  calc = input()
  t1 = time.time()
  speed = t1-t0
  # Reverse the answer and cast it to int for comparison.
  calc = int(calc[::-1]) 

  ans = a*b
  result = check(calc, ans)

  dateT = getFileDate()
  document = ",".join([ str(dateT), str(a),     str(b), 
                        str(ans),   str(calc),  str(result),    
                        str(speed)])
  document += ",\n"
  f.write(document)
  f.close()
  os.system("tail " + str(progressIo))

################################################################################
# IfNEM
################################################################################

if __name__ == "__main__":
  main()

################################################################################
# Notes
################################################################################
# TODO:
# [DONE] Log results.
# System arguments to change the multiplicand and multiplier
# 
