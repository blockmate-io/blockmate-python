<a name="__pageTop"></a>
# blockmate.apis.tags.exchange_rate_info_api.ExchangeRateInfoApi

All URIs are relative to *https://api.blockmate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_exchange_rate**](#get_current_exchange_rate) | **get** /v1/exchangerate/current | Get current exchange rate
[**get_historical_exchange_rate**](#get_historical_exchange_rate) | **get** /v1/exchangerate/history | Get historical exchange rate

# **get_current_exchange_rate**
<a name="get_current_exchange_rate"></a>
> [ExchangeRate] get_current_exchange_rate(pairs)

Get current exchange rate

### Example

* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import exchange_rate_info_api
from blockmate.model.exchange_rate import ExchangeRate
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
    api_instance = exchange_rate_info_api.ExchangeRateInfoApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'pairs': "ETH/USD,BTC/EUR",
    }
    try:
        # Get current exchange rate
        api_response = api_instance.get_current_exchange_rate(
            query_params=query_params,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling ExchangeRateInfoApi->get_current_exchange_rate: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pairs | PairsSchema | | 


# PairsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_current_exchange_rate.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_current_exchange_rate.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_current_exchange_rate.ApiResponseFor401) | Unauthorized

#### get_current_exchange_rate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExchangeRate**]({{complexTypePrefix}}ExchangeRate.md) | [**ExchangeRate**]({{complexTypePrefix}}ExchangeRate.md) | [**ExchangeRate**]({{complexTypePrefix}}ExchangeRate.md) |  | 

#### get_current_exchange_rate.ApiResponseFor400
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

#### get_current_exchange_rate.ApiResponseFor401
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

# **get_historical_exchange_rate**
<a name="get_historical_exchange_rate"></a>
> [ExchangeRate] get_historical_exchange_rate(pairdays)

Get historical exchange rate

### Example

* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import exchange_rate_info_api
from blockmate.model.exchange_rate import ExchangeRate
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
    api_instance = exchange_rate_info_api.ExchangeRateInfoApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'pair': "ETH/USD",
        'days': "2022-06-30,2022-06-29",
    }
    try:
        # Get historical exchange rate
        api_response = api_instance.get_historical_exchange_rate(
            query_params=query_params,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling ExchangeRateInfoApi->get_historical_exchange_rate: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
pair | PairSchema | | 
days | DaysSchema | | 


# PairSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DaysSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_historical_exchange_rate.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_historical_exchange_rate.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_historical_exchange_rate.ApiResponseFor401) | Unauthorized

#### get_historical_exchange_rate.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ExchangeRate**]({{complexTypePrefix}}ExchangeRate.md) | [**ExchangeRate**]({{complexTypePrefix}}ExchangeRate.md) | [**ExchangeRate**]({{complexTypePrefix}}ExchangeRate.md) |  | 

#### get_historical_exchange_rate.ApiResponseFor400
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

#### get_historical_exchange_rate.ApiResponseFor401
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

