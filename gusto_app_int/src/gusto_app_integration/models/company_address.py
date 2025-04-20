"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_app_integration.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CompanyAddressTypedDict(TypedDict):
    r"""The representation of a company's address in Gusto."""

    street_1: NotRequired[str]
    street_2: NotRequired[Nullable[str]]
    city: NotRequired[str]
    state: NotRequired[str]
    zip: NotRequired[str]
    country: NotRequired[str]
    active: NotRequired[bool]
    r"""The status of the location. Inactive locations have been deleted, but may still have historical data associated with them."""


class CompanyAddress(BaseModel):
    r"""The representation of a company's address in Gusto."""

    street_1: Optional[str] = None

    street_2: OptionalNullable[str] = UNSET

    city: Optional[str] = None

    state: Optional[str] = None

    zip: Optional[str] = None

    country: Optional[str] = "USA"

    active: Optional[bool] = None
    r"""The status of the location. Inactive locations have been deleted, but may still have historical data associated with them."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "street_1",
            "street_2",
            "city",
            "state",
            "zip",
            "country",
            "active",
        ]
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
