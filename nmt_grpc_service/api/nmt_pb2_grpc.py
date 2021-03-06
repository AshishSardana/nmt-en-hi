# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nmt_pb2 as nmt__pb2


class RivaTranslateStub(object):
    """Riva NLP Services implement task-specific APIs for popular NLP tasks including
    intent recognition (as well as slot filling), and entity extraction.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TranslateText = channel.unary_unary(
            '/nvidia.riva.nmt.RivaTranslate/TranslateText',
            request_serializer=nmt__pb2.TranslateTextRequest.SerializeToString,
            response_deserializer=nmt__pb2.TranslateTextResponse.FromString,
        )


class RivaTranslateServicer(object):
    """Riva NLP Services implement task-specific APIs for popular NLP tasks including
    intent recognition (as well as slot filling), and entity extraction.
    """

    def TranslateText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RivaTranslateServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'TranslateText': grpc.unary_unary_rpc_method_handler(
            servicer.TranslateText,
            request_deserializer=nmt__pb2.TranslateTextRequest.FromString,
            response_serializer=nmt__pb2.TranslateTextResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler('nvidia.riva.nmt.RivaTranslate', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RivaTranslate(object):
    """Riva NLP Services implement task-specific APIs for popular NLP tasks including
    intent recognition (as well as slot filling), and entity extraction.
    """

    @staticmethod
    def TranslateText(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/nvidia.riva.nmt.RivaTranslate/TranslateText',
            nmt__pb2.TranslateTextRequest.SerializeToString,
            nmt__pb2.TranslateTextResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
