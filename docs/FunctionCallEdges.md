# FunctionCallEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callees** | [**List[CallEdge]**](CallEdge.md) |  | 
**callers** | [**List[CallEdge]**](CallEdge.md) |  | 
**function_id** | **int** |  | 

## Example

```python
from revengai.models.function_call_edges import FunctionCallEdges

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionCallEdges from a JSON string
function_call_edges_instance = FunctionCallEdges.from_json(json)
# print the JSON string representation of the object
print(FunctionCallEdges.to_json())

# convert the object into a dict
function_call_edges_dict = function_call_edges_instance.to_dict()
# create an instance of FunctionCallEdges from a dict
function_call_edges_from_dict = FunctionCallEdges.from_dict(function_call_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


