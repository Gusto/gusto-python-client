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


class PostCompaniesCompanyUUIDHolidayPayPolicyNewYearsDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyNewYearsDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyMlkDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyMlkDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyPresidentsDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyPresidentsDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyMemorialDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyMemorialDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyJuneteenthTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyJuneteenth(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyIndependenceDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyIndependenceDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyLaborDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyLaborDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyColumbusDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyColumbusDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyVeteransDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyVeteransDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyThanksgivingTypedDict(TypedDict):
    selected: NotRequired[bool]


class PostCompaniesCompanyUUIDHolidayPayPolicyThanksgiving(BaseModel):
    selected: Optional[bool] = None


class ChristmasDayTypedDict(TypedDict):
    selected: NotRequired[bool]


class ChristmasDay(BaseModel):
    selected: Optional[bool] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyFederalHolidaysTypedDict(TypedDict):
    r"""An object containing federal holiday objects, each containing a boolean selected property."""

    new_years_day: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyNewYearsDayTypedDict
    ]
    mlk_day: NotRequired[PostCompaniesCompanyUUIDHolidayPayPolicyMlkDayTypedDict]
    presidents_day: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyPresidentsDayTypedDict
    ]
    memorial_day: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyMemorialDayTypedDict
    ]
    juneteenth: NotRequired[PostCompaniesCompanyUUIDHolidayPayPolicyJuneteenthTypedDict]
    independence_day: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyIndependenceDayTypedDict
    ]
    labor_day: NotRequired[PostCompaniesCompanyUUIDHolidayPayPolicyLaborDayTypedDict]
    columbus_day: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyColumbusDayTypedDict
    ]
    veterans_day: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyVeteransDayTypedDict
    ]
    thanksgiving: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyThanksgivingTypedDict
    ]
    christmas_day: NotRequired[ChristmasDayTypedDict]


class PostCompaniesCompanyUUIDHolidayPayPolicyFederalHolidays(BaseModel):
    r"""An object containing federal holiday objects, each containing a boolean selected property."""

    new_years_day: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyNewYearsDay] = None

    mlk_day: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyMlkDay] = None

    presidents_day: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyPresidentsDay] = (
        None
    )

    memorial_day: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyMemorialDay] = None

    juneteenth: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyJuneteenth] = None

    independence_day: Optional[
        PostCompaniesCompanyUUIDHolidayPayPolicyIndependenceDay
    ] = None

    labor_day: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyLaborDay] = None

    columbus_day: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyColumbusDay] = None

    veterans_day: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyVeteransDay] = None

    thanksgiving: Optional[PostCompaniesCompanyUUIDHolidayPayPolicyThanksgiving] = None

    christmas_day: Optional[ChristmasDay] = None


class PostCompaniesCompanyUUIDHolidayPayPolicyRequestBodyTypedDict(TypedDict):
    federal_holidays: NotRequired[
        PostCompaniesCompanyUUIDHolidayPayPolicyFederalHolidaysTypedDict
    ]
    r"""An object containing federal holiday objects, each containing a boolean selected property."""


class PostCompaniesCompanyUUIDHolidayPayPolicyRequestBody(BaseModel):
    federal_holidays: Optional[
        PostCompaniesCompanyUUIDHolidayPayPolicyFederalHolidays
    ] = None
    r"""An object containing federal holiday objects, each containing a boolean selected property."""


class PostCompaniesCompanyUUIDHolidayPayPolicyRequestTypedDict(TypedDict):
    company_uuid: str
    r"""The UUID of the company"""
    request_body: PostCompaniesCompanyUUIDHolidayPayPolicyRequestBodyTypedDict
    x_gusto_api_version: NotRequired[VersionHeader]
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""


class PostCompaniesCompanyUUIDHolidayPayPolicyRequest(BaseModel):
    company_uuid: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The UUID of the company"""

    request_body: Annotated[
        PostCompaniesCompanyUUIDHolidayPayPolicyRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]

    x_gusto_api_version: Annotated[
        Optional[VersionHeader],
        pydantic.Field(alias="X-Gusto-API-Version"),
        FieldMetadata(header=HeaderMetadata(style="simple", explode=False)),
    ] = VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01
    r"""Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used."""
