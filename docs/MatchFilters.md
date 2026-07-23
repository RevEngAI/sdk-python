# MatchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** | Restrict matches to this architecture (multi-platform models only; matches all architectures if omitted). Rejected for single-architecture models. | [optional] 
**binary_ids** | **List[int]** | Restrict the candidate pool to these binary IDs. | [optional] 
**bits** | **int** | Restrict matches to this word size (multi-platform models only). Rejected for single-architecture models. | [optional] 
**collection_ids** | **List[int]** | Restrict the candidate pool to binaries in these collection IDs. | [optional] 
**debug_types** | **List[str]** | Restrict matches to candidates with these debug source types. Accepted: SYSTEM, USER. | [optional] 
**function_ids** | **List[int]** | Restrict the candidate pool to these function IDs. | [optional] 
**platform** | **str** | Restrict matches to this platform (multi-platform models only; matches all platforms if omitted). Rejected for single-architecture models. | [optional] 
**user_ids** | **List[int]** | Restrict the candidate pool to functions owned by these user IDs. | [optional] 

## Example

```python
from revengai.models.match_filters import MatchFilters

# TODO update the JSON string below
json = "{}"
# create an instance of MatchFilters from a JSON string
match_filters_instance = MatchFilters.from_json(json)
# print the JSON string representation of the object
print(MatchFilters.to_json())

# convert the object into a dict
match_filters_dict = match_filters_instance.to_dict()
# create an instance of MatchFilters from a dict
match_filters_from_dict = MatchFilters.from_dict(match_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


