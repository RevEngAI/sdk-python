# BaseResponseGetPublicUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetPublicUserResponse**](GetPublicUserResponse.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_get_public_user_response import BaseResponseGetPublicUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseGetPublicUserResponse from a JSON string
base_response_get_public_user_response_instance = BaseResponseGetPublicUserResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseGetPublicUserResponse.to_json())

# convert the object into a dict
base_response_get_public_user_response_dict = base_response_get_public_user_response_instance.to_dict()
# create an instance of BaseResponseGetPublicUserResponse from a dict
base_response_get_public_user_response_from_dict = BaseResponseGetPublicUserResponse.from_dict(base_response_get_public_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


