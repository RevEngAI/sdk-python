# BaseResponseBinarySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BinarySearchResponse**](BinarySearchResponse.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_binary_search_response import BaseResponseBinarySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseBinarySearchResponse from a JSON string
base_response_binary_search_response_instance = BaseResponseBinarySearchResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseBinarySearchResponse.to_json())

# convert the object into a dict
base_response_binary_search_response_dict = base_response_binary_search_response_instance.to_dict()
# create an instance of BaseResponseBinarySearchResponse from a dict
base_response_binary_search_response_from_dict = BaseResponseBinarySearchResponse.from_dict(base_response_binary_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


