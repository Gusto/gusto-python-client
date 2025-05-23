"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto_embedded import models, utils
from gusto_embedded._hooks import HookContext
from gusto_embedded.types import OptionalNullable, UNSET
from gusto_embedded.utils import get_security_from_env
from typing import Any, List, Mapping, Optional, Union


class TaxRequirements(BaseSDK):
    def get(
        self,
        *,
        company_uuid: str,
        state: str,
        scheduling: Optional[bool] = None,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaxRequirementsState:
        r"""Get State Tax Requirements

        Get all tax requirements for a given state.

        ### Metadata Examples

        ```json select
        {
        \"type\": \"select\",
        \"options\": [
        { \"label\": \"Semiweekly\",  value: \"Semi-weekly\" },
        { \"label\": \"Monthly\",  value: \"Monthly\" },
        { \"label\": \"Quarterly\",  value: \"Quarterly\" },
        ]
        }
        ```
        ```json radio
        {
        \"type\": \"radio\",
        \"options\": [
        { \"label\": \"No, we cannot reimburse\",  value: false, short_label: \"Not Reimbursable\" },
        { \"label\": \"Yes, we can reimburse\",  value: true, short_label: \"Reimbursable\" },
        ]
        }
        ```
        ```json account_number
        {
        \"type\": \"account_number\",
        \"mask\": \"######-##',
        \"prefix\": null
        }
        ```
        ```json tax_rate
        {
        \"type\": \"tax_rate\",
        \"validation\": {
        \"type\": \"min_max\",
        \"min\": \"0.0004\",
        \"max\": \"0.081\"
        }
        }
        ```

        scope: `company_tax_requirements:read`


        :param company_uuid: The UUID of the company
        :param state: 2-letter US state abbreviation
        :param scheduling: When true, return \"new\" requirement sets with valid `effective_from` dates that are available to save new effective dated values.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetV1CompaniesCompanyUUIDTaxRequirementsStateRequest(
            company_uuid=company_uuid,
            state=state,
            scheduling=scheduling,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/companies/{company_uuid}/tax_requirements/{state}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-v1-companies-company_uuid-tax_requirements-state",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaxRequirementsState)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_async(
        self,
        *,
        company_uuid: str,
        state: str,
        scheduling: Optional[bool] = None,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.TaxRequirementsState:
        r"""Get State Tax Requirements

        Get all tax requirements for a given state.

        ### Metadata Examples

        ```json select
        {
        \"type\": \"select\",
        \"options\": [
        { \"label\": \"Semiweekly\",  value: \"Semi-weekly\" },
        { \"label\": \"Monthly\",  value: \"Monthly\" },
        { \"label\": \"Quarterly\",  value: \"Quarterly\" },
        ]
        }
        ```
        ```json radio
        {
        \"type\": \"radio\",
        \"options\": [
        { \"label\": \"No, we cannot reimburse\",  value: false, short_label: \"Not Reimbursable\" },
        { \"label\": \"Yes, we can reimburse\",  value: true, short_label: \"Reimbursable\" },
        ]
        }
        ```
        ```json account_number
        {
        \"type\": \"account_number\",
        \"mask\": \"######-##',
        \"prefix\": null
        }
        ```
        ```json tax_rate
        {
        \"type\": \"tax_rate\",
        \"validation\": {
        \"type\": \"min_max\",
        \"min\": \"0.0004\",
        \"max\": \"0.081\"
        }
        }
        ```

        scope: `company_tax_requirements:read`


        :param company_uuid: The UUID of the company
        :param state: 2-letter US state abbreviation
        :param scheduling: When true, return \"new\" requirement sets with valid `effective_from` dates that are available to save new effective dated values.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetV1CompaniesCompanyUUIDTaxRequirementsStateRequest(
            company_uuid=company_uuid,
            state=state,
            scheduling=scheduling,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/companies/{company_uuid}/tax_requirements/{state}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-v1-companies-company_uuid-tax_requirements-state",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.TaxRequirementsState)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def update_state(
        self,
        *,
        company_uuid: str,
        state: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        requirement_sets: Optional[
            Union[List[models.RequirementSets], List[models.RequirementSetsTypedDict]]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Update State Tax Requirements

        Update State Tax Requirements

        scope: `company_tax_requirements:write`

        :param company_uuid: The UUID of the company
        :param state: 2-letter US state abbreviation
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param requirement_sets:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.PutV1CompaniesCompanyUUIDTaxRequirementsStateRequest(
            company_uuid=company_uuid,
            state=state,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1CompaniesCompanyUUIDTaxRequirementsStateRequestBody(
                requirement_sets=utils.get_pydantic_model(
                    requirement_sets, Optional[List[models.RequirementSets]]
                ),
            ),
        )

        req = self._build_request(
            method="PUT",
            path="/v1/companies/{company_uuid}/tax_requirements/{state}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.PutV1CompaniesCompanyUUIDTaxRequirementsStateRequestBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="put-v1-companies-company_uuid-tax_requirements-state",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectErrorData
            )
            raise models.UnprocessableEntityErrorObjectError(data=response_data)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def update_state_async(
        self,
        *,
        company_uuid: str,
        state: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        requirement_sets: Optional[
            Union[List[models.RequirementSets], List[models.RequirementSetsTypedDict]]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Update State Tax Requirements

        Update State Tax Requirements

        scope: `company_tax_requirements:write`

        :param company_uuid: The UUID of the company
        :param state: 2-letter US state abbreviation
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param requirement_sets:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.PutV1CompaniesCompanyUUIDTaxRequirementsStateRequest(
            company_uuid=company_uuid,
            state=state,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1CompaniesCompanyUUIDTaxRequirementsStateRequestBody(
                requirement_sets=utils.get_pydantic_model(
                    requirement_sets, Optional[List[models.RequirementSets]]
                ),
            ),
        )

        req = self._build_request_async(
            method="PUT",
            path="/v1/companies/{company_uuid}/tax_requirements/{state}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request.request_body,
                False,
                False,
                "json",
                models.PutV1CompaniesCompanyUUIDTaxRequirementsStateRequestBody,
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="put-v1-companies-company_uuid-tax_requirements-state",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "*"):
            return
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectErrorData
            )
            raise models.UnprocessableEntityErrorObjectError(data=response_data)
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    def get_all(
        self,
        *,
        company_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.ResponseBody]:
        r"""Get All Tax Requirement States

        Returns objects describing the states that have tax requirements for the company

        scope: `company_tax_requirements:read`

        :param company_uuid: The UUID of the company
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetV1CompaniesCompanyUUIDTaxRequirementsRequest(
            company_uuid=company_uuid,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/companies/{company_uuid}/tax_requirements",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-v1-companies-company_uuid-tax_requirements",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, List[models.ResponseBody])
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = utils.stream_to_text(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )

    async def get_all_async(
        self,
        *,
        company_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.ResponseBody]:
        r"""Get All Tax Requirement States

        Returns objects describing the states that have tax requirements for the company

        scope: `company_tax_requirements:read`

        :param company_uuid: The UUID of the company
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.GetV1CompaniesCompanyUUIDTaxRequirementsRequest(
            company_uuid=company_uuid,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/companies/{company_uuid}/tax_requirements",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                base_url=base_url or "",
                operation_id="get-v1-companies-company_uuid-tax_requirements",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, List[models.ResponseBody])
        if utils.match_response(http_res, ["404", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise models.APIError(
                "API error occurred", http_res.status_code, http_res_text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        http_res_text = await utils.stream_to_text_async(http_res)
        raise models.APIError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res_text,
            http_res,
        )
