# BatchMatchingOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**per_binary** | [**List[BatchBinaryMatchResult]**](BatchBinaryMatchResult.md) | Per-binary status (order matches the request). | 
**status** | **str** | Aggregate status across the batch: COMPLETED when every binary is completed, FAILED if any failed, RUNNING/PENDING otherwise. | 

## Example

```python
from revengai.models.batch_matching_output_body import BatchMatchingOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of BatchMatchingOutputBody from a JSON string
batch_matching_output_body_instance = BatchMatchingOutputBody.from_json(json)
# print the JSON string representation of the object
print(BatchMatchingOutputBody.to_json())

# convert the object into a dict
batch_matching_output_body_dict = batch_matching_output_body_instance.to_dict()
# create an instance of BatchMatchingOutputBody from a dict
batch_matching_output_body_from_dict = BatchMatchingOutputBody.from_dict(batch_matching_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


