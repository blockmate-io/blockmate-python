# blockmate.model.metadata.Metadata

String - Relevant metadata for NFT contract. This is useful for viewing image url, traits, etc. without having to follow the metadata url in tokenUri to parse manually.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | String - Relevant metadata for NFT contract. This is useful for viewing image url, traits, etc. without having to follow the metadata url in tokenUri to parse manually. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**image** | str,  | str,  | String - URL to the NFT asset image. Can be standard URLs pointing to images on conventional servers, IPFS, or Arweave. Most types of images (SVGs, PNGs, JPEGs, etc.) are supported by NFT marketplaces. | [optional] 
**external_url** | str,  | str,  | String - The image URL that appears alongside the asset image on NFT platforms. | [optional] 
**background_color** | str,  | str,  | String - Background color of the NFT item. Usually must be defined as a six-character hexadecimal. | [optional] 
**name** | str,  | str,  | String - Name of the NFT asset. | [optional] 
**description** | str,  | str,  | String - Human-readable description of the NFT asset. (Markdown is supported/rendered on OpenSea and other NFT platforms) | [optional] 
**[attributes](#attributes)** | list, tuple,  | tuple,  | Object - Traits/attributes/characteristics for each NFT asset. | [optional] 
**media** | [**NftMedia**](NftMedia.md) | [**NftMedia**](NftMedia.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# attributes

Object - Traits/attributes/characteristics for each NFT asset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Object - Traits/attributes/characteristics for each NFT asset. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**value** | str,  | str,  |  | [optional] 
**trait_type** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

