import os
import grpc
from concurrent import futures

from graphmind.api.grpc.chat_service import chat_service_pb2_grpc
from graphmind.api.grpc.status_service import status_service_pb2_grpc
from graphmind.api.grpc.message_service_impl import MessageServiceImpl
from graphmind.api.grpc.status_service_impl import StatusServiceImpl
from dotenv import load_dotenv

load_dotenv()

SERVER_PORT = os.getenv("SERVER_PORT", 50051)

if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_service_pb2_grpc.add_ChatServiceServicer_to_server(MessageServiceImpl(), server)
    status_service_pb2_grpc.add_StatusServiceServicer_to_server(StatusServiceImpl(), server)
    server.add_insecure_port(f'[::]:{SERVER_PORT}')
    server.start()
    print(f"\ngRPC listening at [::]:{SERVER_PORT}")
    server.wait_for_termination()