<a name="__pageTop"></a>
# blockmate.apis.tags.analytics_api.AnalyticsApi

All URIs are relative to *https://api.blockmate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_analytics**](#get_account_analytics) | **get** /v1/analytics/{account_provider}/account/{account_id}/stats | Get analytics focused on gaming for specified account and provider
[**get_project_analytics**](#get_project_analytics) | **get** /v1/analytics/project/stats | Get analytics focused on gaming for whole project
[**get_provider_analytics**](#get_provider_analytics) | **get** /v1/analytics/{account_provider}/stats | Get analytics focused on gaming for specified provider
[**get_user_analytics**](#get_user_analytics) | **get** /v1/analytics/user/stats | Get analytics focused on gaming for this user

# **get_account_analytics**
<a name="get_account_analytics"></a>
> Analytics get_account_analytics(account_provideraccount_id)

Get analytics focused on gaming for specified account and provider

Get analytics focused on gaming for specified account and provider. All empty values are omitted from the response. Values are recalculated once per day.

### Example

* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import analytics_api
from blockmate.model.analytics import Analytics
from pprint import pprint
# Defining the host is optional and defaults to https://api.blockmate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = blockmate.Configuration(
    host = "https://api.blockmate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): UserJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with blockmate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_provider': "onchain/btc",
        'account_id': "163b6df1-dc0b-4086-8922-6068fe1e653d",
    }
    try:
        # Get analytics focused on gaming for specified account and provider
        api_response = api_instance.get_account_analytics(
            path_params=path_params,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AnalyticsApi->get_account_analytics: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_provider | AccountProviderSchema | | 
account_id | AccountIdSchema | | 

# AccountProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AccountIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_account_analytics.ApiResponseFor200) | OK
204 | [ApiResponseFor204](#get_account_analytics.ApiResponseFor204) | No Content (happens when account is connected, but values were not recalculated yet)
400 | [ApiResponseFor400](#get_account_analytics.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_account_analytics.ApiResponseFor401) | Unauthorized

#### get_account_analytics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Analytics**](../../models/Analytics.md) |  | 


#### get_account_analytics.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_account_analytics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_account_analytics.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[UserJWT](../../../README.md#UserJWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_project_analytics**
<a name="get_project_analytics"></a>
> {str: (Analytics,)} get_project_analytics()

Get analytics focused on gaming for whole project

Get analytics focused on gaming for whole project. All empty values are omitted from the response. Values are recalculated once per day.

### Example

* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import analytics_api
from blockmate.model.analytics import Analytics
from pprint import pprint
# Defining the host is optional and defaults to https://api.blockmate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = blockmate.Configuration(
    host = "https://api.blockmate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): UserJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with blockmate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get analytics focused on gaming for whole project
        api_response = api_instance.get_project_analytics()
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AnalyticsApi->get_project_analytics: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_project_analytics.ApiResponseFor200) | OK
204 | [ApiResponseFor204](#get_project_analytics.ApiResponseFor204) | No Content (happens when at least one account is connected, but values were not recalculated yet)
400 | [ApiResponseFor400](#get_project_analytics.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_project_analytics.ApiResponseFor401) | Unauthorized

#### get_project_analytics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**Analytics**]({{complexTypePrefix}}Analytics.md) | [**Analytics**]({{complexTypePrefix}}Analytics.md) | any string name can be used but the value must be the correct type | [optional] 

#### get_project_analytics.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_project_analytics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_project_analytics.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[UserJWT](../../../README.md#UserJWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_provider_analytics**
<a name="get_provider_analytics"></a>
> {str: (Analytics,)} get_provider_analytics(account_provider)

Get analytics focused on gaming for specified provider

Get analytics focused on gaming for specified provider. All empty values are omitted from the response. Values are recalculated once per day.

### Example

* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import analytics_api
from blockmate.model.analytics import Analytics
from pprint import pprint
# Defining the host is optional and defaults to https://api.blockmate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = blockmate.Configuration(
    host = "https://api.blockmate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): UserJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with blockmate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'account_provider': "onchain/btc",
    }
    try:
        # Get analytics focused on gaming for specified provider
        api_response = api_instance.get_provider_analytics(
            path_params=path_params,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AnalyticsApi->get_provider_analytics: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
account_provider | AccountProviderSchema | | 

# AccountProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_provider_analytics.ApiResponseFor200) | OK
204 | [ApiResponseFor204](#get_provider_analytics.ApiResponseFor204) | No Content (happens when at least one account is connected, but values were not recalculated yet)
400 | [ApiResponseFor400](#get_provider_analytics.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_provider_analytics.ApiResponseFor401) | Unauthorized

#### get_provider_analytics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**Analytics**]({{complexTypePrefix}}Analytics.md) | [**Analytics**]({{complexTypePrefix}}Analytics.md) | any string name can be used but the value must be the correct type | [optional] 

#### get_provider_analytics.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_provider_analytics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_provider_analytics.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[UserJWT](../../../README.md#UserJWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_analytics**
<a name="get_user_analytics"></a>
> {str: (Analytics,)} get_user_analytics()

Get analytics focused on gaming for this user

Get analytics focused on gaming for this user. All empty values are omitted from the response. Values are recalculated once per day.

### Example

* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import analytics_api
from blockmate.model.analytics import Analytics
from pprint import pprint
# Defining the host is optional and defaults to https://api.blockmate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = blockmate.Configuration(
    host = "https://api.blockmate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): UserJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with blockmate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = analytics_api.AnalyticsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get analytics focused on gaming for this user
        api_response = api_instance.get_user_analytics()
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AnalyticsApi->get_user_analytics: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_analytics.ApiResponseFor200) | OK
204 | [ApiResponseFor204](#get_user_analytics.ApiResponseFor204) | No Content (happens when at least one account is connected, but values were not recalculated yet)
400 | [ApiResponseFor400](#get_user_analytics.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_user_analytics.ApiResponseFor401) | Unauthorized

#### get_user_analytics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**Analytics**]({{complexTypePrefix}}Analytics.md) | [**Analytics**]({{complexTypePrefix}}Analytics.md) | any string name can be used but the value must be the correct type | [optional] 

#### get_user_analytics.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_user_analytics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_user_analytics.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Authorization

[UserJWT](../../../README.md#UserJWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

