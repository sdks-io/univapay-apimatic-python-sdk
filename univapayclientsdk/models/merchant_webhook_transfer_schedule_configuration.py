"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class MerchantWebhookTransferScheduleConfiguration(object):
    """Implementation of the 'MerchantWebhookTransferScheduleConfiguration' model.

    Transfer schedule configuration inherited by the merchant.

    Attributes:
        wait_period (str): ISO-8601 period before charges become payable.
        period (str): Transfer period selected for payouts.
        full_period_required (bool): Whether the first transfer period must be fully
            completed.
        day_of_week (str): Payout day of week when using weekly schedules.
        week_of_month (int): Week of month used by monthly schedules.
        day_of_month (int): Day of month used by monthly schedules.
        weekly_closing_day (str): Weekly closing day for balance aggregation.
        weekly_payout_day (str): Weekly payout day.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wait_period": "wait_period",
        "period": "period",
        "full_period_required": "full_period_required",
        "day_of_week": "day_of_week",
        "week_of_month": "week_of_month",
        "day_of_month": "day_of_month",
        "weekly_closing_day": "weekly_closing_day",
        "weekly_payout_day": "weekly_payout_day",
    }

    _optionals = [
        "wait_period",
        "period",
        "full_period_required",
        "day_of_week",
        "week_of_month",
        "day_of_month",
        "weekly_closing_day",
        "weekly_payout_day",
    ]

    _nullables = [
        "full_period_required",
        "day_of_week",
        "week_of_month",
        "day_of_month",
        "weekly_closing_day",
        "weekly_payout_day",
    ]

    def __init__(
        self,
        wait_period=APIHelper.SKIP,
        period=APIHelper.SKIP,
        full_period_required=APIHelper.SKIP,
        day_of_week=APIHelper.SKIP,
        week_of_month=APIHelper.SKIP,
        day_of_month=APIHelper.SKIP,
        weekly_closing_day=APIHelper.SKIP,
        weekly_payout_day=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a MerchantWebhookTransferScheduleConfiguration instance."""
        # Initialize members of the class
        if wait_period is not APIHelper.SKIP:
            self.wait_period = wait_period
        if period is not APIHelper.SKIP:
            self.period = period
        if full_period_required is not APIHelper.SKIP:
            self.full_period_required = full_period_required
        if day_of_week is not APIHelper.SKIP:
            self.day_of_week = day_of_week
        if week_of_month is not APIHelper.SKIP:
            self.week_of_month = week_of_month
        if day_of_month is not APIHelper.SKIP:
            self.day_of_month = day_of_month
        if weekly_closing_day is not APIHelper.SKIP:
            self.weekly_closing_day = weekly_closing_day
        if weekly_payout_day is not APIHelper.SKIP:
            self.weekly_payout_day = weekly_payout_day

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
        wait_period =\
            dictionary.get("wait_period")\
            if dictionary.get("wait_period")\
                else APIHelper.SKIP
        period =\
            dictionary.get("period")\
            if dictionary.get("period")\
                else APIHelper.SKIP
        full_period_required =\
            dictionary.get("full_period_required")\
            if "full_period_required" in dictionary.keys()\
                else APIHelper.SKIP
        day_of_week =\
            dictionary.get("day_of_week")\
            if "day_of_week" in dictionary.keys()\
                else APIHelper.SKIP
        week_of_month =\
            dictionary.get("week_of_month")\
            if "week_of_month" in dictionary.keys()\
                else APIHelper.SKIP
        day_of_month =\
            dictionary.get("day_of_month")\
            if "day_of_month" in dictionary.keys()\
                else APIHelper.SKIP
        weekly_closing_day =\
            dictionary.get("weekly_closing_day")\
            if "weekly_closing_day" in dictionary.keys()\
                else APIHelper.SKIP
        weekly_payout_day =\
            dictionary.get("weekly_payout_day")\
            if "weekly_payout_day" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(wait_period,
                   period,
                   full_period_required,
                   day_of_week,
                   week_of_month,
                   day_of_month,
                   weekly_closing_day,
                   weekly_payout_day,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _wait_period=(
            self.wait_period
            if hasattr(self, "wait_period")
            else None
        )
        _period=(
            self.period
            if hasattr(self, "period")
            else None
        )
        _full_period_required=(
            self.full_period_required
            if hasattr(self, "full_period_required")
            else None
        )
        _day_of_week=(
            self.day_of_week
            if hasattr(self, "day_of_week")
            else None
        )
        _week_of_month=(
            self.week_of_month
            if hasattr(self, "week_of_month")
            else None
        )
        _day_of_month=(
            self.day_of_month
            if hasattr(self, "day_of_month")
            else None
        )
        _weekly_closing_day=(
            self.weekly_closing_day
            if hasattr(self, "weekly_closing_day")
            else None
        )
        _weekly_payout_day=(
            self.weekly_payout_day
            if hasattr(self, "weekly_payout_day")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wait_period={_wait_period!r}, "
            f"period={_period!r}, "
            f"full_period_required={_full_period_required!r}, "
            f"day_of_week={_day_of_week!r}, "
            f"week_of_month={_week_of_month!r}, "
            f"day_of_month={_day_of_month!r}, "
            f"weekly_closing_day={_weekly_closing_day!r}, "
            f"weekly_payout_day={_weekly_payout_day!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _wait_period=(
            self.wait_period
            if hasattr(self, "wait_period")
            else None
        )
        _period=(
            self.period
            if hasattr(self, "period")
            else None
        )
        _full_period_required=(
            self.full_period_required
            if hasattr(self, "full_period_required")
            else None
        )
        _day_of_week=(
            self.day_of_week
            if hasattr(self, "day_of_week")
            else None
        )
        _week_of_month=(
            self.week_of_month
            if hasattr(self, "week_of_month")
            else None
        )
        _day_of_month=(
            self.day_of_month
            if hasattr(self, "day_of_month")
            else None
        )
        _weekly_closing_day=(
            self.weekly_closing_day
            if hasattr(self, "weekly_closing_day")
            else None
        )
        _weekly_payout_day=(
            self.weekly_payout_day
            if hasattr(self, "weekly_payout_day")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"wait_period={_wait_period!s}, "
            f"period={_period!s}, "
            f"full_period_required={_full_period_required!s}, "
            f"day_of_week={_day_of_week!s}, "
            f"week_of_month={_week_of_month!s}, "
            f"day_of_month={_day_of_month!s}, "
            f"weekly_closing_day={_weekly_closing_day!s}, "
            f"weekly_payout_day={_weekly_payout_day!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
