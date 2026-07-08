"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookSubscriptionConfiguration(object):
    """Implementation of the 'MerchantWebhookSubscriptionConfiguration' model.

    Subscription feature configuration.

    Attributes:
        enabled (bool): Enables subscription payments.
        failed_charges_to_cancel (int): Number of failed charges allowed before
            cancellation.
        suspend_on_cancel (bool): Suspends the subscription when its latest charge is
            canceled.
        allow_merchant_amount_patch (bool): Allows merchants to update scheduled
            subscription amounts.
        allow_merchant_due_date_patch (bool): Allows merchants to update scheduled
            subscription due dates.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "failed_charges_to_cancel": "failed_charges_to_cancel",
        "suspend_on_cancel": "suspend_on_cancel",
        "allow_merchant_amount_patch": "allow_merchant_amount_patch",
        "allow_merchant_due_date_patch": "allow_merchant_due_date_patch",
    }

    _optionals = [
        "enabled",
        "failed_charges_to_cancel",
        "suspend_on_cancel",
        "allow_merchant_amount_patch",
        "allow_merchant_due_date_patch",
    ]

    _nullables = [
        "enabled",
        "failed_charges_to_cancel",
        "suspend_on_cancel",
        "allow_merchant_amount_patch",
        "allow_merchant_due_date_patch",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        failed_charges_to_cancel=APIHelper.SKIP,
        suspend_on_cancel=APIHelper.SKIP,
        allow_merchant_amount_patch=APIHelper.SKIP,
        allow_merchant_due_date_patch=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookSubscriptionConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if failed_charges_to_cancel is not APIHelper.SKIP:
            self.failed_charges_to_cancel = failed_charges_to_cancel
        if suspend_on_cancel is not APIHelper.SKIP:
            self.suspend_on_cancel = suspend_on_cancel
        if allow_merchant_amount_patch is not APIHelper.SKIP:
            self.allow_merchant_amount_patch = allow_merchant_amount_patch
        if allow_merchant_due_date_patch is not APIHelper.SKIP:
            self.allow_merchant_due_date_patch = allow_merchant_due_date_patch

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
        failed_charges_to_cancel =\
            dictionary.get("failed_charges_to_cancel")\
            if "failed_charges_to_cancel" in dictionary.keys()\
                else APIHelper.SKIP
        suspend_on_cancel =\
            dictionary.get("suspend_on_cancel")\
            if "suspend_on_cancel" in dictionary.keys()\
                else APIHelper.SKIP
        allow_merchant_amount_patch =\
            dictionary.get("allow_merchant_amount_patch")\
            if "allow_merchant_amount_patch" in dictionary.keys()\
                else APIHelper.SKIP
        allow_merchant_due_date_patch =\
            dictionary.get("allow_merchant_due_date_patch")\
            if "allow_merchant_due_date_patch" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   failed_charges_to_cancel,
                   suspend_on_cancel,
                   allow_merchant_amount_patch,
                   allow_merchant_due_date_patch,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _failed_charges_to_cancel=(
            self.failed_charges_to_cancel
            if hasattr(self, "failed_charges_to_cancel")
            else None
        )
        _suspend_on_cancel=(
            self.suspend_on_cancel
            if hasattr(self, "suspend_on_cancel")
            else None
        )
        _allow_merchant_amount_patch=(
            self.allow_merchant_amount_patch
            if hasattr(self, "allow_merchant_amount_patch")
            else None
        )
        _allow_merchant_due_date_patch=(
            self.allow_merchant_due_date_patch
            if hasattr(self, "allow_merchant_due_date_patch")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"failed_charges_to_cancel={_failed_charges_to_cancel!r}, "
            f"suspend_on_cancel={_suspend_on_cancel!r}, "
            f"allow_merchant_amount_patch={_allow_merchant_amount_patch!r}, "
            f"allow_merchant_due_date_patch={_allow_merchant_due_date_patch!r}, "
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
        _failed_charges_to_cancel=(
            self.failed_charges_to_cancel
            if hasattr(self, "failed_charges_to_cancel")
            else None
        )
        _suspend_on_cancel=(
            self.suspend_on_cancel
            if hasattr(self, "suspend_on_cancel")
            else None
        )
        _allow_merchant_amount_patch=(
            self.allow_merchant_amount_patch
            if hasattr(self, "allow_merchant_amount_patch")
            else None
        )
        _allow_merchant_due_date_patch=(
            self.allow_merchant_due_date_patch
            if hasattr(self, "allow_merchant_due_date_patch")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"failed_charges_to_cancel={_failed_charges_to_cancel!s}, "
            f"suspend_on_cancel={_suspend_on_cancel!s}, "
            f"allow_merchant_amount_patch={_allow_merchant_amount_patch!s}, "
            f"allow_merchant_due_date_patch={_allow_merchant_due_date_patch!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
