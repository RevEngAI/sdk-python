# AnalysisStringFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** |  | 
**function_vaddr** | **int** |  | 

## Example

```python
from revengai.models.analysis_string_function import AnalysisStringFunction

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStringFunction from a JSON string
analysis_string_function_instance = AnalysisStringFunction.from_json(json)
# print the JSON string representation of the object
print(AnalysisStringFunction.to_json())

# convert the object into a dict
analysis_string_function_dict = analysis_string_function_instance.to_dict()
# create an instance of AnalysisStringFunction from a dict
analysis_string_function_from_dict = AnalysisStringFunction.from_dict(analysis_string_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


