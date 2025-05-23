"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from gusto_embedded import models, utils
from gusto_embedded._hooks import HookContext
from gusto_embedded.types import OptionalNullable, UNSET
from gusto_embedded.utils import get_security_from_env
from typing import List, Mapping, Optional


class AchTransactions(BaseSDK):
    def get_all(
        self,
        *,
        company_uuid: str,
        contractor_payment_uuid: Optional[str] = None,
        payroll_uuid: Optional[str] = None,
        transaction_type: Optional[str] = None,
        payment_direction: Optional[str] = None,
        page: Optional[int] = None,
        per: Optional[int] = None,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.AchTransaction]:
        r"""Get all ACH transactions for a company

        Fetches all ACH transactions for a company.

        scope: `ach_transactions:read`

        :param company_uuid: The UUID of the company
        :param contractor_payment_uuid: The UUID of the contractor payment
        :param payroll_uuid: The UUID of the payroll
        :param transaction_type: Used to filter the ACH transactions to only include those with a specific transaction type, such as \"Credit employee pay\".
        :param payment_direction: Used to filter the ACH transactions to only include those with a specific payment direction, either \"credit\" or \"debit\".
        :param page: The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.
        :param per: Number of objects per page. For majority of endpoints will default to 25
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

        request = models.GetAchTransactionsRequest(
            company_uuid=company_uuid,
            contractor_payment_uuid=contractor_payment_uuid,
            payroll_uuid=payroll_uuid,
            transaction_type=transaction_type,
            payment_direction=payment_direction,
            page=page,
            per=per,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request(
            method="GET",
            path="/v1/companies/{company_uuid}/ach_transactions",
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
                operation_id="get-ach-transactions",
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
            return utils.unmarshal_json(http_res.text, List[models.AchTransaction])
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
        contractor_payment_uuid: Optional[str] = None,
        payroll_uuid: Optional[str] = None,
        transaction_type: Optional[str] = None,
        payment_direction: Optional[str] = None,
        page: Optional[int] = None,
        per: Optional[int] = None,
        x_gusto_api_version: Optional[
            models.VersionHeader
        ] = models.VersionHeader.TWO_THOUSAND_AND_TWENTY_FOUR_MINUS_04_MINUS_01,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> List[models.AchTransaction]:
        r"""Get all ACH transactions for a company

        Fetches all ACH transactions for a company.

        scope: `ach_transactions:read`

        :param company_uuid: The UUID of the company
        :param contractor_payment_uuid: The UUID of the contractor payment
        :param payroll_uuid: The UUID of the payroll
        :param transaction_type: Used to filter the ACH transactions to only include those with a specific transaction type, such as \"Credit employee pay\".
        :param payment_direction: Used to filter the ACH transactions to only include those with a specific payment direction, either \"credit\" or \"debit\".
        :param page: The page that is requested. When unspecified, will load all objects unless endpoint forces pagination.
        :param per: Number of objects per page. For majority of endpoints will default to 25
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

        request = models.GetAchTransactionsRequest(
            company_uuid=company_uuid,
            contractor_payment_uuid=contractor_payment_uuid,
            payroll_uuid=payroll_uuid,
            transaction_type=transaction_type,
            payment_direction=payment_direction,
            page=page,
            per=per,
            x_gusto_api_version=x_gusto_api_version,
        )

        req = self._build_request_async(
            method="GET",
            path="/v1/companies/{company_uuid}/ach_transactions",
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
                operation_id="get-ach-transactions",
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
            return utils.unmarshal_json(http_res.text, List[models.AchTransaction])
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
