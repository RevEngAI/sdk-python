# OrganisationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**name** | **str** |  | 
**organisation_group_id** | **int** |  | 
**organisation_id** | **int** |  | 
**team_id** | **int** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from revengai.models.organisation_group import OrganisationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of OrganisationGroup from a JSON string
organisation_group_instance = OrganisationGroup.from_json(json)
# print the JSON string representation of the object
print(OrganisationGroup.to_json())

# convert the object into a dict
organisation_group_dict = organisation_group_instance.to_dict()
# create an instance of OrganisationGroup from a dict
organisation_group_from_dict = OrganisationGroup.from_dict(organisation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


