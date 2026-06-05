# CreatePortalSessionInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_url** | **str** | URL the user returns to. | 

## Example

```python
from revengai.models.create_portal_session_input_body import CreatePortalSessionInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePortalSessionInputBody from a JSON string
create_portal_session_input_body_instance = CreatePortalSessionInputBody.from_json(json)
# print the JSON string representation of the object
print(CreatePortalSessionInputBody.to_json())

# convert the object into a dict
create_portal_session_input_body_dict = create_portal_session_input_body_instance.to_dict()
# create an instance of CreatePortalSessionInputBody from a dict
create_portal_session_input_body_from_dict = CreatePortalSessionInputBody.from_dict(create_portal_session_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


