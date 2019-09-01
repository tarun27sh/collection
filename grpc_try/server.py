import grpc
from concurrent import futures
import time

import calc_pb2
import calc_pb2_grpc
import calc

class CalculatorService(calc_pb2_grpc.CalculatorServicer):
	def SquareRoot(self, req, context):
		response = calc_pb2.Number()
		print('=> backend')
		response.value = calc.square_root(req.value)
		print('<= backend')
		return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
calc_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)

print('listening on port {}'.format(50051))
server.add_insecure_port('[::]:50051')
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop()	
