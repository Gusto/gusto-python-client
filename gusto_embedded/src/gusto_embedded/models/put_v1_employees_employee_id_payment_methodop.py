"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto_embedded.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1EmployeesEmployeeIDPaymentMethodType(str, Enum):
    r"""The payment method type. If type is Check, then split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required."""

    DIRECT_DEPOSIT = "Direct Deposit"
    CHECK = "Check"


class PutV1EmployeesEmployeeIDPaymentMethodSplitBy(str, Enum):
    r"""Describes how the payment will be split. If split_by is Percentage, then the split amounts must add up to exactly 100. If split_by is Amount, then the last split amount must be nil to capture the remainder."""

    AMOUNT = "Amount"
    PERCENTAGE = "Percentage"


class SplitsTypedDict(TypedDict):
    uuid: NotRequired[str]
    r"""The bank account ID

    """
    name: NotRequired[str]
    r"""The bank account name"""
    priority: NotRequired[int]
    r"""The order of priority for each payment split, with priority 1 being the first bank account paid. Priority must be unique and sequential."""
    split_amount: NotRequired[Nullable[int]]
    r"""The cents amount allocated for each payment split"""


class Splits(BaseModel):
    uuid: Optional[str] = None
    r"""The bank account ID

    """

    name: Optional[str] = None
    r"""The bank account name"""

    priority: Optional[int] = None
    r"""The order of priority for each payment split, with priority 1 being the first bank account paid. Priority must be unique and sequential."""

    split_amount: OptionalNullable[int] = UNSET
    r"""The cents amount allocated for each payment split"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["uuid", "name", "priority", "split_amount"]
        nullable_fields = ["split_amount"]
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


class PutV1EmployeesEmployeeIDPaymentMethodRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    type: PutV1EmployeesEmployeeIDPaymentMethodType
    r"""The payment method type. If type is Check, then split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required."""
    split_by: NotRequired[PutV1EmployeesEmployeeIDPaymentMethodSplitBy]
    r"""Describes how the payment will be split. If split_by is Percentage, then the split amounts must add up to exactly 100. If split_by is Amount, then the last split amount must be nil to capture the remainder."""
    splits: NotRequired[List[SplitsTypedDict]]


class PutV1EmployeesEmployeeIDPaymentMethodRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    type: PutV1EmployeesEmployeeIDPaymentMethodType
    r"""The payment method type. If type is Check, then split_by and splits do not need to be populated. If type is Direct Deposit, split_by and splits are required."""

    split_by: Optional[PutV1EmployeesEmployeeIDPaymentMethodSplitBy] = None
    r"""Describes how the payment will be split. If split_by is Percentage, then the split amounts must add up to exactly 100. If split_by is Amount, then the last split amount must be nil to capture the remainder."""

    splits: Optional[List[Splits]] = None


class PutV1EmployeesEmployeeIDPaymentMethodRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    request_body: PutV1EmployeesEmployeeIDPaymentMethodRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1EmployeesEmployeeIDPaymentMethodRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    request_body: Annotated[
        PutV1EmployeesEmployeeIDPaymentMethodRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
