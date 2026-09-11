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
from univapayclientsdk.models.bank_transfer_status_webhook_callback import (
    BankTransferStatusWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

BankTransferEventType = Union[BankTransferStatusWebhookCallback, UnknownEvent]

class BankTransferHandler:
    """
     Bank transfer status update events.
    """

    @staticmethod
    def parse_event(request: Request) -> BankTransferEventType:
        """
         Parse the event.

        :return: BankTransferStatusWebhookCallback for successful parsing; UnknownEvent
                 for unknown events.
        :rtype: Union[BankTransferStatusWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("bank-transfer")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
