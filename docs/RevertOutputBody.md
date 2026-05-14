# RevertOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 

## Example

```python
from revengai.models.revert_output_body import RevertOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of RevertOutputBody from a JSON string
revert_output_body_instance = RevertOutputBody.from_json(json)
# print the JSON string representation of the object
print(RevertOutputBody.to_json())

# convert the object into a dict
revert_output_body_dict = revert_output_body_instance.to_dict()
# create an instance of RevertOutputBody from a dict
revert_output_body_from_dict = RevertOutputBody.from_dict(revert_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


