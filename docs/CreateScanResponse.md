# CreateScanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**result** | [**ScanResult**](ScanResult.md) | Inline result for a synchronous scan | [optional] 
**run_mode** | **str** |  | 
**scan_id** | **int** |  | 
**status** | **str** |  | 
**workflow_id** | **str** |  | [optional] 

## Example

```python
from revengai.models.create_scan_response import CreateScanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScanResponse from a JSON string
create_scan_response_instance = CreateScanResponse.from_json(json)
# print the JSON string representation of the object
print(CreateScanResponse.to_json())

# convert the object into a dict
create_scan_response_dict = create_scan_response_instance.to_dict()
# create an instance of CreateScanResponse from a dict
create_scan_response_from_dict = CreateScanResponse.from_dict(create_scan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


