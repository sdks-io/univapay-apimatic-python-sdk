
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


class CheckoutApiTests(ApiTestBase):
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
        cls.controller = cls.client.checkout
        cls.response_catcher = cls.controller.http_call_back

    def test_get_checkout_info(self):
        """
        Returns the merchant's checkout configuration: enabled payment methods and
        their limits, installment/subscription plan settings, convenience-store and
        bank-transfer settings, widget theme, and per-brand feature support. Resolved
        entirely from the bearer credential — takes no parameters.
        """
        # Perform the API call through the SDK function
        result = self.controller.get_checkout_info()
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
            "{\"mode\":\"test\",\"recurring_token_privilege\":\"none\",\"name\":\"Tes"
            "t store\",\"card_configuration\":{\"enabled\":true,\"debit_enabled\":tru"
            "e,\"prepaid_enabled\":true,\"debit_authorization_enabled\":false,\"prepa"
            "id_authorization_enabled\":false,\"only_direct_currency\":false,\"forbid"
            "den_card_brands\":null,\"allowed_countries_by_ip\":null,\"foreign_cards_"
            "allowed\":true,\"fail_on_new_email\":null,\"card_limit\":null,\"allow_em"
            "pty_cvv\":null,\"allow_direct_token_creation\":true,\"three_ds_required"
            "\":false,\"three_ds_address_required\":false,\"three_ds_skip_enabled\":f"
            "alse,\"three_ds_phone_number_required\":true},\"subscription_configurati"
            "on\":{\"enabled\":true},\"installments_configuration\":{\"enabled\":true"
            ",\"card_processor\":{\"revolving\":true,\"fixed_cycle\":true},\"supporte"
            "d_payment_types\":[\"card\"],\"min_charge_amount\":{\"amount\":1000,\"am"
            "ount_formatted\":1000,\"currency\":\"JPY\"},\"max_payout_period\":\"P2Y"
            "\",\"only_with_processor\":true},\"subscription_plan_configuration\":{\""
            "enabled\":true,\"fixed_cycle\":true,\"fixed_cycle_amount\":true,\"suppor"
            "ted_payment_types\":[\"card\"],\"min_charge_amount\":null,\"max_payout_p"
            "eriod\":null},\"checkout_configuration\":{\"ec_email\":{\"enabled\":fals"
            "e},\"ec_products\":{\"enabled\":false}},\"qr_scan_configuration\":{\"ena"
            "bled\":true,\"forbidden_qr_scan_gateways\":null},\"convenience_configura"
            "tion\":{\"enabled\":true,\"expiration\":\"PT720H\",\"expiration_time_shi"
            "ft\":{\"enabled\":false}},\"paidy_configuration\":{\"enabled\":true},\"p"
            "aidy_public_key\":null,\"logo_image\":null,\"theme\":{\"colors\":{\"main"
            "_background\":\"#FFFFFF\",\"secondary_background\":\"#F5F8FC\",\"main_co"
            "lor\":\"#4C5F85\",\"main_text\":\"#FFFFFF\",\"primary_text\":\"#4C5F85\""
            ",\"secondary_text\":\"#4C5F85\",\"base_text\":\"#4C5F85\",\"body_backgro"
            "und\":\"#FFFFFF\"}},\"recurring_card_charge_cvv_confirmation\":{\"enable"
            "d\":false,\"threshold\":null},\"online_configuration\":{\"enabled\":true"
            "},\"bank_transfer_configuration\":{\"enabled\":true,\"match_amount\":\"d"
            "isabled\",\"expiration\":\"PT72H\",\"expiration_time_shift\":{\"enabled"
            "\":false},\"virtual_bank_accounts_threshold\":5,\"virtual_bank_accounts_"
            "fetch_count\":10,\"default_extension_period\":\"PT168H\",\"maximum_exten"
            "sion_period\":\"PT168H\",\"automatic_extension_enabled\":false,\"charge_"
            "request_notification_enabled\":false,\"charge_request_canceled_notificat"
            "ion_enabled\":false,\"charge_expired_notification_enabled\":false,\"depo"
            "sit_received_notification_enabled\":false,\"deposit_insufficient_notific"
            "ation_enabled\":false,\"deposit_exceeded_notification_enabled\":false,\""
            "extension_notification_enabled\":false,\"remind_notification_period\":\""
            "PT168H\",\"remind_notification_enabled\":false},\"supported_brands\":[{"
            "\"payment_type\":\"card\",\"brand\":\"visa\",\"card_brand\":\"visa\",\"d"
            "ynamic_info\":false,\"support_auth_capture\":true,\"requires_full_name\""
            ":false,\"requires_cvv\":true,\"countries_allowed\":null,\"supported_curr"
            "encies\":null,\"cvv_auth\":false,\"installment_capable\":true,\"mcp_capa"
            "ble\":false,\"mcp_only\":false},{\"payment_type\":\"qr_merchant\",\"bran"
            "d\":\"alipay_merchant_qr\",\"qr_brand\":\"alipay_merchant_qr\",\"dynamic"
            "_info\":false,\"support_auth_capture\":false,\"requires_full_name\":fals"
            "e,\"requires_cvv\":false,\"countries_allowed\":null,\"supported_currenci"
            "es\":null,\"cvv_auth\":false,\"installment_capable\":false,\"mcp_capable"
            "\":false,\"mcp_only\":false}]}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

