# ReportModelInterpretation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interpretation** | **str** | The interpretation, or null when the model did not provide one. | 

## Example

```python
from revengai.models.report_model_interpretation import ReportModelInterpretation

# TODO update the JSON string below
json = "{}"
# create an instance of ReportModelInterpretation from a JSON string
report_model_interpretation_instance = ReportModelInterpretation.from_json(json)
# print the JSON string representation of the object
print(ReportModelInterpretation.to_json())

# convert the object into a dict
report_model_interpretation_dict = report_model_interpretation_instance.to_dict()
# create an instance of ReportModelInterpretation from a dict
report_model_interpretation_from_dict = ReportModelInterpretation.from_dict(report_model_interpretation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


