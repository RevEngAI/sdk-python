# AddCalleeInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callee_function_id** | **int** | Internal callee function ID; 0 means not provided | [optional] 
**callee_name** | **str** | Callee name (for external calls) | [optional] 
**callee_vaddr** | **int** | Virtual address of the callee | 
**is_external** | **bool** | Whether the callee is outside the binary | 
**thunked_vaddr** | **int** | Thunked virtual address | [optional] 

## Example

```python
from revengai.models.add_callee_input_body import AddCalleeInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddCalleeInputBody from a JSON string
add_callee_input_body_instance = AddCalleeInputBody.from_json(json)
# print the JSON string representation of the object
print(AddCalleeInputBody.to_json())

# convert the object into a dict
add_callee_input_body_dict = add_callee_input_body_instance.to_dict()
# create an instance of AddCalleeInputBody from a dict
add_callee_input_body_from_dict = AddCalleeInputBody.from_dict(add_callee_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


