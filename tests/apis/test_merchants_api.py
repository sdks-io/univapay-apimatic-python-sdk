
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


class MerchantsApiTests(ApiTestBase):
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
        cls.controller = cls.client.merchants
        cls.response_catcher = cls.controller.http_call_back

    def test_get_current_merchant(self):
        """
        Returns merchant identity and the effective configuration resolved from bearer
        credentials. Treat this as the canonical introspection endpoint for merchant
        integrations.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_current_merchant()
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
            "{\"id\":\"11ef0000-0000-4000-8000-000000000020\",\"verification_data_id"
            "\":\"11ef0000-0000-4000-8000-000000000021\",\"name\":\"Example Merchant"
            "\",\"email\":\"owner@example.com\",\"notification_email\":\"alerts@examp"
            "le.com\",\"finance_notification_email\":\"finance@example.com\",\"verifi"
            "ed\":true,\"configuration\":{\"percent_fee\":3.6,\"country\":\"JP\",\"la"
            "nguage\":\"ja\",\"minimum_charge_amounts\":[{\"amount\":100,\"currency\""
            ":\"JPY\"}],\"maximum_charge_amounts\":[{\"amount\":100000,\"currency\":"
            "\"JPY\"}],\"user_transactions_configuration\":{\"enabled\":true,\"notify"
            "_customer\":true,\"notify_on_webhook_failure\":true},\"card_configuratio"
            "n\":{\"enabled\":true,\"debit_enabled\":true,\"prepaid_enabled\":false,"
            "\"three_ds_required\":true},\"online_configuration\":{\"enabled\":true},"
            "\"bank_transfer_configuration\":{\"enabled\":true,\"match_amount\":true,"
            "\"expiration\":\"P7D\"},\"qr_scan_configuration\":{\"enabled\":true,\"fo"
            "rbidden_qr_scan_gateways\":[\"wechat\"]},\"convenience_configuration\":{"
            "\"enabled\":true,\"expiration\":\"P3D\"},\"paidy_configuration\":{\"enab"
            "led\":false},\"recurring_token_configuration\":{\"recurring_type\":\"inf"
            "inite\",\"charge_wait_period\":\"P7D\",\"card_charge_cvv_confirmation\":"
            "{\"enabled\":false}},\"security_configuration\":{\"card_charge_cooldown"
            "\":\"PT5M\",\"subscription_cooldown\":\"PT10M\",\"restrict_ip_after_fail"
            "ed_charge\":{\"enabled\":true,\"count\":5,\"cooldown\":\"PT1H\"},\"refun"
            "d_percent_limit\":100,\"confirmation_required\":false,\"min_refund_thres"
            "hold\":100,\"limit_refund_by_sales\":{\"enabled\":true,\"period\":\"mont"
            "hly\",\"rolling_window\":true}},\"installments_configuration\":{\"enable"
            "d\":true,\"card_processor\":{\"revolving\":true,\"fixed_cycle\":true},\""
            "supported_payment_types\":[\"card\"],\"min_charge_amount\":{\"amount\":3"
            "000,\"currency\":\"JPY\"},\"max_payout_period\":\"P12M\",\"only_with_pro"
            "cessor\":true},\"card_brand_percent_fees\":{\"visa\":3.6,\"mastercard\":"
            "3.6,\"jcb\":3.8}},\"created_on\":\"2026-04-09T07:35:50.000000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

