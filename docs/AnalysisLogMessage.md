# AnalysisLogMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**time** | **str** |  | 

## Example

```python
from revengai.models.analysis_log_message import AnalysisLogMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AnalysisLogMessage from a JSON string
analysis_log_message_instance = AnalysisLogMessage.from_json(json)
# print the JSON string representation of the object
print(AnalysisLogMessage.to_json())

# convert the object into a dict
analysis_log_message_dict = analysis_log_message_instance.to_dict()
# create an instance of AnalysisLogMessage from a dict
analysis_log_message_from_dict = AnalysisLogMessage.from_dict(analysis_log_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


