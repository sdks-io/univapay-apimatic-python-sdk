
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
from univapayclientsdk.models.webhook_create_request import (
    WebhookCreateRequest,
)
from univapayclientsdk.models.webhook_update_request import (
    WebhookUpdateRequest,
)


class WebhooksControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.webhooks
        cls.response_catcher = cls.controller.http_call_back

    def test_list_webhooks(self):
        """
        Returns a paginated list of webhooks for the specified store. Requires a
        secret-bearing token.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"
        active = True

        # Perform the API call through the SDK function
        result = self.controller.list_webhooks(
            store_id,
            limit,
            cursor,
            cursor_direction,
            active,
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
            "{\"items\":[{\"id\":\"d3e4f5a6-b7c8-9012-def0-123456789abc\",\"store_id"
            "\":\"76cf4a64-02bc-4cb3-9a28-74622e5928a1\",\"merchant_id\":\"01234567-8"
            "9ab-cdef-0123-456789abcdef\",\"triggers\":[\"charge_finished\",\"refund_"
            "finished\"],\"url\":\"https://example.com/webhooks/payments\",\"auth_tok"
            "en\":\"my-secret-token\",\"active\":true,\"is_integration\":false,\"crea"
            "ted_on\":\"2026-04-01T00:00:00.000000Z\",\"updated_on\":\"2026-04-02T00:"
            "00:00.000000Z\"},{\"id\":\"e4f5a6b7-c8d9-0123-ef01-23456789abcd\",\"stor"
            "e_id\":\"76cf4a64-02bc-4cb3-9a28-74622e5928a1\",\"merchant_id\":\"012345"
            "67-89ab-cdef-0123-456789abcdef\",\"triggers\":[\"subscription_payment\","
            "\"subscription_failure\"],\"url\":\"https://example.com/webhooks/subscri"
            "ptions\",\"auth_token\":null,\"active\":true,\"is_integration\":false,\""
            "created_on\":\"2026-04-03T08:30:00.000000Z\",\"updated_on\":\"2026-04-03"
            "T08:30:00.000000Z\"},{\"id\":\"f5a6b7c8-d9e0-1234-f012-3456789abcde\",\""
            "store_id\":\"76cf4a64-02bc-4cb3-9a28-74622e5928a1\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"triggers\":[\"cancel_finished\"],"
            "\"url\":\"https://example.com/webhooks/cancels\",\"auth_token\":\"legacy"
            "-token\",\"active\":false,\"is_integration\":false,\"created_on\":\"2026"
            "-03-20T12:00:00.000000Z\",\"updated_on\":\"2026-04-05T09:15:00.000000Z\""
            "}],\"has_more\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_create_webhook(self):
        """
        Creates a new webhook subscription for the specified store. Requires a
        secret-bearing token. Duplicate URLs within the same scope are not allowed.
        There is a maximum limit on the number of webhooks per store.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        body = APIHelper.json_deserialize(
            "{\"triggers\":[\"charge_finished\"],\"url\":\"https://example.com/webhoo"
            "ks/payments\",\"auth_token\":\"my-secret-token\"}",
            WebhookCreateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.create_webhook(
            store_id,
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
            "{\"id\":\"d3e4f5a6-b7c8-9012-def0-123456789abc\",\"store_id\":\"76cf4a64"
            "-02bc-4cb3-9a28-74622e5928a1\",\"merchant_id\":\"01234567-89ab-cdef-0123"
            "-456789abcdef\",\"triggers\":[\"charge_finished\",\"refund_finished\"],"
            "\"url\":\"https://example.com/webhooks/payments\",\"auth_token\":\"my-se"
            "cret-token\",\"active\":true,\"is_integration\":false,\"created_on\":\"2"
            "026-04-01T00:00:00.000000Z\",\"updated_on\":\"2026-04-01T00:00:00.000000"
            "Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_webhook(self):
        """
        Retrieves a specific webhook by ID.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"

        # Perform the API call through the SDK function
        result = self.controller.get_webhook(
            store_id,
            id,
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
            "{\"id\":\"d3e4f5a6-b7c8-9012-def0-123456789abc\",\"store_id\":\"76cf4a64"
            "-02bc-4cb3-9a28-74622e5928a1\",\"merchant_id\":\"01234567-89ab-cdef-0123"
            "-456789abcdef\",\"triggers\":[\"charge_finished\"],\"url\":\"https://exa"
            "mple.com/webhooks/payments\",\"active\":true}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_webhook(self):
        """
        Updates an existing webhook. All fields are optional; omitted fields are left
        unchanged. Duplicate URLs within the same scope are not allowed.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        body = APIHelper.json_deserialize(
            "{\"active\":false}",
            WebhookUpdateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.update_webhook(
            store_id,
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
            "{\"id\":\"d3e4f5a6-b7c8-9012-def0-123456789abc\",\"store_id\":\"76cf4a64"
            "-02bc-4cb3-9a28-74622e5928a1\",\"merchant_id\":\"01234567-89ab-cdef-0123"
            "-456789abcdef\",\"triggers\":[\"charge_finished\"],\"url\":\"https://exa"
            "mple.com/webhooks/v2\",\"active\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_delete_webhook(self):
        """
        Deactivates and deletes a webhook subscription.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"

        # Perform the API call through the SDK function
        self.controller.delete_webhook(
            store_id,
            id,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 204

    def test_list_webhook_events(self):
        """
        Returns a paginated list of webhook delivery events for the specified webhook.
        Each event captures the result of a single webhook delivery attempt.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_webhook_events(
            store_id,
            id,
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
            "{\"items\":[{\"id\":\"e1f2a3b4-c5d6-7890-efab-123456789cde\",\"webhook_i"
            "d\":\"d3e4f5a6-b7c8-9012-def0-123456789abc\",\"event\":\"charge_finished"
            "\",\"successful\":true,\"fired_on\":\"2026-04-09T07:36:00.000000Z\",\"er"
            "ror_message\":null,\"created_on\":\"2026-04-09T07:35:50.000000Z\"},{\"id"
            "\":\"f2a3b4c5-d6e7-8901-fabc-23456789cdef\",\"webhook_id\":\"d3e4f5a6-b7"
            "c8-9012-def0-123456789abc\",\"event\":\"refund_finished\",\"successful\""
            ":true,\"fired_on\":\"2026-04-10T11:00:05.000000Z\",\"error_message\":nul"
            "l,\"created_on\":\"2026-04-10T11:00:00.000000Z\"},{\"id\":\"a3b4c5d6-e7f"
            "8-9012-abcd-3456789cdef0\",\"webhook_id\":\"d3e4f5a6-b7c8-9012-def0-1234"
            "56789abc\",\"event\":\"cancel_finished\",\"successful\":false,\"fired_on"
            "\":\"2026-04-11T15:30:10.000000Z\",\"error_message\":\"Connection timed "
            "out after 10s\",\"created_on\":\"2026-04-11T15:30:00.000000Z\"}],\"has_m"
            "ore\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_redeliver_webhook_event(self):
        """
        Re-sends the webhook payload for a previously delivered (or failed) event.
        Returns 202 Accepted immediately; delivery is asynchronous.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"
        event_id = "e1f2a3b4-c5d6-7890-efab-123456789cde"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.redeliver_webhook_event(
            store_id,
            id,
            event_id,
            idempotency_key,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 202
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
            "{}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

