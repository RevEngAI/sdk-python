# CryptoExplainResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **bool** | Whether the run was cancelled | 
**error** | **str** | Why no explanation could be produced. Empty when the run succeeded. | [optional] 
**function_id** | **int** | ID of the explained function | 
**function_name** | **str** | Name of the explained function | [optional] 
**functions_involved** | [**List[CryptoExplainedFunction]**](CryptoExplainedFunction.md) | Other functions involved in the cryptographic operation | [optional] 
**summary** | **str** | Explanation of the cryptography the function performs | [optional] 

## Example

```python
from revengai.models.crypto_explain_result import CryptoExplainResult

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoExplainResult from a JSON string
crypto_explain_result_instance = CryptoExplainResult.from_json(json)
# print the JSON string representation of the object
print(CryptoExplainResult.to_json())

# convert the object into a dict
crypto_explain_result_dict = crypto_explain_result_instance.to_dict()
# create an instance of CryptoExplainResult from a dict
crypto_explain_result_from_dict = CryptoExplainResult.from_dict(crypto_explain_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


