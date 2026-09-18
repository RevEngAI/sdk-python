# TriggerExecutionExplainInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Execution category to focus the explanation on. | 

## Example

```python
from revengai.models.trigger_execution_explain_input_body import TriggerExecutionExplainInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerExecutionExplainInputBody from a JSON string
trigger_execution_explain_input_body_instance = TriggerExecutionExplainInputBody.from_json(json)
# print the JSON string representation of the object
print(TriggerExecutionExplainInputBody.to_json())

# convert the object into a dict
trigger_execution_explain_input_body_dict = trigger_execution_explain_input_body_instance.to_dict()
# create an instance of TriggerExecutionExplainInputBody from a dict
trigger_execution_explain_input_body_from_dict = TriggerExecutionExplainInputBody.from_dict(trigger_execution_explain_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


