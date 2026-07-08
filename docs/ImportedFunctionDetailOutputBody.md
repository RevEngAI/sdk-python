# ImportedFunctionDetailOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callers** | [**List[ImportedFunctionCallerEntry]**](ImportedFunctionCallerEntry.md) | Internal functions that call this import, resolved via its PLT/stub addresses. | 
**imported_function_id** | **int** |  | 
**is_function** | **bool** | False for imported data symbols. | 
**library_name** | **str** | Library the symbol is imported from. &#39;&lt;EXTERNAL&gt;&#39; for unattributed imports. | 
**library_version** | **str** | Versioned symbol tag, when the loader records one. | [optional] 
**name** | **str** |  | 
**original_name** | **str** | Pre-demangling / pre-aliasing name, when it differs from name. | [optional] 
**stub_vaddrs** | **List[int]** | PLT/stub addresses that resolve external call edges (function_call_edges.callee_vaddr) to this import. Use these to link a caller&#39;s external callee to this import. | 
**vaddr** | **int** | Virtual address of the import, when known. | [optional] 

## Example

```python
from revengai.models.imported_function_detail_output_body import ImportedFunctionDetailOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedFunctionDetailOutputBody from a JSON string
imported_function_detail_output_body_instance = ImportedFunctionDetailOutputBody.from_json(json)
# print the JSON string representation of the object
print(ImportedFunctionDetailOutputBody.to_json())

# convert the object into a dict
imported_function_detail_output_body_dict = imported_function_detail_output_body_instance.to_dict()
# create an instance of ImportedFunctionDetailOutputBody from a dict
imported_function_detail_output_body_from_dict = ImportedFunctionDetailOutputBody.from_dict(imported_function_detail_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


