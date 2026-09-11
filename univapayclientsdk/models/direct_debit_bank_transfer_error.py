"""univapay_client_sdk.

This file was automatically generated for Univapay by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501

class DirectDebitBankTransferError(object):
    """Implementation of the 'DirectDebitBankTransferError' enum.

    Reason a transfer failed, as reported by the bank.
    | Value | Meaning | | :--- | :--- | | `insufficient_funds` | The account did not
    hold enough money on the debit date. | | `no_deposit_transaction` | The account
    exists but has no deposit activity. | | `transfer_stopped_by_depositor` | The
    consumer instructed their bank to stop the debit. | |
    `no_account_transfer_request` | No valid direct debit mandate is on file for the
    account. | | `transfer_stopped_by_trustee` | The collecting bank stopped the
    debit. | | `other_error` | The bank reported a failure outside the categories
    above. | | `unknown_error` | The failure reason could not be determined. |

    Attributes:
        INSUFFICIENT_FUNDS: The enum member of type str.
        NO_DEPOSIT_TRANSACTION: The enum member of type str.
        TRANSFER_STOPPED_BY_DEPOSITOR: The enum member of type str.
        NO_ACCOUNT_TRANSFER_REQUEST: The enum member of type str.
        TRANSFER_STOPPED_BY_TRUSTEE: The enum member of type str.
        OTHER_ERROR: The enum member of type str.
        UNKNOWN_ERROR: The enum member of type str.

    """

    INSUFFICIENT_FUNDS = "insufficient_funds"

    NO_DEPOSIT_TRANSACTION = "no_deposit_transaction"

    TRANSFER_STOPPED_BY_DEPOSITOR = "transfer_stopped_by_depositor"

    NO_ACCOUNT_TRANSFER_REQUEST = "no_account_transfer_request"

    TRANSFER_STOPPED_BY_TRUSTEE = "transfer_stopped_by_trustee"

    OTHER_ERROR = "other_error"

    UNKNOWN_ERROR = "unknown_error"

    @classmethod
    def from_value(cls, value, default=None):
        """Return the matching enum value for the given input."""
        if value is None:
            return default

        # If numeric and matches directly
        if isinstance(value, int):
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and val == value:
                    return val

        # If string, perform case-insensitive match
        if isinstance(value, str):
            value_lower = value.lower()
            for name, val in cls.__dict__.items():
                if not name.startswith("_") and (
                    name.lower() == value_lower or str(val).lower() == value_lower
                ):
                    return val

        # Fallback to default
        return default
