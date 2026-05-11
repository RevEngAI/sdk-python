# TokenisedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**function_mapping** | [**FunctionMapping**](FunctionMapping.md) | Complete mapping data for token resolution | [optional] 
**predicted_function_name** | **str** | Predicted function name from the AI model | [optional] 
**status** | **str** | Task status | 
**tokenised_decompilation** | **str** | Source code with placeholder tokens | [optional] 

## Example

```python
from revengai.models.tokenised_data import TokenisedData

# TODO update the JSON string below
json = "{}"
# create an instance of TokenisedData from a JSON string
tokenised_data_instance = TokenisedData.from_json(json)
# print the JSON string representation of the object
print(TokenisedData.to_json())

# convert the object into a dict
tokenised_data_dict = tokenised_data_instance.to_dict()
# create an instance of TokenisedData from a dict
tokenised_data_from_dict = TokenisedData.from_dict(tokenised_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


