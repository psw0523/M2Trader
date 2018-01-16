import zmq
import stock_status

host = '127.0.0.1'
port = 5555
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind("tcp://%s:%s" % (host, port))

while True:
    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')

    # Get Stock Info
    d_stock_status = stock_status.get_status(request_str)
    server.send_json(d_stock_status)

