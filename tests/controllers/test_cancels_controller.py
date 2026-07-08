
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
from univapayclientsdk.models.cancel_create_request import (
    CancelCreateRequest,
)
from univapayclientsdk.models.cancel_update_request import (
    CancelUpdateRequest,
)


class CancelsControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.cancels
        cls.response_catcher = cls.controller.http_call_back

    def test_list_cancels(self):
        """
        Returns a paginated list of cancels for the specified charge.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_cancels(
            store_id,
            charge_id,
            limit,
            cursor,
            cursor_direction,
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
            "{\"items\":[{\"id\":\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\",\"charge_id"
            "\":\"6efb4e5c-690a-40f3-a4f1-0e19c5f84e98\",\"store_id\":\"76cf4a64-02bc"
            "-4cb3-9a28-74622e5928a1\",\"status\":\"successful\",\"error\":{},\"metad"
            "ata\":{\"order_id\":\"ORD-987\"},\"mode\":\"live\",\"created_on\":\"2026"
            "-04-09T07:35:50.000000Z\",\"updated_on\":\"2026-04-09T07:36:00.000000Z\""
            "},{\"id\":\"b2c3d4e5-f6a7-8901-bcde-f23456789012\",\"charge_id\":\"7fac5"
            "f6d-7a1b-51e4-b5f2-1f2ad6f95fa9\",\"store_id\":\"76cf4a64-02bc-4cb3-9a28"
            "-74622e5928a1\",\"status\":\"successful\",\"error\":{},\"metadata\":{\"o"
            "rder_id\":\"ORD-988\"},\"mode\":\"live\",\"created_on\":\"2026-04-10T10:"
            "00:00.000000Z\",\"updated_on\":\"2026-04-10T10:00:12.000000Z\"},{\"id\":"
            "\"c3d4e5f6-a7b8-9012-cdef-345678901234\",\"charge_id\":\"80bd6a7e-8b2c-6"
            "2f5-c6a3-2a3be7a06aba\",\"store_id\":\"76cf4a64-02bc-4cb3-9a28-74622e592"
            "8a1\",\"status\":\"pending\",\"error\":{},\"metadata\":{},\"mode\":\"liv"
            "e\",\"created_on\":\"2026-04-11T14:22:08.000000Z\",\"updated_on\":\"2026"
            "-04-11T14:22:08.000000Z\"}],\"has_more\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_create_cancel(self):
        """
        Creates a new cancellation request for a charge. The charge must be in a
        cancellable state. Bank transfer and konbini charges that have already been
        paid cannot be cancelled.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"
        body = APIHelper.json_deserialize(
            "{\"metadata\":{\"order_id\":\"ORD-987\"}}",
            CancelCreateRequest.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.create_cancel(
            store_id,
            charge_id,
            idempotency_key,
            body,
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
            "{\"id\":\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\",\"charge_id\":\"6efb4e5"
            "c-690a-40f3-a4f1-0e19c5f84e98\",\"store_id\":\"76cf4a64-02bc-4cb3-9a28-7"
            "4622e5928a1\",\"status\":\"pending\",\"error\":null,\"metadata\":{},\"mo"
            "de\":\"live\",\"created_on\":\"2026-04-09T07:35:50.000000Z\",\"updated_o"
            "n\":\"2026-04-09T07:35:50.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_cancel(self):
        """
        Retrieves a specific cancel by ID. Supports long-polling by appending
        `?polling=true` to wait for a status change (up to the server timeout).
        Requires a secret-bearing token.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        polling = False

        # Perform the API call through the SDK function
        result = self.controller.get_cancel(
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
            "{\"id\":\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\",\"charge_id\":\"6efb4e5"
            "c-690a-40f3-a4f1-0e19c5f84e98\",\"store_id\":\"76cf4a64-02bc-4cb3-9a28-7"
            "4622e5928a1\",\"status\":\"successful\",\"error\":null,\"metadata\":{},"
            "\"mode\":\"live\",\"created_on\":\"2026-04-09T07:35:50.000000Z\",\"updat"
            "ed_on\":\"2026-04-09T07:36:00.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_cancel(self):
        """
        Updates metadata on an existing cancel. Requires a secret-bearing token.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        charge_id = "6efb4e5c-690a-40f3-a4f1-0e19c5f84e98"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        body = APIHelper.json_deserialize(
            "{\"metadata\":{\"order_id\":\"12345\"}}",
            CancelUpdateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.update_cancel(
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
            "{\"id\":\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\",\"charge_id\":\"6efb4e5"
            "c-690a-40f3-a4f1-0e19c5f84e98\",\"store_id\":\"76cf4a64-02bc-4cb3-9a28-7"
            "4622e5928a1\",\"status\":\"successful\",\"error\":null,\"metadata\":{\"o"
            "rder_id\":\"12345\"},\"mode\":\"live\",\"created_on\":\"2026-04-09T07:35"
            ":50.000000Z\",\"updated_on\":\"2026-04-09T08:00:00.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

