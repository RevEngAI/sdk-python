# ExtractionFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Why this file failed to extract. | 
**retryable** | **bool** | Whether re-submitting the extraction might resolve this failure. | 

## Example

```python
from revengai.models.extraction_failure import ExtractionFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractionFailure from a JSON string
extraction_failure_instance = ExtractionFailure.from_json(json)
# print the JSON string representation of the object
print(ExtractionFailure.to_json())

# convert the object into a dict
extraction_failure_dict = extraction_failure_instance.to_dict()
# create an instance of ExtractionFailure from a dict
extraction_failure_from_dict = ExtractionFailure.from_dict(extraction_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


