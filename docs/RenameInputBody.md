# RenameInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**new_mangled_name** | **str** | New mangled function name | [optional] 
**new_name** | **str** | New function name | 

## Example

```python
from revengai.models.rename_input_body import RenameInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of RenameInputBody from a JSON string
rename_input_body_instance = RenameInputBody.from_json(json)
# print the JSON string representation of the object
print(RenameInputBody.to_json())

# convert the object into a dict
rename_input_body_dict = rename_input_body_instance.to_dict()
# create an instance of RenameInputBody from a dict
rename_input_body_from_dict = RenameInputBody.from_dict(rename_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


