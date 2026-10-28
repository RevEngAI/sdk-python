# CreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_config** | [**Config**](Config.md) |  | [optional] 
**analysis_scope** | **str** |  | [optional] [default to 'PRIVATE']
**binary_config** | [**BinaryConfig**](BinaryConfig.md) |  | [optional] 
**debug_hash** | **str** |  | [optional] 
**filename** | **str** |  | 
**investigation_id** | **int** | Adds the new analysis to this investigation, which you must own. | [optional] 
**operations** | [**List[RequestedOperation]**](RequestedOperation.md) | Operations to run automatically once the analysis completes. Each operation&#39;s prerequisites must also be requested. | [optional] 
**sha_256_hash** | **str** |  | 
**symbols** | [**Symbols**](Symbols.md) |  | [optional] 
**tags** | **List[str]** |  | [optional] 

## Example

```python
from revengai.models.create_request import CreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequest from a JSON string
create_request_instance = CreateRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRequest.to_json())

# convert the object into a dict
create_request_dict = create_request_instance.to_dict()
# create an instance of CreateRequest from a dict
create_request_from_dict = CreateRequest.from_dict(create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


