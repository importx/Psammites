import sys
sys.path.append('./Testing')

from sessionsQuery import *

if __name__ =="__main__":
  print(sessionsQuery(startTime="500000000", stopTime="600000000"))