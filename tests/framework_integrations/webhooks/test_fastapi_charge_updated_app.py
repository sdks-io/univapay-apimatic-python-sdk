"""
 univapay_client_sdk

 This file was automatically generated for Univapay by APIMATIC v3.0 (
https://www.apimatic.io ).
"""
from __future__ import annotations

import unittest

from fastapi.testclient import TestClient

from tests.framework_integrations.webhooks.apps.fastapi_charge_updated_app import (
    app,
)


class FastapiChargeUpdatedTest(unittest.TestCase):
    """
     Integration tests for `chargeUpdated` using a FastAPI application.
    """

    @classmethod
    def setUpClass(cls):
        """
         Set up shared test resources.
        """
        cls.client = TestClient(app)

    def test_charge_updated_from_charge_updated_app(self):
        """
         Tests the `chargeUpdated` event from chargeUpdated application.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "charge_updated",
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

        # act
        resp = self.client.post("/webhooks", json=event_payload)

        # assert
        self.assertEqual(resp.status_code, 200)
