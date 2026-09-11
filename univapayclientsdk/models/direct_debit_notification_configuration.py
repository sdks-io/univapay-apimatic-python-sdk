"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class DirectDebitNotificationConfiguration(object):
    """Implementation of the 'DirectDebitNotificationConfiguration' model.

    Which direct debit email notifications the merchant has opted into.

    Attributes:
        notify_deadline_mailing (bool): Notify when the deadline for the bank to
            receive the signed mandate approaches (郵送期限の通知).
        notify_deadline_debit (bool): Notify when the transfer registration cutoff
            approaches (締切日の通知).
        notify_debit_update (bool): Notify when transfer results are reflected
            (振替結果の通知).
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "notify_deadline_mailing": "notify_deadline_mailing",
        "notify_deadline_debit": "notify_deadline_debit",
        "notify_debit_update": "notify_debit_update",
    }

    _optionals = [
        "notify_deadline_mailing",
        "notify_deadline_debit",
        "notify_debit_update",
    ]

    def __init__(
        self,
        notify_deadline_mailing=APIHelper.SKIP,
        notify_deadline_debit=APIHelper.SKIP,
        notify_debit_update=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a DirectDebitNotificationConfiguration instance."""
        # Initialize members of the class
        if notify_deadline_mailing is not APIHelper.SKIP:
            self.notify_deadline_mailing = notify_deadline_mailing
        if notify_deadline_debit is not APIHelper.SKIP:
            self.notify_deadline_debit = notify_deadline_debit
        if notify_debit_update is not APIHelper.SKIP:
            self.notify_debit_update = notify_debit_update

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
        notify_deadline_mailing =\
            dictionary.get("notify_deadline_mailing")\
            if "notify_deadline_mailing" in dictionary.keys()\
                else APIHelper.SKIP
        notify_deadline_debit =\
            dictionary.get("notify_deadline_debit")\
            if "notify_deadline_debit" in dictionary.keys()\
                else APIHelper.SKIP
        notify_debit_update =\
            dictionary.get("notify_debit_update")\
            if "notify_debit_update" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(notify_deadline_mailing,
                   notify_deadline_debit,
                   notify_debit_update,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _notify_deadline_mailing=(
            self.notify_deadline_mailing
            if hasattr(self, "notify_deadline_mailing")
            else None
        )
        _notify_deadline_debit=(
            self.notify_deadline_debit
            if hasattr(self, "notify_deadline_debit")
            else None
        )
        _notify_debit_update=(
            self.notify_debit_update
            if hasattr(self, "notify_debit_update")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"notify_deadline_mailing={_notify_deadline_mailing!r}, "
            f"notify_deadline_debit={_notify_deadline_debit!r}, "
            f"notify_debit_update={_notify_debit_update!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _notify_deadline_mailing=(
            self.notify_deadline_mailing
            if hasattr(self, "notify_deadline_mailing")
            else None
        )
        _notify_deadline_debit=(
            self.notify_deadline_debit
            if hasattr(self, "notify_deadline_debit")
            else None
        )
        _notify_debit_update=(
            self.notify_debit_update
            if hasattr(self, "notify_debit_update")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"notify_deadline_mailing={_notify_deadline_mailing!s}, "
            f"notify_deadline_debit={_notify_deadline_debit!s}, "
            f"notify_debit_update={_notify_debit_update!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
