# XRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**xref_to** | **str** |  | 
**is_scalar** | **bool** |  | [optional] 
**is_call** | **bool** |  | [optional] 
**is_data** | **bool** |  | [optional] 
**is_string** | **bool** |  | [optional] 
**raw_data** | **bytearray** |  | [optional] 
**segment** | [**SegmentInfo**](SegmentInfo.md) |  | [optional] 
**orig_str_encoding** | **str** |  | [optional] 

## Example

```python
from revengai.models.x_ref import XRef

# TODO update the JSON string below
json = "{}"
# create an instance of XRef from a JSON string
x_ref_instance = XRef.from_json(json)
# print the JSON string representation of the object
print(XRef.to_json())

# convert the object into a dict
x_ref_dict = x_ref_instance.to_dict()
# create an instance of XRef from a dict
x_ref_from_dict = XRef.from_dict(x_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


