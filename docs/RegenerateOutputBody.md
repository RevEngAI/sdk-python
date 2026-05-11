# RegenerateOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**status** | **bool** |  | 

## Example

```python
from revengai.models.regenerate_output_body import RegenerateOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of RegenerateOutputBody from a JSON string
regenerate_output_body_instance = RegenerateOutputBody.from_json(json)
# print the JSON string representation of the object
print(RegenerateOutputBody.to_json())

# convert the object into a dict
regenerate_output_body_dict = regenerate_output_body_instance.to_dict()
# create an instance of RegenerateOutputBody from a dict
regenerate_output_body_from_dict = RegenerateOutputBody.from_dict(regenerate_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


