# PriceOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Lowercase ISO 4217 currency code (e.g. \&quot;usd\&quot;, \&quot;gbp\&quot;). | 
**id** | **str** | Price ID. | 
**interval** | **str** | Billing interval at which the price recurs. | 
**unit_amount** | **int** | Price per billing interval, expressed in the smallest unit of the currency (e.g. cents for USD, pence for GBP). | 

## Example

```python
from revengai.models.price_output import PriceOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PriceOutput from a JSON string
price_output_instance = PriceOutput.from_json(json)
# print the JSON string representation of the object
print(PriceOutput.to_json())

# convert the object into a dict
price_output_dict = price_output_instance.to_dict()
# create an instance of PriceOutput from a dict
price_output_from_dict = PriceOutput.from_dict(price_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


