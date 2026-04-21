# AppApiRestV2AgentSchemaCapability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_vaddr** | **str** | Vaddr of the function containing the capability | 
**description** | **str** | Description of the capability | 
**capability** | **str** | Name of the capability | 
**type** | **str** | Type of the capability | 
**function_name** | **str** | Name of the function containing the capability | 
**function_id** | **int** | ID of the function containing the capability | 

## Example

```python
from revengai.models.app_api_rest_v2_agent_schema_capability import AppApiRestV2AgentSchemaCapability

# TODO update the JSON string below
json = "{}"
# create an instance of AppApiRestV2AgentSchemaCapability from a JSON string
app_api_rest_v2_agent_schema_capability_instance = AppApiRestV2AgentSchemaCapability.from_json(json)
# print the JSON string representation of the object
print(AppApiRestV2AgentSchemaCapability.to_json())

# convert the object into a dict
app_api_rest_v2_agent_schema_capability_dict = app_api_rest_v2_agent_schema_capability_instance.to_dict()
# create an instance of AppApiRestV2AgentSchemaCapability from a dict
app_api_rest_v2_agent_schema_capability_from_dict = AppApiRestV2AgentSchemaCapability.from_dict(app_api_rest_v2_agent_schema_capability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


