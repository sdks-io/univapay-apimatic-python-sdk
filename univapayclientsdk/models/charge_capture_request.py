"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class ChargeCaptureRequest(object):
    """Implementation of the 'ChargeCaptureRequest' model.

    Request payload for capturing an authorized charge.

    Attributes:
        amount (int): The amount to capture. Must be less than or equal to the
            authorized amount.
        currency (str): ISO-4217 currency code. Must exactly match the currency used
            during authorization.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount": "amount",
        "currency": "currency",
    }

    def __init__(
        self,
        amount=None,
        currency=None,
        additional_properties=None):
        """Initialize a ChargeCaptureRequest instance."""
        # Initialize members of the class
        self.amount = amount
        self.currency = currency

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
        amount =\
            dictionary.get("amount")\
            if dictionary.get("amount")\
                else None
        currency =\
            dictionary.get("currency")\
            if dictionary.get("currency")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(amount,
                   currency,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _amount=self.amount
        _currency=self.currency
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!r}, "
            f"currency={_currency!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _amount=self.amount
        _currency=self.currency
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"amount={_amount!s}, "
            f"currency={_currency!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
