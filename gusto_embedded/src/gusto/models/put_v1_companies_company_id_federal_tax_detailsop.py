"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .versionheader import VersionHeader
from enum import Enum
from gusto.types import BaseModel
from gusto.utils import (
    FieldMetadata,
    HeaderMetadata,
    PathParamMetadata,
    RequestMetadata,
)
import pydantic
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class TaxPayerType(str, Enum):
    r"""What type of tax entity the company is"""

    C_CORPORATION = "C-Corporation"
    S_CORPORATION = "S-Corporation"
    SOLE_PROPRIETOR = "Sole proprietor"
    LLC = "LLC"
    LLP = "LLP"
    LIMITED_PARTNERSHIP = "Limited partnership"
    CO_OWNERSHIP = "Co-ownership"
    ASSOCIATION = "Association"
    TRUSTEESHIP = "Trusteeship"
    GENERAL_PARTNERSHIP = "General partnership"
    JOINT_VENTURE = "Joint venture"
    NON_PROFIT = "Non-Profit"


class FilingForm(str, Enum):
    r"""The form used by the company for federal tax filing. One of:
    - 941 (Quarterly federal tax return)
    - 944 (Annual federal tax return)
    """

    NINE_HUNDRED_AND_FORTY_ONE = "941"
    NINE_HUNDRED_AND_FORTY_FOUR = "944"


class PutV1CompaniesCompanyIDFederalTaxDetailsRequestBodyTypedDict(TypedDict):
    r"""Attributes related to federal tax details that can be updated via this endpoint include:"""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""
    legal_name: NotRequired[str]
    r"""The legal name of the company"""
    ein: NotRequired[str]
    r"""The EIN of of the company"""
    tax_payer_type: NotRequired[TaxPayerType]
    r"""What type of tax entity the company is"""
    filing_form: NotRequired[FilingForm]
    r"""The form used by the company for federal tax filing. One of:
    - 941 (Quarterly federal tax return)
    - 944 (Annual federal tax return)
    """
    taxable_as_scorp: NotRequired[bool]
    r"""Whether this company should be taxed as an S-Corporation"""


class PutV1CompaniesCompanyIDFederalTaxDetailsRequestBody(BaseModel):
    r"""Attributes related to federal tax details that can be updated via this endpoint include:"""

    version: str
    r"""The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field."""

    legal_name: Optional[str] = None
    r"""The legal name of the company"""

    ein: Optional[str] = None
    r"""The EIN of of the company"""

    tax_payer_type: Optional[TaxPayerType] = None
    r"""What type of tax entity the company is"""

    filing_form: Optional[FilingForm] = None
    r"""The form used by the company for federal tax filing. One of:
    - 941 (Quarterly federal tax return)
    - 944 (Annual federal tax return)
    """

    taxable_as_scorp: Optional[bool] = None
    r"""Whether this company should be taxed as an S-Corporation"""


class PutV1CompaniesCompanyIDFederalTaxDetailsRequestTypedDict(TypedDict):
    company_id: str
    r"""The UUID of the company"""
    request_body: PutV1CompaniesCompanyIDFederalTaxDetailsRequestBodyTypedDict
    r"""Attributes related to federal tax details that can be updated via this endpoint include:"""
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PutV1CompaniesCompanyIDFederalTaxDetailsRequest(BaseModel):
    company_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PutV1CompaniesCompanyIDFederalTaxDetailsRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
    r"""Attributes related to federal tax details that can be updated via this endpoint include:"""

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = None
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
