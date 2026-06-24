# CreateGroupInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Group name | 

## Example

```python
from revengai.models.create_group_input_body import CreateGroupInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateGroupInputBody from a JSON string
create_group_input_body_instance = CreateGroupInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateGroupInputBody.to_json())

# convert the object into a dict
create_group_input_body_dict = create_group_input_body_instance.to_dict()
# create an instance of CreateGroupInputBody from a dict
create_group_input_body_from_dict = CreateGroupInputBody.from_dict(create_group_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


