"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .garnishment_child_support import (
    GarnishmentChildSupport,
    GarnishmentChildSupportTypedDict,
)
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
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1EmployeesEmployeeIDGarnishmentsGarnishmentType(str, Enum):
    r"""The specific type of garnishment for court ordered garnishments."""

    CHILD_SUPPORT = "child_support"
    FEDERAL_TAX_LIEN = "federal_tax_lien"
    STATE_TAX_LIEN = "state_tax_lien"
    STUDENT_LOAN = "student_loan"
    CREDITOR_GARNISHMENT = "creditor_garnishment"
    FEDERAL_LOAN = "federal_loan"
    OTHER_GARNISHMENT = "other_garnishment"


class PostV1EmployeesEmployeeIDGarnishmentsRequestBodyTypedDict(TypedDict):
    amount: str
    r"""The amount of the garnishment. Either a percentage or a fixed dollar amount. Represented as a float, e.g. \"8.00\"."""
    court_ordered: bool
    r"""Whether the garnishment is court ordered."""
    active: NotRequired[bool]
    r"""Whether or not this garnishment is currently active."""
    description: NotRequired[str]
    r"""The description of the garnishment."""
    garnishment_type: NotRequired[
        Nullable[PostV1EmployeesEmployeeIDGarnishmentsGarnishmentType]
    ]
    r"""The specific type of garnishment for court ordered garnishments."""
    times: NotRequired[Nullable[int]]
    r"""The number of times to apply the garnishment. Ignored if recurring is true."""
    recurring: NotRequired[bool]
    r"""Whether the garnishment should recur indefinitely."""
    annual_maximum: NotRequired[Nullable[str]]
    r"""The maximum deduction per annum. A null value indicates no maximum. Represented as a float, e.g. \"200.00\"."""
    pay_period_maximum: NotRequired[Nullable[str]]
    r"""The maximum deduction per pay period. A null value indicates no maximum. Represented as a float, e.g. \"16.00\"."""
    deduct_as_percentage: NotRequired[bool]
    r"""Whether the amount should be treated as a percentage to be deducted per pay period."""
    total_amount: NotRequired[str]
    r"""A maximum total deduction for the lifetime of this garnishment. A null value indicates no maximum."""
    child_support: NotRequired[Nullable[GarnishmentChildSupportTypedDict]]
    r"""Additional child support order details"""


class PostV1EmployeesEmployeeIDGarnishmentsRequestBody(BaseModel):
    amount: str
    r"""The amount of the garnishment. Either a percentage or a fixed dollar amount. Represented as a float, e.g. \"8.00\"."""

    court_ordered: bool
    r"""Whether the garnishment is court ordered."""

    active: Optional[bool] = True
    r"""Whether or not this garnishment is currently active."""

    description: Optional[str] = None
    r"""The description of the garnishment."""

    garnishment_type: OptionalNullable[
        PostV1EmployeesEmployeeIDGarnishmentsGarnishmentType
    ] = UNSET
    r"""The specific type of garnishment for court ordered garnishments."""

    times: OptionalNullable[int] = None
    r"""The number of times to apply the garnishment. Ignored if recurring is true."""

    recurring: Optional[bool] = False
    r"""Whether the garnishment should recur indefinitely."""

    annual_maximum: OptionalNullable[str] = None
    r"""The maximum deduction per annum. A null value indicates no maximum. Represented as a float, e.g. \"200.00\"."""

    pay_period_maximum: OptionalNullable[str] = None
    r"""The maximum deduction per pay period. A null value indicates no maximum. Represented as a float, e.g. \"16.00\"."""

    deduct_as_percentage: Optional[bool] = False
    r"""Whether the amount should be treated as a percentage to be deducted per pay period."""

    total_amount: Optional[str] = None
    r"""A maximum total deduction for the lifetime of this garnishment. A null value indicates no maximum."""

    child_support: OptionalNullable[GarnishmentChildSupport] = UNSET
    r"""Additional child support order details"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "active",
            "description",
            "garnishment_type",
            "times",
            "recurring",
            "annual_maximum",
            "pay_period_maximum",
            "deduct_as_percentage",
            "total_amount",
            "child_support",
        ]
        nullable_fields = [
            "garnishment_type",
            "times",
            "annual_maximum",
            "pay_period_maximum",
            "child_support",
        ]
        null_default_fields = ["times", "annual_maximum", "pay_period_maximum"]

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
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


class PostV1EmployeesEmployeeIDGarnishmentsRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    request_body: PostV1EmployeesEmployeeIDGarnishmentsRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1EmployeesEmployeeIDGarnishmentsRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    request_body: Annotated[
        PostV1EmployeesEmployeeIDGarnishmentsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
