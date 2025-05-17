import zmq, time
from constPS import * #-

context = zmq.Context()
s = context.socket(zmq.PUB)        # create a publisher socket
p = "tcp://"+HOST+":"+ PORT      # how and where to communicate
s.bind(p)                          # bind socket to the address

while True:
    current_time = "TIME " + time.asctime()
    current_date = "DATE " + time.strftime("%Y-%m-%d")
    weather = "WEATHER " + "Sunny 25°C"

    s.send_string(current_time)
    s.send_string(current_date)
    s.send_string(weather)

    print("Publicadas mensagens para todos os tópicos.")
    time.sleep(5)
