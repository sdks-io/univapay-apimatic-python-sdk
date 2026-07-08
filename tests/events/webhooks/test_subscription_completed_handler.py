"""
 univapay_client_sdk

 This file was automatically generated for Univapay by APIMATIC v3.0 (
https://www.apimatic.io ).
"""
# ruff: noqa: E501

from __future__ import annotations

import unittest
from typing import Any

from univapayclientsdk.api_helper import ApiHelper
from univapayclientsdk.events.unknown_event import (
    UnknownEvent,
)
from univapayclientsdk.events.webhooks.subscription_completed_handler import (
    SubscriptionCompletedHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.subscription_completed_webhook_callback import (
    SubscriptionCompletedWebhookCallback,
)


class TestSubscriptionCompletedHandler(unittest.TestCase):
    """
     Unit tests for the `SubscriptionCompletedHandler` event group handler.
    """

    @classmethod
    def setUpClass(cls):
        """
         Set up shared test resources.
        """
    @staticmethod
    def _json_bytes(obj: Any) -> bytes:
        """
         Serialize an object to UTF-8 encoded JSON bytes.

        :param obj: Object to serialize.

        :return: UTF-8 encoded JSON bytes.
        :rtype: bytes
        """
        return APIHelper.json_serialize(obj).encode("utf-8")

    @staticmethod
    def _make_request(body_obj) -> Request:
        """
         Create a webhook HTTP request with the given payload.

        :param body_obj: The body object to serialize as JSON.
        """
        raw = TestSubscriptionCompletedHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_subscription_completed_from_subscription_completed_handler(self):
        """
         Tests the `subscriptionCompleted` event from subscriptionCompletedHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "subscription_completed",
            "data": {
                "id": "11ef335e-9aa5-c54a-8313-7f9847da313a",
                "store_id": "11edf541-c42d-653c-8c3d-dfe0a55f95c0",
                "transaction_token_id": "11ef32a7-3a71-8662-803f-1bc27702eeec",
                "amount": 1250,
                "currency": "USD",
                "amount_formatted": 12.5,
                "schedule_settings": {
                    "start_on": "2024-07-01",
                    "zone_id": "Asia/Tokyo",
                    "preserve_end_of_month": False,
                    "retry_interval": "P7D",
                    "termination_mode": "on_next_payment",
                },
                "only_direct_currency": False,
                "first_charge_authorization_only": False,
                "status": "current",
                "metadata": {
                    "order_id": "12345",
                },
                "mode": "test",
                "created_on": "2024-06-26T01:51:28.627023Z",
                "period": "monthly",
                "exampleAdditionalProperty": {
                    "key1": "val1",
                    "key2": "val2",
                },
            },
            "created_on": "2026-04-09T07:35:50.000000Z",
            "exampleAdditionalProperty": {
                "key1": "val1",
                "key2": "val2",
            },
        }
        core_req = self._make_request(event_payload)

        # act
        event = SubscriptionCompletedHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, SubscriptionCompletedWebhookCallback) and
            getattr(event, "event", None) == "subscription_completed"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from SubscriptionCompletedHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = SubscriptionCompletedHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
