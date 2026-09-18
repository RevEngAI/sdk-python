# Metadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first, empty until the run logs anything. Each entry is a [timestamp, message] pair. | 
**status** | **str** | Run status. UNINITIALISED means this agent has never been triggered for the analysis, so it is safe to start one. | 

## Example

```python
from revengai.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


