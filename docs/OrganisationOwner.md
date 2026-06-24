# OrganisationOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**organisation_id** | **int** |  | 
**organisation_owner_id** | **int** |  | 
**user_id** | **int** |  | 

## Example

```python
from revengai.models.organisation_owner import OrganisationOwner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganisationOwner from a JSON string
organisation_owner_instance = OrganisationOwner.from_json(json)
# print the JSON string representation of the object
print(OrganisationOwner.to_json())

# convert the object into a dict
organisation_owner_dict = organisation_owner_instance.to_dict()
# create an instance of OrganisationOwner from a dict
organisation_owner_from_dict = OrganisationOwner.from_dict(organisation_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


