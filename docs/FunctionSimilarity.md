# FunctionSimilarity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**similarity** | **float** |  | 
**subject** | [**Subject**](Subject.md) |  | 

## Example

```python
from revengai.models.function_similarity import FunctionSimilarity

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionSimilarity from a JSON string
function_similarity_instance = FunctionSimilarity.from_json(json)
# print the JSON string representation of the object
print(FunctionSimilarity.to_json())

# convert the object into a dict
function_similarity_dict = function_similarity_instance.to_dict()
# create an instance of FunctionSimilarity from a dict
function_similarity_from_dict = FunctionSimilarity.from_dict(function_similarity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


