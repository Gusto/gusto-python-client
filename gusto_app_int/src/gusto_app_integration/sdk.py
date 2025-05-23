"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from .httpclient import AsyncHttpClient, ClientOwner, HttpClient, close_clients
from .sdkconfiguration import SDKConfiguration
from .utils.logger import Logger, get_default_logger
from .utils.retries import RetryConfig
from gusto_app_integration import models, utils
from gusto_app_integration._hooks import SDKHooks
from gusto_app_integration.companies import Companies
from gusto_app_integration.companybenefits import CompanyBenefits
from gusto_app_integration.companylocations import CompanyLocations
from gusto_app_integration.contractorpaymentgroups import ContractorPaymentGroups
from gusto_app_integration.contractorpayments import ContractorPayments
from gusto_app_integration.contractors import Contractors
from gusto_app_integration.departments import Departments
from gusto_app_integration.earningtypes import EarningTypes
from gusto_app_integration.employeeaddresses import EmployeeAddresses
from gusto_app_integration.employeebenefits import EmployeeBenefits
from gusto_app_integration.employeeemployments import EmployeeEmployments
from gusto_app_integration.employees import Employees
from gusto_app_integration.events import Events
from gusto_app_integration.garnishments import Garnishments
from gusto_app_integration.introspection import Introspection
from gusto_app_integration.jobs import Jobs
from gusto_app_integration.jobsandcompensations import JobsAndCompensations
from gusto_app_integration.locations import Locations
from gusto_app_integration.payrolls import Payrolls
from gusto_app_integration.payschedules import PaySchedules
from gusto_app_integration.time_tracking import TimeTracking
from gusto_app_integration.timeoffpolicies import TimeOffPolicies
from gusto_app_integration.types import OptionalNullable, UNSET
from gusto_app_integration.webhooks import Webhooks
import httpx
from typing import Any, Callable, Dict, Optional, Union, cast
import weakref


class GustoAppIntegration(BaseSDK):
    r"""Gusto API: Welcome to Gusto's Embedded Payroll API documentation!"""

    introspection: Introspection
    companies: Companies
    locations: Locations
    company_locations: CompanyLocations
    pay_schedules: PaySchedules
    employees: Employees
    departments: Departments
    employee_employments: EmployeeEmployments
    employee_addresses: EmployeeAddresses
    jobs: Jobs
    jobs_and_compensations: JobsAndCompensations
    earning_types: EarningTypes
    contractors: Contractors
    webhooks: Webhooks
    payrolls: Payrolls
    time_off_policies: TimeOffPolicies
    contractor_payments: ContractorPayments
    contractor_payment_groups: ContractorPaymentGroups
    company_benefits: CompanyBenefits
    employee_benefits: EmployeeBenefits
    garnishments: Garnishments
    events: Events
    time_tracking: TimeTracking

    def __init__(
        self,
        company_access_auth: Optional[
            Union[Optional[str], Callable[[], Optional[str]]]
        ] = None,
        server: Optional[str] = None,
        server_url: Optional[str] = None,
        url_params: Optional[Dict[str, str]] = None,
        client: Optional[HttpClient] = None,
        async_client: Optional[AsyncHttpClient] = None,
        retry_config: OptionalNullable[RetryConfig] = UNSET,
        timeout_ms: Optional[int] = None,
        debug_logger: Optional[Logger] = None,
    ) -> None:
        r"""Instantiates the SDK configuring it with the provided parameters.

        :param company_access_auth: The company_access_auth required for authentication
        :param server: The server by name to use for all methods
        :param server_url: The server URL to use for all methods
        :param url_params: Parameters to optionally template the server URL with
        :param client: The HTTP client to use for all synchronous methods
        :param async_client: The Async HTTP client to use for all asynchronous methods
        :param retry_config: The retry configuration to use for all supported methods
        :param timeout_ms: Optional request timeout applied to each operation in milliseconds
        """
        client_supplied = True
        if client is None:
            client = httpx.Client()
            client_supplied = False

        assert issubclass(
            type(client), HttpClient
        ), "The provided client must implement the HttpClient protocol."

        async_client_supplied = True
        if async_client is None:
            async_client = httpx.AsyncClient()
            async_client_supplied = False

        if debug_logger is None:
            debug_logger = get_default_logger()

        assert issubclass(
            type(async_client), AsyncHttpClient
        ), "The provided async_client must implement the AsyncHttpClient protocol."

        security: Any = None
        if callable(company_access_auth):
            # pylint: disable=unnecessary-lambda-assignment
            security = lambda: models.Security(
                company_access_auth=company_access_auth()
            )
        else:
            security = models.Security(company_access_auth=company_access_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        BaseSDK.__init__(
            self,
            SDKConfiguration(
                client=client,
                client_supplied=client_supplied,
                async_client=async_client,
                async_client_supplied=async_client_supplied,
                security=security,
                server_url=server_url,
                server=server,
                retry_config=retry_config,
                timeout_ms=timeout_ms,
                debug_logger=debug_logger,
            ),
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(
            current_server_url, client
        )
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__["_hooks"] = hooks

        weakref.finalize(
            self,
            close_clients,
            cast(ClientOwner, self.sdk_configuration),
            self.sdk_configuration.client,
            self.sdk_configuration.client_supplied,
            self.sdk_configuration.async_client,
            self.sdk_configuration.async_client_supplied,
        )

        self._init_sdks()

    def _init_sdks(self):
        self.introspection = Introspection(self.sdk_configuration)
        self.companies = Companies(self.sdk_configuration)
        self.locations = Locations(self.sdk_configuration)
        self.company_locations = CompanyLocations(self.sdk_configuration)
        self.pay_schedules = PaySchedules(self.sdk_configuration)
        self.employees = Employees(self.sdk_configuration)
        self.departments = Departments(self.sdk_configuration)
        self.employee_employments = EmployeeEmployments(self.sdk_configuration)
        self.employee_addresses = EmployeeAddresses(self.sdk_configuration)
        self.jobs = Jobs(self.sdk_configuration)
        self.jobs_and_compensations = JobsAndCompensations(self.sdk_configuration)
        self.earning_types = EarningTypes(self.sdk_configuration)
        self.contractors = Contractors(self.sdk_configuration)
        self.webhooks = Webhooks(self.sdk_configuration)
        self.payrolls = Payrolls(self.sdk_configuration)
        self.time_off_policies = TimeOffPolicies(self.sdk_configuration)
        self.contractor_payments = ContractorPayments(self.sdk_configuration)
        self.contractor_payment_groups = ContractorPaymentGroups(self.sdk_configuration)
        self.company_benefits = CompanyBenefits(self.sdk_configuration)
        self.employee_benefits = EmployeeBenefits(self.sdk_configuration)
        self.garnishments = Garnishments(self.sdk_configuration)
        self.events = Events(self.sdk_configuration)
        self.time_tracking = TimeTracking(self.sdk_configuration)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.client is not None
            and not self.sdk_configuration.client_supplied
        ):
            self.sdk_configuration.client.close()
        self.sdk_configuration.client = None

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if (
            self.sdk_configuration.async_client is not None
            and not self.sdk_configuration.async_client_supplied
        ):
            await self.sdk_configuration.async_client.aclose()
        self.sdk_configuration.async_client = None
