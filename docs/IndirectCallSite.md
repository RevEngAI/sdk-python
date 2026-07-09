# IndirectCallSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callee_function_id** | **int** |  | [optional] 
**inst_vaddr** | **int** | Vaddr of the indirect call instruction. | 
**is_external** | **bool** |  | 
**target_name** | **str** |  | [optional] 
**target_vaddr** | **int** | Resolved call target vaddr. | 

## Example

```python
from revengai.models.indirect_call_site import IndirectCallSite

# TODO update the JSON string below
json = "{}"
# create an instance of IndirectCallSite from a JSON string
indirect_call_site_instance = IndirectCallSite.from_json(json)
# print the JSON string representation of the object
print(IndirectCallSite.to_json())

# convert the object into a dict
indirect_call_site_dict = indirect_call_site_instance.to_dict()
# create an instance of IndirectCallSite from a dict
indirect_call_site_from_dict = IndirectCallSite.from_dict(indirect_call_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


