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
from univapayclientsdk.models.subscription_canceled_webhook_callback import (
    SubscriptionCanceledWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

SubscriptionCanceledEventType = Union[SubscriptionCanceledWebhookCallback, UnknownEvent]

class SubscriptionCanceledHandler:
    """
     Subscription canceled event.
    """

    @staticmethod
    def parse_event(request: Request) -> SubscriptionCanceledEventType:
        """
         Parse the event.

        :return: SubscriptionCanceledWebhookCallback for successful parsing;
                 UnknownEvent for unknown events.
        :rtype: Union[SubscriptionCanceledWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("subscriptionCanceled")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
