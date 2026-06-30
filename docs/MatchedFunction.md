# MatchedFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis the candidate&#39;s binary belongs to | 
**binary_id** | **int** | Binary the candidate belongs to | 
**binary_name** | **str** | Binary name | 
**confidence** | **float** | Softmax-normalised confidence over the candidate pool | 
**debug** | **bool** | Whether the candidate&#39;s name came from debug info | 
**function_id** | **int** | Candidate function ID | 
**function_name** | **str** | Candidate function name | 
**function_vaddr** | **int** | Candidate&#39;s virtual address inside its binary | 
**mangled_name** | **str** | Mangled name when available | 
**sha_256_hash** | **str** | SHA-256 of the candidate&#39;s binary | 
**similarity** | **float** | Cosine similarity scaled to a percentage | 

## Example

```python
from revengai.models.matched_function import MatchedFunction

# TODO update the JSON string below
json = "{}"
# create an instance of MatchedFunction from a JSON string
matched_function_instance = MatchedFunction.from_json(json)
# print the JSON string representation of the object
print(MatchedFunction.to_json())

# convert the object into a dict
matched_function_dict = matched_function_instance.to_dict()
# create an instance of MatchedFunction from a dict
matched_function_from_dict = MatchedFunction.from_dict(matched_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


