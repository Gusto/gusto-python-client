"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from gusto_embedded.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class Category(str, Enum):
    r"""The category of the company attachment"""

    GEP_NOTICE = "gep_notice"
    COMPLIANCE = "compliance"
    OTHER = "other"


class CompanyAttachmentTypedDict(TypedDict):
    r"""The company attachment"""

    uuid: NotRequired[str]
    r"""UUID of the company attachment"""
    name: NotRequired[str]
    r"""name of the file uploaded"""
    category: NotRequired[Category]
    r"""The category of the company attachment"""
    upload_time: NotRequired[str]
    r"""The ISO 8601 timestamp of when an attachment was uploaded"""


class CompanyAttachment(BaseModel):
    r"""The company attachment"""

    uuid: Optional[str] = None
    r"""UUID of the company attachment"""

    name: Optional[str] = None
    r"""name of the file uploaded"""

    category: Optional[Category] = None
    r"""The category of the company attachment"""

    upload_time: Optional[str] = None
    r"""The ISO 8601 timestamp of when an attachment was uploaded"""
