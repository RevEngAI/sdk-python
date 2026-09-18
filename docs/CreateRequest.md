# CreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_config** | [**Config**](Config.md) |  | [optional] 
**analysis_scope** | **str** |  | [optional] [default to 'PRIVATE']
**auto_run_agents** | [**AutoRunAgents**](AutoRunAgents.md) |  | [optional] 
**binary_config** | [**BinaryConfig**](BinaryConfig.md) |  | [optional] 
**debug_hash** | **str** |  | [optional] 
**filename** | **str** |  | 
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


