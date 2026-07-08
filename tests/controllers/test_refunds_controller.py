
"""
univapay_client_sdk

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291, W293, E501
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)

from tests.controllers.controller_test_base import (
    ControllerTestBase,
)
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.refund_create_request import (
    RefundCreateRequest,
)
from univapayclientsdk.models.refund_update_request import (
    RefundUpdateRequest,
)


class RefundsControllerTests(ControllerTestBase):
    """
    Endpoint tests for validating the API behavior.

    Ensures controller methods execute correctly and produce the expected
    responses using the shared test client and response catcher.
    """

    controller = None

    @classmethod
    def setUpClass(cls):
        """
        Initialize the shared test client and controller for all test methods.
        """
        super().setUpClass()
        cls.controller = cls.client.refunds
        cls.response_catcher = cls.controller.http_call_back

    def test_list_refunds(self):
        """
        Retrieves a list of all refunds for a specific charge.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"
        metadata = "order_id: 12345"

        # Perform the API call through the SDK function
        result = self.controller.list_refunds(
            store_id,
            charge_id,
            limit,
            cursor,
            cursor_direction,
            metadata,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"items\":[{\"id\":\"b4d9fea9-c9b3-4e76-a25d-b61f7e4821b6\",\"store_id"
            "\":\"76cf4a64-02bc-4cb3-9a28-74622e5928a1\",\"charge_id\":\"6efb4e5c-690"
            "a-40f3-a4f1-0e19c5f84e98\",\"status\":\"successful\",\"amount\":1000,\"c"
            "urrency\":\"JPY\",\"amount_formatted\":1000,\"reason\":\"customer_reques"
            "t\",\"message\":\"Customer returned item\",\"error\":{},\"metadata\":{},"
            "\"mode\":\"live\",\"created_on\":\"2026-04-09T07:35:50.000000Z\",\"updat"
            "ed_on\":\"2026-04-09T07:36:00.000000Z\"},{\"id\":\"c5e0afb0-dac4-5f87-b3"
            "6e-c72f8f5932c7\",\"store_id\":\"76cf4a64-02bc-4cb3-9a28-74622e5928a1\","
            "\"charge_id\":\"7fac5f6d-7a1b-51e4-b5f2-1f2ad6f95fa9\",\"status\":\"pend"
            "ing\",\"amount\":2500,\"currency\":\"JPY\",\"amount_formatted\":2500,\"r"
            "eason\":\"duplicate\",\"message\":\"Duplicate charge\",\"error\":{},\"me"
            "tadata\":{\"order_id\":\"ORD-1002\"},\"mode\":\"live\",\"created_on\":\""
            "2026-04-10T10:00:00.000000Z\",\"updated_on\":\"2026-04-10T10:00:05.00000"
            "0Z\"},{\"id\":\"d6f1bac1-ebd5-6098-c47f-d83a906043d8\",\"store_id\":\"76"
            "cf4a64-02bc-4cb3-9a28-74622e5928a1\",\"charge_id\":\"80bd6a7e-8b2c-62f5-"
            "c6a3-2a3be7a06aba\",\"status\":\"successful\",\"amount\":500,\"currency"
            "\":\"JPY\",\"amount_formatted\":500,\"reason\":\"fraud\",\"message\":\"F"
            "raudulent transaction reversed\",\"error\":{},\"metadata\":{},\"mode\":"
            "\"live\",\"created_on\":\"2026-04-11T14:22:08.000000Z\",\"updated_on\":"
            "\"2026-04-11T14:22:20.000000Z\"}],\"has_more\":false,\"total_hits\":3}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_create_refund(self):
        """
        Creates a refund for a successful charge. The charge must have status
        `successful`. Konbini and bank transfer charges cannot be refunded. The refund
        is processed asynchronously — the initial status will be `pending`.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        body = APIHelper.json_deserialize(
            "{\"amount\":1000,\"currency\":\"JPY\",\"reason\":\"customer_request\"}",
            RefundCreateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.create_refund(
            store_id,
            charge_id,
            body,
            idempotency_key,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 201
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"b4d9fea9-c9b3-4e76-a25d-b61f7e4821b6\",\"store_id\":\"76cf4a64"
            "-02bc-4cb3-9a28-74622e5928a1\",\"charge_id\":\"6efb4e5c-690a-40f3-a4f1-0"
            "e19c5f84e98\",\"status\":\"pending\",\"amount\":1000,\"currency\":\"JPY"
            "\",\"amount_formatted\":1000,\"reason\":\"customer_request\",\"message\""
            ":\"Customer returned item\",\"error\":null,\"metadata\":{},\"mode\":\"li"
            "ve\",\"created_on\":\"2026-04-09T07:35:50.000000Z\",\"updated_on\":\"202"
            "6-04-09T07:35:50.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_refund(self):
        """
        Retrieves the details of a specific refund. Supports long polling — set
        `polling=true` to wait until the refund status changes from `pending` to a
        terminal state (`successful`, `failed`, or `error`).
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        polling = True

        # Perform the API call through the SDK function
        result = self.controller.get_refund(
            store_id,
            charge_id,
            id,
            polling,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"b4d9fea9-c9b3-4e76-a25d-b61f7e4821b6\",\"store_id\":\"76cf4a64"
            "-02bc-4cb3-9a28-74622e5928a1\",\"charge_id\":\"6efb4e5c-690a-40f3-a4f1-0"
            "e19c5f84e98\",\"status\":\"successful\",\"amount\":1000,\"currency\":\"J"
            "PY\",\"amount_formatted\":1000,\"reason\":\"customer_request\",\"message"
            "\":\"Customer returned item\",\"error\":null,\"metadata\":{},\"mode\":\""
            "live\",\"created_on\":\"2026-04-09T07:35:50.000000Z\",\"updated_on\":\"2"
            "026-04-09T07:36:00.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_refund(self):
        """
        Updates metadata, message, or reason on an existing refund.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        body = APIHelper.json_deserialize(
            "{\"message\":\"Updated reason note\",\"metadata\":{\"order_id\":\"12345"
            "\"}}",
            RefundUpdateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.update_refund(
            store_id,
            charge_id,
            id,
            body,
            idempotency_key,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 200
        # Test headers
        expected_headers = {
            "content-type": "application/json",
        }

        assert ComparisonHelper.match_headers(
            expected_headers,
            self.response_catcher.response.headers,
        )
        # Test whether the captured response is as we expected
        assert result is not None
        expected_body = APIHelper.json_deserialize(
            "{\"id\":\"b4d9fea9-c9b3-4e76-a25d-b61f7e4821b6\",\"store_id\":\"76cf4a64"
            "-02bc-4cb3-9a28-74622e5928a1\",\"charge_id\":\"6efb4e5c-690a-40f3-a4f1-0"
            "e19c5f84e98\",\"status\":\"successful\",\"amount\":1000,\"currency\":\"J"
            "PY\",\"amount_formatted\":1000,\"reason\":\"customer_request\",\"message"
            "\":\"Updated reason note\",\"error\":null,\"metadata\":{\"order_id\":\"1"
            "2345\"},\"mode\":\"live\",\"created_on\":\"2026-04-09T07:35:50.000000Z\""
            ",\"updated_on\":\"2026-04-09T08:00:00.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

