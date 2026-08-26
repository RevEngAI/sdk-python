# SecurityScanMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first. | [optional] 
**status** | **str** | Run status. UNINITIALISED means the agent has never been triggered for this analysis. | 

## Example

```python
from revengai.models.security_scan_metadata import SecurityScanMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityScanMetadata from a JSON string
security_scan_metadata_instance = SecurityScanMetadata.from_json(json)
# print the JSON string representation of the object
print(SecurityScanMetadata.to_json())

# convert the object into a dict
security_scan_metadata_dict = security_scan_metadata_instance.to_dict()
# create an instance of SecurityScanMetadata from a dict
security_scan_metadata_from_dict = SecurityScanMetadata.from_dict(security_scan_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


