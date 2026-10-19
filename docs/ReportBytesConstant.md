# ReportBytesConstant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** | Suggested format for displaying the value. | 
**format** | **str** | Encoding of the value. | 
**value** | **str** | The bytes of the constant, hex-encoded. | 

## Example

```python
from revengai.models.report_bytes_constant import ReportBytesConstant

# TODO update the JSON string below
json = "{}"
# create an instance of ReportBytesConstant from a JSON string
report_bytes_constant_instance = ReportBytesConstant.from_json(json)
# print the JSON string representation of the object
print(ReportBytesConstant.to_json())

# convert the object into a dict
report_bytes_constant_dict = report_bytes_constant_instance.to_dict()
# create an instance of ReportBytesConstant from a dict
report_bytes_constant_from_dict = ReportBytesConstant.from_dict(report_bytes_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


