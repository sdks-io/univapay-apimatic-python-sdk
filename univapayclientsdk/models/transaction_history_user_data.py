"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper
from univapayclientsdk.models.transaction_history_refund import (
    TransactionHistoryRefund,
)


class TransactionHistoryUserData(object):
    """Implementation of the 'TransactionHistoryUserData' model.

    Payment-type-specific details for this row. This is a single flat object covering
    every payment type — the fields actually populated depend on `payment_type`
    (documented per field below). Fields not applicable to a given payment type are
    omitted.

    Attributes:
        mtype (TransactionHistoryType): Whether this row represents a charge or a
            refund.
        cardholder_name (str): Cardholder name. Present for `card` and `apple_pay`
            rows only.
        cardholder_email_address (str): Cardholder/customer email address. Present
            for every payment type except `konbini`'s legacy alias fields; always
            non-null for `bank_transfer` rows, nullable for every other type.
        cardholder_phone_number (str): Cardholder phone number. Present for `paidy`
            rows only.
        customer_name (str): Customer name as entered at checkout. Present for
            `konbini` rows only (empty string when not provided).
        convenience_store (str): Legacy duplicate of `brand`. Present for `konbini`
            rows only.
        brand (str): Raw brand identifier for the payment method. Present for every
            payment type; the value set is payment-type-specific (e.g. card brands
            for `card`/`apple_pay`, QR brands for `qr_scan`/`qr_merchant`,
            online-wallet brands for `online`, convenience-store brands for
            `konbini`, `paidy` for `paidy` rows). Nullable for `qr_scan`,
            `qr_merchant`, and `online`; always non-null for the other types.
        gateway (str): Raw gateway identifier that processed the payment. Present for
            every payment type.
        service_provider (TransactionHistoryServiceProvider): Service provider, or
            `null` when not reported.
        refunds (List[TransactionHistoryRefund]): Refunds issued against this charge.
            Present for charge rows only (`type: charge`); absent for refund rows.
        reason (TransactionHistoryRefundReason): Refund reason, or `null` when unset.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": "type",
        "cardholder_name": "cardholder_name",
        "cardholder_email_address": "cardholder_email_address",
        "cardholder_phone_number": "cardholder_phone_number",
        "customer_name": "customer_name",
        "convenience_store": "convenience_store",
        "brand": "brand",
        "gateway": "gateway",
        "service_provider": "service_provider",
        "refunds": "refunds",
        "reason": "reason",
    }

    _optionals = [
        "mtype",
        "cardholder_name",
        "cardholder_email_address",
        "cardholder_phone_number",
        "customer_name",
        "convenience_store",
        "brand",
        "gateway",
        "service_provider",
        "refunds",
        "reason",
    ]

    _nullables = [
        "cardholder_email_address",
        "cardholder_phone_number",
        "brand",
        "gateway",
        "service_provider",
        "reason",
    ]

    def __init__(
        self,
        mtype=APIHelper.SKIP,
        cardholder_name=APIHelper.SKIP,
        cardholder_email_address=APIHelper.SKIP,
        cardholder_phone_number=APIHelper.SKIP,
        customer_name=APIHelper.SKIP,
        convenience_store=APIHelper.SKIP,
        brand=APIHelper.SKIP,
        gateway=APIHelper.SKIP,
        service_provider=APIHelper.SKIP,
        refunds=APIHelper.SKIP,
        reason=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a TransactionHistoryUserData instance."""
        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype
        if cardholder_name is not APIHelper.SKIP:
            self.cardholder_name = cardholder_name
        if cardholder_email_address is not APIHelper.SKIP:
            self.cardholder_email_address = cardholder_email_address
        if cardholder_phone_number is not APIHelper.SKIP:
            self.cardholder_phone_number = cardholder_phone_number
        if customer_name is not APIHelper.SKIP:
            self.customer_name = customer_name
        if convenience_store is not APIHelper.SKIP:
            self.convenience_store = convenience_store
        if brand is not APIHelper.SKIP:
            self.brand = brand
        if gateway is not APIHelper.SKIP:
            self.gateway = gateway
        if service_provider is not APIHelper.SKIP:
            self.service_provider = service_provider
        if refunds is not APIHelper.SKIP:
            self.refunds = refunds
        if reason is not APIHelper.SKIP:
            self.reason = reason

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
        mtype =\
            dictionary.get("type")\
            if dictionary.get("type")\
                else APIHelper.SKIP
        cardholder_name =\
            dictionary.get("cardholder_name")\
            if dictionary.get("cardholder_name")\
                else APIHelper.SKIP
        cardholder_email_address =\
            dictionary.get("cardholder_email_address")\
            if "cardholder_email_address" in dictionary.keys()\
                else APIHelper.SKIP
        cardholder_phone_number =\
            dictionary.get("cardholder_phone_number")\
            if "cardholder_phone_number" in dictionary.keys()\
                else APIHelper.SKIP
        customer_name =\
            dictionary.get("customer_name")\
            if dictionary.get("customer_name")\
                else APIHelper.SKIP
        convenience_store =\
            dictionary.get("convenience_store")\
            if dictionary.get("convenience_store")\
                else APIHelper.SKIP
        brand =\
            dictionary.get("brand")\
            if "brand" in dictionary.keys()\
                else APIHelper.SKIP
        gateway =\
            dictionary.get("gateway")\
            if "gateway" in dictionary.keys()\
                else APIHelper.SKIP
        service_provider =\
            dictionary.get("service_provider")\
            if "service_provider" in dictionary.keys()\
                else APIHelper.SKIP
        refunds = None
        if dictionary.get("refunds") is not None:
            refunds = [
                TransactionHistoryRefund.from_dictionary(x)
                    for x in dictionary.get("refunds")
            ]
        else:
            refunds = APIHelper.SKIP
        reason =\
            dictionary.get("reason")\
            if "reason" in dictionary.keys()\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(mtype,
                   cardholder_name,
                   cardholder_email_address,
                   cardholder_phone_number,
                   customer_name,
                   convenience_store,
                   brand,
                   gateway,
                   service_provider,
                   refunds,
                   reason,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _cardholder_name=(
            self.cardholder_name
            if hasattr(self, "cardholder_name")
            else None
        )
        _cardholder_email_address=(
            self.cardholder_email_address
            if hasattr(self, "cardholder_email_address")
            else None
        )
        _cardholder_phone_number=(
            self.cardholder_phone_number
            if hasattr(self, "cardholder_phone_number")
            else None
        )
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
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _gateway=(
            self.gateway
            if hasattr(self, "gateway")
            else None
        )
        _service_provider=(
            self.service_provider
            if hasattr(self, "service_provider")
            else None
        )
        _refunds=(
            self.refunds
            if hasattr(self, "refunds")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mtype={_mtype!r}, "
            f"cardholder_name={_cardholder_name!r}, "
            f"cardholder_email_address={_cardholder_email_address!r}, "
            f"cardholder_phone_number={_cardholder_phone_number!r}, "
            f"customer_name={_customer_name!r}, "
            f"convenience_store={_convenience_store!r}, "
            f"brand={_brand!r}, "
            f"gateway={_gateway!r}, "
            f"service_provider={_service_provider!r}, "
            f"refunds={_refunds!r}, "
            f"reason={_reason!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _mtype=(
            self.mtype
            if hasattr(self, "mtype")
            else None
        )
        _cardholder_name=(
            self.cardholder_name
            if hasattr(self, "cardholder_name")
            else None
        )
        _cardholder_email_address=(
            self.cardholder_email_address
            if hasattr(self, "cardholder_email_address")
            else None
        )
        _cardholder_phone_number=(
            self.cardholder_phone_number
            if hasattr(self, "cardholder_phone_number")
            else None
        )
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
        _brand=(
            self.brand
            if hasattr(self, "brand")
            else None
        )
        _gateway=(
            self.gateway
            if hasattr(self, "gateway")
            else None
        )
        _service_provider=(
            self.service_provider
            if hasattr(self, "service_provider")
            else None
        )
        _refunds=(
            self.refunds
            if hasattr(self, "refunds")
            else None
        )
        _reason=(
            self.reason
            if hasattr(self, "reason")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"mtype={_mtype!s}, "
            f"cardholder_name={_cardholder_name!s}, "
            f"cardholder_email_address={_cardholder_email_address!s}, "
            f"cardholder_phone_number={_cardholder_phone_number!s}, "
            f"customer_name={_customer_name!s}, "
            f"convenience_store={_convenience_store!s}, "
            f"brand={_brand!s}, "
            f"gateway={_gateway!s}, "
            f"service_provider={_service_provider!s}, "
            f"refunds={_refunds!s}, "
            f"reason={_reason!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
