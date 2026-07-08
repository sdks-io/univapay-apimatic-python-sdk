"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CustomsDeclarationPatchRequest(object):
    """Implementation of the 'CustomsDeclarationPatchRequest' model.

    Request body for updating a customs declaration. Backend patch handling keeps the
    original `customs`, `certificate_id`, and `certificate_name` values and only
    accepts a new `merchant_customs_no`.

    Attributes:
        merchant_customs_no (str): Updated merchant customs registration number.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "merchant_customs_no": "merchant_customs_no",
    }

    def __init__(
        self,
        merchant_customs_no=None,
        additional_properties=None):
        """Initialize a CustomsDeclarationPatchRequest instance."""
        # Initialize members of the class
        self.merchant_customs_no = merchant_customs_no

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
        merchant_customs_no =\
            dictionary.get("merchant_customs_no")\
            if dictionary.get("merchant_customs_no")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(merchant_customs_no,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _merchant_customs_no=self.merchant_customs_no
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"merchant_customs_no={_merchant_customs_no!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _merchant_customs_no=self.merchant_customs_no
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"merchant_customs_no={_merchant_customs_no!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
