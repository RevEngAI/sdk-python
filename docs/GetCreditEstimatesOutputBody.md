# GetCreditEstimatesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operations** | [**List[OperationCostBody]**](OperationCostBody.md) | Estimated cost of each operation | 
**size_buckets** | [**List[SizeBucketBody]**](SizeBucketBody.md) | Size buckets in ascending order of size | 

## Example

```python
from revengai.models.get_credit_estimates_output_body import GetCreditEstimatesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetCreditEstimatesOutputBody from a JSON string
get_credit_estimates_output_body_instance = GetCreditEstimatesOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetCreditEstimatesOutputBody.to_json())

# convert the object into a dict
get_credit_estimates_output_body_dict = get_credit_estimates_output_body_instance.to_dict()
# create an instance of GetCreditEstimatesOutputBody from a dict
get_credit_estimates_output_body_from_dict = GetCreditEstimatesOutputBody.from_dict(get_credit_estimates_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


