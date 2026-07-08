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
from univapayclientsdk.events.webhooks.recurring_token_deleted_handler import (
    RecurringTokenDeletedHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.recurring_token_deleted_webhook_callback import (
    RecurringTokenDeletedWebhookCallback,
)


class TestRecurringTokenDeletedHandler(unittest.TestCase):
    """
     Unit tests for the `RecurringTokenDeletedHandler` event group handler.
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
        raw = TestRecurringTokenDeletedHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_recurring_token_deleted_from_recurring_token_deleted_handler(self):
        """
         Tests the `recurringTokenDeleted` event from recurringTokenDeletedHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "recurring_token_deleted",
            "data": {
                "id": "6426bbd2-17bd-41bf-883b-1fe970db48ee",
                "store_id": "fc264608-9a9e-495e-844e-a08129a81af4",
                "email": "test@univapay.com",
                "payment_type": "card",
                "active": True,
                "mode": "live",
                "type": "recurring",
                "confirmed": True,
                "metadata": {
                    "customer_id": "cust_12345",
                },
                "created_on": "2026-04-09T07:35:50.000000Z",
                "updated_on": "2026-04-09T07:35:50.000000Z",
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
        event = RecurringTokenDeletedHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, RecurringTokenDeletedWebhookCallback) and
            getattr(event, "event", None) == "recurring_token_deleted"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from RecurringTokenDeletedHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = RecurringTokenDeletedHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
