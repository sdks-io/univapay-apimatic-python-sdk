"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class CheckoutInstallmentCardProcessor(object):
    """Implementation of the 'CheckoutInstallmentCardProcessor' model.

    Card-processor capabilities available for installment payments.

    Attributes:
        revolving (bool): Whether revolving installment payments are allowed.
        fixed_cycle (bool): Whether fixed-cycle installment payments are allowed.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "revolving": "revolving",
        "fixed_cycle": "fixed_cycle",
    }

    _optionals = [
        "revolving",
        "fixed_cycle",
    ]

    def __init__(
        self,
        revolving=APIHelper.SKIP,
        fixed_cycle=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a CheckoutInstallmentCardProcessor instance."""
        # Initialize members of the class
        if revolving is not APIHelper.SKIP:
            self.revolving = revolving
        if fixed_cycle is not APIHelper.SKIP:
            self.fixed_cycle = fixed_cycle

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
        revolving =\
            dictionary.get("revolving")\
            if "revolving" in dictionary.keys()\
                else APIHelper.SKIP
        fixed_cycle =\
            dictionary.get("fixed_cycle")\
            if "fixed_cycle" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(revolving,
                   fixed_cycle,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _revolving=(
            self.revolving
            if hasattr(self, "revolving")
            else None
        )
        _fixed_cycle=(
            self.fixed_cycle
            if hasattr(self, "fixed_cycle")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"revolving={_revolving!r}, "
            f"fixed_cycle={_fixed_cycle!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _revolving=(
            self.revolving
            if hasattr(self, "revolving")
            else None
        )
        _fixed_cycle=(
            self.fixed_cycle
            if hasattr(self, "fixed_cycle")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"revolving={_revolving!s}, "
            f"fixed_cycle={_fixed_cycle!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
