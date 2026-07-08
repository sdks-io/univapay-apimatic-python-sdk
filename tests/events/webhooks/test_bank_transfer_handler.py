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
from univapayclientsdk.events.webhooks.bank_transfer_handler import (
    BankTransferHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.bank_transfer_status_webhook_callback import (
    BankTransferStatusWebhookCallback,
)


class TestBankTransferHandler(unittest.TestCase):
    """
     Unit tests for the `BankTransferHandler` event group handler.
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
        raw = TestBankTransferHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_bank_transfer_status_updated_from_bank_transfer_handler(self):
        """
         Tests the `bankTransferStatusUpdated` event from bank-transferHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "bank_transfer_status_updated",
            "data": {
                "id": "11ef0000-0000-4000-8000-000000000002",
                "charge_id": "11ef0000-0000-4000-8000-000000000001",
                "payment_status": "exact",
                "latest_deposit_date": "2026-04-09T07:35:50.000000Z",
                "created_on": "2026-04-09T07:35:50.000000Z",
                "latest_deposit_amount": 1000,
                "balance": 0,
                "currency": "JPY",
                "amount": 1000,
                "amount_difference": 0,
                "token_metadata": {
                    "order_id": "12345",
                },
                "charge_metadata": {
                    "order_id": "order_12345",
                },
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
        event = BankTransferHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, BankTransferStatusWebhookCallback) and
            getattr(event, "event", None) == "bank_transfer_status_updated"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from BankTransferHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = BankTransferHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
