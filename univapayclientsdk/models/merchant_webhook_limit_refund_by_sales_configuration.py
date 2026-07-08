"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookLimitRefundBySalesConfiguration(object):
    """Implementation of the 'MerchantWebhookLimitRefundBySalesConfiguration' model.

    Refund-limiting configuration based on sales history.

    Attributes:
        enabled (bool): Enables sales-based refund limit checks.
        period (str): Sales aggregation period used to evaluate refund limits.
        rolling_window (bool): Uses a rolling window instead of fixed calendar
            periods.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "enabled": "enabled",
        "period": "period",
        "rolling_window": "rolling_window",
    }

    _optionals = [
        "enabled",
        "period",
        "rolling_window",
    ]

    _nullables = [
        "enabled",
        "period",
        "rolling_window",
    ]

    def __init__(
        self,
        enabled=APIHelper.SKIP,
        period=APIHelper.SKIP,
        rolling_window=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookLimitRefundBySalesConfiguration instance."""
        # Initialize members of the class
        if enabled is not APIHelper.SKIP:
            self.enabled = enabled
        if period is not APIHelper.SKIP:
            self.period = period
        if rolling_window is not APIHelper.SKIP:
            self.rolling_window = rolling_window

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
        period =\
            dictionary.get("period")\
            if "period" in dictionary.keys()\
                else APIHelper.SKIP
        rolling_window =\
            dictionary.get("rolling_window")\
            if "rolling_window" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(enabled,
                   period,
                   rolling_window,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _enabled=(
            self.enabled
            if hasattr(self, "enabled")
            else None
        )
        _period=(
            self.period
            if hasattr(self, "period")
            else None
        )
        _rolling_window=(
            self.rolling_window
            if hasattr(self, "rolling_window")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!r}, "
            f"period={_period!r}, "
            f"rolling_window={_rolling_window!r}, "
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
        _period=(
            self.period
            if hasattr(self, "period")
            else None
        )
        _rolling_window=(
            self.rolling_window
            if hasattr(self, "rolling_window")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"enabled={_enabled!s}, "
            f"period={_period!s}, "
            f"rolling_window={_rolling_window!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
