# blockmate.model.nft_media.NftMedia

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

