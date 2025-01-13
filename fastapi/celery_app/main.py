from tasks import add
import time 


result = add.delay(4, 6)


while not result.ready():
  print(f"Task Status: {result.status}")
  time.sleep(1) 

print(f"Task Result: {result.get()}") 