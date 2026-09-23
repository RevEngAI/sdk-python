# Binary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** |  | 
**binary_id** | **int** |  | 
**binary_name** | **str** |  | 
**created_at** | **datetime** |  | 
**detected_architecture** | **str** | Detected instruction-set architecture; empty when unavailable | 
**detected_binary_type** | **str** | Detected operating-system platform; empty when unavailable | 
**is_system_analysis** | **bool** |  | 
**model_name** | **str** | Name of the model the analysis ran on | 
**owner_id** | **int** |  | 
**sha_256_hash** | **str** |  | 
**supplied_architecture** | **str** | User-supplied instruction-set architecture; \&quot;AUTO\&quot; when not overridden | 
**supplied_binary_type** | **str** | User-supplied operating-system platform; \&quot;AUTO\&quot; when not overridden | 

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


