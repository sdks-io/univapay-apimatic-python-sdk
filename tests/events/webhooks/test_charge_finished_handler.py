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
from univapayclientsdk.events.webhooks.charge_finished_handler import (
    ChargeFinishedHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.charge_finished_webhook_callback import (
    ChargeFinishedWebhookCallback,
)


class TestChargeFinishedHandler(unittest.TestCase):
    """
     Unit tests for the `ChargeFinishedHandler` event group handler.
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
        raw = TestChargeFinishedHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_charge_finished_from_charge_finished_handler(self):
        """
         Tests the `chargeFinished` event from chargeFinishedHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "charge_finished",
            "data": {
                "id": "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98",
                "store_id": "11edf541-c42d-653c-8c3d-dfe0a55f95c0",
                "transaction_token_id": "11ef32a7-3a71-8662-803f-1bc27702eeec",
                "transaction_token_type": "recurring",
                "subscription_id": "11ef335e-9aa5-c54a-8313-7f9847da313a",
                "requested_amount": 1250,
                "requested_currency": "USD",
                "requested_amount_formatted": 12.5,
                "charged_amount": 1250,
                "charged_currency": "USD",
                "charged_amount_formatted": 12.5,
                "only_direct_currency": False,
                "status": "successful",
                "error": None,
                "mode": "test",
                "created_on": "2024-06-26T01:51:30.000000Z",
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
        event = ChargeFinishedHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, ChargeFinishedWebhookCallback) and
            getattr(event, "event", None) == "charge_finished"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from ChargeFinishedHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = ChargeFinishedHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
