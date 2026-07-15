# GetAnalysisStringsStatusOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | String-extraction task status | 

## Example

```python
from revengai.models.get_analysis_strings_status_output_body import GetAnalysisStringsStatusOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetAnalysisStringsStatusOutputBody from a JSON string
get_analysis_strings_status_output_body_instance = GetAnalysisStringsStatusOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetAnalysisStringsStatusOutputBody.to_json())

# convert the object into a dict
get_analysis_strings_status_output_body_dict = get_analysis_strings_status_output_body_instance.to_dict()
# create an instance of GetAnalysisStringsStatusOutputBody from a dict
get_analysis_strings_status_output_body_from_dict = GetAnalysisStringsStatusOutputBody.from_dict(get_analysis_strings_status_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


