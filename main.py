import robot
import style

print(style.blankAll)
robot1 = robot.robot()

while True:
  print ('ACTIONs: rotate, forward, backward, status')
  action = input ("initiating prompt: type ACTION: ")
  print(style.blankAll)
  robot1.do(action)
  input("PRESS ENTER TO CONTINUE")
  print(style.blankAll)