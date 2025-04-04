"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from gusto_embedded.types import BaseModel
from gusto_embedded.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class PutV1EmployeeFormSignRequestBodyTypedDict(TypedDict):
    signature_text: str
    r"""The signature"""
    agree: bool
    r"""Whether you agree to sign electronically"""
    signed_by_ip_address: NotRequired[str]
    r"""The IP address of the signatory who signed the form. Both IPv4 AND IPv6 are supported. You must provide the IP address with either this parameter OR you can leave out this parameter and set the IP address in the request header using the `x-gusto-client-ip` header instead."""
    preparer: NotRequired[bool]
    r"""Whether there is a preparer"""
    preparer_first_name: NotRequired[str]
    preparer_last_name: NotRequired[str]
    preparer_street_1: NotRequired[str]
    preparer_street_2: NotRequired[str]
    preparer_city: NotRequired[str]
    preparer_state: NotRequired[str]
    preparer_zip: NotRequired[str]
    preparer_agree: NotRequired[str]
    r"""Whether preparer agrees to sign electronically"""
    preparer2: NotRequired[bool]
    r"""Whether there is a 2nd preparer"""
    preparer2_first_name: NotRequired[str]
    preparer2_last_name: NotRequired[str]
    preparer2_street_1: NotRequired[str]
    preparer2_street_2: NotRequired[str]
    preparer2_city: NotRequired[str]
    preparer2_state: NotRequired[str]
    preparer2_zip: NotRequired[str]
    preparer2_agree: NotRequired[str]
    r"""Whether 2nd preparer agrees to sign electronically"""
    preparer3: NotRequired[bool]
    r"""Whether there is a 3rd preparer"""
    preparer3_first_name: NotRequired[str]
    preparer3_last_name: NotRequired[str]
    preparer3_street_1: NotRequired[str]
    preparer3_street_2: NotRequired[str]
    preparer3_city: NotRequired[str]
    preparer3_state: NotRequired[str]
    preparer3_zip: NotRequired[str]
    preparer3_agree: NotRequired[str]
    r"""Whether 3rd preparer agrees to sign electronically"""
    preparer4: NotRequired[bool]
    r"""Whether there is a 4th preparer"""
    preparer4_first_name: NotRequired[str]
    preparer4_last_name: NotRequired[str]
    preparer4_street_1: NotRequired[str]
    preparer4_street_2: NotRequired[str]
    preparer4_city: NotRequired[str]
    preparer4_state: NotRequired[str]
    preparer4_zip: NotRequired[str]
    preparer4_agree: NotRequired[str]
    r"""Whether 4th preparer agrees to sign electronically"""


class PutV1EmployeeFormSignRequestBody(BaseModel):
    signature_text: str
    r"""The signature"""

    agree: bool
    r"""Whether you agree to sign electronically"""

    signed_by_ip_address: Optional[str] = None
    r"""The IP address of the signatory who signed the form. Both IPv4 AND IPv6 are supported. You must provide the IP address with either this parameter OR you can leave out this parameter and set the IP address in the request header using the `x-gusto-client-ip` header instead."""

    preparer: Optional[bool] = None
    r"""Whether there is a preparer"""

    preparer_first_name: Optional[str] = None

    preparer_last_name: Optional[str] = None

    preparer_street_1: Optional[str] = None

    preparer_street_2: Optional[str] = None

    preparer_city: Optional[str] = None

    preparer_state: Optional[str] = None

    preparer_zip: Optional[str] = None

    preparer_agree: Optional[str] = None
    r"""Whether preparer agrees to sign electronically"""

    preparer2: Optional[bool] = None
    r"""Whether there is a 2nd preparer"""

    preparer2_first_name: Optional[str] = None

    preparer2_last_name: Optional[str] = None

    preparer2_street_1: Optional[str] = None

    preparer2_street_2: Optional[str] = None

    preparer2_city: Optional[str] = None

    preparer2_state: Optional[str] = None

    preparer2_zip: Optional[str] = None

    preparer2_agree: Optional[str] = None
    r"""Whether 2nd preparer agrees to sign electronically"""

    preparer3: Optional[bool] = None
    r"""Whether there is a 3rd preparer"""

    preparer3_first_name: Optional[str] = None

    preparer3_last_name: Optional[str] = None

    preparer3_street_1: Optional[str] = None

    preparer3_street_2: Optional[str] = None

    preparer3_city: Optional[str] = None

    preparer3_state: Optional[str] = None

    preparer3_zip: Optional[str] = None

    preparer3_agree: Optional[str] = None
    r"""Whether 3rd preparer agrees to sign electronically"""

    preparer4: Optional[bool] = None
    r"""Whether there is a 4th preparer"""

    preparer4_first_name: Optional[str] = None

    preparer4_last_name: Optional[str] = None

    preparer4_street_1: Optional[str] = None

    preparer4_street_2: Optional[str] = None

    preparer4_city: Optional[str] = None

    preparer4_state: Optional[str] = None

    preparer4_zip: Optional[str] = None

    preparer4_agree: Optional[str] = None
    r"""Whether 4th preparer agrees to sign electronically"""


class PutV1EmployeeFormSignRequestTypedDict(TypedDict):
    employee_id: str
    r"""The UUID of the employee"""
    form_id: str
    r"""The UUID of the form"""
    request_body: PutV1EmployeeFormSignRequestBodyTypedDict
    x_gusto_client_ip: NotRequired[str]
    r"""Optional header to supply the IP address. This can be used to supply the IP address for signature endpoints instead of the signed_by_ip_address parameter."""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1EmployeeFormSignRequest(BaseModel):
    employee_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the employee"""

    form_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the form"""

    request_body: Annotated[
        PutV1EmployeeFormSignRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_client_ip: Annotated[
        Optional[str],
        pydantic.Field(alias="x-gusto-client-ip"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Optional header to supply the IP address. This can be used to supply the IP address for signature endpoints instead of the signed_by_ip_address parameter."""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
