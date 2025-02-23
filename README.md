<div align="center">
    <picture>
        <source srcset="logo here" media="(prefers-color-scheme: dark)">
        <img src="logo here">
    </picture>
    <h1>Gusto Python Client</h1>
        <p><strong>Payroll, HR, benefits. Simplified</strong></p>
        <p>Secondary Description.</p>
    <a href="https://docs.gusto.com/embedded-payroll/docs/introduction"><img src="https://img.shields.io/static/v1?label=Docs&message=API Ref&color=4c2cec&style=for-the-badge" /></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" /></a>
</div>

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

Each partner managed company has a single access token that cannot be used to access other companies. If you're on a version older than 2023-05-01, see [Upgrading to Strict Access](https://docs.gusto.com/embedded-payroll/docs/strict-access) for more information on upgrading to strict access.

See the [System Access Tokens](https://docs.gusto.com/embedded-payroll/docs/system-access-tokens) and [Company Access Tokens](https://docs.gusto.com/embedded-payroll/docs/company-access-tokens) for more details.

## Client Libraries

<!-- Start Gusto Python Client Libraries -->
| Library | Description | PyPI |
| :- |:- |:- |
| **[Gusto Embedded](https://github.com/Gusto/gusto-python-client/tree/main/gusto_embedded)** | Description for this library. | [![PyPI](https://img.shields.io/pypi/v/gusto-embedded.svg)](https://pypi.org/project/gusto_embedded) |

<!-- End Gusto Python Client Libraries -->

<!-- Start Gusto Support Notes -->
## Support

If you encounter any challenges while utilizing our SDKs, please don't hesitate to reach out for assistance. 
You can raise any issues by filing a new [Github issue](https://github.com/Gusto/gusto-python-client/issues/new) on this repository.

<!-- End Gusto Support Notes -->
