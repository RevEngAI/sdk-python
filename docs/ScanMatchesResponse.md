# ScanMatchesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**matches** | [**List[Match]**](Match.md) |  | 
**scan_id** | **int** |  | 

## Example

```python
from revengai.models.scan_matches_response import ScanMatchesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScanMatchesResponse from a JSON string
scan_matches_response_instance = ScanMatchesResponse.from_json(json)
# print the JSON string representation of the object
print(ScanMatchesResponse.to_json())

# convert the object into a dict
scan_matches_response_dict = scan_matches_response_instance.to_dict()
# create an instance of ScanMatchesResponse from a dict
scan_matches_response_from_dict = ScanMatchesResponse.from_dict(scan_matches_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


