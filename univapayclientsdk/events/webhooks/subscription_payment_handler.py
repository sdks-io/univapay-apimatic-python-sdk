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
from univapayclientsdk.models.subscription_payment_webhook_callback import (
    SubscriptionPaymentWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

SubscriptionPaymentEventType = Union[SubscriptionPaymentWebhookCallback, UnknownEvent]

class SubscriptionPaymentHandler:
    """
     Subscription payment event.
    """

    @staticmethod
    def parse_event(request: Request) -> SubscriptionPaymentEventType:
        """
         Parse the event.

        :return: SubscriptionPaymentWebhookCallback for successful parsing; UnknownEvent
                 for unknown events.
        :rtype: Union[SubscriptionPaymentWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("subscriptionPayment")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
