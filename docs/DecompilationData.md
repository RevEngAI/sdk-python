# DecompilationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decompilation** | **str** | Source code with placeholders replaced | [optional] 
**status** | **str** | Task status | 

## Example

```python
from revengai.models.decompilation_data import DecompilationData

# TODO update the JSON string below
json = "{}"
# create an instance of DecompilationData from a JSON string
decompilation_data_instance = DecompilationData.from_json(json)
# print the JSON string representation of the object
print(DecompilationData.to_json())

# convert the object into a dict
decompilation_data_dict = decompilation_data_instance.to_dict()
# create an instance of DecompilationData from a dict
decompilation_data_from_dict = DecompilationData.from_dict(decompilation_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


