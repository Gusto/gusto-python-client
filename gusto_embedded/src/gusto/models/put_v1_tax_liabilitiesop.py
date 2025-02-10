"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto.types import BaseModel, Nullable, UNSET_SENTINEL
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class LiabilitySelectionsTypedDict(TypedDict):
    tax_id: int
    r"""The ID of the tax."""
    last_unpaid_external_payroll_uuid: Nullable[str]
    r"""The UUID of the last unpaid external payroll uuid. It should be null when the full amount of tax liability has been paid."""
    unpaid_liability_amount: float
    r"""A selection of unpaid liability amount."""


class LiabilitySelections(BaseModel):
    tax_id: int
    r"""The ID of the tax."""

    last_unpaid_external_payroll_uuid: Nullable[str]
    r"""The UUID of the last unpaid external payroll uuid. It should be null when the full amount of tax liability has been paid."""

    unpaid_liability_amount: float
    r"""A selection of unpaid liability amount."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["last_unpaid_external_payroll_uuid"]
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


class PutV1TaxLiabilitiesRequestBodyTypedDict(TypedDict):
    liability_selections: NotRequired[List[LiabilitySelectionsTypedDict]]


class PutV1TaxLiabilitiesRequestBody(BaseModel):
    liability_selections: Optional[List[LiabilitySelections]] = None


class PutV1TaxLiabilitiesRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PutV1TaxLiabilitiesRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1TaxLiabilitiesRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutV1TaxLiabilitiesRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
