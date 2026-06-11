# Binary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** |  | 
**binary_id** | **int** |  | 
**binary_name** | **str** |  | 
**created_at** | **datetime** |  | 
**is_system_analysis** | **bool** |  | 
**owner_id** | **int** |  | 
**sha_256_hash** | **str** |  | 

## Example

```python
from revengai.models.binary import Binary

# TODO update the JSON string below
json = "{}"
# create an instance of Binary from a JSON string
binary_instance = Binary.from_json(json)
# print the JSON string representation of the object
print(Binary.to_json())

# convert the object into a dict
binary_dict = binary_instance.to_dict()
# create an instance of Binary from a dict
binary_from_dict = Binary.from_dict(binary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


