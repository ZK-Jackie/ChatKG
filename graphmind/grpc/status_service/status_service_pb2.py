# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: status_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'status_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14status_service.proto\x12\x1dgraphmind.grpc.status_service\"\xa7\x01\n\nChatStatus\x12\x0e\n\x06userId\x18\x01 \x01(\t\x12\x0e\n\x06\x63onvId\x18\x02 \x01(\t\x12\x15\n\ruserMessageId\x18\x03 \x01(\t\x12\x39\n\x08statusId\x18\x04 \x01(\x0e\x32\'.graphmind.grpc.status_service.StatusId\x12\x15\n\rstatusMessage\x18\x05 \x01(\t\x12\x10\n\x08sendTime\x18\x06 \x01(\t\"\x07\n\x05\x45mpty*j\n\x08StatusId\x12\r\n\tUNPROCESS\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\r\n\tPROCESSED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\x12\x0b\n\x07TIMEOUT\x10\x04\x12\r\n\tCANCELLED\x10\x05\x12\x08\n\x04STOP\x10\n2\xca\x01\n\rStatusService\x12[\n\x06report\x12).graphmind.grpc.status_service.ChatStatus\x1a$.graphmind.grpc.status_service.Empty\"\x00\x12\\\n\x07\x63ontrol\x12).graphmind.grpc.status_service.ChatStatus\x1a$.graphmind.grpc.status_service.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'status_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STATUSID']._serialized_start=234
  _globals['_STATUSID']._serialized_end=340
  _globals['_CHATSTATUS']._serialized_start=56
  _globals['_CHATSTATUS']._serialized_end=223
  _globals['_EMPTY']._serialized_start=225
  _globals['_EMPTY']._serialized_end=232
  _globals['_STATUSSERVICE']._serialized_start=343
  _globals['_STATUSSERVICE']._serialized_end=545
# @@protoc_insertion_point(module_scope)
