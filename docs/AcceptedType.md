# AcceptedType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **bool** | False when the analysis already held a type under this name and kind, which this request resolved to rather than replaced. | 
**data_type_id** | **int** | The data type the suggestion is now stored as. | 
**key** | **str** | The suggestion this entry answers. | 
**skipped_members** | **int** | Members left out of the stored type because no offset or width was established for them. | 

## Example

```python
from revengai.models.accepted_type import AcceptedType

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptedType from a JSON string
accepted_type_instance = AcceptedType.from_json(json)
# print the JSON string representation of the object
print(AcceptedType.to_json())

# convert the object into a dict
accepted_type_dict = accepted_type_instance.to_dict()
# create an instance of AcceptedType from a dict
accepted_type_from_dict = AcceptedType.from_dict(accepted_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


