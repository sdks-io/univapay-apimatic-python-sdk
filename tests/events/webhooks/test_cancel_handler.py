"""
 univapay_client_sdk

 This file was automatically generated for Univapay by APIMATIC v3.0 (
https://www.apimatic.io ).
"""
# ruff: noqa: E501

from __future__ import annotations

import unittest
from typing import Any

from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.events.unknown_event import (
    UnknownEvent,
)
from univapayclientsdk.events.webhooks.cancel_handler import (
    CancelHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.cancel_webhook_callback import (
    CancelWebhookCallback,
)


class TestCancelHandler(unittest.TestCase):
    """
     Unit tests for the `CancelHandler` event group handler.
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
        raw = TestCancelHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_cancel_finished_from_cancel_handler(self):
        """
         Tests the `cancelFinished` event from cancelHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "cancel_finished",
            "data": {
                "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                "charge_id": "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98",
                "store_id": "76cf4a64-02bc-4cb3-9a28-74622e5928a1",
                "status": "successful",
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
        event = CancelHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, CancelWebhookCallback) and
            getattr(event, "event", None) == "cancel_finished"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from CancelHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = CancelHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
