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
from univapayclientsdk.models.customs_declaration_webhook_callback import (
    CustomsDeclarationWebhookCallback,
)
from univapayclientsdk.utilities.union_type_lookup import (
    UnionTypeLookUp,
)

CustomsEventType = Union[CustomsDeclarationWebhookCallback, UnknownEvent]

class CustomsHandler:
    """
     Customs declaration lifecycle events.
    """

    @staticmethod
    def parse_event(request: Request) -> CustomsEventType:
        """
         Parse the event.

        :return: CustomsDeclarationWebhookCallback for successful parsing; UnknownEvent
                 for unknown events.
        :rtype: Union[CustomsDeclarationWebhookCallback, UnknownEvent]
        """
        # Deserialize payload
        try:
            union = UnionTypeLookUp.get("customs")
            return APIHelper.deserialize_union_type(union, request.raw_body)
        except Exception as e:
            return UnknownEvent([
                "Deserialization failed.",
                str(e),
            ])
