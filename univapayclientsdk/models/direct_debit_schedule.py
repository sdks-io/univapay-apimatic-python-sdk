"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from univapayclientsdk.api_helper import APIHelper


class DirectDebitSchedule(object):
    """Implementation of the 'DirectDebitSchedule' model.

    The key dates for one debit cycle. Use these to work out whether the current
    month's registration window is still open.

    Attributes:
        merchant_bank_account_transfer_date (date): The date funds are pulled from
            consumer accounts (指定振替日).
        merchant_bank_account_registration_deadline (date): The date by which the
            bank must receive the signed direct debit mandate (振替依頼書到着期限).
        merchant_bank_transfer_upload_deadline (date): The last date transfers can be
            registered or edited for this cycle (振替データアップロード期限). After this,
            transfers lock.
        platform_result_registration_date (date): The date transfer results are
            reflected on the platform (振替結果反映日).
        platform_scheduled_payout (date): The date collected funds are paid out to
            the merchant (支払日).
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "merchant_bank_account_transfer_date": "merchant_bank_account_transfer_date",
        "merchant_bank_account_registration_deadline":
            "merchant_bank_account_registration_deadline",
        "merchant_bank_transfer_upload_deadline":
            "merchant_bank_transfer_upload_deadline",
        "platform_result_registration_date": "platform_result_registration_date",
        "platform_scheduled_payout": "platform_scheduled_payout",
    }

    _optionals = [
        "merchant_bank_account_transfer_date",
        "merchant_bank_account_registration_deadline",
        "merchant_bank_transfer_upload_deadline",
        "platform_result_registration_date",
        "platform_scheduled_payout",
    ]

    def __init__(
        self,
        merchant_bank_account_transfer_date=APIHelper.SKIP,
        merchant_bank_account_registration_deadline=APIHelper.SKIP,
        merchant_bank_transfer_upload_deadline=APIHelper.SKIP,
        platform_result_registration_date=APIHelper.SKIP,
        platform_scheduled_payout=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a DirectDebitSchedule instance."""
        # Initialize members of the class
        if merchant_bank_account_transfer_date is not APIHelper.SKIP:
            self.merchant_bank_account_transfer_date =\
                 merchant_bank_account_transfer_date
        if merchant_bank_account_registration_deadline is not APIHelper.SKIP:
            self.merchant_bank_account_registration_deadline =\
                 merchant_bank_account_registration_deadline
        if merchant_bank_transfer_upload_deadline is not APIHelper.SKIP:
            self.merchant_bank_transfer_upload_deadline =\
                 merchant_bank_transfer_upload_deadline
        if platform_result_registration_date is not APIHelper.SKIP:
            self.platform_result_registration_date =\
                 platform_result_registration_date
        if platform_scheduled_payout is not APIHelper.SKIP:
            self.platform_scheduled_payout = platform_scheduled_payout

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        merchant_bank_account_transfer_date = dateutil.parser.parse(
            dictionary.get("merchant_bank_account_transfer_date")).date()\
            if dictionary.get("merchant_bank_account_transfer_date") else APIHelper.SKIP
        merchant_bank_account_registration_deadline = dateutil.parser.parse(
            dictionary.get("merchant_bank_account_registration_deadline")).date()\
            if dictionary.get("merchant_bank_account_registration_deadline") else APIHelper.SKIP
        merchant_bank_transfer_upload_deadline = dateutil.parser.parse(
            dictionary.get("merchant_bank_transfer_upload_deadline")).date()\
            if dictionary.get("merchant_bank_transfer_upload_deadline") else APIHelper.SKIP
        platform_result_registration_date = dateutil.parser.parse(
            dictionary.get("platform_result_registration_date")).date()\
            if dictionary.get("platform_result_registration_date") else APIHelper.SKIP
        platform_scheduled_payout = dateutil.parser.parse(
            dictionary.get("platform_scheduled_payout")).date()\
            if dictionary.get("platform_scheduled_payout") else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(merchant_bank_account_transfer_date,
                   merchant_bank_account_registration_deadline,
                   merchant_bank_transfer_upload_deadline,
                   platform_result_registration_date,
                   platform_scheduled_payout,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _merchant_bank_account_transfer_date=(
            self.merchant_bank_account_transfer_date
            if hasattr(self, "merchant_bank_account_transfer_date")
            else None
        )
        _merchant_bank_account_registration_deadline=(
            self.merchant_bank_account_registration_deadline
            if hasattr(self, "merchant_bank_account_registration_deadline")
            else None
        )
        _merchant_bank_transfer_upload_deadline=(
            self.merchant_bank_transfer_upload_deadline
            if hasattr(self, "merchant_bank_transfer_upload_deadline")
            else None
        )
        _platform_result_registration_date=(
            self.platform_result_registration_date
            if hasattr(self, "platform_result_registration_date")
            else None
        )
        _platform_scheduled_payout=(
            self.platform_scheduled_payout
            if hasattr(self, "platform_scheduled_payout")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"merchant_bank_account_transfer_date={_merchant_bank_account_transfer_date!r}, "
            f"merchant_bank_account_registration_deadline={_merchant_bank_account_registration_deadline!r}, "
            f"merchant_bank_transfer_upload_deadline={_merchant_bank_transfer_upload_deadline!r}, "
            f"platform_result_registration_date={_platform_result_registration_date!r}, "
            f"platform_scheduled_payout={_platform_scheduled_payout!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _merchant_bank_account_transfer_date=(
            self.merchant_bank_account_transfer_date
            if hasattr(self, "merchant_bank_account_transfer_date")
            else None
        )
        _merchant_bank_account_registration_deadline=(
            self.merchant_bank_account_registration_deadline
            if hasattr(self, "merchant_bank_account_registration_deadline")
            else None
        )
        _merchant_bank_transfer_upload_deadline=(
            self.merchant_bank_transfer_upload_deadline
            if hasattr(self, "merchant_bank_transfer_upload_deadline")
            else None
        )
        _platform_result_registration_date=(
            self.platform_result_registration_date
            if hasattr(self, "platform_result_registration_date")
            else None
        )
        _platform_scheduled_payout=(
            self.platform_scheduled_payout
            if hasattr(self, "platform_scheduled_payout")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"merchant_bank_account_transfer_date={_merchant_bank_account_transfer_date!s}, "
            f"merchant_bank_account_registration_deadline={_merchant_bank_account_registration_deadline!s}, "
            f"merchant_bank_transfer_upload_deadline={_merchant_bank_transfer_upload_deadline!s}, "
            f"platform_result_registration_date={_platform_result_registration_date!s}, "
            f"platform_scheduled_payout={_platform_scheduled_payout!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
