# NetworkingExplainResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **bool** | Whether the run was cancelled | 
**data_received** | **str** | Description of the data received | [optional] 
**data_sent** | **str** | Description of the data sent | [optional] 
**data_usage** | **str** | How the sent or received data is used | [optional] 
**endpoints** | **List[str]** | Concrete remote endpoints identified -- IPs, hostnames, or URLs | [optional] 
**function_id** | **int** | ID of the explained function | 
**function_name** | **str** | Name of the explained function | [optional] 
**functions_involved** | [**List[NetworkingExplainedFunction]**](NetworkingExplainedFunction.md) | Other functions involved in the network communication | [optional] 
**protocol** | **str** | Protocol used for the communication | [optional] 
**purpose** | **str** | Purpose of the network communication | [optional] 
**summary** | **str** | Explanation of the network communication the function performs | [optional] 

## Example

```python
from revengai.models.networking_explain_result import NetworkingExplainResult

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingExplainResult from a JSON string
networking_explain_result_instance = NetworkingExplainResult.from_json(json)
# print the JSON string representation of the object
print(NetworkingExplainResult.to_json())

# convert the object into a dict
networking_explain_result_dict = networking_explain_result_instance.to_dict()
# create an instance of NetworkingExplainResult from a dict
networking_explain_result_from_dict = NetworkingExplainResult.from_dict(networking_explain_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


