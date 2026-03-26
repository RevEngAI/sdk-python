# XrefResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xref_from_list** | [**List[XrefFromResponse]**](XrefFromResponse.md) |  | 
**xref_to_list** | [**List[XrefToResponse]**](XrefToResponse.md) |  | 

## Example

```python
from revengai.models.xref_response import XrefResponse

# TODO update the JSON string below
json = "{}"
# create an instance of XrefResponse from a JSON string
xref_response_instance = XrefResponse.from_json(json)
# print the JSON string representation of the object
print(XrefResponse.to_json())

# convert the object into a dict
xref_response_dict = xref_response_instance.to_dict()
# create an instance of XrefResponse from a dict
xref_response_from_dict = XrefResponse.from_dict(xref_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


