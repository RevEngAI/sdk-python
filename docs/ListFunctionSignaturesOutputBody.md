# ListFunctionSignaturesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_types** | [**List[AnalysisDataTypesGroup]**](AnalysisDataTypesGroup.md) | The types the returned signatures name, grouped by analysis and ordered by analysis_id. Returned only when include_data_types is true. | [optional] 
**items** | [**List[BatchFunctionSignatureEntry]**](BatchFunctionSignatureEntry.md) | One entry per distinct requested function ID, in request order. A repeated ID yields one entry. | 

## Example

```python
from revengai.models.list_function_signatures_output_body import ListFunctionSignaturesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListFunctionSignaturesOutputBody from a JSON string
list_function_signatures_output_body_instance = ListFunctionSignaturesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListFunctionSignaturesOutputBody.to_json())

# convert the object into a dict
list_function_signatures_output_body_dict = list_function_signatures_output_body_instance.to_dict()
# create an instance of ListFunctionSignaturesOutputBody from a dict
list_function_signatures_output_body_from_dict = ListFunctionSignaturesOutputBody.from_dict(list_function_signatures_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


