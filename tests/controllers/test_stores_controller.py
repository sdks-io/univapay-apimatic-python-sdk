
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


class StoresControllerTests(ControllerTestBase):
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
        cls.controller = cls.client.stores
        cls.response_catcher = cls.controller.http_call_back

    def test_list_stores(self):
        """
        Returns stores visible to the current merchant credential. Supports cursor
        pagination plus `short_id` and free-text `search` filters.
        """
        # Parameters for the API call
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"
        short_id = "st_01hxy9p8zw4d"
        search = "tokyo"

        # Perform the API call through the SDK function
        result = self.controller.list_stores(
            limit,
            cursor,
            cursor_direction,
            short_id,
            search,
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
            "{\"items\":[{\"id\":\"11ef0000-0000-4000-8000-000000000022\",\"name\":\""
            "Tokyo Store\",\"merchant_name\":\"Example Merchant\",\"created_on\":\"20"
            "26-04-09T07:35:50.000000Z\"},{\"id\":\"11ef0000-0000-4000-8000-000000000"
            "023\",\"name\":\"Osaka Store\",\"merchant_name\":\"Example Merchant\",\""
            "created_on\":\"2026-04-10T09:12:30.000000Z\"},{\"id\":\"11ef0000-0000-40"
            "00-8000-000000000024\",\"name\":\"Online Store\",\"merchant_name\":\"Exa"
            "mple Merchant\",\"created_on\":\"2026-04-12T14:45:05.000000Z\"}],\"has_m"
            "ore\":false,\"total_hits\":3}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_store(self):
        """
        Returns a single store plus its resolved configuration snapshot for the
        current merchant context.
        """
        # Parameters for the API call
        id = "c4e87129-cad4-47fb-8ded-b4c0a4ae0dd4"

        # Perform the API call through the SDK function
        result = self.controller.get_store(
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
            "{\"id\":\"11ef0000-0000-4000-8000-000000000022\",\"name\":\"Tokyo Store"
            "\",\"created_on\":\"2026-04-09T07:35:50.000000Z\",\"configuration\":{\"p"
            "ercent_fee\":3.6,\"country\":\"JP\",\"language\":\"ja\",\"minimum_charge"
            "_amounts\":[{\"amount\":100,\"currency\":\"JPY\"}],\"maximum_charge_amou"
            "nts\":[{\"amount\":100000,\"currency\":\"JPY\"}],\"user_transactions_con"
            "figuration\":{\"enabled\":true,\"notify_customer\":true,\"notify_on_webh"
            "ook_failure\":true},\"card_configuration\":{\"enabled\":true,\"debit_ena"
            "bled\":true,\"prepaid_enabled\":false,\"three_ds_required\":true},\"onli"
            "ne_configuration\":{\"enabled\":true},\"bank_transfer_configuration\":{"
            "\"enabled\":true,\"match_amount\":true,\"expiration\":\"P7D\"}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

