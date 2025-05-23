"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing_extensions import NotRequired, TypedDict


class FormPdfTypedDict(TypedDict):
    r"""Example response"""

    uuid: str
    r"""the UUID of the form"""
    document_url: NotRequired[Nullable[str]]
    r"""the URL of the form"""
    document_content_type: NotRequired[Nullable[str]]
    r"""The content type of the associated document. Most forms are PDFs with a content type of `application/pdf`. Some tax file packages will be zip files (containing PDFs) with a content type of `application/zip`. This attribute will be `null` when the document has not been prepared."""


class FormPdf(BaseModel):
    r"""Example response"""

    uuid: str
    r"""the UUID of the form"""

    document_url: OptionalNullable[str] = UNSET
    r"""the URL of the form"""

    document_content_type: OptionalNullable[str] = UNSET
    r"""The content type of the associated document. Most forms are PDFs with a content type of `application/pdf`. Some tax file packages will be zip files (containing PDFs) with a content type of `application/zip`. This attribute will be `null` when the document has not been prepared."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["document_url", "document_content_type"]
        nullable_fields = ["document_url", "document_content_type"]
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
