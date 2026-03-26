# PutAnalysisStringsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strings** | [**List[AnalysisStringInput]**](AnalysisStringInput.md) | The strings to add to the analysis | 

## Example

```python
from revengai.models.put_analysis_strings_request import PutAnalysisStringsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutAnalysisStringsRequest from a JSON string
put_analysis_strings_request_instance = PutAnalysisStringsRequest.from_json(json)
# print the JSON string representation of the object
print(PutAnalysisStringsRequest.to_json())

# convert the object into a dict
put_analysis_strings_request_dict = put_analysis_strings_request_instance.to_dict()
# create an instance of PutAnalysisStringsRequest from a dict
put_analysis_strings_request_from_dict = PutAnalysisStringsRequest.from_dict(put_analysis_strings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


