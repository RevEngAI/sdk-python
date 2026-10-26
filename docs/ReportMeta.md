# ReportMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endianness** | **str** | Byte order of the analysed binary. | 

## Example

```python
from revengai.models.report_meta import ReportMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ReportMeta from a JSON string
report_meta_instance = ReportMeta.from_json(json)
# print the JSON string representation of the object
print(ReportMeta.to_json())

# convert the object into a dict
report_meta_dict = report_meta_instance.to_dict()
# create an instance of ReportMeta from a dict
report_meta_from_dict = ReportMeta.from_dict(report_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


