# ListTeamsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**teams** | [**List[Team]**](Team.md) |  | 
**total** | **int** |  | 

## Example

```python
from revengai.models.list_teams_output_body import ListTeamsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListTeamsOutputBody from a JSON string
list_teams_output_body_instance = ListTeamsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListTeamsOutputBody.to_json())

# convert the object into a dict
list_teams_output_body_dict = list_teams_output_body_instance.to_dict()
# create an instance of ListTeamsOutputBody from a dict
list_teams_output_body_from_dict = ListTeamsOutputBody.from_dict(list_teams_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


