# Example


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis ID | 
**analysis_scope** | **str** | Scope of the analysis (always PUBLIC for examples) | 
**binary_id** | **int** | Binary ID | 
**binary_name** | **str** | Binary filename | 
**binary_size** | **int** | Binary size in bytes | 
**creation** | **datetime** | When the analysis was created | 
**is_owner** | **bool** | True when the caller owns the analysis | 
**model_id** | **int** | Model ID | 
**sha_256_hash** | **str** | SHA-256 hash of the binary | 
**status** | **str** | Analysis status | 
**tags** | **List[str]** | Tags associated with this binary | 
**username** | **str** | Username of the analysis owner | 

## Example

```python
from revengai.models.example import Example

# TODO update the JSON string below
json = "{}"
# create an instance of Example from a JSON string
example_instance = Example.from_json(json)
# print the JSON string representation of the object
print(Example.to_json())

# convert the object into a dict
example_dict = example_instance.to_dict()
# create an instance of Example from a dict
example_from_dict = Example.from_dict(example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


