# RelatedBinary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Most recent analysis of the related binary, null when it has never been analysed | 
**binary_id** | **int** | ID of the related binary | 
**name** | **str** | Name of the related binary | 
**sha256** | **str** | SHA-256 of the related binary | 

## Example

```python
from revengai.models.related_binary import RelatedBinary

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedBinary from a JSON string
related_binary_instance = RelatedBinary.from_json(json)
# print the JSON string representation of the object
print(RelatedBinary.to_json())

# convert the object into a dict
related_binary_dict = related_binary_instance.to_dict()
# create an instance of RelatedBinary from a dict
related_binary_from_dict = RelatedBinary.from_dict(related_binary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


