"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from gusto_embedded.types import BaseModel
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class ReportTemplateTypedDict(TypedDict):
    r"""Example response"""

    columns: NotRequired[List[str]]
    r"""List of columns recommended"""
    groupings: NotRequired[List[str]]
    r"""List of groupings recommended"""
    company_uuid: NotRequired[str]
    r"""Company UUID"""
    report_type: NotRequired[str]
    r"""Type of report template"""


class ReportTemplate(BaseModel):
    r"""Example response"""

    columns: Optional[List[str]] = None
    r"""List of columns recommended"""

    groupings: Optional[List[str]] = None
    r"""List of groupings recommended"""

    company_uuid: Optional[str] = None
    r"""Company UUID"""

    report_type: Optional[str] = None
    r"""Type of report template"""
