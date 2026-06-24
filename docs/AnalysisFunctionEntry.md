# AnalysisFunctionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_id** | **int** |  | 
**debug** | **bool** |  | 
**function_id** | **int** |  | 
**function_name** | **str** |  | 
**function_size** | **int** |  | 
**function_vaddr** | **int** |  | 
**mangled_name** | **str** |  | [optional] 
**source_binary_id** | **int** |  | [optional] 
**source_type** | **str** |  | 

## Example

```python
from revengai.models.analysis_function_entry import AnalysisFunctionEntry

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisFunctionEntry from a JSON string
analysis_function_entry_instance = AnalysisFunctionEntry.from_json(json)
# print the JSON string representation of the object
print(AnalysisFunctionEntry.to_json())

# convert the object into a dict
analysis_function_entry_dict = analysis_function_entry_instance.to_dict()
# create an instance of AnalysisFunctionEntry from a dict
analysis_function_entry_from_dict = AnalysisFunctionEntry.from_dict(analysis_function_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


