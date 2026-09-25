# XrefSegmentBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **int** | End address of the segment, inclusive | 
**var_exec** | **bool** | True when the segment is executable | 
**kind** | **str** | Coarse classification of the segment | 
**name** | **str** | Segment name | 
**read** | **bool** | True when the segment is readable | 
**start** | **int** | Start address of the segment | 
**write** | **bool** | True when the segment is writable | 

## Example

```python
from revengai.models.xref_segment_body import XrefSegmentBody

# TODO update the JSON string below
json = "{}"
# create an instance of XrefSegmentBody from a JSON string
xref_segment_body_instance = XrefSegmentBody.from_json(json)
# print the JSON string representation of the object
print(XrefSegmentBody.to_json())

# convert the object into a dict
xref_segment_body_dict = xref_segment_body_instance.to_dict()
# create an instance of XrefSegmentBody from a dict
xref_segment_body_from_dict = XrefSegmentBody.from_dict(xref_segment_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


