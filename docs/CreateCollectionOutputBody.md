# CreateCollectionOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaries** | [**List[Binary]**](Binary.md) |  | [optional] 
**collection_id** | **int** |  | 
**collection_name** | **str** |  | 
**collection_scope** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | 
**tags** | **List[str]** |  | [optional] 
**team_id** | **int** |  | 
**updated_at** | **datetime** |  | 
**user_id** | **int** |  | 

## Example

```python
from revengai.models.create_collection_output_body import CreateCollectionOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollectionOutputBody from a JSON string
create_collection_output_body_instance = CreateCollectionOutputBody.from_json(json)
# print the JSON string representation of the object
print(CreateCollectionOutputBody.to_json())

# convert the object into a dict
create_collection_output_body_dict = create_collection_output_body_instance.to_dict()
# create an instance of CreateCollectionOutputBody from a dict
create_collection_output_body_from_dict = CreateCollectionOutputBody.from_dict(create_collection_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


