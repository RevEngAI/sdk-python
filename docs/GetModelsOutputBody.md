# GetModelsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **List[str]** | Models a new analysis may be run on | 

## Example

```python
from revengai.models.get_models_output_body import GetModelsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetModelsOutputBody from a JSON string
get_models_output_body_instance = GetModelsOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetModelsOutputBody.to_json())

# convert the object into a dict
get_models_output_body_dict = get_models_output_body_instance.to_dict()
# create an instance of GetModelsOutputBody from a dict
get_models_output_body_from_dict = GetModelsOutputBody.from_dict(get_models_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


