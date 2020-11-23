import socket
import time

host = ''
port = 9000
locaddr = (host, port)

# Create a UDP socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

# command mode
socket.sendto('command'.encode('utf-8'), tello_address)

time.sleep(3)

# takeoff
socket.sendto('takeoff'.encode('utf-8'), tello_address)

time.sleep(3)

# land
socket.sendto('land'.encode('utf-8'), tello_address)
