"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_app_integration.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from gusto_app_integration.utils import (
    FieldMetadata,
    HeaderMetadata,
    RequestMetadata,
    SecurityMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1ProvisionSecurityTypedDict(TypedDict):
    system_access_auth: str


class PostV1ProvisionSecurity(BaseModel):
    system_access_auth: Annotated[
        str,
        FieldMetadata(
            security=SecurityMetadata(
                scheme=True,
                scheme_type="http",
                sub_type="bearer",
                field_name="Authorization",
            )
        ),
    ]


class UserTypedDict(TypedDict):
    r"""Information for the user who will be the primary payroll administrator for the new company."""

    first_name: str
    r"""The first name of the user who will be the primary payroll admin."""
    last_name: str
    r"""The last name of the user who will be the primary payroll admin."""
    email: str
    r"""The email of the user who will be the primary payroll admin."""
    phone: NotRequired[str]
    r"""The phone number of the user who will be the primary payroll admin."""


class User(BaseModel):
    r"""Information for the user who will be the primary payroll administrator for the new company."""

    first_name: str
    r"""The first name of the user who will be the primary payroll admin."""

    last_name: str
    r"""The last name of the user who will be the primary payroll admin."""

    email: str
    r"""The email of the user who will be the primary payroll admin."""

    phone: Optional[str] = None
    r"""The phone number of the user who will be the primary payroll admin."""


class AddressesTypedDict(TypedDict):
    street_1: NotRequired[str]
    street_2: NotRequired[Nullable[str]]
    city: NotRequired[str]
    zip_code: NotRequired[str]
    state: NotRequired[str]
    phone: NotRequired[str]
    is_primary: NotRequired[str]
    r"""Whether or not this is a primary address for the company. If set to true, the address will be used as the mailing and filing address for the company and will be added as a work location. If set to false or not included, the address will only be added as a work location for the company. If multiple addresses are included, only one should be marked as primary."""


class Addresses(BaseModel):
    street_1: Optional[str] = None

    street_2: OptionalNullable[str] = UNSET

    city: Optional[str] = None

    zip_code: Annotated[Optional[str], pydantic.Field(alias="zip")] = None

    state: Optional[str] = None

    phone: Optional[str] = None

    is_primary: Optional[str] = None
    r"""Whether or not this is a primary address for the company. If set to true, the address will be used as the mailing and filing address for the company and will be added as a work location. If set to false or not included, the address will only be added as a work location for the company. If multiple addresses are included, only one should be marked as primary."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "street_1",
            "street_2",
            "city",
            "zip_code",
            "state",
            "phone",
            "is_primary",
        ]
        nullable_fields = ["street_2"]
        null_default_fields = []

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


class PostV1ProvisionCompanyTypedDict(TypedDict):
    name: str
    r"""The legal name of the company."""
    trade_name: NotRequired[str]
    r"""The name of the company."""
    ein: NotRequired[str]
    r"""The employer identification number (EIN) of the company."""
    states: NotRequired[List[str]]
    r"""The states in which the company operates. States should be included by their two letter code, i.e. NY for New York."""
    number_employees: NotRequired[float]
    r"""The number of employees in the company."""
    addresses: NotRequired[List[AddressesTypedDict]]
    r"""The locations for the company. This includes mailing, work, and filing addresses."""


class PostV1ProvisionCompany(BaseModel):
    name: str
    r"""The legal name of the company."""

    trade_name: Optional[str] = None
    r"""The name of the company."""

    ein: Optional[str] = None
    r"""The employer identification number (EIN) of the company."""

    states: Optional[List[str]] = None
    r"""The states in which the company operates. States should be included by their two letter code, i.e. NY for New York."""

    number_employees: Optional[float] = None
    r"""The number of employees in the company."""

    addresses: Optional[List[Addresses]] = None
    r"""The locations for the company. This includes mailing, work, and filing addresses."""


class PostV1ProvisionRequestBodyTypedDict(TypedDict):
    user: UserTypedDict
    r"""Information for the user who will be the primary payroll administrator for the new company."""
    company: PostV1ProvisionCompanyTypedDict


class PostV1ProvisionRequestBody(BaseModel):
    user: User
    r"""Information for the user who will be the primary payroll administrator for the new company."""

    company: PostV1ProvisionCompany


class PostV1ProvisionRequestTypedDict(TypedDict):
    request_body: PostV1ProvisionRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1ProvisionRequest(BaseModel):
    request_body: Annotated[
        PostV1ProvisionRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1ProvisionResponseBodyTypedDict(TypedDict):
    r"""OK"""

    account_claim_url: NotRequired[str]
    r"""A URL where the user should be redirected to complete their account setup inside of Gusto."""


class PostV1ProvisionResponseBody(BaseModel):
    r"""OK"""

    account_claim_url: Optional[str] = None
    r"""A URL where the user should be redirected to complete their account setup inside of Gusto."""
