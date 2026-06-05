# PriceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Lowercase ISO 4217 currency code. | 
**interval** | **str** | Billing interval at which the price recurs. | 
**unit_amount** | **int** | Price per billing interval, in the smallest unit of the currency. | 

## Example

```python
from revengai.models.price_summary import PriceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PriceSummary from a JSON string
price_summary_instance = PriceSummary.from_json(json)
# print the JSON string representation of the object
print(PriceSummary.to_json())

# convert the object into a dict
price_summary_dict = price_summary_instance.to_dict()
# create an instance of PriceSummary from a dict
price_summary_from_dict = PriceSummary.from_dict(price_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


