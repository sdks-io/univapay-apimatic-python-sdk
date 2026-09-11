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
from univapayclientsdk.events.webhooks.customs_handler import (
    CustomsHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.customs_declaration_webhook_callback import (
    CustomsDeclarationWebhookCallback,
)


class TestCustomsHandler(unittest.TestCase):
    """
     Unit tests for the `CustomsHandler` event group handler.
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
        raw = TestCustomsHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_customs_declaration_finished_from_customs_handler(self):
        """
         Tests the `customsDeclarationFinished` event from customsHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "customs_declaration_finished",
            "data": {
                "id": "11ef0000-0000-4000-8000-000000000040",
                "charge_id": "11ef0000-0000-4000-8000-000000000001",
                "merchant_id": "11ef0000-0000-4000-8000-000000000020",
                "store_id": "11ef0000-0000-4000-8000-000000000022",
                "mode": "test",
                "gateway": "wechat_online",
                "declaration": {
                    "customs": "TOKYO",
                    "merchant_customs_no": "1234567890",
                    "certificate_id": "AB1234567",
                    "certificate_name": "TARO YAMADA",
                },
                "declaration_result": {
                    "approving_authority": "TOKYO",
                    "trade_id": "wx_trade_12345",
                    "transaction_id": "wx_txn_12345",
                    "charge_transaction_id": "wx_charge_12345",
                },
                "status": "successful",
                "created_on": "2026-04-09T07:35:50.000000Z",
                "platform_id": "00000550-0000-0000-0000-000000000000",
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
        event = CustomsHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, CustomsDeclarationWebhookCallback) and
            getattr(event, "event", None) == "customs_declaration_finished"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from CustomsHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = CustomsHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
