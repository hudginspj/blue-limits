import time
import xSimData
import collectorv3 as col

import socket
import sys
from threading import Thread

nextPoint = None

DISABLE = True


def threaded_function():
    global nextPoint
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    server_address = ('localhost', 3000)
    #print >>sys.stderr, 'starting up on %s port %s' % server_address
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print ('connection from', client_address)

            # Receive the data in small chunks and retransmit it
            #while True:
            # data = b'some-pattern'
            while True:
                time.sleep(0.5)
                # point = xSimData.nextPoint()
                outputArr = [
                    nextPoint[1]['mode'],
                    nextPoint[1]['TEMP2'],
                    nextPoint[1]['ACCELX']
                ]
                print(outputArr)
                data = (str(outputArr) + '\n').encode('utf-8')
                connection.send(data)
            # if data:
            #     print('sending data back to the client')
            #     connection.send(data)
            # else:
            #     print  ('no more data from', client_address)
            break
        #except KeyboardInterrupt as e:
            #raise e
        except Exception as e:
            print(e)
            pass        
        finally:
            # Clean up the connection
            connection.close()
            print("connection closed by server")

if not DISABLE:
    thread = Thread(target = threaded_function)
    thread.start()