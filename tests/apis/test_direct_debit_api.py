
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
from univapayclientsdk.models.direct_debit_bank_account_create_request import (
    DirectDebitBankAccountCreateRequest,
)
from univapayclientsdk.models.direct_debit_bank_account_update_request import (
    DirectDebitBankAccountUpdateRequest,
)
from univapayclientsdk.models.direct_debit_bank_transfer_create_request import (
    DirectDebitBankTransferCreateRequest,
)
from univapayclientsdk.models.direct_debit_bank_transfer_patch_request import (
    DirectDebitBankTransferPatchRequest,
)


class DirectDebitApiTests(ApiTestBase):
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
        cls.controller = cls.client.direct_debit
        cls.response_catcher = cls.controller.http_call_back

    def test_get_direct_debit_configuration(self):
        """
        Retrieves the merchant's direct debit configuration — whether direct debit is
        enabled and which monthly debit cycle applies.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"

        # Perform the API call through the SDK function
        result = self.controller.get_direct_debit_configuration(
            merchant_id,
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
            "{\"legacy_id\":\"1283794\",\"enabled\":true,\"debit_date\":\"fourteen\","
            "\"consignor_code\":\"135456\",\"classifier\":\"99\",\"signature\":\"モモサン"
            "\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_direct_debit_notification_configuration(self):
        """
        Retrieves which direct debit email notifications the merchant has opted into.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"

        # Perform the API call through the SDK function
        result = self.controller.get_direct_debit_notification_configuration(
            merchant_id,
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
            "{\"notify_deadline_mailing\":true,\"notify_deadline_debit\":true,\"notif"
            "y_debit_update\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_direct_debit_current_schedule(self):
        """
        Retrieves the key dates for the debit cycle currently in progress, based on
        the merchant's configured cycle. Compare
        `merchant_bank_transfer_upload_deadline` against today to decide whether
        transfers can still be registered or edited this month.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"

        # Perform the API call through the SDK function
        result = self.controller.get_direct_debit_current_schedule(
            merchant_id,
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
            "{\"merchant_bank_account_transfer_date\":\"2026-03-14\",\"merchant_bank_"
            "account_registration_deadline\":\"2026-02-20\",\"merchant_bank_transfer_"
            "upload_deadline\":\"2026-03-04\",\"platform_result_registration_date\":"
            "\"2026-03-24\",\"platform_scheduled_payout\":\"2026-03-31\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_direct_debit_bank_accounts(self):
        """
        Lists the consumer bank accounts registered for direct debit under this
        merchant.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        limit = 10
        cursor = "1098116"
        cursor_direction = "desc"
        user_number = "SD02688328"
        bank_account_id = "1098116"
        bank_code = "0012"
        bank_name = "ﾗｸﾃﾝｷﾞﾝｺｳ"
        branch_code = "120"
        bank_account_type = "regular"
        bank_account_number = "1234567"
        bank_account_name = "ﾀﾅｶﾕﾐｺ"
        registration_origin = "merchant_console"
        bank_account_status = "active"
        mfrom = "2026-04-01T00:00:00Z"
        to = "2026-04-30T23:59:59.999Z"

        # Perform the API call through the SDK function
        result = self.controller.list_direct_debit_bank_accounts(
            merchant_id,
            limit,
            cursor,
            cursor_direction,
            user_number,
            bank_account_id,
            bank_code,
            bank_name,
            branch_code,
            bank_account_type,
            bank_account_number,
            bank_account_name,
            registration_origin,
            bank_account_status,
            mfrom,
            to,
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
            "{\"items\":[{\"id\":\"1098116\",\"legacy_store_id\":\"1283794\",\"mercha"
            "nt_id\":\"01234567-89ab-cdef-0123-456789abcdef\",\"user_number\":\"SD026"
            "88328\",\"bank_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷﾞﾝｺｳ\",\"branch_code"
            "\":\"120\",\"bank_account_type\":\"regular\",\"bank_account_name\":\"ﾀﾅｶ"
            "ﾕﾐｺ\",\"bank_account_number\":\"1234567\",\"registration_origin\":\"merc"
            "hant_console\",\"status\":\"active\",\"created_on\":\"2026-04-09T07:35:5"
            "0.000Z\",\"updated_on\":\"2026-04-09T07:35:50.000Z\"},{\"id\":\"1098117"
            "\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01234567-89ab-cdef-"
            "0123-456789abcdef\",\"user_number\":\"SD02688329\",\"bank_code\":\"0009"
            "\",\"bank_name\":\"ﾐﾂｲｽﾐﾄﾓ\",\"branch_code\":\"221\",\"bank_account_type"
            "\":\"current\",\"bank_account_name\":\"ｽｽﾞｷﾀﾛｳ\",\"bank_account_number\""
            ":\"7654321\",\"registration_origin\":\"anywhere\",\"status\":\"inactive"
            "\",\"created_on\":\"2026-04-10T09:12:04.000Z\",\"updated_on\":\"2026-04-"
            "12T11:03:41.000Z\"}],\"has_more\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_create_direct_debit_bank_account(self):
        """
        Registers a consumer bank account for direct debit. The account is created and
        then verified against the bank, so it starts out unusable — poll its `status`
        until it becomes `active` (or `registration_failed`) before scheduling
        transfers against it.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        body = APIHelper.json_deserialize(
            "{\"user_number\":\"SD02688328\",\"bank_code\":\"0012\",\"bank_name\":\"ﾗ"
            "ｸﾃﾝｷﾞﾝｺｳ\",\"branch_code\":\"120\",\"bank_account_type\":\"regular\",\"b"
            "ank_account_name\":\"ﾀﾅｶﾕﾐｺ\",\"bank_account_number\":\"1234567\"}",
            DirectDebitBankAccountCreateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.create_direct_debit_bank_account(
            merchant_id,
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
            "{\"id\":\"1098116\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"user_number\":\"SD02688328\",\"ba"
            "nk_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷﾞﾝｺｳ\",\"branch_code\":\"120\","
            "\"bank_account_type\":\"regular\",\"bank_account_name\":\"ﾀﾅｶﾕﾐｺ\",\"ban"
            "k_account_number\":\"1234567\",\"registration_origin\":\"merchant_consol"
            "e\",\"status\":\"active\",\"created_on\":\"2026-04-09T07:35:50.000Z\",\""
            "updated_on\":\"2026-04-09T07:35:50.000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_direct_debit_bank_account(self):
        """
        Retrieves a single registered bank account, including its current verification
        status.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_account_id = "1098116"

        # Perform the API call through the SDK function
        result = self.controller.get_direct_debit_bank_account(
            merchant_id,
            bank_account_id,
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
            "{\"id\":\"1098116\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"user_number\":\"SD02688328\",\"ba"
            "nk_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷﾞﾝｺｳ\",\"branch_code\":\"120\","
            "\"bank_account_type\":\"regular\",\"bank_account_name\":\"ﾀﾅｶﾕﾐｺ\",\"ban"
            "k_account_number\":\"1234567\",\"registration_origin\":\"merchant_consol"
            "e\",\"status\":\"active\",\"created_on\":\"2026-04-09T07:35:50.000Z\",\""
            "updated_on\":\"2026-04-09T07:35:50.000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_direct_debit_bank_account(self):
        """
        Updates a registered bank account. Changing bank details re-triggers
        verification with the bank. Transfers already registered keep the details they
        were created with.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_account_id = "1098116"
        body = APIHelper.json_deserialize(
            "{\"bank_account_name\":\"ﾀﾅｶﾕﾐｺ\"}",
            DirectDebitBankAccountUpdateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.update_direct_debit_bank_account(
            merchant_id,
            bank_account_id,
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
            "{\"id\":\"1098116\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"user_number\":\"SD02688328\",\"ba"
            "nk_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷﾞﾝｺｳ\",\"branch_code\":\"120\","
            "\"bank_account_type\":\"regular\",\"bank_account_name\":\"ﾀﾅｶﾕﾐｺ\",\"ban"
            "k_account_number\":\"1234567\",\"registration_origin\":\"merchant_consol"
            "e\",\"status\":\"active\",\"created_on\":\"2026-04-09T07:35:50.000Z\",\""
            "updated_on\":\"2026-04-09T07:35:50.000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_deactivate_direct_debit_bank_account(self):
        """
        Deactivates a bank account so no further transfers can be registered against
        it. The record is retained (status becomes `inactive`) rather than deleted,
        and can be re-enabled later.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_account_id = "1098116"

        # Perform the API call through the SDK function
        result = self.controller.deactivate_direct_debit_bank_account(
            merchant_id,
            bank_account_id,
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
            "{\"id\":\"1098116\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"user_number\":\"SD02688328\",\"ba"
            "nk_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷﾞﾝｺｳ\",\"branch_code\":\"120\","
            "\"bank_account_type\":\"regular\",\"bank_account_name\":\"ﾀﾅｶﾕﾐｺ\",\"ban"
            "k_account_number\":\"1234567\",\"registration_origin\":\"merchant_consol"
            "e\",\"status\":\"inactive\",\"created_on\":\"2026-04-09T07:35:50.000Z\","
            "\"updated_on\":\"2026-04-14T02:11:07.000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_reenable_direct_debit_bank_account(self):
        """
        Returns a deactivated bank account to `active` so transfers can be registered
        against it again. The account must currently be `inactive`.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_account_id = "1098116"
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.reenable_direct_debit_bank_account(
            merchant_id,
            bank_account_id,
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
            "{\"id\":\"1098116\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"user_number\":\"SD02688328\",\"ba"
            "nk_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷﾞﾝｺｳ\",\"branch_code\":\"120\","
            "\"bank_account_type\":\"regular\",\"bank_account_name\":\"ﾀﾅｶﾕﾐｺ\",\"ban"
            "k_account_number\":\"1234567\",\"registration_origin\":\"merchant_consol"
            "e\",\"status\":\"active\",\"created_on\":\"2026-04-09T07:35:50.000Z\",\""
            "updated_on\":\"2026-04-09T07:35:50.000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_create_direct_debit_bank_transfer(self):
        """
        Schedules a pull of funds from an active bank account. The transfer is queued
        for the merchant's next debit cycle and stays editable until that cycle's
        upload deadline passes.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_account_id = "1098116"
        body = APIHelper.json_deserialize(
            "{\"amount\":1000}",
            DirectDebitBankTransferCreateRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.create_direct_debit_bank_transfer(
            merchant_id,
            bank_account_id,
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
            "{\"id\":\"2594976\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"bank_account_id\":\"1098116\",\"u"
            "ser_number\":\"SD02688328\",\"bank_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷ"
            "ﾞﾝｺｳ\",\"branch_code\":\"120\",\"bank_account_type\":\"regular\",\"bank_"
            "account_name\":\"ﾀﾅｶﾕﾐｺ\",\"bank_account_number\":\"1234567\",\"amount\""
            ":1000,\"debit_date\":\"fourteen\",\"calculated_debit_date\":\"2026-03-14"
            "\",\"lock\":\"unlocked\",\"status\":\"awaiting\",\"error\":null,\"create"
            "d_on\":\"2026-04-09T07:35:50.000Z\",\"updated_on\":\"2026-04-09T07:35:50"
            ".000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_list_direct_debit_bank_transfers(self):
        """
        Lists the direct debit transfers registered under this merchant, across all
        bank accounts.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        limit = 10
        cursor = "1098116"
        cursor_direction = "desc"
        bank_transfer_id = "2594976"
        bank_transfer_start = "2026-01"
        bank_transfer_end = "2026-03"
        debit_date = "fourteen"
        user_number = "SD02688328"
        bank_account_number = "1234567"
        bank_account_name = "ﾀﾅｶﾕﾐｺ"
        lock_status = "unlocked"
        bank_transfer_status = "awaiting"

        # Perform the API call through the SDK function
        result = self.controller.list_direct_debit_bank_transfers(
            merchant_id,
            limit,
            cursor,
            cursor_direction,
            bank_transfer_id,
            bank_transfer_start,
            bank_transfer_end,
            debit_date,
            user_number,
            bank_account_number,
            bank_account_name,
            lock_status,
            bank_transfer_status,
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
            "{\"items\":[{\"id\":\"2594976\",\"legacy_store_id\":\"1283794\",\"mercha"
            "nt_id\":\"01234567-89ab-cdef-0123-456789abcdef\",\"bank_account_id\":\"1"
            "098116\",\"user_number\":\"SD02688328\",\"bank_code\":\"0012\",\"bank_na"
            "me\":\"ﾗｸﾃﾝｷﾞﾝｺｳ\",\"branch_code\":\"120\",\"bank_account_type\":\"regul"
            "ar\",\"bank_account_name\":\"ﾀﾅｶﾕﾐｺ\",\"bank_account_number\":\"1234567"
            "\",\"amount\":1000,\"debit_date\":\"fourteen\",\"calculated_debit_date\""
            ":\"2026-03-14\",\"lock\":\"unlocked\",\"status\":\"awaiting\",\"error\":"
            "null,\"created_on\":\"2026-04-09T07:35:50.000Z\",\"updated_on\":\"2026-0"
            "4-09T07:35:50.000Z\"},{\"id\":\"2594977\",\"legacy_store_id\":\"1283794"
            "\",\"merchant_id\":\"01234567-89ab-cdef-0123-456789abcdef\",\"bank_accou"
            "nt_id\":\"1098117\",\"user_number\":\"SD02688329\",\"bank_code\":\"0009"
            "\",\"bank_name\":\"ﾐﾂｲｽﾐﾄﾓ\",\"branch_code\":\"221\",\"bank_account_type"
            "\":\"current\",\"bank_account_name\":\"ｽｽﾞｷﾀﾛｳ\",\"bank_account_number\""
            ":\"7654321\",\"amount\":1850,\"debit_date\":\"twenty_seven\",\"calculate"
            "d_debit_date\":\"2026-03-27\",\"lock\":\"locked\",\"status\":\"failed\","
            "\"error\":\"insufficient_funds\",\"created_on\":\"2026-04-10T09:12:04.00"
            "0Z\",\"updated_on\":\"2026-04-12T11:03:41.000Z\"}],\"has_more\":false}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_get_direct_debit_bank_transfer(self):
        """
        Retrieves a single transfer. Poll this after the cycle's result registration
        date to pick up the outcome and, on failure, the bank's reason.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_transfer_id = "2594976"

        # Perform the API call through the SDK function
        result = self.controller.get_direct_debit_bank_transfer(
            merchant_id,
            bank_transfer_id,
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
            "{\"id\":\"2594976\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"bank_account_id\":\"1098116\",\"u"
            "ser_number\":\"SD02688328\",\"bank_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷ"
            "ﾞﾝｺｳ\",\"branch_code\":\"120\",\"bank_account_type\":\"regular\",\"bank_"
            "account_name\":\"ﾀﾅｶﾕﾐｺ\",\"bank_account_number\":\"1234567\",\"amount\""
            ":1000,\"debit_date\":\"fourteen\",\"calculated_debit_date\":\"2026-03-14"
            "\",\"lock\":\"unlocked\",\"status\":\"awaiting\",\"error\":null,\"create"
            "d_on\":\"2026-04-09T07:35:50.000Z\",\"updated_on\":\"2026-04-09T07:35:50"
            ".000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_update_direct_debit_bank_transfer(self):
        """
        Changes a scheduled transfer's amount. Only permitted while the transfer is
        `unlocked` — once its cycle's upload deadline passes the amount is fixed.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_transfer_id = "2594976"
        body = APIHelper.json_deserialize(
            "{\"amount\":1850}",
            DirectDebitBankTransferPatchRequest.from_dictionary,
        )
        idempotency_key = "f64be872-353d-4c3c-84cb-3dc617fe89f7"

        # Perform the API call through the SDK function
        result = self.controller.update_direct_debit_bank_transfer(
            merchant_id,
            bank_transfer_id,
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
            "{\"id\":\"2594976\",\"legacy_store_id\":\"1283794\",\"merchant_id\":\"01"
            "234567-89ab-cdef-0123-456789abcdef\",\"bank_account_id\":\"1098116\",\"u"
            "ser_number\":\"SD02688328\",\"bank_code\":\"0012\",\"bank_name\":\"ﾗｸﾃﾝｷ"
            "ﾞﾝｺｳ\",\"branch_code\":\"120\",\"bank_account_type\":\"regular\",\"bank_"
            "account_name\":\"ﾀﾅｶﾕﾐｺ\",\"bank_account_number\":\"1234567\",\"amount\""
            ":1000,\"debit_date\":\"fourteen\",\"calculated_debit_date\":\"2026-03-14"
            "\",\"lock\":\"unlocked\",\"status\":\"awaiting\",\"error\":null,\"create"
            "d_on\":\"2026-04-09T07:35:50.000Z\",\"updated_on\":\"2026-04-09T07:35:50"
            ".000Z\"}",
        )
        received_body = APIHelper.json_deserialize(
            self.response_catcher.response.text,
        )
        assert ComparisonHelper.match_body(
            expected_body,
            received_body,
        )

    def test_delete_direct_debit_bank_transfer(self):
        """
        Cancels a scheduled transfer so it is not sent to the bank. Only permitted
        while the transfer is `unlocked`.
        """
        # Parameters for the API call
        merchant_id = "01234567-89ab-cdef-0123-456789abcdef"
        bank_transfer_id = "2594976"

        # Perform the API call through the SDK function
        self.controller.delete_direct_debit_bank_transfer(
            merchant_id,
            bank_transfer_id,
        )
        # Test response code
        assert self.response_catcher.response.status_code == 204

