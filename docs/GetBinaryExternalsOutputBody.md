# GetBinaryExternalsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_id** | **int** |  | 
**externals** | [**BinaryExternalsBody**](BinaryExternalsBody.md) | Null until at least one external lookup has run for this binary&#39;s content hash | 

## Example

```python
from revengai.models.get_binary_externals_output_body import GetBinaryExternalsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetBinaryExternalsOutputBody from a JSON string
get_binary_externals_output_body_instance = GetBinaryExternalsOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetBinaryExternalsOutputBody.to_json())

# convert the object into a dict
get_binary_externals_output_body_dict = get_binary_externals_output_body_instance.to_dict()
# create an instance of GetBinaryExternalsOutputBody from a dict
get_binary_externals_output_body_from_dict = GetBinaryExternalsOutputBody.from_dict(get_binary_externals_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


