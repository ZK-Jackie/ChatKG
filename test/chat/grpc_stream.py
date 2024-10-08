# 测试stream接口
import grpc

from graphmind.api.grpc.chat_service import chat_service_pb2_grpc, chat_service_pb2

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = chat_service_pb2_grpc.ChatServiceStub(channel)
        response = stub.stream(chat_service_pb2.ChatMessage(
            role=1,
            content="你可以总结一下我前文收获到的知识点吗？",
            chunkResp=False,
            userId="Test",
            convId="1",
            messageId="Test"
        ))
        for resp in response:
            print(resp, end="")