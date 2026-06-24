# UpdateOrganisationInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | New organisation name | 

## Example

```python
from revengai.models.update_organisation_input_body import UpdateOrganisationInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganisationInputBody from a JSON string
update_organisation_input_body_instance = UpdateOrganisationInputBody.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganisationInputBody.to_json())

# convert the object into a dict
update_organisation_input_body_dict = update_organisation_input_body_instance.to_dict()
# create an instance of UpdateOrganisationInputBody from a dict
update_organisation_input_body_from_dict = UpdateOrganisationInputBody.from_dict(update_organisation_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


