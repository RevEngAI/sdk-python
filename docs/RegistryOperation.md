# RegistryOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**key** | **str** |  | 

## Example

```python
from revengai.models.registry_operation import RegistryOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryOperation from a JSON string
registry_operation_instance = RegistryOperation.from_json(json)
# print the JSON string representation of the object
print(RegistryOperation.to_json())

# convert the object into a dict
registry_operation_dict = registry_operation_instance.to_dict()
# create an instance of RegistryOperation from a dict
registry_operation_from_dict = RegistryOperation.from_dict(registry_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


