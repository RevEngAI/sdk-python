# GetRelatedBinariesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[RelatedBinary]**](RelatedBinary.md) | Binaries unpacked out of this one | 
**parent** | [**RelatedBinary**](RelatedBinary.md) | Archive this binary was unpacked from, null when it was uploaded directly | 

## Example

```python
from revengai.models.get_related_binaries_output_body import GetRelatedBinariesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetRelatedBinariesOutputBody from a JSON string
get_related_binaries_output_body_instance = GetRelatedBinariesOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetRelatedBinariesOutputBody.to_json())

# convert the object into a dict
get_related_binaries_output_body_dict = get_related_binaries_output_body_instance.to_dict()
# create an instance of GetRelatedBinariesOutputBody from a dict
get_related_binaries_output_body_from_dict = GetRelatedBinariesOutputBody.from_dict(get_related_binaries_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


