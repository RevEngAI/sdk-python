# AppApiRestV2InfoTypesCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_name** | **str** | The name of the function with a capability | 
**function_vaddr** | **int** | The virtual address of the function where the capability comes from | 
**capabilities** | **List[str]** | The list of capabilities associated with the function | 

## Example

```python
from revengai.models.app_api_rest_v2_info_types_capability import AppApiRestV2InfoTypesCapability

# TODO update the JSON string below
json = "{}"
# create an instance of AppApiRestV2InfoTypesCapability from a JSON string
app_api_rest_v2_info_types_capability_instance = AppApiRestV2InfoTypesCapability.from_json(json)
# print the JSON string representation of the object
print(AppApiRestV2InfoTypesCapability.to_json())

# convert the object into a dict
app_api_rest_v2_info_types_capability_dict = app_api_rest_v2_info_types_capability_instance.to_dict()
# create an instance of AppApiRestV2InfoTypesCapability from a dict
app_api_rest_v2_info_types_capability_from_dict = AppApiRestV2InfoTypesCapability.from_dict(app_api_rest_v2_info_types_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


