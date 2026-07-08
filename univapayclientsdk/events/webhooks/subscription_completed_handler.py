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
from univapayclientsdk.models.subscription_completed_webhook_callback import (
    SubscriptionCompletedWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

SubscriptionCompletedEventType = Union[
    SubscriptionCompletedWebhookCallback,
    UnknownEvent,
]

class SubscriptionCompletedHandler:
    """
     Subscription completed event.
    """

    @staticmethod
    def parse_event(request: Request) -> SubscriptionCompletedEventType:
        """
         Parse the event.

        :return: SubscriptionCompletedWebhookCallback for successful parsing;
                 UnknownEvent for unknown events.
        :rtype: Union[SubscriptionCompletedWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("subscriptionCompleted")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
