# FunctionHeader


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr** | **int** |  | 
**args** | [**Dict[str, FunctionArgument]**](FunctionArgument.md) | Argument map keyed by ordinal hex (e.g. \&quot;0x0\&quot;, \&quot;0x1\&quot;). | 
**last_change** | **str** |  | [optional] 
**name** | **str** |  | 
**scope** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from revengai.models.function_header import FunctionHeader

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionHeader from a JSON string
function_header_instance = FunctionHeader.from_json(json)
# print the JSON string representation of the object
print(FunctionHeader.to_json())

# convert the object into a dict
function_header_dict = function_header_instance.to_dict()
# create an instance of FunctionHeader from a dict
function_header_from_dict = FunctionHeader.from_dict(function_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


