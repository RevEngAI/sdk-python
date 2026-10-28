# PrincipalBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The user or team&#39;s ID | 
**name** | **str** | The user&#39;s username or the team&#39;s name | 
**type** | **str** | Whether this result is a user or a team | 

## Example

```python
from revengai.models.principal_body import PrincipalBody

# TODO update the JSON string below
json = "{}"
# create an instance of PrincipalBody from a JSON string
principal_body_instance = PrincipalBody.from_json(json)
# print the JSON string representation of the object
print(PrincipalBody.to_json())

# convert the object into a dict
principal_body_dict = principal_body_instance.to_dict()
# create an instance of PrincipalBody from a dict
principal_body_from_dict = PrincipalBody.from_dict(principal_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


