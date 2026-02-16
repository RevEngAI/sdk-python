# InsertAnalysisLogRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **str** | The log message to insert for the analysis | 

## Example

```python
from revengai.models.insert_analysis_log_request import InsertAnalysisLogRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InsertAnalysisLogRequest from a JSON string
insert_analysis_log_request_instance = InsertAnalysisLogRequest.from_json(json)
# print the JSON string representation of the object
print(InsertAnalysisLogRequest.to_json())

# convert the object into a dict
insert_analysis_log_request_dict = insert_analysis_log_request_instance.to_dict()
# create an instance of InsertAnalysisLogRequest from a dict
insert_analysis_log_request_from_dict = InsertAnalysisLogRequest.from_dict(insert_analysis_log_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


