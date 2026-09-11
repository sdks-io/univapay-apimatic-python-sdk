
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


class TransactionHistoryApiTests(ApiTestBase):
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
        cls.controller = cls.client.transaction_history
        cls.response_catcher = cls.controller.http_call_back

    def test_list_transaction_history(self):
        """
        Returns a paginated, searchable history of charges and refunds across all of
        the merchant's stores, combining both resource types into a single unified row
        shape.
        """
        # Parameters for the API call
        mode = "test"
        short_id = "8bfc29"
        mfrom = "2026-04-01T00:00:00Z"
        to = "2026-04-30T23:59:59.999Z"
        status = "successful"
        mtype = "charge"
        search = "Taro Yamada"
        email = "user@example.com"
        id = "11ef0000-0000-4000-8000-000000000070"
        metadata = "order_id: 12345"
        card_exp = "2026-04"
        card_last_four = "4242"
        cardholder = "TARO YAMADA"
        card_brand = APIHelper.json_deserialize(
            "[\"visa\"]",
        )
        brand = APIHelper.json_deserialize(
            "[\"visa\"]",
        )
        brands = APIHelper.json_deserialize(
            "[\"visa\",\"jcb\"]",
        )
        currency = "JPY"
        service_provider = "credit"
        service_providers = APIHelper.json_deserialize(
            "[\"credit\",\"paidy\"]",
        )
        gateway_transaction_id = "gw-txn-00123456"
        bank_transfer_payment_statuses = APIHelper.json_deserialize(
            "[\"exact\"]",
        )
        bank_transfer_latest_deposit_date_from = "2026-04-01T00:00:00Z"
        bank_transfer_latest_deposit_date_to = "2026-04-30T23:59:59.999Z"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_transaction_history(
            mode,
            short_id,
            mfrom,
            to,
            status,
            mtype,
            search,
            email,
            id,
            metadata,
            card_exp,
            card_last_four,
            cardholder,
            card_brand,
            brand,
            brands,
            currency,
            service_provider,
            service_providers,
            gateway_transaction_id,
            bank_transfer_payment_statuses,
            bank_transfer_latest_deposit_date_from,
            bank_transfer_latest_deposit_date_to,
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
            "{\"items\":[{\"store_id\":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"res"
            "ource_id\":\"11ef0000-0000-4000-8000-000000000070\",\"charge_id\":null,"
            "\"amount\":1000,\"currency\":\"JPY\",\"amount_formatted\":1000,\"type\":"
            "\"charge\",\"status\":\"successful\",\"metadata\":{},\"created_on\":\"20"
            "24-05-01T12:34:56.789Z\",\"mode\":\"test\",\"merchant_name\":\"Test merc"
            "hant\",\"store_name\":\"Test store\",\"payment_type\":\"card\",\"user_da"
            "ta\":{\"type\":\"charge\",\"cardholder_name\":\"Some Guy\",\"cardholder_"
            "email_address\":\"test4@univapay.com\",\"brand\":\"visa\",\"gateway\":\""
            "test\",\"service_provider\":\"credit\",\"refunds\":[{\"refund_id\":\"11e"
            "f0000-0000-4000-8000-000000000010\",\"amount\":500,\"currency\":\"JPY\","
            "\"amount_formatted\":500,\"status\":\"successful\"}]},\"bank_transfer_pa"
            "yment_status\":null,\"bank_transfer_latest_deposit_date\":null,\"mcp_tok"
            "en_id\":null,\"charge_type\":\"normal\"},{\"store_id\":\"11edf541-c42d-6"
            "53c-8c3d-dfe0a55f95c0\",\"resource_id\":\"11ef0000-0000-4000-8000-000000"
            "000010\",\"charge_id\":\"11ef0000-0000-4000-8000-000000000070\",\"amount"
            "\":500,\"currency\":\"JPY\",\"amount_formatted\":500,\"type\":\"refund\""
            ",\"status\":\"successful\",\"metadata\":{},\"created_on\":\"2024-05-01T1"
            "3:00:00.000000Z\",\"mode\":\"test\",\"merchant_name\":\"Test merchant\","
            "\"store_name\":\"Test store\",\"payment_type\":\"card\",\"user_data\":{"
            "\"type\":\"refund\",\"reason\":\"customer_request\"},\"bank_transfer_pay"
            "ment_status\":null,\"bank_transfer_latest_deposit_date\":null,\"mcp_toke"
            "n_id\":null,\"charge_type\":null}],\"has_more\":false,\"total_hits\":2}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_store_transaction_history(self):
        """
        Returns a paginated, searchable history of charges and refunds for a single
        store, combining both resource types into a single unified row shape.
        """
        # Parameters for the API call
        store_id = "0cab399b-5621-425b-993b-f8507eba1e78"
        mode = "test"
        short_id = "8bfc29"
        mfrom = "2026-04-01T00:00:00Z"
        to = "2026-04-30T23:59:59.999Z"
        status = "successful"
        mtype = "charge"
        search = "Taro Yamada"
        email = "user@example.com"
        id = "11ef0000-0000-4000-8000-000000000070"
        metadata = "order_id: 12345"
        card_exp = "2026-04"
        card_last_four = "4242"
        cardholder = "TARO YAMADA"
        card_brand = APIHelper.json_deserialize(
            "[\"visa\"]",
        )
        brand = APIHelper.json_deserialize(
            "[\"visa\"]",
        )
        brands = APIHelper.json_deserialize(
            "[\"visa\",\"jcb\"]",
        )
        currency = "JPY"
        service_provider = "credit"
        service_providers = APIHelper.json_deserialize(
            "[\"credit\",\"paidy\"]",
        )
        gateway_transaction_id = "gw-txn-00123456"
        bank_transfer_payment_statuses = APIHelper.json_deserialize(
            "[\"exact\"]",
        )
        bank_transfer_latest_deposit_date_from = "2026-04-01T00:00:00Z"
        bank_transfer_latest_deposit_date_to = "2026-04-30T23:59:59.999Z"
        limit = 10
        cursor = "3541d4fa-596d-428e-8a36-f274e1b3d505"
        cursor_direction = "desc"

        # Perform the API call through the SDK function
        result = self.controller.list_store_transaction_history(
            store_id,
            mode,
            short_id,
            mfrom,
            to,
            status,
            mtype,
            search,
            email,
            id,
            metadata,
            card_exp,
            card_last_four,
            cardholder,
            card_brand,
            brand,
            brands,
            currency,
            service_provider,
            service_providers,
            gateway_transaction_id,
            bank_transfer_payment_statuses,
            bank_transfer_latest_deposit_date_from,
            bank_transfer_latest_deposit_date_to,
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
            "{\"items\":[{\"store_id\":\"11edf541-c42d-653c-8c3d-dfe0a55f95c0\",\"res"
            "ource_id\":\"11ef0000-0000-4000-8000-000000000072\",\"charge_id\":null,"
            "\"amount\":2500,\"currency\":\"JPY\",\"amount_formatted\":2500,\"type\":"
            "\"charge\",\"status\":\"awaiting\",\"metadata\":{},\"created_on\":\"2024"
            "-05-03T10:00:00.000000Z\",\"mode\":\"live\",\"merchant_name\":\"Test mer"
            "chant\",\"store_name\":\"Test store\",\"payment_type\":\"bank_transfer\""
            ",\"user_data\":{\"type\":\"charge\",\"cardholder_email_address\":\"test_"
            "bank_transfer@test.com\",\"brand\":\"aozora_bank\",\"gateway\":\"aozora_"
            "bank\",\"service_provider\":\"bank_transfer\",\"refunds\":[]},\"bank_tra"
            "nsfer_payment_status\":\"unpaid\",\"bank_transfer_latest_deposit_date\":"
            "null,\"mcp_token_id\":null,\"charge_type\":\"normal\"}],\"has_more\":fal"
            "se,\"total_hits\":1}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

