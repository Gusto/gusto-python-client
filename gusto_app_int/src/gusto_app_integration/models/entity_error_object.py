"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_app_integration.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class MetadataTypedDict(TypedDict):
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""


class Metadata(BaseModel):
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""


class EntityErrorObjectMetadataTypedDict(TypedDict):
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""


class EntityErrorObjectMetadata(BaseModel):
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""


class ErrorsTypedDict(TypedDict):
    error_key: NotRequired[str]
    r"""Specifies where the error occurs. Typically this key identifies the attribute/parameter related to the error."""
    category: NotRequired[str]
    r"""Specifies the type of error. The category provides error groupings and can be used to build custom error handling in your integration. If category is `nested_errors`, the object will contain a nested `errors` property with entity errors."""
    message: NotRequired[str]
    r"""Provides details about the error - generally this message can be surfaced to an end user."""
    metadata: NotRequired[EntityErrorObjectMetadataTypedDict]
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""


class Errors(BaseModel):
    error_key: Optional[str] = None
    r"""Specifies where the error occurs. Typically this key identifies the attribute/parameter related to the error."""

    category: Optional[str] = None
    r"""Specifies the type of error. The category provides error groupings and can be used to build custom error handling in your integration. If category is `nested_errors`, the object will contain a nested `errors` property with entity errors."""

    message: Optional[str] = None
    r"""Provides details about the error - generally this message can be surfaced to an end user."""

    metadata: Optional[EntityErrorObjectMetadata] = None
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""


class EntityErrorObjectTypedDict(TypedDict):
    error_key: NotRequired[str]
    r"""Specifies where the error occurs. Typically this key identifies the attribute/parameter related to the error."""
    category: NotRequired[str]
    r"""Specifies the type of error. The category provides error groupings and can be used to build custom error handling in your integration. If category is `nested_errors`, the object will contain a nested `errors` property with entity errors."""
    message: NotRequired[str]
    r"""Provides details about the error - generally this message can be surfaced to an end user."""
    metadata: NotRequired[MetadataTypedDict]
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""
    errors: NotRequired[List[ErrorsTypedDict]]
    r"""Will only exist if category is `nested_errors`. It is possible to have multiple levels of nested errors."""


class EntityErrorObject(BaseModel):
    error_key: Optional[str] = None
    r"""Specifies where the error occurs. Typically this key identifies the attribute/parameter related to the error."""

    category: Optional[str] = None
    r"""Specifies the type of error. The category provides error groupings and can be used to build custom error handling in your integration. If category is `nested_errors`, the object will contain a nested `errors` property with entity errors."""

    message: Optional[str] = None
    r"""Provides details about the error - generally this message can be surfaced to an end user."""

    metadata: Optional[Metadata] = None
    r"""Contains relevant data to identify the resource in question when applicable. For example, to identify an entity `entity_type` and `entity_uuid` will be provided."""

    errors: Optional[List[Errors]] = None
    r"""Will only exist if category is `nested_errors`. It is possible to have multiple levels of nested errors."""
