# GetDieInfoOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matches** | [**List[DieMatch]**](DieMatch.md) | Signatures Detect It Easy recognised in the binary | 

## Example

```python
from revengai.models.get_die_info_output_body import GetDieInfoOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetDieInfoOutputBody from a JSON string
get_die_info_output_body_instance = GetDieInfoOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetDieInfoOutputBody.to_json())

# convert the object into a dict
get_die_info_output_body_dict = get_die_info_output_body_instance.to_dict()
# create an instance of GetDieInfoOutputBody from a dict
get_die_info_output_body_from_dict = GetDieInfoOutputBody.from_dict(get_die_info_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


