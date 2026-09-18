# NetworkingExplainMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first. | [optional] 
**status** | **str** | Run status. UNINITIALISED means the agent has never been triggered for this function. | 

## Example

```python
from revengai.models.networking_explain_metadata import NetworkingExplainMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingExplainMetadata from a JSON string
networking_explain_metadata_instance = NetworkingExplainMetadata.from_json(json)
# print the JSON string representation of the object
print(NetworkingExplainMetadata.to_json())

# convert the object into a dict
networking_explain_metadata_dict = networking_explain_metadata_instance.to_dict()
# create an instance of NetworkingExplainMetadata from a dict
networking_explain_metadata_from_dict = NetworkingExplainMetadata.from_dict(networking_explain_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


