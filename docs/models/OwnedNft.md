# blockmate.model.owned_nft.OwnedNft

OwnedNft

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | OwnedNft | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[contract](#contract)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Object - Contract for returned NFT | [optional] 
**id** | [**NftId**](NftId.md) | [**NftId**](NftId.md) |  | [optional] 
**balance** | str,  | str,  | String - Token balance | [optional] 
**title** | str,  | str,  | String - Name of the NFT asset. | [optional] 
**description** | str,  | str,  | String - Brief human-readable description | [optional] 
**tokenUri** | [**NftTokenUri**](NftTokenUri.md) | [**NftTokenUri**](NftTokenUri.md) |  | [optional] 
**[media](#media)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**metadata** | [**Metadata**](Metadata.md) | [**Metadata**](Metadata.md) |  | [optional] 
**timeLastUpdated** | str,  | str,  | String - ISO timestamp of the last cache refresh for the information returned in the metadata field. | [optional] 
**error** | str,  | str,  | String - A string describing a particular reason that we were unable to fetch complete metadata for the NFT. | [optional] 
**contractMetadata** | [**NftContractMetadata**](NftContractMetadata.md) | [**NftContractMetadata**](NftContractMetadata.md) |  | [optional] 
**spamInfo** | [**NftSpamInfo**](NftSpamInfo.md) | [**NftSpamInfo**](NftSpamInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# contract

Object - Contract for returned NFT

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Object - Contract for returned NFT | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**address** | str,  | str,  | String - Address of NFT contract. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# media

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**raw** | str,  | str,  | String - Uri representing the location of the NFT&#x27;s original metadata blob. This is a backup for you to parse when the metadata field is not automatically populated. | [optional] 
**gateway** | str,  | str,  | String - Public gateway uri for the raw uri above. | [optional] 
**thumbnail** | str,  | str,  | URL for a resized thumbnail of the NFT media asset. | [optional] 
**format** | str,  | str,  | The media format (jpg, gif, png, etc.) of the gateway and thumbnail assets. | [optional] 
**bytes** | decimal.Decimal, int,  | decimal.Decimal,  | The size of the media asset in bytes. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

