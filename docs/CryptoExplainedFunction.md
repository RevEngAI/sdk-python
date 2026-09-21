# CryptoExplainedFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Role this function plays in the cryptographic operation | 
**function_id** | **int** | ID of the function | 
**function_name** | **str** | Name of the function | 

## Example

```python
from revengai.models.crypto_explained_function import CryptoExplainedFunction

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoExplainedFunction from a JSON string
crypto_explained_function_instance = CryptoExplainedFunction.from_json(json)
# print the JSON string representation of the object
print(CryptoExplainedFunction.to_json())

# convert the object into a dict
crypto_explained_function_dict = crypto_explained_function_instance.to_dict()
# create an instance of CryptoExplainedFunction from a dict
crypto_explained_function_from_dict = CryptoExplainedFunction.from_dict(crypto_explained_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


