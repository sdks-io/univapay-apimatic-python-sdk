"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class SubscriptionPatchTokenRequest(object):
    """Implementation of the 'SubscriptionPatchTokenRequest' model.

    Request body for updating the payment method (transaction token) of a
    subscription. The new token must belong to the same store, be active, and match
    the subscription's mode.

    Attributes:
        transaction_token_id (uuid|str): The ID of the new transaction token to use
            for future subscription payments. Must be a recurring or
            subscription-type token for the same store.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_token_id": "transaction_token_id",
    }

    def __init__(
        self,
        transaction_token_id=None,
        additional_properties=None):
        """Initialize a SubscriptionPatchTokenRequest instance."""
        # Initialize members of the class
        self.transaction_token_id = transaction_token_id

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
        transaction_token_id =\
            dictionary.get("transaction_token_id")\
            if dictionary.get("transaction_token_id")\
                else None

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(transaction_token_id,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _transaction_token_id=self.transaction_token_id
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _transaction_token_id=self.transaction_token_id
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"transaction_token_id={_transaction_token_id!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
