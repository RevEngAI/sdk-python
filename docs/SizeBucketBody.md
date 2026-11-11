# SizeBucketBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**below_bytes** | **int** | Exclusive upper bound of the bucket, in bytes. Null for the last bucket, which has no upper bound. | 
**functions** | **int** | Functions a binary this size is estimated to have | 
**uncertain** | **bool** | True where too few operations have run on binaries this size for the estimate to be reliable | 

## Example

```python
from revengai.models.size_bucket_body import SizeBucketBody

# TODO update the JSON string below
json = "{}"
# create an instance of SizeBucketBody from a JSON string
size_bucket_body_instance = SizeBucketBody.from_json(json)
# print the JSON string representation of the object
print(SizeBucketBody.to_json())

# convert the object into a dict
size_bucket_body_dict = size_bucket_body_instance.to_dict()
# create an instance of SizeBucketBody from a dict
size_bucket_body_from_dict = SizeBucketBody.from_dict(size_bucket_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


