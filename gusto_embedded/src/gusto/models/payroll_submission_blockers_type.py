"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class PayrollSubmissionBlockersTypeMetadataTypedDict(TypedDict):
    r"""Additional data associated with the unblock option."""


class PayrollSubmissionBlockersTypeMetadata(BaseModel):
    r"""Additional data associated with the unblock option."""


class UnblockOptionsTypedDict(TypedDict):
    unblock_type: NotRequired[str]
    r"""The type of unblock option for the submission blocker."""
    check_date: NotRequired[str]
    r"""The payment check date associated with the unblock option."""
    metadata: NotRequired[PayrollSubmissionBlockersTypeMetadataTypedDict]
    r"""Additional data associated with the unblock option."""


class UnblockOptions(BaseModel):
    unblock_type: Optional[str] = None
    r"""The type of unblock option for the submission blocker."""

    check_date: Optional[str] = None
    r"""The payment check date associated with the unblock option."""

    metadata: Optional[PayrollSubmissionBlockersTypeMetadata] = None
    r"""Additional data associated with the unblock option."""


class PayrollSubmissionBlockersTypeStatus(str, Enum):
    r"""The status of the submission blocker."""

    UNRESOLVED = "unresolved"
    RESOLVED = "resolved"


class PayrollSubmissionBlockersTypeTypedDict(TypedDict):
    blocker_type: NotRequired[str]
    r"""The type of blocker that's blocking the payment submission."""
    blocker_name: NotRequired[str]
    r"""The name of the submission blocker."""
    unblock_options: NotRequired[List[UnblockOptionsTypedDict]]
    r"""The available options to unblock a submission blocker."""
    selected_option: NotRequired[Nullable[str]]
    r"""The unblock option that's been selected to resolve the submission blocker."""
    status: NotRequired[PayrollSubmissionBlockersTypeStatus]
    r"""The status of the submission blocker."""


class PayrollSubmissionBlockersType(BaseModel):
    blocker_type: Optional[str] = None
    r"""The type of blocker that's blocking the payment submission."""

    blocker_name: Optional[str] = None
    r"""The name of the submission blocker."""

    unblock_options: Optional[List[UnblockOptions]] = None
    r"""The available options to unblock a submission blocker."""

    selected_option: OptionalNullable[str] = UNSET
    r"""The unblock option that's been selected to resolve the submission blocker."""

    status: Optional[PayrollSubmissionBlockersTypeStatus] = None
    r"""The status of the submission blocker."""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "blocker_type",
            "blocker_name",
            "unblock_options",
            "selected_option",
            "status",
        ]
        nullable_fields = ["selected_option"]
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
