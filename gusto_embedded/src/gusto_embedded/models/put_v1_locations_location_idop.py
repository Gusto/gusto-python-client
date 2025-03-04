"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
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


class PutV1LocationsLocationIDRequestBodyTypedDict(TypedDict):
    r"""Update a location"""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""
    phone_number: NotRequired[str]
    street_1: NotRequired[str]
    street_2: NotRequired[Nullable[str]]
    city: NotRequired[str]
    state: NotRequired[str]
    zip_code: NotRequired[str]
    country: NotRequired[str]
    mailing_address: NotRequired[bool]
    r"""For a company location, specify if this location is the company's mailing address. A company has a single mailing address, so this designation will override any previous selection."""
    filing_address: NotRequired[bool]
    r"""For a company location, specify if this location is the company's filing address. A company has a single filing address, so this designation will override any previous selection."""


class PutV1LocationsLocationIDRequestBody(BaseModel):
    r"""Update a location"""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/idempotency) for information on how to use this field."""

    phone_number: Optional[str] = None

    street_1: Optional[str] = None

    street_2: OptionalNullable[str] = UNSET

    city: Optional[str] = None

    state: Optional[str] = None

    zip_code: Annotated[Optional[str], pydantic.Field(alias="zip")] = None

    country: Optional[str] = None

    mailing_address: Optional[bool] = None
    r"""For a company location, specify if this location is the company's mailing address. A company has a single mailing address, so this designation will override any previous selection."""

    filing_address: Optional[bool] = None
    r"""For a company location, specify if this location is the company's filing address. A company has a single filing address, so this designation will override any previous selection."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "phone_number",
            "street_1",
            "street_2",
            "city",
            "state",
            "zip_code",
            "country",
            "mailing_address",
            "filing_address",
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


class PutV1LocationsLocationIDRequestTypedDict(TypedDict):
    location_id: str
    r"""The UUID of the location"""
    request_body: PutV1LocationsLocationIDRequestBodyTypedDict
    r"""Update a location"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1LocationsLocationIDRequest(BaseModel):
    location_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the location"""

    request_body: Annotated[
        PutV1LocationsLocationIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Update a location"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
