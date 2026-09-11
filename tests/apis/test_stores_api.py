
"""
univapay_client_sdk

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: PLR0915, W291, W293, E501
from apimatic_core.utilities.comparison_helper import (
    ComparisonHelper,
)

from tests.apis.api_test_base import ApiTestBase
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.create_customer_id_request import (
    CreateCustomerIdRequest,
)


class StoresApiTests(ApiTestBase):
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
            "\"enabled\":true,\"match_amount\":true,\"expiration\":\"P7D\"},\"qr_scan"
            "_configuration\":{\"enabled\":true,\"forbidden_qr_scan_gateways\":[\"wec"
            "hat\"]},\"convenience_configuration\":{\"enabled\":true,\"expiration\":"
            "\"P3D\"},\"paidy_configuration\":{\"enabled\":false},\"recurring_token_c"
            "onfiguration\":{\"recurring_type\":\"infinite\",\"charge_wait_period\":"
            "\"P7D\",\"card_charge_cvv_confirmation\":{\"enabled\":false}},\"security"
            "_configuration\":{\"card_charge_cooldown\":\"PT5M\",\"subscription_coold"
            "own\":\"PT10M\",\"restrict_ip_after_failed_charge\":{\"enabled\":true,\""
            "count\":5,\"cooldown\":\"PT1H\"},\"refund_percent_limit\":100,\"confirma"
            "tion_required\":false,\"min_refund_threshold\":100,\"limit_refund_by_sal"
            "es\":{\"enabled\":true,\"period\":\"monthly\",\"rolling_window\":true}},"
            "\"installments_configuration\":{\"enabled\":true,\"card_processor\":{\"r"
            "evolving\":true,\"fixed_cycle\":true},\"supported_payment_types\":[\"car"
            "d\"],\"min_charge_amount\":{\"amount\":3000,\"currency\":\"JPY\"},\"max_"
            "payout_period\":\"P12M\",\"only_with_processor\":true},\"card_brand_perc"
            "ent_fees\":{\"visa\":3.6,\"mastercard\":3.6,\"jcb\":3.8}}}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_create_customer_id(self):
        """
        Derives a deterministic, store-scoped UUID from a local customer identifier
        supplied by the merchant. Calling this endpoint again with the same
        `customer_id` for the same store always returns the same UUID — the operation
        has no side effects (nothing is persisted), so it is safe to call repeatedly
        and does not require an `Idempotency-Key`. App Token Secret is required.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        body = APIHelper.json_deserialize(
            "{\"customer_id\":\"local-customer-1902\"}",
            CreateCustomerIdRequest.from_dictionary,
        )

        # Perform the API call through the SDK function
        result = self.controller.create_customer_id(
            store_id,
            body,
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
            "{\"customer_id\":\"8a3f1b8e-2c1a-4b7a-9c2e-6f6b6f6e2b10\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

