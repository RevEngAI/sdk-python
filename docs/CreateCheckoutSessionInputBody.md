# CreateCheckoutSessionInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_url** | **str** | URL to redirect to on cancel. | 
**price_id** | **str** | Price ID from /v3/billing/products. | 
**success_url** | **str** | URL to redirect to on success. | 

## Example

```python
from revengai.models.create_checkout_session_input_body import CreateCheckoutSessionInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCheckoutSessionInputBody from a JSON string
create_checkout_session_input_body_instance = CreateCheckoutSessionInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateCheckoutSessionInputBody.to_json())

# convert the object into a dict
create_checkout_session_input_body_dict = create_checkout_session_input_body_instance.to_dict()
# create an instance of CreateCheckoutSessionInputBody from a dict
create_checkout_session_input_body_from_dict = CreateCheckoutSessionInputBody.from_dict(create_checkout_session_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


