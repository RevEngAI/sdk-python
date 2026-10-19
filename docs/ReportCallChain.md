# ReportCallChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[int]** | Call addresses along the path, entry point first. | 

## Example

```python
from revengai.models.report_call_chain import ReportCallChain

# TODO update the JSON string below
json = "{}"
# create an instance of ReportCallChain from a JSON string
report_call_chain_instance = ReportCallChain.from_json(json)
# print the JSON string representation of the object
print(ReportCallChain.to_json())

# convert the object into a dict
report_call_chain_dict = report_call_chain_instance.to_dict()
# create an instance of ReportCallChain from a dict
report_call_chain_from_dict = ReportCallChain.from_dict(report_call_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


