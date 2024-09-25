import grpc
from concurrent import futures
import warnings
import os
from graphmind.grpc.status_service import status_service_pb2, status_service_pb2_grpc

AIM_HOST = os.getenv("JAVA_HOST") + ":" + os.getenv("JAVA_GRPC_PORT")

class StatusServiceImpl(status_service_pb2_grpc.StatusServiceServicer):
    def control(self, request, context):
        """
        接受来自 Java 端的控制请求
        Args:
            request: 从 Java 端发送的控制请求
            context: 上下文

        Returns: 空响应

        """
        print(f"Received control request: {request}")
        return status_service_pb2.Empty()

    def report(self, request, context):
        """
        形式实现，无任何作用
        """
        warnings.warn(f"Unexpected receive from report: {request}")
        return status_service_pb2.Empty()

def report(chat_status: dict):
    """
    向目标回报状态信息
    """
    try:
        send_obj = status_service_pb2.ChatStatus(**chat_status)
    except Exception as e:
        raise Exception(f"Failed to convert chat_status to gRPC message object ChatStatus: {e}")
    with grpc.insecure_channel(AIM_HOST) as channel:
        stub = status_service_pb2_grpc.StatusServiceStub(channel)
        response = stub.report(send_obj)
        if response:
            warnings.warn(f"When reporting status, unexpected receive: {response}")


if __name__ == '__main__':
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    status_service_pb2_grpc.add_StatusServiceServicer_to_server(StatusServiceImpl(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()