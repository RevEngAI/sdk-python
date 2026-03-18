# XrefToResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**is_scalar** | **bool** |  | [optional] 
**is_call** | **bool** |  | [optional] 
**is_data** | **bool** |  | [optional] 
**is_string** | **bool** |  | [optional] 
**raw_data** | **str** |  | [optional] 
**segment** | [**SegmentInfo**](SegmentInfo.md) |  | [optional] 
**orig_str_encoding** | **str** |  | [optional] 
**xref_from** | **str** |  | 

## Example

```python
from revengai.models.xref_to_response import XrefToResponse

# TODO update the JSON string below
json = "{}"
# create an instance of XrefToResponse from a JSON string
xref_to_response_instance = XrefToResponse.from_json(json)
# print the JSON string representation of the object
print(XrefToResponse.to_json())

# convert the object into a dict
xref_to_response_dict = xref_to_response_instance.to_dict()
# create an instance of XrefToResponse from a dict
xref_to_response_from_dict = XrefToResponse.from_dict(xref_to_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


