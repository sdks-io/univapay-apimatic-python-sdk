"""
 univapay_client_sdk

 This file was automatically generated for Univapay by APIMATIC v3.0 (
https://www.apimatic.io ).
"""
from __future__ import annotations

from typing import Union

from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.events.unknown_event import (
    UnknownEvent,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.charge_webhook_event import (
    ChargeWebhookEvent,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

ChargeEventType = Union[ChargeWebhookEvent, UnknownEvent]

class ChargeHandler:
    """
     Charge lifecycle events.
    """

    @staticmethod
    def parse_event(request: Request) -> ChargeEventType:
        """
         Parse the event.

        :return: ChargeWebhookEvent for successful parsing; UnknownEvent for unknown
                 events.
        :rtype: Union[ChargeWebhookEvent, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("charge")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
