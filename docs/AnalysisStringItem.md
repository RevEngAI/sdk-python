# AnalysisStringItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | [**List[AnalysisStringFunction]**](AnalysisStringFunction.md) |  | 
**source** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from revengai.models.analysis_string_item import AnalysisStringItem

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisStringItem from a JSON string
analysis_string_item_instance = AnalysisStringItem.from_json(json)
# print the JSON string representation of the object
print(AnalysisStringItem.to_json())

# convert the object into a dict
analysis_string_item_dict = analysis_string_item_instance.to_dict()
# create an instance of AnalysisStringItem from a dict
analysis_string_item_from_dict = AnalysisStringItem.from_dict(analysis_string_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


