# DynamicExecutionStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error detail, set when status is ERROR | [optional] 
**status** | **str** | Task status: UNINITIALISED, PENDING, RUNNING, COMPLETED, or ERROR | 

## Example

```python
from revengai.models.dynamic_execution_status_response import DynamicExecutionStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicExecutionStatusResponse from a JSON string
dynamic_execution_status_response_instance = DynamicExecutionStatusResponse.from_json(json)
# print the JSON string representation of the object
print(DynamicExecutionStatusResponse.to_json())

# convert the object into a dict
dynamic_execution_status_response_dict = dynamic_execution_status_response_instance.to_dict()
# create an instance of DynamicExecutionStatusResponse from a dict
dynamic_execution_status_response_from_dict = DynamicExecutionStatusResponse.from_dict(dynamic_execution_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


