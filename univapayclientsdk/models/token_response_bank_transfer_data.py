"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenResponseBankTransferData(object):
    """Implementation of the 'TokenResponseBankTransferData' model.

    Token Response Bank Transfer Data schema.

    Attributes:
        brand (str): The bank brand identifier (e.g., 'aozora_bank').
        expiration_period (str): ISO 8601 duration format (e.g., 'PT168H').
        expiration_time_shift (str): Time shift applied to the expiration, typically
            pushing it to the end of the day  in a specific timezone (e.g.,
            '23:59:59+09:00').
        bank_code (str): Bank code value.
        bank_name (str): Bank name value.
        branch_code (str): Bank branch code.
        branch_name (str): Bank branch name.
        account_number (str): Bank account number.
        account_holder_name (str): Bank account holder name.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "brand": "brand",
        "expiration_period": "expiration_period",
        "expiration_time_shift": "expiration_time_shift",
        "bank_code": "bank_code",
        "bank_name": "bank_name",
        "branch_code": "branch_code",
        "branch_name": "branch_name",
        "account_number": "account_number",
        "account_holder_name": "account_holder_name",
    }

    _optionals = [
        "brand",
        "expiration_period",
        "expiration_time_shift",
        "bank_code",
        "bank_name",
        "branch_code",
        "branch_name",
        "account_number",
        "account_holder_name",
    ]

    _nullables = [
        "bank_code",
        "bank_name",
        "branch_code",
        "branch_name",
        "account_number",
        "account_holder_name",
    ]

    def __init__(
        self,
        brand=APIHelper.SKIP,
        expiration_period=APIHelper.SKIP,
        expiration_time_shift=APIHelper.SKIP,
        bank_code=APIHelper.SKIP,
        bank_name=APIHelper.SKIP,
        branch_code=APIHelper.SKIP,
        branch_name=APIHelper.SKIP,
        account_number=APIHelper.SKIP,
        account_holder_name=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseBankTransferData instance."""
        # Initialize members of the class
        if brand is not APIHelper.SKIP:
            self.brand = brand
        if expiration_period is not APIHelper.SKIP:
            self.expiration_period = expiration_period
        if expiration_time_shift is not APIHelper.SKIP:
            self.expiration_time_shift = expiration_time_shift
        if bank_code is not APIHelper.SKIP:
            self.bank_code = bank_code
        if bank_name is not APIHelper.SKIP:
            self.bank_name = bank_name
        if branch_code is not APIHelper.SKIP:
            self.branch_code = branch_code
        if branch_name is not APIHelper.SKIP:
            self.branch_name = branch_name
        if account_number is not APIHelper.SKIP:
            self.account_number = account_number
        if account_holder_name is not APIHelper.SKIP:
            self.account_holder_name = account_holder_name

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
        brand =\
            dictionary.get("brand")\
            if dictionary.get("brand")\
                else APIHelper.SKIP
        expiration_period =\
            dictionary.get("expiration_period")\
            if dictionary.get("expiration_period")\
                else APIHelper.SKIP
        expiration_time_shift =\
            dictionary.get("expiration_time_shift")\
            if dictionary.get("expiration_time_shift")\
                else APIHelper.SKIP
        bank_code =\
            dictionary.get("bank_code")\
            if "bank_code" in dictionary.keys()\
                else APIHelper.SKIP
        bank_name =\
            dictionary.get("bank_name")\
            if "bank_name" in dictionary.keys()\
                else APIHelper.SKIP
        branch_code =\
            dictionary.get("branch_code")\
            if "branch_code" in dictionary.keys()\
                else APIHelper.SKIP
        branch_name =\
            dictionary.get("branch_name")\
            if "branch_name" in dictionary.keys()\
                else APIHelper.SKIP
        account_number =\
            dictionary.get("account_number")\
            if "account_number" in dictionary.keys()\
                else APIHelper.SKIP
        account_holder_name =\
            dictionary.get("account_holder_name")\
            if "account_holder_name" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(brand,
                   expiration_period,
                   expiration_time_shift,
                   bank_code,
                   bank_name,
                   branch_code,
                   branch_name,
                   account_number,
                   account_holder_name,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _expiration_period=(
            self.expiration_period
            if hasattr(self, "expiration_period")
            else None
        )
        _expiration_time_shift=(
            self.expiration_time_shift
            if hasattr(self, "expiration_time_shift")
            else None
        )
        _bank_code=(
            self.bank_code
            if hasattr(self, "bank_code")
            else None
        )
        _bank_name=(
            self.bank_name
            if hasattr(self, "bank_name")
            else None
        )
        _branch_code=(
            self.branch_code
            if hasattr(self, "branch_code")
            else None
        )
        _branch_name=(
            self.branch_name
            if hasattr(self, "branch_name")
            else None
        )
        _account_number=(
            self.account_number
            if hasattr(self, "account_number")
            else None
        )
        _account_holder_name=(
            self.account_holder_name
            if hasattr(self, "account_holder_name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!r}, "
            f"expiration_period={_expiration_period!r}, "
            f"expiration_time_shift={_expiration_time_shift!r}, "
            f"bank_code={_bank_code!r}, "
            f"bank_name={_bank_name!r}, "
            f"branch_code={_branch_code!r}, "
            f"branch_name={_branch_name!r}, "
            f"account_number={_account_number!r}, "
            f"account_holder_name={_account_holder_name!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _expiration_period=(
            self.expiration_period
            if hasattr(self, "expiration_period")
            else None
        )
        _expiration_time_shift=(
            self.expiration_time_shift
            if hasattr(self, "expiration_time_shift")
            else None
        )
        _bank_code=(
            self.bank_code
            if hasattr(self, "bank_code")
            else None
        )
        _bank_name=(
            self.bank_name
            if hasattr(self, "bank_name")
            else None
        )
        _branch_code=(
            self.branch_code
            if hasattr(self, "branch_code")
            else None
        )
        _branch_name=(
            self.branch_name
            if hasattr(self, "branch_name")
            else None
        )
        _account_number=(
            self.account_number
            if hasattr(self, "account_number")
            else None
        )
        _account_holder_name=(
            self.account_holder_name
            if hasattr(self, "account_holder_name")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"brand={_brand!s}, "
            f"expiration_period={_expiration_period!s}, "
            f"expiration_time_shift={_expiration_time_shift!s}, "
            f"bank_code={_bank_code!s}, "
            f"bank_name={_bank_name!s}, "
            f"branch_code={_branch_code!s}, "
            f"branch_name={_branch_name!s}, "
            f"account_number={_account_number!s}, "
            f"account_holder_name={_account_holder_name!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
