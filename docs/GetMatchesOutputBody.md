# GetMatchesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[FunctionMatch]**](FunctionMatch.md) | Per-source-function matches. Populated when status&#x3D;COMPLETED; empty otherwise. | [optional] 
**status** | **str** | Current workflow status | 

## Example

```python
from revengai.models.get_matches_output_body import GetMatchesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetMatchesOutputBody from a JSON string
get_matches_output_body_instance = GetMatchesOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetMatchesOutputBody.to_json())

# convert the object into a dict
get_matches_output_body_dict = get_matches_output_body_instance.to_dict()
# create an instance of GetMatchesOutputBody from a dict
get_matches_output_body_from_dict = GetMatchesOutputBody.from_dict(get_matches_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


