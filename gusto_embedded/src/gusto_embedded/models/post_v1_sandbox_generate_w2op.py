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
from gusto_embedded.utils import FieldMetadata, HeaderMetadata, RequestMetadata
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PostV1SandboxGenerateW2RequestBodyTypedDict(TypedDict):
    employee_id: str
    r"""The employee UUID."""
    year: NotRequired[int]
    r"""Must be equal to or more recent than 2015. If not specified, defaults to the previous year.

    """


class PostV1SandboxGenerateW2RequestBody(BaseModel):
    employee_id: str
    r"""The employee UUID."""

    year: Optional[int] = None
    r"""Must be equal to or more recent than 2015. If not specified, defaults to the previous year.

    """


class PostV1SandboxGenerateW2RequestTypedDict(TypedDict):
    request_body: PostV1SandboxGenerateW2RequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1SandboxGenerateW2Request(BaseModel):
    request_body: Annotated[
        PostV1SandboxGenerateW2RequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostV1SandboxGenerateW2FormTypedDict(TypedDict):
    r"""OK"""

    uuid: str
    r"""The UUID of the form"""
    employee_uuid: NotRequired[str]
    r"""The UUID of the employee"""
    name: NotRequired[str]
    r"""The type identifier of the form"""
    title: NotRequired[str]
    r"""The title of the form"""
    description: NotRequired[str]
    r"""The description of the form"""
    draft: NotRequired[bool]
    r"""If the form is in a draft state. E.g. End of year tax forms may be provided in a draft state prior to being finalized."""
    year: NotRequired[Nullable[int]]
    r"""The year of this form. For some forms, e.g. tax forms, this is the year which the form represents. A W2 for January - December 2022 would be delivered in January 2023 and have a year value of 2022. This value is nullable and will not be present on all forms."""
    quarter: NotRequired[Nullable[int]]
    r"""The quarter of this form. For some forms, e.g. tax forms, this is the calendar quarter which this form represents. An Employer's Quarterly Federal Tax Return (Form 941) for April, May, June 2022 would have a quarter value of 2 (and a year value of 2022). This value is nullable and will not be present on all forms."""
    requires_signing: NotRequired[bool]
    r"""A boolean flag that indicates whether the form needs signing or not. Note that this value will change after the form is signed."""
    document_content_type: NotRequired[Nullable[str]]
    r"""The content type of the associated document. Most forms are PDFs with a content type of `application/pdf`. Some tax file packages will be zip files (containing PDFs) with a content type of `application/zip`. This attribute will be `null` when the document has not been prepared."""


class PostV1SandboxGenerateW2Form(BaseModel):
    r"""OK"""

    uuid: str
    r"""The UUID of the form"""

    employee_uuid: Optional[str] = None
    r"""The UUID of the employee"""

    name: Optional[str] = None
    r"""The type identifier of the form"""

    title: Optional[str] = None
    r"""The title of the form"""

    description: Optional[str] = None
    r"""The description of the form"""

    draft: Optional[bool] = None
    r"""If the form is in a draft state. E.g. End of year tax forms may be provided in a draft state prior to being finalized."""

    year: OptionalNullable[int] = UNSET
    r"""The year of this form. For some forms, e.g. tax forms, this is the year which the form represents. A W2 for January - December 2022 would be delivered in January 2023 and have a year value of 2022. This value is nullable and will not be present on all forms."""

    quarter: OptionalNullable[int] = UNSET
    r"""The quarter of this form. For some forms, e.g. tax forms, this is the calendar quarter which this form represents. An Employer's Quarterly Federal Tax Return (Form 941) for April, May, June 2022 would have a quarter value of 2 (and a year value of 2022). This value is nullable and will not be present on all forms."""

    requires_signing: Optional[bool] = None
    r"""A boolean flag that indicates whether the form needs signing or not. Note that this value will change after the form is signed."""

    document_content_type: OptionalNullable[str] = UNSET
    r"""The content type of the associated document. Most forms are PDFs with a content type of `application/pdf`. Some tax file packages will be zip files (containing PDFs) with a content type of `application/zip`. This attribute will be `null` when the document has not been prepared."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "employee_uuid",
            "name",
            "title",
            "description",
            "draft",
            "year",
            "quarter",
            "requires_signing",
            "document_content_type",
        ]
        nullable_fields = ["year", "quarter", "document_content_type"]
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
