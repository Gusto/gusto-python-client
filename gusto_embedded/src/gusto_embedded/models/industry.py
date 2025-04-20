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
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class IndustryTypedDict(TypedDict):
    r"""Example response"""

    company_uuid: NotRequired[str]
    r"""Company uuid"""
    naics_code: NotRequired[Nullable[str]]
    r"""North American Industry Classification System (NAICS) is used to classify businesses with a six digit number based on the primary type of work the business performs."""
    sic_codes: NotRequired[List[str]]
    r"""A list of Standard Industrial Classification (SIC) codes, which are four digit number that categorize the industries that companies belong to based on their business activities."""
    title: NotRequired[Nullable[str]]
    r"""Industry title"""


class Industry(BaseModel):
    r"""Example response"""

    company_uuid: Optional[str] = None
    r"""Company uuid"""

    naics_code: OptionalNullable[str] = UNSET
    r"""North American Industry Classification System (NAICS) is used to classify businesses with a six digit number based on the primary type of work the business performs."""

    sic_codes: Optional[List[str]] = None
    r"""A list of Standard Industrial Classification (SIC) codes, which are four digit number that categorize the industries that companies belong to based on their business activities."""

    title: OptionalNullable[str] = UNSET
    r"""Industry title"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["company_uuid", "naics_code", "sic_codes", "title"]
        nullable_fields = ["naics_code", "title"]
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
