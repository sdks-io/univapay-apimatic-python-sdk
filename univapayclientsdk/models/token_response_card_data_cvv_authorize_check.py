"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class TokenResponseCardDataCvvAuthorizeCheck(object):
    """Implementation of the 'TokenResponseCardDataCvvAuthorizeCheck' model.

    Token Response Card Data Cvv Authorize Check schema.

    Attributes:
        status (str): Current status of the resource.
        charge_id (uuid|str): Charge identifier.
        date (datetime): Date value.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": "status",
        "charge_id": "charge_id",
        "date": "date",
    }

    _optionals = [
        "status",
        "charge_id",
        "date",
    ]

    _nullables = [
        "status",
        "charge_id",
        "date",
    ]

    def __init__(
        self,
        status=APIHelper.SKIP,
        charge_id=APIHelper.SKIP,
        date=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TokenResponseCardDataCvvAuthorizeCheck instance."""
        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status
        if charge_id is not APIHelper.SKIP:
            self.charge_id = charge_id
        if date is not APIHelper.SKIP:
            self.date =\
                 APIHelper.apply_datetime_converter(
                date, APIHelper.RFC3339DateTime)\
                 if date else None

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
        status =\
            dictionary.get("status")\
            if "status" in dictionary.keys()\
                else APIHelper.SKIP
        charge_id =\
            dictionary.get("charge_id")\
            if "charge_id" in dictionary.keys()\
                else APIHelper.SKIP
        if "date" in dictionary.keys():
            date = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("date")).datetime\
                if dictionary.get("date") else None

        else:
            date = APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(status,
                   charge_id,
                   date,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return True

        if not isinstance(dictionary, dict):
            return False

        return True

    def __repr__(self):
        """Return a unambiguous string representation."""
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _date=(
            self.date
            if hasattr(self, "date")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"status={_status!r}, "
            f"charge_id={_charge_id!r}, "
            f"date={_date!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _status=(
            self.status
            if hasattr(self, "status")
            else None
        )
        _charge_id=(
            self.charge_id
            if hasattr(self, "charge_id")
            else None
        )
        _date=(
            self.date
            if hasattr(self, "date")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"status={_status!s}, "
            f"charge_id={_charge_id!s}, "
            f"date={_date!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
