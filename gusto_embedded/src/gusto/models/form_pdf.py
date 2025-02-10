"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class FormPdfTypedDict(TypedDict):
    r"""Example response"""

    uuid: str
    r"""the UUID of the form"""
    document_url: NotRequired[str]
    r"""the URL of the form"""


class FormPdf(BaseModel):
    r"""Example response"""

    uuid: str
    r"""the UUID of the form"""

    document_url: Optional[str] = None
    r"""the URL of the form"""
