# DatasetInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**file_count** | **int** | Object count; omitted for discovered datasets (counted on scan) | [optional] 
**name** | **str** |  | 

## Example

```python
from revengai.models.dataset_info import DatasetInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetInfo from a JSON string
dataset_info_instance = DatasetInfo.from_json(json)
# print the JSON string representation of the object
print(DatasetInfo.to_json())

# convert the object into a dict
dataset_info_dict = dataset_info_instance.to_dict()
# create an instance of DatasetInfo from a dict
dataset_info_from_dict = DatasetInfo.from_dict(dataset_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


