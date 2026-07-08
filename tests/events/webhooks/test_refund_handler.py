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
from univapayclientsdk.events.webhooks.refund_handler import (
    RefundHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.refund_webhook_callback import (
    RefundWebhookCallback,
)


class TestRefundHandler(unittest.TestCase):
    """
     Unit tests for the `RefundHandler` event group handler.
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
        raw = TestRefundHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_refund_finished_from_refund_handler(self):
        """
         Tests the `refundFinished` event from refundHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "refund_finished",
            "data": {
                "id": "b4d9fea9-c9b3-4e76-a25d-b61f7e4821b6",
                "store_id": "76cf4a64-02bc-4cb3-9a28-74622e5928a1",
                "charge_id": "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98",
                "status": "successful",
                "amount": 1000,
                "currency": "JPY",
                "amount_formatted": 1000,
                "reason": "customer_request",
                "message": "Customer returned item",
                "error": None,
                "metadata": {
                    "order_id": "order_12345",
                },
                "mode": "live",
                "created_on": "2026-04-09T07:35:50.000000Z",
                "updated_on": "2026-04-09T07:36:00.000000Z",
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
        event = RefundHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, RefundWebhookCallback) and
            getattr(event, "event", None) == "refund_finished"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from RefundHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = RefundHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
