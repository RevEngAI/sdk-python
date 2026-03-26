# BaseResponseGetAiDecompilationRatingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetAiDecompilationRatingResponse**](GetAiDecompilationRatingResponse.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_get_ai_decompilation_rating_response import BaseResponseGetAiDecompilationRatingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseGetAiDecompilationRatingResponse from a JSON string
base_response_get_ai_decompilation_rating_response_instance = BaseResponseGetAiDecompilationRatingResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseGetAiDecompilationRatingResponse.to_json())

# convert the object into a dict
base_response_get_ai_decompilation_rating_response_dict = base_response_get_ai_decompilation_rating_response_instance.to_dict()
# create an instance of BaseResponseGetAiDecompilationRatingResponse from a dict
base_response_get_ai_decompilation_rating_response_from_dict = BaseResponseGetAiDecompilationRatingResponse.from_dict(base_response_get_ai_decompilation_rating_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


