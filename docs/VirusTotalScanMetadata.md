# VirusTotalScanMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Lookup status. UNINITIALISED means this binary has never had a lookup triggered. | 

## Example

```python
from revengai.models.virus_total_scan_metadata import VirusTotalScanMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of VirusTotalScanMetadata from a JSON string
virus_total_scan_metadata_instance = VirusTotalScanMetadata.from_json(json)
# print the JSON string representation of the object
print(VirusTotalScanMetadata.to_json())

# convert the object into a dict
virus_total_scan_metadata_dict = virus_total_scan_metadata_instance.to_dict()
# create an instance of VirusTotalScanMetadata from a dict
virus_total_scan_metadata_from_dict = VirusTotalScanMetadata.from_dict(virus_total_scan_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


