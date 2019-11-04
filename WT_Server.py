import time
import zmq
import pandas as pd
import numpy as np


data = pd.read_csv("windturbine_80790.csv", sep=';')
# windturbine = data.loc[data['Wind_turbine_name'] == 'R80790']
# windturbine_final = windturbine.loc[:,(col for col in windturbine.columns if 'Ws_avg' in col)]
#print(data['Ws_avg'].iloc[7])
port = '5555'
connect = zmq.Context()
socket = connect.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)
while True:

    message = socket.recv()
    print("Recieved  Request: %s" % message)

    time.sleep(1)
    socket.send_string(str(data['Ws_avg'].iloc[int(message)]))

