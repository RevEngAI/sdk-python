# PublicTeamBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_id** | **int** | The team&#39;s ID | 
**team_name** | **str** | The team&#39;s name | 

## Example

```python
from revengai.models.public_team_body import PublicTeamBody

# TODO update the JSON string below
json = "{}"
# create an instance of PublicTeamBody from a JSON string
public_team_body_instance = PublicTeamBody.from_json(json)
# print the JSON string representation of the object
print(PublicTeamBody.to_json())

# convert the object into a dict
public_team_body_dict = public_team_body_instance.to_dict()
# create an instance of PublicTeamBody from a dict
public_team_body_from_dict = PublicTeamBody.from_dict(public_team_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


