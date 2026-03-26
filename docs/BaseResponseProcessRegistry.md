# BaseResponseProcessRegistry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ProcessRegistry**](ProcessRegistry.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_process_registry import BaseResponseProcessRegistry

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseProcessRegistry from a JSON string
base_response_process_registry_instance = BaseResponseProcessRegistry.from_json(json)
# print the JSON string representation of the object
print(BaseResponseProcessRegistry.to_json())

# convert the object into a dict
base_response_process_registry_dict = base_response_process_registry_instance.to_dict()
# create an instance of BaseResponseProcessRegistry from a dict
base_response_process_registry_from_dict = BaseResponseProcessRegistry.from_dict(base_response_process_registry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


