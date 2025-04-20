"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from datetime import date
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


class PutV1HistoricalEmployeesWorkAddressTypedDict(TypedDict):
    location_uuid: NotRequired[str]
    r"""Reference to a company location"""


class PutV1HistoricalEmployeesWorkAddress(BaseModel):
    location_uuid: Optional[str] = None
    r"""Reference to a company location"""


class PutV1HistoricalEmployeesHomeAddressTypedDict(TypedDict):
    street_1: str
    city: str
    state: str
    zip: str
    street_2: NotRequired[Nullable[str]]


class PutV1HistoricalEmployeesHomeAddress(BaseModel):
    street_1: str

    city: str

    state: str

    zip: str

    street_2: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["street_2"]
        nullable_fields = ["street_2"]
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


class PutV1HistoricalEmployeesTerminationTypedDict(TypedDict):
    effective_date: NotRequired[date]
    r"""Date the employee was terminated from the company"""


class PutV1HistoricalEmployeesTermination(BaseModel):
    effective_date: Optional[date] = None
    r"""Date the employee was terminated from the company"""


class PutV1HistoricalEmployeesJobTypedDict(TypedDict):
    hire_date: NotRequired[date]
    r"""The date when the employee was hired to the company"""


class PutV1HistoricalEmployeesJob(BaseModel):
    hire_date: Optional[date] = None
    r"""The date when the employee was hired to the company"""


class PutV1HistoricalEmployeesEmployeeStateTaxesTypedDict(TypedDict):
    wc_covered: NotRequired[bool]
    r"""Whether this job is eligible for workers' compensation coverage in the states of Washington (WA) or Wyoming (WY)."""
    wc_class_code: NotRequired[str]
    r"""The risk class code for workers' compensation in Washington or Wyoming state. For Washington, visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more. For Wyoming you can search for the code online using [WY Workforce Services website](https://dws.wyo.gov/dws-division/workers-compensation/) or call the agency at (307) 235-3217."""


class PutV1HistoricalEmployeesEmployeeStateTaxes(BaseModel):
    wc_covered: Optional[bool] = None
    r"""Whether this job is eligible for workers' compensation coverage in the states of Washington (WA) or Wyoming (WY)."""

    wc_class_code: Optional[str] = None
    r"""The risk class code for workers' compensation in Washington or Wyoming state. For Washington, visit [Washington state's Risk Class page](https://www.lni.wa.gov/insurance/rates-risk-classes/risk-classes-for-workers-compensation/risk-class-lookup#/) to learn more. For Wyoming you can search for the code online using [WY Workforce Services website](https://dws.wyo.gov/dws-division/workers-compensation/) or call the agency at (307) 235-3217."""


class PutV1HistoricalEmployeesRequestBodyTypedDict(TypedDict):
    r"""Update a historical employee."""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    first_name: str
    last_name: str
    date_of_birth: str
    ssn: str
    work_address: PutV1HistoricalEmployeesWorkAddressTypedDict
    home_address: PutV1HistoricalEmployeesHomeAddressTypedDict
    termination: PutV1HistoricalEmployeesTerminationTypedDict
    job: PutV1HistoricalEmployeesJobTypedDict
    middle_initial: NotRequired[str]
    preferred_first_name: NotRequired[str]
    email: NotRequired[str]
    r"""Optional. If provided, the email address will be saved to the employee."""
    employee_state_taxes: NotRequired[
        PutV1HistoricalEmployeesEmployeeStateTaxesTypedDict
    ]


class PutV1HistoricalEmployeesRequestBody(BaseModel):
    r"""Update a historical employee."""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    first_name: str

    last_name: str

    date_of_birth: str

    ssn: str

    work_address: PutV1HistoricalEmployeesWorkAddress

    home_address: PutV1HistoricalEmployeesHomeAddress

    termination: PutV1HistoricalEmployeesTermination

    job: PutV1HistoricalEmployeesJob

    middle_initial: Optional[str] = None

    preferred_first_name: Optional[str] = None

    email: Optional[str] = None
    r"""Optional. If provided, the email address will be saved to the employee."""

    employee_state_taxes: Optional[PutV1HistoricalEmployeesEmployeeStateTaxes] = None


class PutV1HistoricalEmployeesRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    historical_employee_uuid: str
    r"""The UUID of the historical employee"""
    request_body: PutV1HistoricalEmployeesRequestBodyTypedDict
    r"""Update a historical employee."""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1HistoricalEmployeesRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    historical_employee_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the historical employee"""

    request_body: Annotated[
        PutV1HistoricalEmployeesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Update a historical employee."""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
