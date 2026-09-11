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
from univapayclientsdk.events.webhooks.token_handler import (
    TokenHandler,
)
from univapayclientsdk.http.request import Request
from univapayclientsdk.models.token_webhook_event import (
    TokenWebhookEvent,
)


class TestTokenHandler(unittest.TestCase):
    """
     Unit tests for the `TokenHandler` event group handler.
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
        raw = TestTokenHandler._json_bytes(body_obj)
        return Request(
            method="POST",
            path="/webhooks",
            url="https://example.test/webhooks",
            headers={
                "Content-Type": "application/json",
            },
            raw_body=raw,
        )

    def test_token_created_from_token_handler(self):
        """
         Tests the `tokenCreated` event from tokenHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "token_created",
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
                "data": {
                    "card": {
                        "cardholder": "TARO YAMADA",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "brand": "visa",
                        "last_four": "4242",
                        "card_bin": "card_bin0",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "cvv_authorize": {
                        "enabled": True,
                        "status": "current",
                        "charge_id": None,
                        "credentials_id": None,
                        "currency": "JPY",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "billing": None,
                    "cvv_authorize_check": None,
                    "three_ds": None,
                    "exampleAdditionalProperty": {
                        "key1": "val1",
                        "key2": "val2",
                    },
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
        event = TokenHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, TokenWebhookEvent) and
            getattr(event, "event", None) == "token_created"
        )

    def test_token_updated_from_token_handler(self):
        """
         Tests the `tokenUpdated` event from tokenHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "token_updated",
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
                "data": {
                    "card": {
                        "cardholder": "TARO YAMADA",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "brand": "visa",
                        "last_four": "4242",
                        "card_bin": "card_bin0",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "cvv_authorize": {
                        "enabled": True,
                        "status": "current",
                        "charge_id": None,
                        "credentials_id": None,
                        "currency": "JPY",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "billing": None,
                    "cvv_authorize_check": None,
                    "three_ds": None,
                    "exampleAdditionalProperty": {
                        "key1": "val1",
                        "key2": "val2",
                    },
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
        event = TokenHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, TokenWebhookEvent) and
            getattr(event, "event", None) == "token_updated"
        )

    def test_token_three_ds_updated_from_token_handler(self):
        """
         Tests the `tokenThreeDsUpdated` event from tokenHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "token_three_d_s_updated",
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
                "data": {
                    "card": {
                        "cardholder": "TARO YAMADA",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "brand": "visa",
                        "last_four": "4242",
                        "card_bin": "card_bin0",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "cvv_authorize": {
                        "enabled": True,
                        "status": "current",
                        "charge_id": None,
                        "credentials_id": None,
                        "currency": "JPY",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "billing": None,
                    "cvv_authorize_check": None,
                    "three_ds": None,
                    "exampleAdditionalProperty": {
                        "key1": "val1",
                        "key2": "val2",
                    },
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
        event = TokenHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, TokenWebhookEvent) and
            getattr(event, "event", None) == "token_three_d_s_updated"
        )

    def test_token_cvv_auth_updated_from_token_handler(self):
        """
         Tests the `tokenCvvAuthUpdated` event from tokenHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "token_cvv_auth_updated",
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
                "data": {
                    "card": {
                        "cardholder": "TARO YAMADA",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "brand": "visa",
                        "last_four": "4242",
                        "card_bin": "card_bin0",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "cvv_authorize": {
                        "enabled": True,
                        "status": "current",
                        "charge_id": None,
                        "credentials_id": None,
                        "currency": "JPY",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "billing": None,
                    "cvv_authorize_check": None,
                    "three_ds": None,
                    "exampleAdditionalProperty": {
                        "key1": "val1",
                        "key2": "val2",
                    },
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
        event = TokenHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, TokenWebhookEvent) and
            getattr(event, "event", None) == "token_cvv_auth_updated"
        )

    def test_token_cvv_auth_check_updated_from_token_handler(self):
        """
         Tests the `tokenCvvAuthCheckUpdated` event from tokenHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "token_cvv_auth_check_updated",
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
                "data": {
                    "card": {
                        "cardholder": "TARO YAMADA",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "brand": "visa",
                        "last_four": "4242",
                        "card_bin": "card_bin0",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "cvv_authorize": {
                        "enabled": True,
                        "status": "current",
                        "charge_id": None,
                        "credentials_id": None,
                        "currency": "JPY",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "billing": None,
                    "cvv_authorize_check": None,
                    "three_ds": None,
                    "exampleAdditionalProperty": {
                        "key1": "val1",
                        "key2": "val2",
                    },
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
        event = TokenHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, TokenWebhookEvent) and
            getattr(event, "event", None) == "token_cvv_auth_check_updated"
        )

    def test_token_replaced_from_token_handler(self):
        """
         Tests the `tokenReplaced` event from tokenHandler.
        """
        # arrange
        event_payload = {
            "id": "11ef0000-0000-4000-8000-000000000001",
            "event": "token_replaced",
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
                "data": {
                    "card": {
                        "cardholder": "TARO YAMADA",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "brand": "visa",
                        "last_four": "4242",
                        "card_bin": "card_bin0",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "cvv_authorize": {
                        "enabled": True,
                        "status": "current",
                        "charge_id": None,
                        "credentials_id": None,
                        "currency": "JPY",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "billing": None,
                    "cvv_authorize_check": None,
                    "three_ds": None,
                    "exampleAdditionalProperty": {
                        "key1": "val1",
                        "key2": "val2",
                    },
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
        event = TokenHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, TokenWebhookEvent) and
            getattr(event, "event", None) == "token_replaced"
        )

    def test_recurring_token_deleted_from_token_handler(self):
        """
         Tests the `recurringTokenDeleted` event from tokenHandler.
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
                "data": {
                    "card": {
                        "cardholder": "TARO YAMADA",
                        "exp_month": 12,
                        "exp_year": 2026,
                        "brand": "visa",
                        "last_four": "4242",
                        "card_bin": "card_bin0",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "cvv_authorize": {
                        "enabled": True,
                        "status": "current",
                        "charge_id": None,
                        "credentials_id": None,
                        "currency": "JPY",
                        "exampleAdditionalProperty": {
                            "key1": "val1",
                            "key2": "val2",
                        },
                    },
                    "billing": None,
                    "cvv_authorize_check": None,
                    "three_ds": None,
                    "exampleAdditionalProperty": {
                        "key1": "val1",
                        "key2": "val2",
                    },
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
        event = TokenHandler.parse_event(core_req)

        # assert
        assert (
            isinstance(event, TokenWebhookEvent) and
            getattr(event, "event", None) == "recurring_token_deleted"
        )

    def test_unknown_event(self):
        """
         Tests the `UnknownEvent` case from TokenHandler.
        """
        # arrange
        event_payload = ""
        core_req = self._make_request(event_payload)

        # act
        event = TokenHandler.parse_event(core_req)

        # assert
        assert isinstance(event, UnknownEvent)
