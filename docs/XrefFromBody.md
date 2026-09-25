# XrefFromBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_call** | **bool** | True when the xref is a call instruction | 
**is_data** | **bool** | True when the xref targets data rather than code | 
**is_scalar** | **bool** | True when the xref is a scalar constant | 
**is_string** | **bool** | True when the xref targets a string | 
**orig_str_encoding** | **str** | String encoding, set only when is_string is true | [optional] 
**raw_data** | **str** | Raw bytes at the xref target, when captured | [optional] 
**segment** | [**XrefSegmentBody**](XrefSegmentBody.md) | Memory segment the xref target sits in | [optional] 
**value** | **str** | The xref&#39;s resolved value, when the sequencer could determine one | [optional] 
**xref_to** | **int** | Address the reference targets | 

## Example

```python
from revengai.models.xref_from_body import XrefFromBody

# TODO update the JSON string below
json = "{}"
# create an instance of XrefFromBody from a JSON string
xref_from_body_instance = XrefFromBody.from_json(json)
# print the JSON string representation of the object
print(XrefFromBody.to_json())

# convert the object into a dict
xref_from_body_dict = xref_from_body_instance.to_dict()
# create an instance of XrefFromBody from a dict
xref_from_body_from_dict = XrefFromBody.from_dict(xref_from_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


