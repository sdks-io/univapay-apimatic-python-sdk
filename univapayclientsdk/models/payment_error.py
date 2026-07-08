"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from univapayclientsdk.api_helper import APIHelper


class PaymentError(object):
    """Implementation of the 'PaymentError' model.

    Payment errors that occur during resource processing (like Charges or Refunds).
    The HTTP status will return success (2xx), but the resource `status` will be
    `failed`, and this object will be populated.

    Attributes:
        code (int): Payment Error Codes.  | Code | Description | | :--- | :--- | |
            301 | Card number error. | | 302 | Invalid expiration month. | | 303 |
            Invalid expiration year. | | 304 | Card expired. | | 305 | Security code
            (CVV) error. | | 306 | Card declined (authorization screening error). | |
            307 | Invalid card. | | 308 | This card has not been approved by the card
            company. | | 309 | General error occurred. Detailed information can be
            confirmed in the dashboard. | | 310 | Invalid consumer data (invalid
            request data). | | 311 | Too many charges on the same card in a short
            period. Please wait and try again. | | 312 | This charge cannot be
            canceled. | | 313 | Authorization expired (during charge capture). | |
            314 | This card has been reported stolen or invalidated by the issuer. |
            | 315 | Please contact the card issuer. | | 316 | Cardholder's last name
            is required. | | 317 | Partial capture is not supported. | | 318 |
            Partial refund is not supported. | | 319 | Suspected fraud (security
            restriction). | | 320 | An error occurred in the bank's system. | | 321 |
            Dynamic descriptor is not supported. | | 322 | Barcode/QR code is
            invalid. | | 323 | Barcode/QR code has expired. | | 324 | This barcode/QR
            code has already been processed. | | 325 | This barcode/QR code is
            currently being processed. | | 326 | Rejected due to a high-risk profile.
            | | 327 | Payment deadline (5-minute timeout) has expired. | | 328 |
            Recovery failed. Manual intervention is required. | | 329 | Refund
            failed. | | 330 | Insufficient funds. | | 331 | Metadata field value is
            invalid or missing. | | 332 | Cross-border transaction not permitted:
            missing ID. | | 333 | Cross-border transaction not permitted: missing
            phone number. | | 334 | Cross-border transaction not permitted:
            unauthorized payment method. | | 335 | Cross-border transaction not
            permitted: missing name. | | 336 | Exceeded the payment limit for this
            payment method. | | 337 | Exceeded the payment limit for this merchant. |
            | 338 | Payment information not found. | | 339 | Duplicate payment
            information. | | 340 | This consumer's retail QR account was rejected by
            the gateway. | | 341 | This merchant lacks the necessary information for
            this gateway. | | 342 | Cross-border transaction not permitted:
            unauthorized currency. | | 343 | Payment could not be processed due to a
            server error at the gateway. | | 344 | The selected payment method is
            temporarily unavailable from the gateway. | | 345 | The payment has
            already been canceled. | | 346 | Payment processing timed out due to
            system delay and was canceled. | | 351 | Invalid transaction. | | 355 |
            The card does not support the specified payment division (e.g.,
            installments). | | 356 | The card is not registered for 3D Secure. | |
            358 | 3D Secure authentication failed (consumer reason, e.g., wrong
            password). | | 359 | 3D Secure authentication failed (card company
            reason). | | 500 | A pre-processing error occurred during the request
            execution. | | 501 | An internal error occurred. Please contact support.
            | | 502 | The request timed out waiting for a response. | | 601 | A
            system-released error occurred in this service. Check details. | | 602 |
            The payment processor rejected the submitted request. Check details. | |
            603 | The submitted customer identity verification was rejected by
            customs. | | 604 | The required customer ID information was not submitted
            by the merchant. |
        message (str): A brief message detailing why the payment failed.
        detail (str): Further specific details regarding the payment failure, if
            available.
        additional_properties (Dict[str, Any]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": "code",
        "message": "message",
        "detail": "detail",
    }

    _optionals = [
        "code",
        "message",
        "detail",
    ]

    def __init__(
        self,
        code=APIHelper.SKIP,
        message=APIHelper.SKIP,
        detail=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a PaymentError instance."""
        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code
        if message is not APIHelper.SKIP:
            self.message = message
        if detail is not APIHelper.SKIP:
            self.detail = detail

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
        code =\
            dictionary.get("code")\
            if dictionary.get("code")\
                else APIHelper.SKIP
        message =\
            dictionary.get("message")\
            if dictionary.get("message")\
                else APIHelper.SKIP
        detail =\
            dictionary.get("detail")\
            if dictionary.get("detail")\
                else APIHelper.SKIP

        additional_properties = APIHelper.get_additional_properties(
            dictionary={k: v for k, v in dictionary.items()
                        if k not in cls._names.values()},
            unboxing_function=lambda value: value)

        # Return an object of this model
        return cls(code,
                   message,
                   detail,
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
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _detail=(
            self.detail
            if hasattr(self, "detail")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!r}, "
            f"message={_message!r}, "
            f"detail={_detail!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _code=(
            self.code
            if hasattr(self, "code")
            else None
        )
        _message=(
            self.message
            if hasattr(self, "message")
            else None
        )
        _detail=(
            self.detail
            if hasattr(self, "detail")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"code={_code!s}, "
            f"message={_message!s}, "
            f"detail={_detail!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
