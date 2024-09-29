# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import status_service_pb2 as status__service__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in status_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StatusServiceStub(object):
    """定义状态发送、状态控制服务
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.report = channel.unary_unary(
                '/graphmind.grpc.status_service.StatusService/report',
                request_serializer=status__service__pb2.ProcessStatus.SerializeToString,
                response_deserializer=status__service__pb2.Empty.FromString,
                _registered_method=True)
        self.control = channel.unary_unary(
                '/graphmind.grpc.status_service.StatusService/control',
                request_serializer=status__service__pb2.ProcessStatus.SerializeToString,
                response_deserializer=status__service__pb2.Empty.FromString,
                _registered_method=True)


class StatusServiceServicer(object):
    """定义状态发送、状态控制服务
    """

    def report(self, request, context):
        """发送当前处理状态信息（理解：python 汇报处理状态，提供 ChatProcessStat，但 Java 端只需返回空）
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def control(self, request, context):
        """接受状态控制信息（理解：Java 端发送控制信息，提供 ChatProcessStat，python 端只需返回空，晚点再返回一个 Report）
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatusServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'report': grpc.unary_unary_rpc_method_handler(
                    servicer.report,
                    request_deserializer=status__service__pb2.ProcessStatus.FromString,
                    response_serializer=status__service__pb2.Empty.SerializeToString,
            ),
            'control': grpc.unary_unary_rpc_method_handler(
                    servicer.control,
                    request_deserializer=status__service__pb2.ProcessStatus.FromString,
                    response_serializer=status__service__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'graphmind.grpc.status_service.StatusService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('graphmind.grpc.status_service.StatusService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StatusService(object):
    """定义状态发送、状态控制服务
    """

    @staticmethod
    def report(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/graphmind.grpc.status_service.StatusService/report',
            status__service__pb2.ProcessStatus.SerializeToString,
            status__service__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def control(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/graphmind.grpc.status_service.StatusService/control',
            status__service__pb2.ProcessStatus.SerializeToString,
            status__service__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
