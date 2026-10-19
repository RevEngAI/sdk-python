# ReportFunctionSimilarity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the known function. | 
**similarity** | **float** | Similarity score, from 0 to 1. | 
**subject** | [**ReportSubject**](ReportSubject.md) | The matching function in the analysed binary. | 

## Example

```python
from revengai.models.report_function_similarity import ReportFunctionSimilarity

# TODO update the JSON string below
json = "{}"
# create an instance of ReportFunctionSimilarity from a JSON string
report_function_similarity_instance = ReportFunctionSimilarity.from_json(json)
# print the JSON string representation of the object
print(ReportFunctionSimilarity.to_json())

# convert the object into a dict
report_function_similarity_dict = report_function_similarity_instance.to_dict()
# create an instance of ReportFunctionSimilarity from a dict
report_function_similarity_from_dict = ReportFunctionSimilarity.from_dict(report_function_similarity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


