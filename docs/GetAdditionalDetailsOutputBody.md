# GetAdditionalDetailsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_id** | **int** |  | 
**details** | **object** |  | 

## Example

```python
from revengai.models.get_additional_details_output_body import GetAdditionalDetailsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdditionalDetailsOutputBody from a JSON string
get_additional_details_output_body_instance = GetAdditionalDetailsOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetAdditionalDetailsOutputBody.to_json())

# convert the object into a dict
get_additional_details_output_body_dict = get_additional_details_output_body_instance.to_dict()
# create an instance of GetAdditionalDetailsOutputBody from a dict
get_additional_details_output_body_from_dict = GetAdditionalDetailsOutputBody.from_dict(get_additional_details_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


