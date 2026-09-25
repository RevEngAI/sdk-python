# UpdateTagsInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** | The complete set of user tags the analysis&#39; binary should carry after this call | 

## Example

```python
from revengai.models.update_tags_input_body import UpdateTagsInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTagsInputBody from a JSON string
update_tags_input_body_instance = UpdateTagsInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateTagsInputBody.to_json())

# convert the object into a dict
update_tags_input_body_dict = update_tags_input_body_instance.to_dict()
# create an instance of UpdateTagsInputBody from a dict
update_tags_input_body_from_dict = UpdateTagsInputBody.from_dict(update_tags_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


