import zmq

host = '127.0.0.1'
port = 5555

# Connect M2 Server
context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect("tcp://%s:%s" % (host, port))

# 종목코드
stock_code = 'A003540'
request_bytes = stock_code.encode('utf-8')

# Send Stock Code
client.send(request_bytes)

# Receive Stock Status
d_stock_status = client.recv_json()

# Print Stock Status
for name, val in d_stock_status.items():
    print(name, val)