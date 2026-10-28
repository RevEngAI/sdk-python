# RunErrorData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_uuid** | **str** |  | [optional] 
**definition_name** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from revengai.models.run_error_data import RunErrorData

# TODO update the JSON string below
json = "{}"
# create an instance of RunErrorData from a JSON string
run_error_data_instance = RunErrorData.from_json(json)
# print the JSON string representation of the object
print(RunErrorData.to_json())

# convert the object into a dict
run_error_data_dict = run_error_data_instance.to_dict()
# create an instance of RunErrorData from a dict
run_error_data_from_dict = RunErrorData.from_dict(run_error_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


