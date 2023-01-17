# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import node_connection_pb2 as node__connection__pb2


class NodeConnectionStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.requestVote = channel.unary_unary(
                '/nodeconnection.NodeConnection/requestVote',
                request_serializer=node__connection__pb2.VoteRequest.SerializeToString,
                response_deserializer=node__connection__pb2.VoteResponse.FromString,
                )
        self.appendEntries = channel.unary_unary(
                '/nodeconnection.NodeConnection/appendEntries',
                request_serializer=node__connection__pb2.AppendEntriesRequest.SerializeToString,
                response_deserializer=node__connection__pb2.AppendEntriesResponse.FromString,
                )


class NodeConnectionServicer(object):
    """Missing associated documentation comment in .proto file."""

    def requestVote(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def appendEntries(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeConnectionServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'requestVote': grpc.unary_unary_rpc_method_handler(
                    servicer.requestVote,
                    request_deserializer=node__connection__pb2.VoteRequest.FromString,
                    response_serializer=node__connection__pb2.VoteResponse.SerializeToString,
            ),
            'appendEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.appendEntries,
                    request_deserializer=node__connection__pb2.AppendEntriesRequest.FromString,
                    response_serializer=node__connection__pb2.AppendEntriesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nodeconnection.NodeConnection', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NodeConnection(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def requestVote(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nodeconnection.NodeConnection/requestVote',
            node__connection__pb2.VoteRequest.SerializeToString,
            node__connection__pb2.VoteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def appendEntries(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nodeconnection.NodeConnection/appendEntries',
            node__connection__pb2.AppendEntriesRequest.SerializeToString,
            node__connection__pb2.AppendEntriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
