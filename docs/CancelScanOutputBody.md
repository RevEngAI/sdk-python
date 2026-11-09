# CancelScanOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**scan_id** | **int** |  | 
**status** | **str** |  | 

## Example

```python
from revengai.models.cancel_scan_output_body import CancelScanOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CancelScanOutputBody from a JSON string
cancel_scan_output_body_instance = CancelScanOutputBody.from_json(json)
# print the JSON string representation of the object
print(CancelScanOutputBody.to_json())

# convert the object into a dict
cancel_scan_output_body_dict = cancel_scan_output_body_instance.to_dict()
# create an instance of CancelScanOutputBody from a dict
cancel_scan_output_body_from_dict = CancelScanOutputBody.from_dict(cancel_scan_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


