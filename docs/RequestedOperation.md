# RequestedOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** |  | 

## Example

```python
from revengai.models.requested_operation import RequestedOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedOperation from a JSON string
requested_operation_instance = RequestedOperation.from_json(json)
# print the JSON string representation of the object
print(RequestedOperation.to_json())

# convert the object into a dict
requested_operation_dict = requested_operation_instance.to_dict()
# create an instance of RequestedOperation from a dict
requested_operation_from_dict = RequestedOperation.from_dict(requested_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


