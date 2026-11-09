# OperationCostBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_credits** | **float** | Credits the operation is estimated to use regardless of the binary&#39;s size | 
**credits_per_function** | **float** | Credits the operation is estimated to use per function in the binary | 
**operation** | **str** | The operation, as requested when creating an analysis, or binary-analysis for the analysis itself | 

## Example

```python
from revengai.models.operation_cost_body import OperationCostBody

# TODO update the JSON string below
json = "{}"
# create an instance of OperationCostBody from a JSON string
operation_cost_body_instance = OperationCostBody.from_json(json)
# print the JSON string representation of the object
print(OperationCostBody.to_json())

# convert the object into a dict
operation_cost_body_dict = operation_cost_body_instance.to_dict()
# create an instance of OperationCostBody from a dict
operation_cost_body_from_dict = OperationCostBody.from_dict(operation_cost_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


