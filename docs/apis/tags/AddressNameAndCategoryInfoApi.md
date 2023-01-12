<a name="__pageTop"></a>
# blockmate.apis.tags.address_name_and_category_info_api.AddressNameAndCategoryInfoApi

All URIs are relative to *https://api.blockmate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address_name_info_multi**](#get_address_name_info_multi) | **post** /v1/addressname/multi | Get address name and category info for multiple addresses
[**get_address_name_info_single**](#get_address_name_info_single) | **get** /v1/addressname/simple | Get address name and category info for single address

# **get_address_name_info_multi**
<a name="get_address_name_info_multi"></a>
> {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} get_address_name_info_multi(chain)

Get address name and category info for multiple addresses

### Example

* Bearer (JWT) Authentication (ProjectJWT):
* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import address_name_and_category_info_api
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

# Configure Bearer authorization (JWT): ProjectJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): UserJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with blockmate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = address_name_and_category_info_api.AddressNameAndCategoryInfoApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'chain': "btc",
    }
    try:
        # Get address name and category info for multiple addresses
        api_response = api_instance.get_address_name_info_multi(
            query_params=query_params,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AddressNameAndCategoryInfoApi->get_address_name_info_multi: %s\n" % e)

    # example passing only optional values
    query_params = {
        'chain': "btc",
    }
    body = [
        "bc1qjl7k0dpcsw3djmzq25qv6peavgxysq95pcduuq"
    ]
    try:
        # Get address name and category info for multiple addresses
        api_response = api_instance.get_address_name_info_multi(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AddressNameAndCategoryInfoApi->get_address_name_info_multi: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
chain | ChainSchema | | 


# ChainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_address_name_info_multi.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_address_name_info_multi.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_address_name_info_multi.ApiResponseFor401) | Unauthorized

#### get_address_name_info_multi.ApiResponseFor200
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
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  |  | [optional] 
**category** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_address_name_info_multi.ApiResponseFor400
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

#### get_address_name_info_multi.ApiResponseFor401
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

[ProjectJWT](../../../README.md#ProjectJWT), [UserJWT](../../../README.md#UserJWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_address_name_info_single**
<a name="get_address_name_info_single"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_address_name_info_single(addresschain)

Get address name and category info for single address

### Example

* Bearer (JWT) Authentication (ProjectJWT):
* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import address_name_and_category_info_api
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

# Configure Bearer authorization (JWT): ProjectJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Configure Bearer authorization (JWT): UserJWT
configuration = blockmate.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)
# Enter a context with an instance of the API client
with blockmate.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = address_name_and_category_info_api.AddressNameAndCategoryInfoApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'address': "bc1qjl7k0dpcsw3djmzq25qv6peavgxysq95pcduuq",
        'chain': "btc",
    }
    try:
        # Get address name and category info for single address
        api_response = api_instance.get_address_name_info_single(
            query_params=query_params,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AddressNameAndCategoryInfoApi->get_address_name_info_single: %s\n" % e)
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
address | AddressSchema | | 
chain | ChainSchema | | 


# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ChainSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_address_name_info_single.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_address_name_info_single.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_address_name_info_single.ApiResponseFor401) | Unauthorized

#### get_address_name_info_single.ApiResponseFor200
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
**name** | str,  | str,  |  | [optional] 
**category** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_address_name_info_single.ApiResponseFor400
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

#### get_address_name_info_single.ApiResponseFor401
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

[ProjectJWT](../../../README.md#ProjectJWT), [UserJWT](../../../README.md#UserJWT)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

