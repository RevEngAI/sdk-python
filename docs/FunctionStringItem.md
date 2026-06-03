# FunctionStringItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** |  | 
**vaddr** | **int** |  | 
**value** | **str** |  | 

## Example

```python
from revengai.models.function_string_item import FunctionStringItem

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionStringItem from a JSON string
function_string_item_instance = FunctionStringItem.from_json(json)
# print the JSON string representation of the object
print(FunctionStringItem.to_json())

# convert the object into a dict
function_string_item_dict = function_string_item_instance.to_dict()
# create an instance of FunctionStringItem from a dict
function_string_item_from_dict = FunctionStringItem.from_dict(function_string_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


