# RunStartedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** |  | [optional] 
**definition_name** | **str** |  | [optional] 

## Example

```python
from revengai.models.run_started_data import RunStartedData

# TODO update the JSON string below
json = "{}"
# create an instance of RunStartedData from a JSON string
run_started_data_instance = RunStartedData.from_json(json)
# print the JSON string representation of the object
print(RunStartedData.to_json())

# convert the object into a dict
run_started_data_dict = run_started_data_instance.to_dict()
# create an instance of RunStartedData from a dict
run_started_data_from_dict = RunStartedData.from_dict(run_started_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


