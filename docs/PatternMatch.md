# PatternMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** |  | 
**length** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from revengai.models.pattern_match import PatternMatch

# TODO update the JSON string below
json = "{}"
# create an instance of PatternMatch from a JSON string
pattern_match_instance = PatternMatch.from_json(json)
# print the JSON string representation of the object
print(PatternMatch.to_json())

# convert the object into a dict
pattern_match_dict = pattern_match_instance.to_dict()
# create an instance of PatternMatch from a dict
pattern_match_from_dict = PatternMatch.from_dict(pattern_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


