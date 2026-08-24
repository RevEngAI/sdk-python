# MatchFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architectures** | **List[str]** | Restrict matches to candidates whose binary was detected as one of these architectures. Word size is part of the value, so there is no separate bits filter. Matches all architectures if omitted. | [optional] 
**binary_ids** | **List[int]** | Restrict the candidate pool to these binary IDs. | [optional] 
**collection_ids** | **List[int]** | Restrict the candidate pool to binaries in these collection IDs. | [optional] 
**debug** | **bool** | Restrict matches to candidates with auto/system debug symbols. Multi-platform models only; rejected for single-architecture models. | [optional] 
**debug_types** | **List[Optional[str]]** | Restrict matches to candidates with these debug source types. Accepted: SYSTEM, USER. | [optional] 
**function_ids** | **List[int]** | Restrict the candidate pool to these function IDs. | [optional] 
**include_user_debug** | **bool** | When debug is set, also match user-named functions (not only auto/system debug). No effect unless debug is true. | [optional] 
**platforms** | **List[str]** | Restrict matches to candidates whose binary was detected as one of these platforms. Matches all platforms if omitted; a binary whose detection has not run is never matched by a non-empty filter. | [optional] 
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


