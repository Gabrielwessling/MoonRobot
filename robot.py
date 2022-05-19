class robot:
  maxBattery = int(100)
  battery = int(maxBattery)
  def do(self, action):
    if action == "rotate":
      angle = int(input("input the ANGLE of the rotation: "))
      print ("rotating " + str(angle) + "º degrees")
      self.battery -= 10
      print ("this ACTION has drained 10 battery")
    elif action == "forward":
      print("going FORWARD a meter")
      self.battery -= 10
      print ("this ACTION has drained 10 battery")
    elif action == "backward":
      print("going BACKWARD a meter")
      self.battery -= 10
      print ("this ACTION has drained 10 battery")
    elif action == "status":
      print("this module has " + str(self.battery) + " remaining battery")
    else:
      print ("error")