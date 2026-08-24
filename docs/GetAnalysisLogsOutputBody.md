# GetAnalysisLogsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[AnalysisLogEntry]**](AnalysisLogEntry.md) | Analysis log lines, oldest first | 

## Example

```python
from revengai.models.get_analysis_logs_output_body import GetAnalysisLogsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnalysisLogsOutputBody from a JSON string
get_analysis_logs_output_body_instance = GetAnalysisLogsOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetAnalysisLogsOutputBody.to_json())

# convert the object into a dict
get_analysis_logs_output_body_dict = get_analysis_logs_output_body_instance.to_dict()
# create an instance of GetAnalysisLogsOutputBody from a dict
get_analysis_logs_output_body_from_dict = GetAnalysisLogsOutputBody.from_dict(get_analysis_logs_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


