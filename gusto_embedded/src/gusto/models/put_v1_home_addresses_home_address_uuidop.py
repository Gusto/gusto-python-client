"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from datetime import date
from gusto.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1HomeAddressesHomeAddressUUIDRequestBodyTypedDict(TypedDict):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    street_1: NotRequired[str]
    street_2: NotRequired[Nullable[str]]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    effective_date: NotRequired[date]
    courtesy_withholding: NotRequired[bool]


class PutV1HomeAddressesHomeAddressUUIDRequestBody(BaseModel):
    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    street_1: Optional[str] = None

    street_2: OptionalNullable[str] = UNSET

    city: Optional[str] = None

    state: Optional[str] = None

    zip: Optional[str] = None

    effective_date: Optional[date] = None

    courtesy_withholding: Optional[bool] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "street_1",
            "street_2",
            "city",
            "state",
            "zip",
            "effective_date",
            "courtesy_withholding",
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


class PutV1HomeAddressesHomeAddressUUIDRequestTypedDict(TypedDict):
    home_address_uuid: str
    r"""The UUID of the home address"""
    request_body: PutV1HomeAddressesHomeAddressUUIDRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1HomeAddressesHomeAddressUUIDRequest(BaseModel):
    home_address_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the home address"""

    request_body: Annotated[
        PutV1HomeAddressesHomeAddressUUIDRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
