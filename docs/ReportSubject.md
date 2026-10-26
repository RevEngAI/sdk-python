# ReportSubject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**call_site** | **int** | Call-site address. | [optional] 
**data** | **int** | Data address. | [optional] 
**function** | **int** | Function entry address. | [optional] 
**instruction** | **int** | Instruction address. | [optional] 

## Example

```python
from revengai.models.report_subject import ReportSubject

# TODO update the JSON string below
json = "{}"
# create an instance of ReportSubject from a JSON string
report_subject_instance = ReportSubject.from_json(json)
# print the JSON string representation of the object
print(ReportSubject.to_json())

# convert the object into a dict
report_subject_dict = report_subject_instance.to_dict()
# create an instance of ReportSubject from a dict
report_subject_from_dict = ReportSubject.from_dict(report_subject_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


