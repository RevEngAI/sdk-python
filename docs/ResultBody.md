# ResultBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binaries** | [**List[ExtractedBinary]**](ExtractedBinary.md) | Child binaries recovered from the extraction. | 
**extraction_depth** | **int** | Number of nested-archive extraction passes taken. | 
**filename_to_failure** | [**Dict[str, ExtractionFailure]**](ExtractionFailure.md) | Per-file extraction failures, keyed by filename. | 
**skipped_files** | **int** | Files skipped because they were not recognised as binaries. | 

## Example

```python
from revengai.models.result_body import ResultBody

# TODO update the JSON string below
json = "{}"
# create an instance of ResultBody from a JSON string
result_body_instance = ResultBody.from_json(json)
# print the JSON string representation of the object
print(ResultBody.to_json())

# convert the object into a dict
result_body_dict = result_body_instance.to_dict()
# create an instance of ResultBody from a dict
result_body_from_dict = ResultBody.from_dict(result_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


