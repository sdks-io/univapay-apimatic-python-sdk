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
from univapayclientsdk.models.charge_updated_webhook_callback import (
    ChargeUpdatedWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

ChargeUpdatedEventType = Union[ChargeUpdatedWebhookCallback, UnknownEvent]

class ChargeUpdatedHandler:
    """
     Charge updated event.
    """

    @staticmethod
    def parse_event(request: Request) -> ChargeUpdatedEventType:
        """
         Parse the event.

        :return: ChargeUpdatedWebhookCallback for successful parsing; UnknownEvent for
                 unknown events.
        :rtype: Union[ChargeUpdatedWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("chargeUpdated")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
