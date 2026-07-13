from djitellopy import tello

drone = tello.Tello()
drone.connect()

print(drone.get_battery())
print(drone.VS_UDP_IP)
print(drone.VS_UDP_PORT)
print(drone.TIME_BTW_COMMANDS)
print(drone.RESPONSE_TIMEOUT)

drone.end()