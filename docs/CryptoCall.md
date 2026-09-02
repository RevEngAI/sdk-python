# CryptoCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callee_name** | **str** | Name of the called function | 
**category** | **str** | Crypto category of the match | 
**how** | **str** | Detection tier that produced the match | 
**library** | **str** | Crypto library the match belongs to | 
**matched_name** | **str** | Name or token that matched | 

## Example

```python
from revengai.models.crypto_call import CryptoCall

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoCall from a JSON string
crypto_call_instance = CryptoCall.from_json(json)
# print the JSON string representation of the object
print(CryptoCall.to_json())

# convert the object into a dict
crypto_call_dict = crypto_call_instance.to_dict()
# create an instance of CryptoCall from a dict
crypto_call_from_dict = CryptoCall.from_dict(crypto_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


