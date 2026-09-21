# DieMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display** | **str** | Human-readable description from DIE; suitable for display, not parsing | 
**name** | **str** | Canonical name of the matched signature or technology | 
**type** | **str** | Category DIE assigns the match, such as compiler, packer or file | 
**version** | **str** | Version DIE extracted, empty when it could not determine one | 

## Example

```python
from revengai.models.die_match import DieMatch

# TODO update the JSON string below
json = "{}"
# create an instance of DieMatch from a JSON string
die_match_instance = DieMatch.from_json(json)
# print the JSON string representation of the object
print(DieMatch.to_json())

# convert the object into a dict
die_match_dict = die_match_instance.to_dict()
# create an instance of DieMatch from a dict
die_match_from_dict = DieMatch.from_dict(die_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


