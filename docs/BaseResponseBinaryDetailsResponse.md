# BaseResponseBinaryDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BinaryDetailsResponse**](BinaryDetailsResponse.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_binary_details_response import BaseResponseBinaryDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseBinaryDetailsResponse from a JSON string
base_response_binary_details_response_instance = BaseResponseBinaryDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseBinaryDetailsResponse.to_json())

# convert the object into a dict
base_response_binary_details_response_dict = base_response_binary_details_response_instance.to_dict()
# create an instance of BaseResponseBinaryDetailsResponse from a dict
base_response_binary_details_response_from_dict = BaseResponseBinaryDetailsResponse.from_dict(base_response_binary_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


