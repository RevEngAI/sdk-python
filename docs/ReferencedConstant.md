# ReferencedConstant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**Subject**](Subject.md) |  | 
**value** | [**BytesConstant**](BytesConstant.md) |  | 
**display** | [**Display**](Display.md) |  | [optional] 

## Example

```python
from revengai.models.referenced_constant import ReferencedConstant

# TODO update the JSON string below
json = "{}"
# create an instance of ReferencedConstant from a JSON string
referenced_constant_instance = ReferencedConstant.from_json(json)
# print the JSON string representation of the object
print(ReferencedConstant.to_json())

# convert the object into a dict
referenced_constant_dict = referenced_constant_instance.to_dict()
# create an instance of ReferencedConstant from a dict
referenced_constant_from_dict = ReferencedConstant.from_dict(referenced_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


