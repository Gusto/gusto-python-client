"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .tax_requirement_metadata import (
    TaxRequirementMetadata,
    TaxRequirementMetadataTypedDict,
)
from gusto_embedded.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from pydantic import model_serializer
from typing import List, Optional, Union
from typing_extensions import NotRequired, TypeAliasType, TypedDict


TaxRequirementApplicableIfValueTypedDict = TypeAliasType(
    "TaxRequirementApplicableIfValueTypedDict", Union[bool, str, float]
)
r"""The required value of the requirement identified by `key`"""


TaxRequirementApplicableIfValue = TypeAliasType(
    "TaxRequirementApplicableIfValue", Union[bool, str, float]
)
r"""The required value of the requirement identified by `key`"""


class ApplicableIfTypedDict(TypedDict):
    key: NotRequired[str]
    r"""An identifier for an individual requirement. Uniqueness is guaranteed within a requirement set."""
    value: NotRequired[Nullable[TaxRequirementApplicableIfValueTypedDict]]
    r"""The required value of the requirement identified by `key`"""


class ApplicableIf(BaseModel):
    key: Optional[str] = None
    r"""An identifier for an individual requirement. Uniqueness is guaranteed within a requirement set."""

    value: OptionalNullable[TaxRequirementApplicableIfValue] = UNSET
    r"""The required value of the requirement identified by `key`"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["key", "value"]
        nullable_fields = ["value"]
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


TaxRequirementValueTypedDict = TypeAliasType(
    "TaxRequirementValueTypedDict", Union[str, bool]
)
r"""The \"answer\" """


TaxRequirementValue = TypeAliasType("TaxRequirementValue", Union[str, bool])
r"""The \"answer\" """


class TaxRequirementTypedDict(TypedDict):
    key: NotRequired[str]
    r"""An identifier for an individual requirement. Uniqueness is guaranteed within a requirement set."""
    applicable_if: NotRequired[List[ApplicableIfTypedDict]]
    r"""An array of references to other requirements within the requirement set. This requirement is only applicable if all referenced requirements have values matching the corresponding `value`. The primary use-case is dynamically hiding and showing requirements as values change. E.g. Show Requirement-B when Requirement-A has been answered with `false`. To be explicit, an empty array means the requirement is applicable."""
    label: NotRequired[str]
    r"""A customer facing description of the requirement"""
    description: NotRequired[Nullable[str]]
    r"""A more detailed customer facing description of the requirement"""
    value: NotRequired[Nullable[TaxRequirementValueTypedDict]]
    r"""The \"answer\" """
    metadata: NotRequired[TaxRequirementMetadataTypedDict]


class TaxRequirement(BaseModel):
    key: Optional[str] = None
    r"""An identifier for an individual requirement. Uniqueness is guaranteed within a requirement set."""

    applicable_if: Optional[List[ApplicableIf]] = None
    r"""An array of references to other requirements within the requirement set. This requirement is only applicable if all referenced requirements have values matching the corresponding `value`. The primary use-case is dynamically hiding and showing requirements as values change. E.g. Show Requirement-B when Requirement-A has been answered with `false`. To be explicit, an empty array means the requirement is applicable."""

    label: Optional[str] = None
    r"""A customer facing description of the requirement"""

    description: OptionalNullable[str] = UNSET
    r"""A more detailed customer facing description of the requirement"""

    value: OptionalNullable[TaxRequirementValue] = UNSET
    r"""The \"answer\" """

    metadata: Optional[TaxRequirementMetadata] = None

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "key",
            "applicable_if",
            "label",
            "description",
            "value",
            "metadata",
        ]
        nullable_fields = ["description", "value"]
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
