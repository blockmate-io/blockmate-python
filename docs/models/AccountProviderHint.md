# blockmate.model.account_provider_hint.AccountProviderHint

Account provider hint containing info about what is needed to connect such an account

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Account provider hint containing info about what is needed to connect such an account | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**account_type** | str,  | str,  |  | must be one of ["crypto_wallet", "crypto_exchange", "crypto_nft", ] 
**account_name** | str,  | str,  |  | 
**account_url** | str,  | str,  |  | 
**description** | str,  | str,  |  | 
**[fields](#fields)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**oauth** | bool,  | BoolClass,  |  | 
**url** | str,  | str,  |  | 
**info** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**intro** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fields

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**api_key** | str,  | str,  |  | [optional] 
**api_secret** | str,  | str,  |  | [optional] 
**api_passphrase** | str,  | str,  |  | [optional] 
**description** | str,  | str,  |  | [optional] 
**wallet** | str,  | str,  |  | [optional] 
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

