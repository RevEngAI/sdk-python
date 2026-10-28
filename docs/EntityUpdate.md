# EntityUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**refs** | [**List[EntityRef]**](EntityRef.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from revengai.models.entity_update import EntityUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of EntityUpdate from a JSON string
entity_update_instance = EntityUpdate.from_json(json)
# print the JSON string representation of the object
print(EntityUpdate.to_json())

# convert the object into a dict
entity_update_dict = entity_update_instance.to_dict()
# create an instance of EntityUpdate from a dict
entity_update_from_dict = EntityUpdate.from_dict(entity_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


