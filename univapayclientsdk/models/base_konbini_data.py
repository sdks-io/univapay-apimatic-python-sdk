"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class BaseKonbiniData(object):
    """Implementation of the 'BaseKonbiniData' model.

    Base Konbini Data schema.

    Attributes:
        customer_name (str): Customer name.
        convenience_store (BaseKonbiniDataConvenienceStore): Base Konbini Data
            Convenience Store schema.
        expiration_period (str): ISO-8601 Duration (e.g., 'P7D'). Default is 30 days.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_name": "customer_name",
        "convenience_store": "convenience_store",
        "expiration_period": "expiration_period",
    }

    _optionals = [
        "customer_name",
        "convenience_store",
        "expiration_period",
    ]

    def __init__(
        self,
        customer_name=APIHelper.SKIP,
        convenience_store=APIHelper.SKIP,
        expiration_period=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a BaseKonbiniData instance."""
        # Initialize members of the class
        if customer_name is not APIHelper.SKIP:
            self.customer_name = customer_name
        if convenience_store is not APIHelper.SKIP:
            self.convenience_store = convenience_store
        if expiration_period is not APIHelper.SKIP:
            self.expiration_period = expiration_period

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
        customer_name =\
            dictionary.get("customer_name")\
            if dictionary.get("customer_name")\
                else APIHelper.SKIP
        convenience_store =\
            dictionary.get("convenience_store")\
            if dictionary.get("convenience_store")\
                else APIHelper.SKIP
        expiration_period =\
            dictionary.get("expiration_period")\
            if dictionary.get("expiration_period")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(customer_name,
                   convenience_store,
                   expiration_period,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _customer_name=(
            self.customer_name
            if hasattr(self, "customer_name")
            else None
        )
        _convenience_store=(
            self.convenience_store
            if hasattr(self, "convenience_store")
            else None
        )
        _expiration_period=(
            self.expiration_period
            if hasattr(self, "expiration_period")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customer_name={_customer_name!r}, "
            f"convenience_store={_convenience_store!r}, "
            f"expiration_period={_expiration_period!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _customer_name=(
            self.customer_name
            if hasattr(self, "customer_name")
            else None
        )
        _convenience_store=(
            self.convenience_store
            if hasattr(self, "convenience_store")
            else None
        )
        _expiration_period=(
            self.expiration_period
            if hasattr(self, "expiration_period")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"customer_name={_customer_name!s}, "
            f"convenience_store={_convenience_store!s}, "
            f"expiration_period={_expiration_period!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
