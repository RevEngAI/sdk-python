# TriageFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **int** | Virtual address of the function | 
**capabilities** | **List[str]** | Capability categories the function exhibits | 
**id** | **int** | ID of the function | 
**score** | **float** | Maliciousness score for the function, 0 to 1 | 
**summary** | **str** | What the function does | 

## Example

```python
from revengai.models.triage_function import TriageFunction

# TODO update the JSON string below
json = "{}"
# create an instance of TriageFunction from a JSON string
triage_function_instance = TriageFunction.from_json(json)
# print the JSON string representation of the object
print(TriageFunction.to_json())

# convert the object into a dict
triage_function_dict = triage_function_instance.to_dict()
# create an instance of TriageFunction from a dict
triage_function_from_dict = TriageFunction.from_dict(triage_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


