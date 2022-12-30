# blockmate
Blockmate API OpenAPI documentation

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import blockmate
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import blockmate
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import blockmate
from pprint import pprint
from blockmate.apis import account_provider_info_api
# Defining the host is optional and defaults to https://api.blockmate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = blockmate.Configuration(
    host = "https://api.blockmate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectToken
configuration.api_key['ProjectToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectToken'] = 'Bearer'

# Enter a context with an instance of the API client
with blockmate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_provider_info_api.AccountProviderInfoApi(api_client)
    account_provider = "onchain/btc" # str | URL value from account_providers method
any_type = dict(
        wallet="bc1qjl7k0dpcsw3djmzq25qv6peavgxysq95pcduuq",
        description="some-description",
    ) # anyType | OK (optional)

    try:
        # Connect new account
        api_response = api_instance.connect_account(account_providerany_type=any_type)
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AccountProviderInfoApi->connect_account: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.blockmate.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountProviderInfoApi* | [**connect_account**](docs/apis/tags/AccountProviderInfoApi.md#connect_account) | **post** /v1/{account_provider}/connect | Connect new account
*AccountProviderInfoApi* | [**delete_account**](docs/apis/tags/AccountProviderInfoApi.md#delete_account) | **delete** /v1/{account_provider}/account/{account_id} | Delete account
*AccountProviderInfoApi* | [**get_account_hint**](docs/apis/tags/AccountProviderInfoApi.md#get_account_hint) | **get** /v1/{account_provider}/connect | Get account hint
*AddressNameAndCategoryInfoApi* | [**get_address_name_info_multi**](docs/apis/tags/AddressNameAndCategoryInfoApi.md#get_address_name_info_multi) | **post** /v1/addressname/multi | Get address name and category info for multiple addresses
*AddressNameAndCategoryInfoApi* | [**get_address_name_info_single**](docs/apis/tags/AddressNameAndCategoryInfoApi.md#get_address_name_info_single) | **get** /v1/addressname/simple | Get address name and category info for single address
*AggregatedInfoApi* | [**account_provider_hints_list**](docs/apis/tags/AggregatedInfoApi.md#account_provider_hints_list) | **get** /v1/aggregate/account_provider_hints | Get list of account providers hints
*AggregatedInfoApi* | [**account_providers_list**](docs/apis/tags/AggregatedInfoApi.md#account_providers_list) | **get** /v1/aggregate/account_providers | Get list of account providers
*AggregatedInfoApi* | [**accounts**](docs/apis/tags/AggregatedInfoApi.md#accounts) | **get** /v1/aggregate/accounts | List accounts
*AggregatedInfoApi* | [**balance**](docs/apis/tags/AggregatedInfoApi.md#balance) | **get** /v1/aggregate/balance | Get balance
*AggregatedInfoApi* | [**n_ft_metadata**](docs/apis/tags/AggregatedInfoApi.md#n_ft_metadata) | **get** /v1/aggregate/nft_metadata | Get NFT metadata
*AggregatedInfoApi* | [**transactions**](docs/apis/tags/AggregatedInfoApi.md#transactions) | **get** /v1/aggregate/transactions | Get transactions
*AnalyticsApi* | [**get_account_analytics**](docs/apis/tags/AnalyticsApi.md#get_account_analytics) | **get** /v1/analytics/{account_provider}/account/{account_id}/stats | Get analytics focused on gaming for specified account and provider
*AnalyticsApi* | [**get_project_analytics**](docs/apis/tags/AnalyticsApi.md#get_project_analytics) | **get** /v1/analytics/project/stats | Get analytics focused on gaming for whole project
*AnalyticsApi* | [**get_provider_analytics**](docs/apis/tags/AnalyticsApi.md#get_provider_analytics) | **get** /v1/analytics/{account_provider}/stats | Get analytics focused on gaming for specified provider
*AnalyticsApi* | [**get_user_analytics**](docs/apis/tags/AnalyticsApi.md#get_user_analytics) | **get** /v1/analytics/user/stats | Get analytics focused on gaming for this user
*AuthenticationApi* | [**user_api_authenticate_developer**](docs/apis/tags/AuthenticationApi.md#user_api_authenticate_developer) | **get** /v1/auth/developer | Authenticate developer
*AuthenticationApi* | [**user_api_authenticate_project**](docs/apis/tags/AuthenticationApi.md#user_api_authenticate_project) | **get** /v1/auth | Authenticate project
*ENSApi* | [**get_address_from_domain**](docs/apis/tags/ENSApi.md#get_address_from_domain) | **get** /v1/ens/addressFromDomain | Get address for specified ENS domain
*ENSApi* | [**get_domain_from_address**](docs/apis/tags/ENSApi.md#get_domain_from_address) | **get** /v1/ens/domainFromAddress | Get domain and metadata for specified ENS address
*ExchangeRateInfoApi* | [**get_current_exchange_rate**](docs/apis/tags/ExchangeRateInfoApi.md#get_current_exchange_rate) | **get** /v1/exchangerate/current | Get current exchange rate
*ExchangeRateInfoApi* | [**get_historical_exchange_rate**](docs/apis/tags/ExchangeRateInfoApi.md#get_historical_exchange_rate) | **get** /v1/exchangerate/history | Get historical exchange rate
*RiskInfoApi* | [**get_address_risk_score**](docs/apis/tags/RiskInfoApi.md#get_address_risk_score) | **get** /v1/risk/score | Get address risk score
*RiskInfoApi* | [**get_address_risk_score_case**](docs/apis/tags/RiskInfoApi.md#get_address_risk_score_case) | **get** /v1/risk/score/details/{case_id} | Get address risk score case
*RiskInfoApi* | [**get_address_risk_score_details**](docs/apis/tags/RiskInfoApi.md#get_address_risk_score_details) | **get** /v1/risk/score/details | Get address risk score details
*RiskInfoApi* | [**get_transaction_risk_score**](docs/apis/tags/RiskInfoApi.md#get_transaction_risk_score) | **get** /v1/risk/transaction/score | Get transaction risk score
*RiskInfoApi* | [**get_transaction_risk_score_case**](docs/apis/tags/RiskInfoApi.md#get_transaction_risk_score_case) | **get** /v1/risk/transaction/score/details/{case_id} | Get transaction risk score case
*RiskInfoApi* | [**get_transaction_risk_score_details**](docs/apis/tags/RiskInfoApi.md#get_transaction_risk_score_details) | **get** /v1/risk/transaction/score/details | Get transaction risk score details
*UserManagementApi* | [**auth_user**](docs/apis/tags/UserManagementApi.md#auth_user) | **get** /v1/users/{id}/auth | Authenticate user
*UserManagementApi* | [**create_user**](docs/apis/tags/UserManagementApi.md#create_user) | **post** /v1/users | Create user
*UserManagementApi* | [**delete_user**](docs/apis/tags/UserManagementApi.md#delete_user) | **delete** /v1/users/{id} | Delete user
*UserManagementApi* | [**get_user**](docs/apis/tags/UserManagementApi.md#get_user) | **get** /v1/users/{id} | Get user
*UserManagementApi* | [**list_users**](docs/apis/tags/UserManagementApi.md#list_users) | **get** /v1/users | List users
*UserManagementApi* | [**update_user**](docs/apis/tags/UserManagementApi.md#update_user) | **post** /v1/users/{id} | Update user

## Documentation For Models

 - [AccountProvider](docs/models/AccountProvider.md)
 - [AccountProviderHint](docs/models/AccountProviderHint.md)
 - [AddressRiskReport](docs/models/AddressRiskReport.md)
 - [Amount](docs/models/Amount.md)
 - [Analytics](docs/models/Analytics.md)
 - [ExchangeRate](docs/models/ExchangeRate.md)
 - [Metadata](docs/models/Metadata.md)
 - [Movement](docs/models/Movement.md)
 - [NftContractMetadata](docs/models/NftContractMetadata.md)
 - [NftGateway](docs/models/NftGateway.md)
 - [NftId](docs/models/NftId.md)
 - [NftMedia](docs/models/NftMedia.md)
 - [NftRaw](docs/models/NftRaw.md)
 - [NftSpamInfo](docs/models/NftSpamInfo.md)
 - [NftTokenType](docs/models/NftTokenType.md)
 - [NftTokenUri](docs/models/NftTokenUri.md)
 - [OwnedNft](docs/models/OwnedNft.md)
 - [RiskReportCategory](docs/models/RiskReportCategory.md)
 - [TransactionRiskReport](docs/models/TransactionRiskReport.md)
 - [User](docs/models/User.md)

## Documentation For Authorization


## ProjectJWT

- **Type**: Bearer authentication (JWT)


## ProjectToken

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header

 Authentication schemes defined for the API:
## UserJWT

- **Type**: Bearer authentication (JWT)


## Author











## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in blockmate.apis and blockmate.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from blockmate.apis.default_api import DefaultApi`
- `from blockmate.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import blockmate
from blockmate.apis import *
from blockmate.models import *
```
