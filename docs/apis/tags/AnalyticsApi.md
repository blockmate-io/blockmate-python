<a name="__pageTop"></a>
# blockmate.apis.tags.analytics_api.AnalyticsApi

All URIs are relative to *https://api.blockmate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analytics**](#get_analytics) | **get** /v1/analytics/{account_provider}/account/{account_id}/stats | Get analytics focused on gaming

# **get_analytics**
<a name="get_analytics"></a>
> {str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)} get_analytics(account_provideraccount_id)

Get analytics focused on gaming

Get analytics focused on gaming. All empty values are omitted from the response.

### Example

* Bearer (JWT) Authentication (UserJWT):
```python
import blockmate
from blockmate.apis.tags import analytics_api
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
        # Get analytics focused on gaming
        api_response = api_instance.get_analytics(
            path_params=path_params,
        )
        pprint(api_response)
    except blockmate.ApiException as e:
        print("Exception when calling AnalyticsApi->get_analytics: %s\n" % e)
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
200 | [ApiResponseFor200](#get_analytics.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_analytics.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_analytics.ApiResponseFor401) | Unauthorized

#### get_analytics.ApiResponseFor200
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
**count_txs_all_forever_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | Transactions count | [optional] 
**count_txs_all_forever_nft** | decimal.Decimal, int,  | decimal.Decimal,  | NFT transactions count | [optional] 
**count_txs_all_forever_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | Gaming transactions count | [optional] 
**count_txs_all_forever_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | Gambling transactions count | [optional] 
**count_txs_all_365_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | Transactions count during last year | [optional] 
**count_txs_all_365_nft** | decimal.Decimal, int,  | decimal.Decimal,  | NFT transactions count during last year | [optional] 
**count_txs_all_365_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | Gaming transactions count during last year | [optional] 
**count_txs_all_365_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | Gambling transactions count during last year | [optional] 
**count_txs_all_31_60_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | Transactions count during previous month | [optional] 
**count_txs_all_31_60_nft** | decimal.Decimal, int,  | decimal.Decimal,  | NFT transactions count during previous month | [optional] 
**count_txs_all_31_60_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | Gaming transactions count during previous month | [optional] 
**count_txs_all_31_60_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | Gambling transactions count during previous month | [optional] 
**count_txs_all_30_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | Transactions count during last month | [optional] 
**count_txs_all_30_nft** | decimal.Decimal, int,  | decimal.Decimal,  | NFT transactions count during last month | [optional] 
**count_txs_all_30_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | Gaming transactions count during last month | [optional] 
**count_txs_all_30_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | Gambling transactions count during last month | [optional] 
**count_txs_all_7_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | Transactions count during last week | [optional] 
**count_txs_all_7_nft** | decimal.Decimal, int,  | decimal.Decimal,  | NFT transactions count during last week | [optional] 
**count_txs_all_7_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | Gaming transactions count during last week | [optional] 
**count_txs_all_7_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | Gambling transactions count during last week | [optional] 
**count_txs_in_forever_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | IN transactions count | [optional] 
**count_txs_in_forever_nft** | decimal.Decimal, int,  | decimal.Decimal,  | IN NFT transactions count | [optional] 
**count_txs_in_forever_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | IN gaming transactions count | [optional] 
**count_txs_in_forever_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | IN gambling transactions count | [optional] 
**count_txs_in_365_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | IN transactions count during last year | [optional] 
**count_txs_in_365_nft** | decimal.Decimal, int,  | decimal.Decimal,  | IN NFT transactions count during last year | [optional] 
**count_txs_in_365_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | IN gaming transactions count during last year | [optional] 
**count_txs_in_365_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | IN gambling transactions count during last year | [optional] 
**count_txs_in_31_60_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | IN transactions count during previous month | [optional] 
**count_txs_in_31_60_nft** | decimal.Decimal, int,  | decimal.Decimal,  | IN NFT transactions count during previous month | [optional] 
**count_txs_in_31_60_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | IN gaming transactions count during previous month | [optional] 
**count_txs_in_31_60_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | IN gambling transactions count during previous month | [optional] 
**count_txs_in_30_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | IN transactions count during last month | [optional] 
**count_txs_in_30_nft** | decimal.Decimal, int,  | decimal.Decimal,  | IN NFT transactions count during last month | [optional] 
**count_txs_in_30_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | IN gaming transactions count during last month | [optional] 
**count_txs_in_30_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | IN gambling transactions count during last month | [optional] 
**count_txs_in_7_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | IN transactions count during last week | [optional] 
**count_txs_in_7_nft** | decimal.Decimal, int,  | decimal.Decimal,  | IN NFT transactions count during last week | [optional] 
**count_txs_in_7_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | IN gaming transactions count during last week | [optional] 
**count_txs_in_7_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | IN gambling transactions count during last week | [optional] 
**count_txs_out_forever_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | OUT transactions count | [optional] 
**count_txs_out_forever_nft** | decimal.Decimal, int,  | decimal.Decimal,  | OUT NFT transactions count | [optional] 
**count_txs_out_forever_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gaming transactions count | [optional] 
**count_txs_out_forever_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gambling transactions count | [optional] 
**count_txs_out_365_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | OUT transactions count during last year | [optional] 
**count_txs_out_365_nft** | decimal.Decimal, int,  | decimal.Decimal,  | OUT NFT transactions count during last year | [optional] 
**count_txs_out_365_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gaming transactions count during last year | [optional] 
**count_txs_out_365_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gambling transactions count during last year | [optional] 
**count_txs_out_31_60_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | OUT transactions count during previous month | [optional] 
**count_txs_out_31_60_nft** | decimal.Decimal, int,  | decimal.Decimal,  | OUT NFT transactions count during previous month | [optional] 
**count_txs_out_31_60_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gaming transactions count during previous month | [optional] 
**count_txs_out_31_60_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gambling transactions count during previous month | [optional] 
**count_txs_out_30_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | OUT transactions count during last month | [optional] 
**count_txs_out_30_nft** | decimal.Decimal, int,  | decimal.Decimal,  | OUT NFT transactions count during last month | [optional] 
**count_txs_out_30_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gaming transactions count during last month | [optional] 
**count_txs_out_30_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gambling transactions count during last month | [optional] 
**count_txs_out_7_onchain** | decimal.Decimal, int,  | decimal.Decimal,  | OUT transactions count during last week | [optional] 
**count_txs_out_7_nft** | decimal.Decimal, int,  | decimal.Decimal,  | OUT NFT transactions count during last week | [optional] 
**count_txs_out_7_gaming** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gaming transactions count during last week | [optional] 
**count_txs_out_7_gambling** | decimal.Decimal, int,  | decimal.Decimal,  | OUT gambling transactions count during last week | [optional] 
**first_txs_all_onchain** | str,  | str,  | Time when first transaction occurred | [optional] 
**first_txs_all_nft** | str,  | str,  | Time when first NFT transaction occurred | [optional] 
**first_txs_all_gaming** | str,  | str,  | Time when first gaming transaction occurred | [optional] 
**first_txs_all_gambling** | str,  | str,  | Time when first gambling transaction occurred | [optional] 
**first_txs_in_onchain** | str,  | str,  | Time when first IN transaction occurred | [optional] 
**first_txs_in_nft** | str,  | str,  | Time when first IN NFT transaction occurred | [optional] 
**first_txs_in_gaming** | str,  | str,  | Time when first IN gaming transaction occurred | [optional] 
**first_txs_in_gambling** | str,  | str,  | Time when first IN gambling transaction occurred | [optional] 
**first_txs_out_onchain** | str,  | str,  | Time when first OUT transaction occurred | [optional] 
**first_txs_out_nft** | str,  | str,  | Time when first OUT NFT transaction occurred | [optional] 
**first_txs_out_gaming** | str,  | str,  | Time when first OUT gaming transaction occurred | [optional] 
**first_txs_out_gambling** | str,  | str,  | Time when first OUT gambling transaction occurred | [optional] 
**last_txs_all_onchain** | str,  | str,  | Time when last transaction occurred | [optional] 
**last_txs_all_nft** | str,  | str,  | Time when last NFT transaction occurred | [optional] 
**last_txs_all_gaming** | str,  | str,  | Time when last gaming transaction occurred | [optional] 
**last_txs_all_gambling** | str,  | str,  | Time when last gambling transaction occurred | [optional] 
**last_txs_in_onchain** | str,  | str,  | Time when last IN transaction occurred | [optional] 
**last_txs_in_nft** | str,  | str,  | Time when last IN NFT transaction occurred | [optional] 
**last_txs_in_gaming** | str,  | str,  | Time when last IN gaming transaction occurred | [optional] 
**last_txs_in_gambling** | str,  | str,  | Time when last IN gambling transaction occurred | [optional] 
**last_txs_out_onchain** | str,  | str,  | Time when last OUT transaction occurred | [optional] 
**last_txs_out_nft** | str,  | str,  | Time when last OUT NFT transaction occurred | [optional] 
**last_txs_out_gaming** | str,  | str,  | Time when last OUT gaming transaction occurred | [optional] 
**last_txs_out_gambling** | str,  | str,  | Time when last OUT gambling transaction occurred | [optional] 
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sum_txs_all_forever_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all transactions | [optional] 
**sum_txs_all_forever_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all NFT transactions | [optional] 
**sum_txs_all_forever_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gaming transactions | [optional] 
**sum_txs_all_forever_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gambling transactions | [optional] 
**sum_txs_all_365_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all transactions during last year | [optional] 
**sum_txs_all_365_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all NFT transactions during last year | [optional] 
**sum_txs_all_365_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gaming transactions during last year | [optional] 
**sum_txs_all_365_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gambling transactions during last year | [optional] 
**sum_txs_all_31_60_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all transactions during previous month | [optional] 
**sum_txs_all_31_60_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all NFT transactions during previous month | [optional] 
**sum_txs_all_31_60_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gaming transactions during previous month | [optional] 
**sum_txs_all_31_60_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gambling transactions during previous month | [optional] 
**sum_txs_all_30_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all transactions during last month | [optional] 
**sum_txs_all_30_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all NFT transactions during last month | [optional] 
**sum_txs_all_30_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gaming transactions during last month | [optional] 
**sum_txs_all_30_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gambling transactions during last month | [optional] 
**sum_txs_all_7_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all transactions during last week | [optional] 
**sum_txs_all_7_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all NFT transactions during last week | [optional] 
**sum_txs_all_7_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gaming transactions during last week | [optional] 
**sum_txs_all_7_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all gambling transactions during last week | [optional] 
**sum_txs_in_forever_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN transactions | [optional] 
**sum_txs_in_forever_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN NFT transactions | [optional] 
**sum_txs_in_forever_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gaming transactions | [optional] 
**sum_txs_in_forever_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gambling transactions | [optional] 
**sum_txs_in_365_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN transactions during last year | [optional] 
**sum_txs_in_365_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN NFT transactions during last year | [optional] 
**sum_txs_in_365_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gaming transactions during last year | [optional] 
**sum_txs_in_365_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gambling transactions during last year | [optional] 
**sum_txs_in_31_60_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN transactions during previous month | [optional] 
**sum_txs_in_31_60_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN NFT transactions during previous month | [optional] 
**sum_txs_in_31_60_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gaming transactions during previous month | [optional] 
**sum_txs_in_31_60_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gambling transactions during previous month | [optional] 
**sum_txs_in_30_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN transactions during last month | [optional] 
**sum_txs_in_30_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN NFT transactions during last month | [optional] 
**sum_txs_in_30_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gaming transactions during last month | [optional] 
**sum_txs_in_30_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gambling transactions during last month | [optional] 
**sum_txs_in_7_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN transactions during last week | [optional] 
**sum_txs_in_7_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN NFT transactions during last week | [optional] 
**sum_txs_in_7_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gaming transactions during last week | [optional] 
**sum_txs_in_7_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all IN gambling transactions during last week | [optional] 
**sum_txs_out_forever_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT transactions | [optional] 
**sum_txs_out_forever_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT NFT transactions | [optional] 
**sum_txs_out_forever_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gaming transactions | [optional] 
**sum_txs_out_forever_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gambling transactions | [optional] 
**sum_txs_out_365_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT transactions during last year | [optional] 
**sum_txs_out_365_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT NFT transactions during last year | [optional] 
**sum_txs_out_365_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gaming transactions during last year | [optional] 
**sum_txs_out_365_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gambling transactions during last year | [optional] 
**sum_txs_out_31_60_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT transactions during previous month | [optional] 
**sum_txs_out_31_60_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT NFT transactions during previous month | [optional] 
**sum_txs_out_31_60_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gaming transactions during previous month | [optional] 
**sum_txs_out_31_60_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gambling transactions during previous month | [optional] 
**sum_txs_out_30_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT transactions during last month | [optional] 
**sum_txs_out_30_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT NFT transactions during last month | [optional] 
**sum_txs_out_30_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gaming transactions during last month | [optional] 
**sum_txs_out_30_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gambling transactions during last month | [optional] 
**sum_txs_out_7_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT transactions during last week | [optional] 
**sum_txs_out_7_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT NFT transactions during last week | [optional] 
**sum_txs_out_7_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gaming transactions during last week | [optional] 
**sum_txs_out_7_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Sum of all OUT gambling transactions during last week | [optional] 
**max_balance_forever_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum balance | [optional] 
**max_balance_forever_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum NFT balance | [optional] 
**max_balance_forever_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gaming balance | [optional] 
**max_balance_forever_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gambing balance | [optional] 
**max_balance_365_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum balance during last year | [optional] 
**max_balance_365_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum NFT balance during last year | [optional] 
**max_balance_365_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gaming balance during last year | [optional] 
**max_balance_365_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gambling balance during last year | [optional] 
**max_balance_31_60_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum balance during previous month | [optional] 
**max_balance_31_60_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum NFT balance during previous month | [optional] 
**max_balance_31_60_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gaming balance during previous month | [optional] 
**max_balance_31_60_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gambling balance during previous month | [optional] 
**max_balance_30_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum balance during last month | [optional] 
**max_balance_30_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum NFT balance during last month | [optional] 
**max_balance_30_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gaming balance during last month | [optional] 
**max_balance_30_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gambling balance during last month | [optional] 
**max_balance_7_onchain** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum balance during last week | [optional] 
**max_balance_7_nft** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum NFT balance during last week | [optional] 
**max_balance_7_gaming** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gaming balance during last week | [optional] 
**max_balance_7_gambling** | decimal.Decimal, int, float,  | decimal.Decimal,  | Maximum gambling balance during last week | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_analytics.ApiResponseFor400
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

#### get_analytics.ApiResponseFor401
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
