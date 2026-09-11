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
from univapayclientsdk.models.subscription_webhook_event import (
    SubscriptionWebhookEvent,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

SubscriptionEventType = Union[SubscriptionWebhookEvent, UnknownEvent]

class SubscriptionHandler:
    """
     Subscription lifecycle events.
    """

    @staticmethod
    def parse_event(request: Request) -> SubscriptionEventType:
        """
         Parse the event.

        :return: SubscriptionWebhookEvent for successful parsing; UnknownEvent for
                 unknown events.
        :rtype: Union[SubscriptionWebhookEvent, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("subscription")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
