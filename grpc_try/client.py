import grpc
import calc_pb2
import calc_pb2_grpc
import time
channel = grpc.insecure_channel('localhost:50051')

stub = calc_pb2_grpc.CalculatorStub(channel)
val = 0
while True:
	number = calc_pb2.Number(value=val)
	response = stub.SquareRoot(number)
	print(response.value)
	val+=1000
	time.sleep(1)
	break
