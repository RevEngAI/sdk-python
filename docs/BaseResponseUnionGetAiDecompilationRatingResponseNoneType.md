# BaseResponseUnionGetAiDecompilationRatingResponseNoneType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]
**data** | [**GetAiDecompilationRatingResponse**](GetAiDecompilationRatingResponse.md) |  | [optional] 
**message** | **str** |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 

## Example

```python
from revengai.models.base_response_union_get_ai_decompilation_rating_response_none_type import BaseResponseUnionGetAiDecompilationRatingResponseNoneType

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseUnionGetAiDecompilationRatingResponseNoneType from a JSON string
base_response_union_get_ai_decompilation_rating_response_none_type_instance = BaseResponseUnionGetAiDecompilationRatingResponseNoneType.from_json(json)
# print the JSON string representation of the object
print(BaseResponseUnionGetAiDecompilationRatingResponseNoneType.to_json())

# convert the object into a dict
base_response_union_get_ai_decompilation_rating_response_none_type_dict = base_response_union_get_ai_decompilation_rating_response_none_type_instance.to_dict()
# create an instance of BaseResponseUnionGetAiDecompilationRatingResponseNoneType from a dict
base_response_union_get_ai_decompilation_rating_response_none_type_from_dict = BaseResponseUnionGetAiDecompilationRatingResponseNoneType.from_dict(base_response_union_get_ai_decompilation_rating_response_none_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


