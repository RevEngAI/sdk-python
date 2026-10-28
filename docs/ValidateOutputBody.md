# ValidateOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**results** | [**List[RuleValidation]**](RuleValidation.md) |  | 

## Example

```python
from revengai.models.validate_output_body import ValidateOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateOutputBody from a JSON string
validate_output_body_instance = ValidateOutputBody.from_json(json)
# print the JSON string representation of the object
print(ValidateOutputBody.to_json())

# convert the object into a dict
validate_output_body_dict = validate_output_body_instance.to_dict()
# create an instance of ValidateOutputBody from a dict
validate_output_body_from_dict = ValidateOutputBody.from_dict(validate_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


