"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FlowTypedDict(TypedDict):
    r"""The representation of a flow in Gusto white-label UI."""

    url: NotRequired[str]


class Flow(BaseModel):
    r"""The representation of a flow in Gusto white-label UI."""

    url: Optional[str] = None
