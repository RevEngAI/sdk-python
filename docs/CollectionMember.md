# CollectionMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**pinned** | **bool** |  | 
**rule_id** | **int** |  | 
**version** | **int** |  | 

## Example

```python
from revengai.models.collection_member import CollectionMember

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionMember from a JSON string
collection_member_instance = CollectionMember.from_json(json)
# print the JSON string representation of the object
print(CollectionMember.to_json())

# convert the object into a dict
collection_member_dict = collection_member_instance.to_dict()
# create an instance of CollectionMember from a dict
collection_member_from_dict = CollectionMember.from_dict(collection_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


