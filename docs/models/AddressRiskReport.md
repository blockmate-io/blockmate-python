# blockmate.model.address_risk_report.AddressRiskReport

AddressRiskReport

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | AddressRiskReport | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**chain** | str,  | str,  |  | 
**address** | str,  | str,  |  | 
**[details](#details)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**risk** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**case_id** | str,  | str,  |  | [optional] 
**request_datetime** | str,  | str,  |  | [optional] 
**response_datetime** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# details

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[own_categories](#own_categories)** | list, tuple,  | tuple,  |  | [optional] 
**[source_of_funds_categories](#source_of_funds_categories)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# own_categories

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RiskReportCategory**](RiskReportCategory.md) | [**RiskReportCategory**](RiskReportCategory.md) | [**RiskReportCategory**](RiskReportCategory.md) |  | 

# source_of_funds_categories

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RiskReportCategory**](RiskReportCategory.md) | [**RiskReportCategory**](RiskReportCategory.md) | [**RiskReportCategory**](RiskReportCategory.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

