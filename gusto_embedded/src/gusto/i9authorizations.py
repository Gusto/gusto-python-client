"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto import models, utils
from gusto._hooks import HookContext
from gusto.types import OptionalNullable, UNSET
from gusto.utils import get_security_from_env
from typing import Any, List, Mapping, Optional


class I9Authorizations(BaseSDK):
    def put_v1_employees_employee_id_i9_authorization(
        self,
        *,
        employee_id: str,
        authorization_status: models.PutV1EmployeesEmployeeIDI9AuthorizationAuthorizationStatus,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        document_type: Optional[
            models.PutV1EmployeesEmployeeIDI9AuthorizationDocumentType
        ] = None,
        document_number: Optional[str] = None,
        country: Optional[str] = None,
        expiration_date: Optional[str] = None,
        version: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.I9Authorization:
        r"""Create or update an employee's I-9 authorization

        An employee's I-9 authorization stores information about an employee's authorization status, as well as signatures and other information required to complete the Form I-9 for employment eligibility verification.

        If the version is supplied and the employee I-9 authorization exists, this endpoint acts as an update. Otherwise, it will create an employee I-9 authorization.

        Validations on this endpoint are conditional:

        * `document_type` may be required, depending on `authorization_status`.
        * Valid formats for `document_number` vary, depending on `document_type`.
        * `country` is only allowed with `document_type: 'foreign_passport'`.
        * `expiration_date` is only allowed with `authorization_status: 'alien'`.

        > ℹ️ Unneeded information is automatically removed during updates.
        >
        > If an update causes some formerly-required fields to be unneeded, the now-unneeded data will be removed automatically.
        >
        > **Example:** Updating `authorization_status` from `alien` to `citizen` will cause any data in `document_type`, `document_number`, `country`, and `expiration_date` to be removed, since these fields are unused for `authorization_status:'citizen'`.

        Detailed instructions for completing Form I-9 can be found at https://www.uscis.gov/sites/default/files/document/forms/i-9instr.pdf

        scope: `i9_authorizations:write`


        :param employee_id: The UUID of the employee
        :param authorization_status: The employee's authorization status    * `citizen`: A citizen is someone who was born in the United States or is a naturalized citizen living in the United States.   * `noncitizen`: A noncitizen national is someone born in American Samoa, certain former citizens of the former Trust Territory of the Pacific Islands, and certain children of noncitizen nationals born abroad.   * `permanent_resident`: A lawful permanent resident is someone who is not a US citizen and who resides under legally recognized and lawfully recorded permanent residence as an immigrant.   * `alien`: Also referred to as a \"noncitizen authorized to work\". This includes anyone who is authorized to work in the United States but is not a US citizen, US national or lawful permanent resident.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param document_type: The type of document an employee holds, based on their authorization status.    * This is unused for authorization status `citizen` or `noncitizen`.   * If the authorization status is `permanent_resident`, this must be `uscis_alien_registration_number`.   * If the authorization status is `alien`, this is required and may be any of the valid values.
        :param document_number: The document number. Formatting depends on the employee's document type.    * For `document_type:'uscis_alien_registration_number'`, this must be a USCIS Number/A-Number, which is 7 to 9 digits.   * For `document_type:'form_i94'`, this must be a Form I-94 Admission Number, which is 11 digits.   * For `document_type:'foreign_passport'`, this must be the passport number.  This is required when the document type is present.
        :param country: The document's country of issuance.  This is required when the document type is `foreign_passport`.
        :param expiration_date: The document's expiration date.  This may only be used when the authorization status is `alien`.
        :param version: The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field. If supplied, this endpoint will update the existing I-9 authorization if it exists.
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

        request = models.PutV1EmployeesEmployeeIDI9AuthorizationRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1EmployeesEmployeeIDI9AuthorizationRequestBody(
                authorization_status=authorization_status,
                document_type=document_type,
                document_number=document_number,
                country=country,
                expiration_date=expiration_date,
                version=version,
            ),
        )

        req = self._build_request(
            method="PUT",
            path="/v1/employees/{employee_id}/i9_authorization",
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
                models.PutV1EmployeesEmployeeIDI9AuthorizationRequestBody,
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
                operation_id="put-v1-employees-employee_id-i9_authorization",
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
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.I9Authorization)
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

    async def put_v1_employees_employee_id_i9_authorization_async(
        self,
        *,
        employee_id: str,
        authorization_status: models.PutV1EmployeesEmployeeIDI9AuthorizationAuthorizationStatus,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        document_type: Optional[
            models.PutV1EmployeesEmployeeIDI9AuthorizationDocumentType
        ] = None,
        document_number: Optional[str] = None,
        country: Optional[str] = None,
        expiration_date: Optional[str] = None,
        version: Optional[str] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.I9Authorization:
        r"""Create or update an employee's I-9 authorization

        An employee's I-9 authorization stores information about an employee's authorization status, as well as signatures and other information required to complete the Form I-9 for employment eligibility verification.

        If the version is supplied and the employee I-9 authorization exists, this endpoint acts as an update. Otherwise, it will create an employee I-9 authorization.

        Validations on this endpoint are conditional:

        * `document_type` may be required, depending on `authorization_status`.
        * Valid formats for `document_number` vary, depending on `document_type`.
        * `country` is only allowed with `document_type: 'foreign_passport'`.
        * `expiration_date` is only allowed with `authorization_status: 'alien'`.

        > ℹ️ Unneeded information is automatically removed during updates.
        >
        > If an update causes some formerly-required fields to be unneeded, the now-unneeded data will be removed automatically.
        >
        > **Example:** Updating `authorization_status` from `alien` to `citizen` will cause any data in `document_type`, `document_number`, `country`, and `expiration_date` to be removed, since these fields are unused for `authorization_status:'citizen'`.

        Detailed instructions for completing Form I-9 can be found at https://www.uscis.gov/sites/default/files/document/forms/i-9instr.pdf

        scope: `i9_authorizations:write`


        :param employee_id: The UUID of the employee
        :param authorization_status: The employee's authorization status    * `citizen`: A citizen is someone who was born in the United States or is a naturalized citizen living in the United States.   * `noncitizen`: A noncitizen national is someone born in American Samoa, certain former citizens of the former Trust Territory of the Pacific Islands, and certain children of noncitizen nationals born abroad.   * `permanent_resident`: A lawful permanent resident is someone who is not a US citizen and who resides under legally recognized and lawfully recorded permanent residence as an immigrant.   * `alien`: Also referred to as a \"noncitizen authorized to work\". This includes anyone who is authorized to work in the United States but is not a US citizen, US national or lawful permanent resident.
        :param x_gusto_api_version: Determines the date-based API version associated with your API call. If none is provided, your application's [minimum API version](https://docs.gusto.com/embedded-payroll/docs/api-versioning#minimum-api-version) is used.
        :param document_type: The type of document an employee holds, based on their authorization status.    * This is unused for authorization status `citizen` or `noncitizen`.   * If the authorization status is `permanent_resident`, this must be `uscis_alien_registration_number`.   * If the authorization status is `alien`, this is required and may be any of the valid values.
        :param document_number: The document number. Formatting depends on the employee's document type.    * For `document_type:'uscis_alien_registration_number'`, this must be a USCIS Number/A-Number, which is 7 to 9 digits.   * For `document_type:'form_i94'`, this must be a Form I-94 Admission Number, which is 11 digits.   * For `document_type:'foreign_passport'`, this must be the passport number.  This is required when the document type is present.
        :param country: The document's country of issuance.  This is required when the document type is `foreign_passport`.
        :param expiration_date: The document's expiration date.  This may only be used when the authorization status is `alien`.
        :param version: The current version of the object. See the [versioning guide](https://docs.gusto.com/embedded-payroll/docs/versioning#object-layer) for information on how to use this field. If supplied, this endpoint will update the existing I-9 authorization if it exists.
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

        request = models.PutV1EmployeesEmployeeIDI9AuthorizationRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
            request_body=models.PutV1EmployeesEmployeeIDI9AuthorizationRequestBody(
                authorization_status=authorization_status,
                document_type=document_type,
                document_number=document_number,
                country=country,
                expiration_date=expiration_date,
                version=version,
            ),
        )

        req = self._build_request_async(
            method="PUT",
            path="/v1/employees/{employee_id}/i9_authorization",
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
                models.PutV1EmployeesEmployeeIDI9AuthorizationRequestBody,
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
                operation_id="put-v1-employees-employee_id-i9_authorization",
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
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, models.I9Authorization)
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

    def get_v1_employees_employee_id_i9_authorization_documents(
        self,
        *,
        employee_id: str,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.I9AuthorizationDocument]:
        r"""Get an employee's I-9 verification documents

        An employee's I-9 verification documents are the documents an employee has provided the employer to verify their identity and authorization to work in the United States.

        scope: `i9_authorizations:read`

        :param employee_id: The UUID of the employee
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

        request = models.GetV1EmployeesEmployeeIDI9AuthorizationDocumentsRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/employees/{employee_id}/i9_authorization/documents",
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
                operation_id="get-v1-employees-employee_id-i9_authorization-documents",
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
            return utils.unmarshal_json(
                http_res.text, List[models.I9AuthorizationDocument]
            )
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

    async def get_v1_employees_employee_id_i9_authorization_documents_async(
        self,
        *,
        employee_id: str,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.I9AuthorizationDocument]:
        r"""Get an employee's I-9 verification documents

        An employee's I-9 verification documents are the documents an employee has provided the employer to verify their identity and authorization to work in the United States.

        scope: `i9_authorizations:read`

        :param employee_id: The UUID of the employee
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

        request = models.GetV1EmployeesEmployeeIDI9AuthorizationDocumentsRequest(
            employee_id=employee_id,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/employees/{employee_id}/i9_authorization/documents",
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
                operation_id="get-v1-employees-employee_id-i9_authorization-documents",
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
            return utils.unmarshal_json(
                http_res.text, List[models.I9AuthorizationDocument]
            )
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

    def delete_v1_employees_employee_id_i9_authorization_documents_document_id(
        self,
        *,
        employee_id: str,
        document_id: str,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Delete an employee's I-9 verification document

        An employee's I-9 verification documents are the documents an employee has provided the employer to verify their identity and authorization to work in the United States. This endpoint deletes a specific verification document.

        scope: `i9_authorizations:manage`

        :param employee_id: The UUID of the employee
        :param document_id: The UUID of the document
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

        request = (
            models.DeleteV1EmployeesEmployeeIDI9AuthorizationDocumentsDocumentIDRequest(
                employee_id=employee_id,
                document_id=document_id,
                x_gusto_api_version=x_gusto_api_version,
            )
        )

        req = self._build_request(
            method="DELETE",
            path="/v1/employees/{employee_id}/i9_authorization/documents/{document_id}",
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
                operation_id="delete-v1-employees-employee_id-i9_authorization-documents-document_id",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
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

    async def delete_v1_employees_employee_id_i9_authorization_documents_document_id_async(
        self,
        *,
        employee_id: str,
        document_id: str,
        x_gusto_api_version: Optional[models.VersionHeader] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ):
        r"""Delete an employee's I-9 verification document

        An employee's I-9 verification documents are the documents an employee has provided the employer to verify their identity and authorization to work in the United States. This endpoint deletes a specific verification document.

        scope: `i9_authorizations:manage`

        :param employee_id: The UUID of the employee
        :param document_id: The UUID of the document
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

        request = (
            models.DeleteV1EmployeesEmployeeIDI9AuthorizationDocumentsDocumentIDRequest(
                employee_id=employee_id,
                document_id=document_id,
                x_gusto_api_version=x_gusto_api_version,
            )
        )

        req = self._build_request_async(
            method="DELETE",
            path="/v1/employees/{employee_id}/i9_authorization/documents/{document_id}",
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
                operation_id="delete-v1-employees-employee_id-i9_authorization-documents-document_id",
                oauth2_scopes=[],
                security_source=get_security_from_env(
                    self.sdk_configuration.security, models.Security
                ),
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
