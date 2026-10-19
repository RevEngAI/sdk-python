# ListOperationPrerequisitesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[OperationPrerequisitesBody]**](OperationPrerequisitesBody.md) | Operations that have prerequisites | 

## Example

```python
from revengai.models.list_operation_prerequisites_output_body import ListOperationPrerequisitesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListOperationPrerequisitesOutputBody from a JSON string
list_operation_prerequisites_output_body_instance = ListOperationPrerequisitesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListOperationPrerequisitesOutputBody.to_json())

# convert the object into a dict
list_operation_prerequisites_output_body_dict = list_operation_prerequisites_output_body_instance.to_dict()
# create an instance of ListOperationPrerequisitesOutputBody from a dict
list_operation_prerequisites_output_body_from_dict = ListOperationPrerequisitesOutputBody.from_dict(list_operation_prerequisites_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


