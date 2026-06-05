# GetSubscriptionOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ends_at** | **datetime** | Date access ends (CANCELING only). | [optional] 
**price** | [**PriceSummary**](PriceSummary.md) | Current price (ACTIVE / CANCELING / PAYMENT_ISSUE only). | [optional] 
**product** | [**ProductSummary**](ProductSummary.md) | Subscribed product (ACTIVE / CANCELING / PAYMENT_ISSUE only). | [optional] 
**renews_at** | **datetime** | Next billing date (ACTIVE only). | [optional] 
**status** | **str** | Subscription state. | 
**tier** | **str** | User&#39;s effective tier. | 

## Example

```python
from revengai.models.get_subscription_output_body import GetSubscriptionOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionOutputBody from a JSON string
get_subscription_output_body_instance = GetSubscriptionOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionOutputBody.to_json())

# convert the object into a dict
get_subscription_output_body_dict = get_subscription_output_body_instance.to_dict()
# create an instance of GetSubscriptionOutputBody from a dict
get_subscription_output_body_from_dict = GetSubscriptionOutputBody.from_dict(get_subscription_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


