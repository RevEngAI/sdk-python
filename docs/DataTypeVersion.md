# DataTypeVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | When this version was written. Absent on a version that predates the recorded history. | [optional] 
**updated_by** | [**HistoryActor**](HistoryActor.md) | Who wrote this version. Absent on a version that predates the recorded history. | [optional] 
**value** | [**DataTypeEntry**](DataTypeEntry.md) | The type as it stood in this version. | 

## Example

```python
from revengai.models.data_type_version import DataTypeVersion

# TODO update the JSON string below
json = "{}"
# create an instance of DataTypeVersion from a JSON string
data_type_version_instance = DataTypeVersion.from_json(json)
# print the JSON string representation of the object
print(DataTypeVersion.to_json())

# convert the object into a dict
data_type_version_dict = data_type_version_instance.to_dict()
# create an instance of DataTypeVersion from a dict
data_type_version_from_dict = DataTypeVersion.from_dict(data_type_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


