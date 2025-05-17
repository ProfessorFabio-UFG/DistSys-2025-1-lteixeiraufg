import zmq
from constPS import *

context = zmq.Context()
s = context.socket(zmq.SUB)
s.connect("tcp://" + HOST + ":" + PORT)
s.setsockopt_string(zmq.SUBSCRIBE, "WEATHER")

for i in range(5):
    msg = s.recv()
    print("WEATHER subscriber recebeu:", msg.decode())
