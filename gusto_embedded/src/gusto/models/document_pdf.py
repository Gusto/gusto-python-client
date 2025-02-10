"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class DocumentPdfTypedDict(TypedDict):
    uuid: NotRequired[str]
    r"""the UUID of the document"""
    document_url: NotRequired[str]
    r"""the URL of the document"""


class DocumentPdf(BaseModel):
    uuid: Optional[str] = None
    r"""the UUID of the document"""

    document_url: Optional[str] = None
    r"""the URL of the document"""
