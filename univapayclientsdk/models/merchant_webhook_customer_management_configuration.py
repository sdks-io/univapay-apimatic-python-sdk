"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookCustomerManagementConfiguration(object):
    """Implementation of the 'MerchantWebhookCustomerManagementConfiguration' model.

    Customer-management defaults.

    Attributes:
        enabled (bool): Enables customer-management features.
        default_roles (List[str]): Roles applied to newly created customers.
        default_mode (str): Default processing mode assigned to new customer records.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "default_roles": "default_roles",
        "default_mode": "default_mode",
    }

    _optionals = [
        "enabled",
        "default_roles",
        "default_mode",
    ]

    _nullables = [
        "enabled",
        "default_roles",
        "default_mode",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        default_roles=APIHelper.SKIP,
        default_mode=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookCustomerManagementConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if default_roles is not APIHelper.SKIP:
            self.default_roles = default_roles
        if default_mode is not APIHelper.SKIP:
            self.default_mode = default_mode

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
        enabled =\
            dictionary.get("enabled")\
            if "enabled" in dictionary.keys()\
                else APIHelper.SKIP
        default_roles =\
            dictionary.get("default_roles")\
            if "default_roles" in dictionary.keys()\
                else APIHelper.SKIP
        default_mode =\
            dictionary.get("default_mode")\
            if "default_mode" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   default_roles,
                   default_mode,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _default_roles=(
            self.default_roles
            if hasattr(self, "default_roles")
            else None
        )
        _default_mode=(
            self.default_mode
            if hasattr(self, "default_mode")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"default_roles={_default_roles!r}, "
            f"default_mode={_default_mode!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _default_roles=(
            self.default_roles
            if hasattr(self, "default_roles")
            else None
        )
        _default_mode=(
            self.default_mode
            if hasattr(self, "default_mode")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"default_roles={_default_roles!s}, "
            f"default_mode={_default_mode!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
