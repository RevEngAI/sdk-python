# NetworkingScanResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis the run was performed against | 
**findings** | [**List[NetworkingFinding]**](NetworkingFinding.md) | Functions with networking-related evidence, sorted by remoteness then confidence then evidence count | [optional] 
**total_functions** | **int** | Functions the run considered | 

## Example

```python
from revengai.models.networking_scan_result import NetworkingScanResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingScanResult from a JSON string
networking_scan_result_instance = NetworkingScanResult.from_json(json)
# print the JSON string representation of the object
print(NetworkingScanResult.to_json())

# convert the object into a dict
networking_scan_result_dict = networking_scan_result_instance.to_dict()
# create an instance of NetworkingScanResult from a dict
networking_scan_result_from_dict = NetworkingScanResult.from_dict(networking_scan_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


