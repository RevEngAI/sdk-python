# CallEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callee_function_id** | **int** |  | [optional] 
**callee_name** | **str** |  | [optional] 
**callee_vaddr** | **int** |  | 
**caller_function_id** | **int** |  | 
**caller_name** | **str** |  | [optional] 
**caller_vaddr** | **int** | Entry vaddr of the caller function (joined from function_t). | 
**imported_function_id** | **int** | Imported function ID for an external callee, resolved via the thunk/stub address. | [optional] 
**is_external** | **bool** |  | 
**thunked_vaddr** | **int** |  | [optional] 

## Example

```python
from revengai.models.call_edge import CallEdge

# TODO update the JSON string below
json = "{}"
# create an instance of CallEdge from a JSON string
call_edge_instance = CallEdge.from_json(json)
# print the JSON string representation of the object
print(CallEdge.to_json())

# convert the object into a dict
call_edge_dict = call_edge_instance.to_dict()
# create an instance of CallEdge from a dict
call_edge_from_dict = CallEdge.from_dict(call_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


