# SuggestedHole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**byte_offset** | **int** |  | 
**byte_size** | **int** |  | 

## Example

```python
from revengai.models.suggested_hole import SuggestedHole

# TODO update the JSON string below
json = "{}"
# create an instance of SuggestedHole from a JSON string
suggested_hole_instance = SuggestedHole.from_json(json)
# print the JSON string representation of the object
print(SuggestedHole.to_json())

# convert the object into a dict
suggested_hole_dict = suggested_hole_instance.to_dict()
# create an instance of SuggestedHole from a dict
suggested_hole_from_dict = SuggestedHole.from_dict(suggested_hole_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


