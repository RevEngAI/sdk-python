# CreateOrganisationInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Organisation name | 

## Example

```python
from revengai.models.create_organisation_input_body import CreateOrganisationInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganisationInputBody from a JSON string
create_organisation_input_body_instance = CreateOrganisationInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateOrganisationInputBody.to_json())

# convert the object into a dict
create_organisation_input_body_dict = create_organisation_input_body_instance.to_dict()
# create an instance of CreateOrganisationInputBody from a dict
create_organisation_input_body_from_dict = CreateOrganisationInputBody.from_dict(create_organisation_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


