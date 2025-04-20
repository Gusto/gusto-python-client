"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .contractor_payment_for_group import (
    ContractorPaymentForGroup,
    ContractorPaymentForGroupTypedDict,
)
from enum import Enum
from gusto_app_integration.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ContractorPaymentGroupStatus(str, Enum):
    r"""The status of the contractor payment group.  Will be `Funded` if all payments that should be funded (i.e. have `Direct Deposit` for payment method) are funded.  A group can have status `Funded` while having associated payments that have status `Unfunded`, i.e. payment with `Check` payment method."""

    UNFUNDED = "Unfunded"
    FUNDED = "Funded"


class ContractorPaymentGroupTotalsTypedDict(TypedDict):
    amount: NotRequired[str]
    r"""The total amount for the group of contractor payments."""
    debit_amount: NotRequired[str]
    r"""The total debit amount for the group of contractor payments. Sum of wage & reimbursement amount."""
    wage_amount: NotRequired[str]
    r"""The total wage amount for the group of contractor payments."""
    reimbursement_amount: NotRequired[str]
    r"""The total reimbursement amount for the group of contractor payments."""


class ContractorPaymentGroupTotals(BaseModel):
    amount: Optional[str] = None
    r"""The total amount for the group of contractor payments."""

    debit_amount: Optional[str] = None
    r"""The total debit amount for the group of contractor payments. Sum of wage & reimbursement amount."""

    wage_amount: Optional[str] = None
    r"""The total wage amount for the group of contractor payments."""

    reimbursement_amount: Optional[str] = None
    r"""The total reimbursement amount for the group of contractor payments."""


class ContractorPaymentGroupTypedDict(TypedDict):
    r"""The full contractor payment group, including associated contractor payments."""

    uuid: NotRequired[str]
    r"""The unique identifier of the contractor payment group."""
    company_uuid: NotRequired[str]
    r"""The UUID of the company."""
    check_date: NotRequired[str]
    r"""The check date of the contractor payment group."""
    debit_date: NotRequired[str]
    r"""The debit date of the contractor payment group."""
    status: NotRequired[ContractorPaymentGroupStatus]
    r"""The status of the contractor payment group.  Will be `Funded` if all payments that should be funded (i.e. have `Direct Deposit` for payment method) are funded.  A group can have status `Funded` while having associated payments that have status `Unfunded`, i.e. payment with `Check` payment method."""
    creation_token: NotRequired[Nullable[str]]
    r"""Token used to make contractor payment group creation idempotent.  Will error if attempting to create a group with a duplicate token."""
    totals: NotRequired[ContractorPaymentGroupTotalsTypedDict]
    contractor_payments: NotRequired[List[ContractorPaymentForGroupTypedDict]]


class ContractorPaymentGroup(BaseModel):
    r"""The full contractor payment group, including associated contractor payments."""

    uuid: Optional[str] = None
    r"""The unique identifier of the contractor payment group."""

    company_uuid: Optional[str] = None
    r"""The UUID of the company."""

    check_date: Optional[str] = None
    r"""The check date of the contractor payment group."""

    debit_date: Optional[str] = None
    r"""The debit date of the contractor payment group."""

    status: Optional[ContractorPaymentGroupStatus] = None
    r"""The status of the contractor payment group.  Will be `Funded` if all payments that should be funded (i.e. have `Direct Deposit` for payment method) are funded.  A group can have status `Funded` while having associated payments that have status `Unfunded`, i.e. payment with `Check` payment method."""

    creation_token: OptionalNullable[str] = UNSET
    r"""Token used to make contractor payment group creation idempotent.  Will error if attempting to create a group with a duplicate token."""

    totals: Optional[ContractorPaymentGroupTotals] = None

    contractor_payments: Optional[List[ContractorPaymentForGroup]] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "uuid",
            "company_uuid",
            "check_date",
            "debit_date",
            "status",
            "creation_token",
            "totals",
            "contractor_payments",
        ]
        nullable_fields = ["creation_token"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
