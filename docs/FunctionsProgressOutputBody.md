# FunctionsProgressOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_embeddings_count** | **int** | Functions whose embedding has been written back | 
**functions_count** | **int** | Functions found in the analysis | 
**percentage_completed** | **float** | Embeddings as a percentage of functions, to 2 decimal places. 0 when the analysis has no functions | 

## Example

```python
from revengai.models.functions_progress_output_body import FunctionsProgressOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionsProgressOutputBody from a JSON string
functions_progress_output_body_instance = FunctionsProgressOutputBody.from_json(json)
# print the JSON string representation of the object
print(FunctionsProgressOutputBody.to_json())

# convert the object into a dict
functions_progress_output_body_dict = functions_progress_output_body_instance.to_dict()
# create an instance of FunctionsProgressOutputBody from a dict
functions_progress_output_body_from_dict = FunctionsProgressOutputBody.from_dict(functions_progress_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


