# CallEdgesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**List[FunctionCallEdges]**](FunctionCallEdges.md) |  | 

## Example

```python
from revengai.models.call_edges_output_body import CallEdgesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CallEdgesOutputBody from a JSON string
call_edges_output_body_instance = CallEdgesOutputBody.from_json(json)
# print the JSON string representation of the object
print(CallEdgesOutputBody.to_json())

# convert the object into a dict
call_edges_output_body_dict = call_edges_output_body_instance.to_dict()
# create an instance of CallEdgesOutputBody from a dict
call_edges_output_body_from_dict = CallEdgesOutputBody.from_dict(call_edges_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


