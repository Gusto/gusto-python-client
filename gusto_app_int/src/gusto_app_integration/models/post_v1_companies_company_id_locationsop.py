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
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1CompaniesCompanyIDLocationsRequestBodyTypedDict(TypedDict):
    r"""Create a company location."""

    phone_number: str
    street_1: str
    city: str
    state: str
    zip_code: str
    street_2: NotRequired[Nullable[str]]
    mailing_address: NotRequired[bool]
    r"""Specify if this location is the company's mailing address."""
    filing_address: NotRequired[bool]
    r"""Specify if this location is the company's filing address."""


class PostV1CompaniesCompanyIDLocationsRequestBody(BaseModel):
    r"""Create a company location."""

    phone_number: str

    street_1: str

    city: str

    state: str

    zip_code: Annotated[str, pydantic.Field(alias="zip")]

    street_2: OptionalNullable[str] = UNSET

    mailing_address: Optional[bool] = None
    r"""Specify if this location is the company's mailing address."""

    filing_address: Optional[bool] = None
    r"""Specify if this location is the company's filing address."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["street_2", "mailing_address", "filing_address"]
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


class PostV1CompaniesCompanyIDLocationsRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PostV1CompaniesCompanyIDLocationsRequestBodyTypedDict
    r"""Create a company location."""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1CompaniesCompanyIDLocationsRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostV1CompaniesCompanyIDLocationsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Create a company location."""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
