# SessionOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Hosted session URL to redirect the user to. | 

## Example

```python
from revengai.models.session_output_body import SessionOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of SessionOutputBody from a JSON string
session_output_body_instance = SessionOutputBody.from_json(json)
# print the JSON string representation of the object
print(SessionOutputBody.to_json())

# convert the object into a dict
session_output_body_dict = session_output_body_instance.to_dict()
# create an instance of SessionOutputBody from a dict
session_output_body_from_dict = SessionOutputBody.from_dict(session_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


