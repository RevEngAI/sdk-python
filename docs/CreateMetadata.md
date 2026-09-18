# CreateMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis ID | 
**binary_id** | **int** | Binary ID | 
**status** | **str** | Analysis status | 

## Example

```python
from revengai.models.create_metadata import CreateMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMetadata from a JSON string
create_metadata_instance = CreateMetadata.from_json(json)
# print the JSON string representation of the object
print(CreateMetadata.to_json())

# convert the object into a dict
create_metadata_dict = create_metadata_instance.to_dict()
# create an instance of CreateMetadata from a dict
create_metadata_from_dict = CreateMetadata.from_dict(create_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


