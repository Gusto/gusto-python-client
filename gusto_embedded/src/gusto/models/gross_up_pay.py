"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class GrossUpPayTypedDict(TypedDict):
    r"""Example response"""

    gross_up: NotRequired[str]
    r"""Gross up earnings."""


class GrossUpPay(BaseModel):
    r"""Example response"""

    gross_up: Optional[str] = None
    r"""Gross up earnings."""
