"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CreateCustomerIdResponse(object):
    """Implementation of the 'CreateCustomerIdResponse' model.

    Response payload returned after deriving a deterministic customer ID.

    Attributes:
        customer_id (uuid|str): Deterministic UUID derived from the store and the
            supplied local `customer_id`. Identical for repeated calls with the same
            inputs.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_id": "customer_id",
    }

    _optionals = [
        "customer_id",
    ]

    def __init__(
        self,
        customer_id=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CreateCustomerIdResponse instance."""
        # Initialize members of the class
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id

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
        customer_id =\
            dictionary.get("customer_id")\
            if dictionary.get("customer_id")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(customer_id,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customer_id={_customer_id!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _customer_id=(
            self.customer_id
            if hasattr(self, "customer_id")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customer_id={_customer_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
