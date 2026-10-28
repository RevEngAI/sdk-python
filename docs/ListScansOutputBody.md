# ListScansOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**scans** | [**List[ScanSummary]**](ScanSummary.md) |  | 

## Example

```python
from revengai.models.list_scans_output_body import ListScansOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListScansOutputBody from a JSON string
list_scans_output_body_instance = ListScansOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListScansOutputBody.to_json())

# convert the object into a dict
list_scans_output_body_dict = list_scans_output_body_instance.to_dict()
# create an instance of ListScansOutputBody from a dict
list_scans_output_body_from_dict = ListScansOutputBody.from_dict(list_scans_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


