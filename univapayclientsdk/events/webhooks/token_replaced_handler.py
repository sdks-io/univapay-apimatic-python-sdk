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
from univapayclientsdk.models.token_replaced_webhook_callback import (
    TokenReplacedWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

TokenReplacedEventType = Union[TokenReplacedWebhookCallback, UnknownEvent]

class TokenReplacedHandler:
    """
     Token replaced event.
    """

    @staticmethod
    def parse_event(request: Request) -> TokenReplacedEventType:
        """
         Parse the event.

        :return: TokenReplacedWebhookCallback for successful parsing; UnknownEvent for
                 unknown events.
        :rtype: Union[TokenReplacedWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("tokenReplaced")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
