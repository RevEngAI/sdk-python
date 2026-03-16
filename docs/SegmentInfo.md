# SegmentInfo

Represents the information about a segment.  Attributes:     name: The name of the segment.     r: Determines if the segment has read permission.     w: Determines if the segment has write permission.     x: Determines if the segment has execute permission.     start: The start address of the segment.     end: The end address of the segment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [default to '']
**r** | **bool** |  | [optional] 
**w** | **bool** |  | [optional] 
**x** | **bool** |  | [optional] 
**start** | **int** |  | [optional] [default to 0]
**end** | **int** |  | [optional] [default to 0]

## Example

```python
from revengai.models.segment_info import SegmentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentInfo from a JSON string
segment_info_instance = SegmentInfo.from_json(json)
# print the JSON string representation of the object
print(SegmentInfo.to_json())

# convert the object into a dict
segment_info_dict = segment_info_instance.to_dict()
# create an instance of SegmentInfo from a dict
segment_info_from_dict = SegmentInfo.from_dict(segment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


