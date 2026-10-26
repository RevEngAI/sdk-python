# OperationPrerequisitesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The operation | 
**prerequisites** | **List[str]** | Operations that must complete before this operation can start | 

## Example

```python
from revengai.models.operation_prerequisites_body import OperationPrerequisitesBody

# TODO update the JSON string below
json = "{}"
# create an instance of OperationPrerequisitesBody from a JSON string
operation_prerequisites_body_instance = OperationPrerequisitesBody.from_json(json)
# print the JSON string representation of the object
print(OperationPrerequisitesBody.to_json())

# convert the object into a dict
operation_prerequisites_body_dict = operation_prerequisites_body_instance.to_dict()
# create an instance of OperationPrerequisitesBody from a dict
operation_prerequisites_body_from_dict = OperationPrerequisitesBody.from_dict(operation_prerequisites_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


