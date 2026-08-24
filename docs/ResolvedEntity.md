# ResolvedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addr_token** | **str** |  | 
**all_addr_tokens** | **List[str]** |  | 
**bit_offset** | **int** |  | 
**byte_offset** | **int** |  | 
**byte_size** | **int** |  | 
**count** | **int** |  | 
**data_type_index** | **int** |  | 
**field_status** | **str** |  | [optional] 
**function_id** | **int** |  | [optional] 
**imported_function_id** | **int** |  | [optional] 
**kind** | **str** |  | 
**name** | **str** |  | 
**name_source** | **str** |  | 
**needs_naming** | **bool** |  | 
**provenance** | **str** |  | 
**resolved_name** | **str** |  | 
**suggested_type** | **str** |  | 
**suggestion_confidence** | **str** |  | 
**token** | **str** |  | 
**type_index** | **int** |  | 
**vaddr** | **int** |  | 
**value** | **str** |  | 
**value_confidence** | **str** |  | 
**value_type** | **str** |  | 

## Example

```python
from revengai.models.resolved_entity import ResolvedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedEntity from a JSON string
resolved_entity_instance = ResolvedEntity.from_json(json)
# print the JSON string representation of the object
print(ResolvedEntity.to_json())

# convert the object into a dict
resolved_entity_dict = resolved_entity_instance.to_dict()
# create an instance of ResolvedEntity from a dict
resolved_entity_from_dict = ResolvedEntity.from_dict(resolved_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


