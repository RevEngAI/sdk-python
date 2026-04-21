# TriageFunctionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of the function | 
**address** | **int** | Address of the function in the binary | 
**summary** | **str** | Summary of the function&#39;s behaviour | 
**score** | **float** | Score indicating the function&#39;s relevance | 
**capabilities** | **List[str]** | List of capabilities exhibited by the function | 

## Example

```python
from revengai.models.triage_function_response import TriageFunctionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriageFunctionResponse from a JSON string
triage_function_response_instance = TriageFunctionResponse.from_json(json)
# print the JSON string representation of the object
print(TriageFunctionResponse.to_json())

# convert the object into a dict
triage_function_response_dict = triage_function_response_instance.to_dict()
# create an instance of TriageFunctionResponse from a dict
triage_function_response_from_dict = TriageFunctionResponse.from_dict(triage_function_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


