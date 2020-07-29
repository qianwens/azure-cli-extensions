# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Sku(Model):
    """Model representing SKU for Codespaces Plan.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar name: Required. The name of the SKU for Codespaces Plan. Default
     value: "Free" .
    :vartype name: str
    :param tier: The tier of the SKU for Codespaces Plan. Possible values
     include: 'Standard'
    :type tier: str or ~microsoft.codespaces.models.SkuTier
    """

    _validation = {
        'name': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    name = "Free"

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.tier = kwargs.get('tier', None)