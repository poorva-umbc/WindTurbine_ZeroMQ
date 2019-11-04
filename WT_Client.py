import zmq

context = zmq.Context()
print ("Connecting to server...")
port = '5555'
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)

#doing 10 request waiting each time for response

for request in range(12):
    print("sending request %s..." % request)
    socket.send_string(str(request))

# get the reply

    message = socket.recv()
    print ("Recieved reply %s [%s]" % (request,message))