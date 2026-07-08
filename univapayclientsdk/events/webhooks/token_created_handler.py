"""
 univapay_client_sdk

 This file was automatically generated for Univapay by APIMATIC v3.0 (
https://www.apimatic.io ).
"""
from __future__ import annotations

from typing import Union

from univapayclientsdk.api_helper import ApiHelper
from univapayclientsdk.events.unknown_event import (
    UnknownEvent,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.token_created_webhook_callback import (
    TokenCreatedWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

TokenCreatedEventType = Union[TokenCreatedWebhookCallback, UnknownEvent]

class TokenCreatedHandler:
    """
     Token created event.
    """

    @staticmethod
    def parse_event(request: Request) -> TokenCreatedEventType:
        """
         Parse the event.

        :return: TokenCreatedWebhookCallback for successful parsing; UnknownEvent for
                 unknown events.
        :rtype: Union[TokenCreatedWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("tokenCreated")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
