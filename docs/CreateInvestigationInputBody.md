# CreateInvestigationInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_type** | **str** |  | 
**name** | **str** | Investigation name. Must contain a non-whitespace character. | 
**scope** | **str** | PRIVATE is visible only to you, TEAM to your whole team. Only you can modify it either way. | [optional] [default to 'PRIVATE']
**severity** | **str** | Initial severity. | 

## Example

```python
from revengai.models.create_investigation_input_body import CreateInvestigationInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInvestigationInputBody from a JSON string
create_investigation_input_body_instance = CreateInvestigationInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateInvestigationInputBody.to_json())

# convert the object into a dict
create_investigation_input_body_dict = create_investigation_input_body_instance.to_dict()
# create an instance of CreateInvestigationInputBody from a dict
create_investigation_input_body_from_dict = CreateInvestigationInputBody.from_dict(create_investigation_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


