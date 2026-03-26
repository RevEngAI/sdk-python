# AnalysisStringInput

Input model for inserting a string into an analysis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The string literal value | 
**vaddr** | **int** | The virtual address of the string | 
**source** | [**StringSource**](StringSource.md) | The source of the string | 

## Example

```python
from revengai.models.analysis_string_input import AnalysisStringInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStringInput from a JSON string
analysis_string_input_instance = AnalysisStringInput.from_json(json)
# print the JSON string representation of the object
print(AnalysisStringInput.to_json())

# convert the object into a dict
analysis_string_input_dict = analysis_string_input_instance.to_dict()
# create an instance of AnalysisStringInput from a dict
analysis_string_input_from_dict = AnalysisStringInput.from_dict(analysis_string_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


