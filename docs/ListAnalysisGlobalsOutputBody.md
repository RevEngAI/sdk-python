# ListAnalysisGlobalsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**globals** | [**List[GlobalVariable]**](GlobalVariable.md) |  | 
**total** | **int** |  | 
**total_unfiltered** | **int** |  | 

## Example

```python
from revengai.models.list_analysis_globals_output_body import ListAnalysisGlobalsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListAnalysisGlobalsOutputBody from a JSON string
list_analysis_globals_output_body_instance = ListAnalysisGlobalsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListAnalysisGlobalsOutputBody.to_json())

# convert the object into a dict
list_analysis_globals_output_body_dict = list_analysis_globals_output_body_instance.to_dict()
# create an instance of ListAnalysisGlobalsOutputBody from a dict
list_analysis_globals_output_body_from_dict = ListAnalysisGlobalsOutputBody.from_dict(list_analysis_globals_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


