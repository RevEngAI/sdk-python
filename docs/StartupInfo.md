# StartupInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **str** |  | [optional] 
**error** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**pid** | **int** |  | [optional] 
**process** | **int** |  | [optional] 
**process_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from revengai.models.startup_info import StartupInfo

# TODO update the JSON string below
json = "{}"
# create an instance of StartupInfo from a JSON string
startup_info_instance = StartupInfo.from_json(json)
# print the JSON string representation of the object
print(StartupInfo.to_json())

# convert the object into a dict
startup_info_dict = startup_info_instance.to_dict()
# create an instance of StartupInfo from a dict
startup_info_from_dict = StartupInfo.from_dict(startup_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


