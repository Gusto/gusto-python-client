"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto_app_integration import models, utils
from gusto_app_integration._hooks import HookContext
from gusto_app_integration.types import OptionalNullable, UNSET
from typing import Any, Mapping, Optional


class EarningTypes(BaseSDK):
    def create(
        self,
        *,
        company_id: str,
        name: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EarningType:
        r"""Create a custom earning type

        Create a custom earning type.

        If an inactive earning type exists with the same name, this will reactivate it instead of creating a new one.

        scope: `payrolls:write`

        :param company_id: The UUID of the company
        :param name: The name of the custom earning type.
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

        request = models.PostV1CompaniesCompanyIDEarningTypesRequest(
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostV1CompaniesCompanyIDEarningTypesRequestBody(
                name=name,
            ),
        )

        req = self._build_request(
            method="POST",
            path="/v1/companies/{company_id}/earning_types",
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
                models.PostV1CompaniesCompanyIDEarningTypesRequestBody,
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
                operation_id="post-v1-companies-company_id-earning_types",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.EarningType)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectData
            )
            raise models.UnprocessableEntityErrorObject(data=response_data)
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

    async def create_async(
        self,
        *,
        company_id: str,
        name: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EarningType:
        r"""Create a custom earning type

        Create a custom earning type.

        If an inactive earning type exists with the same name, this will reactivate it instead of creating a new one.

        scope: `payrolls:write`

        :param company_id: The UUID of the company
        :param name: The name of the custom earning type.
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

        request = models.PostV1CompaniesCompanyIDEarningTypesRequest(
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PostV1CompaniesCompanyIDEarningTypesRequestBody(
                name=name,
            ),
        )

        req = self._build_request_async(
            method="POST",
            path="/v1/companies/{company_id}/earning_types",
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
                models.PostV1CompaniesCompanyIDEarningTypesRequestBody,
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
                operation_id="post-v1-companies-company_id-earning_types",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "201", "application/json"):
            return utils.unmarshal_json(http_res.text, models.EarningType)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectData
            )
            raise models.UnprocessableEntityErrorObject(data=response_data)
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

    def get(
        self,
        *,
        company_id: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EarningTypeList:
        r"""Get all earning types for a company

        A payroll item in Gusto is associated to an earning type to name the type of earning described by the payroll item.

        #### Default Earning Type
        Certain earning types are special because they have tax considerations. Those earning types are mostly the same for every company depending on its legal structure (LLC, Corporation, etc.)

        #### Custom Earning Type
        Custom earning types are all the other earning types added specifically for a company.

        scope: `payrolls:read`

        :param company_id: The UUID of the company
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

        request = models.GetV1CompaniesCompanyIDEarningTypesRequest(
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/companies/{company_id}/earning_types",
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
                operation_id="get-v1-companies-company_id-earning_types",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.EarningTypeList)
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
        company_id: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EarningTypeList:
        r"""Get all earning types for a company

        A payroll item in Gusto is associated to an earning type to name the type of earning described by the payroll item.

        #### Default Earning Type
        Certain earning types are special because they have tax considerations. Those earning types are mostly the same for every company depending on its legal structure (LLC, Corporation, etc.)

        #### Custom Earning Type
        Custom earning types are all the other earning types added specifically for a company.

        scope: `payrolls:read`

        :param company_id: The UUID of the company
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

        request = models.GetV1CompaniesCompanyIDEarningTypesRequest(
            company_id=company_id,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/companies/{company_id}/earning_types",
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
                operation_id="get-v1-companies-company_id-earning_types",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.EarningTypeList)
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

    def update(
        self,
        *,
        company_id: str,
        earning_type_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EarningType:
        r"""Update an earning type

        Update an earning type.

        scope: `payrolls:write`

        :param company_id: The UUID of the company
        :param earning_type_uuid: The UUID of the earning type
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param name: The name of the custom earning type.
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

        request = models.PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequest(
            company_id=company_id,
            earning_type_uuid=earning_type_uuid,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBody(
                name=name,
            ),
        )

        req = self._build_request(
            method="PUT",
            path="/v1/companies/{company_id}/earning_types/{earning_type_uuid}",
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
                models.PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBody,
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
                operation_id="put-v1-companies-company_id-earning_types-earning_type_uuid",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.EarningType)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectData
            )
            raise models.UnprocessableEntityErrorObject(data=response_data)
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

    async def update_async(
        self,
        *,
        company_id: str,
        earning_type_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        name: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.EarningType:
        r"""Update an earning type

        Update an earning type.

        scope: `payrolls:write`

        :param company_id: The UUID of the company
        :param earning_type_uuid: The UUID of the earning type
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param name: The name of the custom earning type.
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

        request = models.PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequest(
            company_id=company_id,
            earning_type_uuid=earning_type_uuid,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBody(
                name=name,
            ),
        )

        req = self._build_request_async(
            method="PUT",
            path="/v1/companies/{company_id}/earning_types/{earning_type_uuid}",
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
                models.PutV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequestBody,
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
                operation_id="put-v1-companies-company_id-earning_types-earning_type_uuid",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        response_data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.EarningType)
        if utils.match_response(http_res, "422", "application/json"):
            response_data = utils.unmarshal_json(
                http_res.text, models.UnprocessableEntityErrorObjectData
            )
            raise models.UnprocessableEntityErrorObject(data=response_data)
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

    def deactivate(
        self,
        *,
        company_id: str,
        earning_type_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Deactivate an earning type

        Deactivate an earning type.

        scope: `payrolls:write`

        :param company_id: The UUID of the company
        :param earning_type_uuid: The UUID of the earning type
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

        request = models.DeleteV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequest(
            company_id=company_id,
            earning_type_uuid=earning_type_uuid,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="DELETE",
            path="/v1/companies/{company_id}/earning_types/{earning_type_uuid}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="*/*",
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
                operation_id="delete-v1-companies-company_id-earning_types-earning_type_uuid",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "204", "*"):
            return
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

    async def deactivate_async(
        self,
        *,
        company_id: str,
        earning_type_uuid: str,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_04_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Deactivate an earning type

        Deactivate an earning type.

        scope: `payrolls:write`

        :param company_id: The UUID of the company
        :param earning_type_uuid: The UUID of the earning type
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

        request = models.DeleteV1CompaniesCompanyIDEarningTypesEarningTypeUUIDRequest(
            company_id=company_id,
            earning_type_uuid=earning_type_uuid,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="DELETE",
            path="/v1/companies/{company_id}/earning_types/{earning_type_uuid}",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="*/*",
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
                operation_id="delete-v1-companies-company_id-earning_types-earning_type_uuid",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "204", "*"):
            return
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
