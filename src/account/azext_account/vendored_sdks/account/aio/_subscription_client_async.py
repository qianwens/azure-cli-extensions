# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6219, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import SubscriptionClientConfiguration
from .operations_async import SubscriptionOperations
from .operations_async import SubscriptionOperationOperations
from .operations_async import Operations
from .. import models


class SubscriptionClient(object):
    """The subscription client

    :ivar subscription: SubscriptionOperations operations
    :vartype subscription: subscription_client.aio.operations_async.SubscriptionOperations
    :ivar subscription_operation: SubscriptionOperationOperations operations
    :vartype subscription_operation: subscription_client.aio.operations_async.SubscriptionOperationOperations
    :ivar operations: Operations operations
    :vartype operations: subscription_client.aio.operations_async.Operations
    :param str base_url: Service URL
    """

    def __init__(
        self,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SubscriptionClientConfiguration(**kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.subscription = SubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.subscription_operation = SubscriptionOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "SubscriptionClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
