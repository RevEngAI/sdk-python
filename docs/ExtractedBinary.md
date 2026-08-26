# ExtractedBinary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | Original filename inside the upload | 
**sha_256_hash** | **str** | Content hash of the recovered binary | 
**size** | **int** | File size (in bytes) | 

## Example

```python
from revengai.models.extracted_binary import ExtractedBinary

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractedBinary from a JSON string
extracted_binary_instance = ExtractedBinary.from_json(json)
# print the JSON string representation of the object
print(ExtractedBinary.to_json())

# convert the object into a dict
extracted_binary_dict = extracted_binary_instance.to_dict()
# create an instance of ExtractedBinary from a dict
extracted_binary_from_dict = ExtractedBinary.from_dict(extracted_binary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


