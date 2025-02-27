![gusto logo](./assets/Gusto_logo.png)

# Gusto Python Client
**Payroll, HR, benefits. Simplified**

> [!NOTE]
> Exciting news! Our first Python library beta release is here.

## Authentication

Gusto Embedded supports two types of tokens that are used throughout development: company-level tokens and system-level tokens.

System access tokens allow you to carry out application level actions such as:
* Creating a partner managed company
* Viewing invoices

Company access tokens allow you to carry out company level actions, such as:
* Getting company employees
* Running payroll for a company

Each partner managed company has a single access token that cannot be used to access other companies.

See the [System Access Tokens](https://docs.gusto.com/embedded-payroll/docs/system-access-tokens) and [Company Access Tokens](https://docs.gusto.com/embedded-payroll/docs/company-access-tokens) for more details.

## Client Libraries

<!-- Start Gusto Python Client Libraries -->
| Library | Description | PyPI |
| :- |:- |:- |
| **[Gusto Embedded](https://github.com/Gusto/gusto-python-client/tree/main/gusto_embedded)** | Client library for the Gusto Embedded API | [![PyPI](https://img.shields.io/pypi/v/gusto-embedded.svg?color=%230A8080)](https://pypi.org/project/gusto_embedded) |
| **[Gusto App Integration](https://github.com/Gusto/gusto-python-client/tree/main/gusto_app_int)** | Client library for the Gusto App Integration API | [![PyPI](https://img.shields.io/pypi/v/gusto_app_integration.svg?color=%230A8080)](https://pypi.org/project/gusto_app_integration/) |
<!-- End Gusto Python Client Libraries -->

<!-- Start Gusto Support Notes -->
## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance.
You can raise any issues by filing a new [Github issue](https://github.com/Gusto/gusto-python-client/issues/new) on this repository.

<!-- End Gusto Support Notes -->
