# CryptoDirectMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Crypto category of the match | 
**how** | **str** | Detection tier that produced the match | 
**library** | **str** | Crypto library the match belongs to | 
**matched_name** | **str** | Name or token that matched | 

## Example

```python
from revengai.models.crypto_direct_match import CryptoDirectMatch

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoDirectMatch from a JSON string
crypto_direct_match_instance = CryptoDirectMatch.from_json(json)
# print the JSON string representation of the object
print(CryptoDirectMatch.to_json())

# convert the object into a dict
crypto_direct_match_dict = crypto_direct_match_instance.to_dict()
# create an instance of CryptoDirectMatch from a dict
crypto_direct_match_from_dict = CryptoDirectMatch.from_dict(crypto_direct_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


