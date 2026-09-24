# StringMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**subject** | [**Subject**](Subject.md) |  | [optional] 

## Example

```python
from revengai.models.string_match import StringMatch

# TODO update the JSON string below
json = "{}"
# create an instance of StringMatch from a JSON string
string_match_instance = StringMatch.from_json(json)
# print the JSON string representation of the object
print(StringMatch.to_json())

# convert the object into a dict
string_match_dict = string_match_instance.to_dict()
# create an instance of StringMatch from a dict
string_match_from_dict = StringMatch.from_dict(string_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


