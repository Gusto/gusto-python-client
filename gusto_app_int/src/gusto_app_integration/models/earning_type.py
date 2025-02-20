"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_app_integration.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class EarningTypeTypedDict(TypedDict):
    r"""Example response"""

    uuid: str
    r"""The ID of the earning type."""
    name: NotRequired[str]
    r"""The name of the earning type."""


class EarningType(BaseModel):
    r"""Example response"""

    uuid: str
    r"""The ID of the earning type."""

    name: Optional[str] = None
    r"""The name of the earning type."""
