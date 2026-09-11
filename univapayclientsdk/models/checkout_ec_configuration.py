"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.checkout_ec_email_configuration import (
    CheckoutEcEmailConfiguration,
)
from univapayclientsdk.models.checkout_ec_products_configuration import (
    CheckoutEcProductsConfiguration,
)


class CheckoutEcConfiguration(object):
    """Implementation of the 'CheckoutEcConfiguration' model.

    EC checkout feature toggles for hosted email receipts and product line items.

    Attributes:
        ec_email (CheckoutEcEmailConfiguration): Email-related EC checkout settings.
        ec_products (CheckoutEcProductsConfiguration): Product-related EC checkout
            settings.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ec_email": "ec_email",
        "ec_products": "ec_products",
    }

    _optionals = [
        "ec_email",
        "ec_products",
    ]

    def __init__(
        self,
        ec_email=APIHelper.SKIP,
        ec_products=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutEcConfiguration instance."""
        # Initialize members of the class
        if ec_email is not APIHelper.SKIP:
            self.ec_email = ec_email
        if ec_products is not APIHelper.SKIP:
            self.ec_products = ec_products

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
        ec_email =\
            CheckoutEcEmailConfiguration.from_dictionary(
                dictionary.get("ec_email"))\
                if "ec_email" in dictionary.keys()\
                else APIHelper.SKIP
        ec_products =\
            CheckoutEcProductsConfiguration.from_dictionary(
                dictionary.get("ec_products"))\
                if "ec_products" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(ec_email,
                   ec_products,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _ec_email=(
            self.ec_email
            if hasattr(self, "ec_email")
            else None
        )
        _ec_products=(
            self.ec_products
            if hasattr(self, "ec_products")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"ec_email={_ec_email!r}, "
            f"ec_products={_ec_products!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _ec_email=(
            self.ec_email
            if hasattr(self, "ec_email")
            else None
        )
        _ec_products=(
            self.ec_products
            if hasattr(self, "ec_products")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"ec_email={_ec_email!s}, "
            f"ec_products={_ec_products!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
