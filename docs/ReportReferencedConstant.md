# ReportReferencedConstant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** | Suggested format for displaying the value at this reference, absent to use the constant&#39;s own. | [optional] 
**subject** | [**ReportSubject**](ReportSubject.md) | Where the constant is referenced. | 
**value** | [**ReportBytesConstant**](ReportBytesConstant.md) | The constant. | 

## Example

```python
from revengai.models.report_referenced_constant import ReportReferencedConstant

# TODO update the JSON string below
json = "{}"
# create an instance of ReportReferencedConstant from a JSON string
report_referenced_constant_instance = ReportReferencedConstant.from_json(json)
# print the JSON string representation of the object
print(ReportReferencedConstant.to_json())

# convert the object into a dict
report_referenced_constant_dict = report_referenced_constant_instance.to_dict()
# create an instance of ReportReferencedConstant from a dict
report_referenced_constant_from_dict = ReportReferencedConstant.from_dict(report_referenced_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


