# LookupAnalysisByBinaryIDOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Most recent analysis for this binary that the caller may see | 

## Example

```python
from revengai.models.lookup_analysis_by_binary_id_output_body import LookupAnalysisByBinaryIDOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of LookupAnalysisByBinaryIDOutputBody from a JSON string
lookup_analysis_by_binary_id_output_body_instance = LookupAnalysisByBinaryIDOutputBody.from_json(json)
# print the JSON string representation of the object
print(LookupAnalysisByBinaryIDOutputBody.to_json())

# convert the object into a dict
lookup_analysis_by_binary_id_output_body_dict = lookup_analysis_by_binary_id_output_body_instance.to_dict()
# create an instance of LookupAnalysisByBinaryIDOutputBody from a dict
lookup_analysis_by_binary_id_output_body_from_dict = LookupAnalysisByBinaryIDOutputBody.from_dict(lookup_analysis_by_binary_id_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


