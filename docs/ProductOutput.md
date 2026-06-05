# ProductOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credits_per_month** | **int** | Credits awarded per billing month, if applicable. | [optional] 
**description** | **str** | Human-readable product description. | 
**features** | **List[str]** | Marketing feature list for this product. | 
**id** | **str** | Product ID. | 
**name** | **str** | Human-readable product name. | 
**prices** | [**List[PriceOutput]**](PriceOutput.md) | All active recurring prices for this product. | 
**tier** | **str** | User tier associated with this product, if any. | [optional] 

## Example

```python
from revengai.models.product_output import ProductOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ProductOutput from a JSON string
product_output_instance = ProductOutput.from_json(json)
# print the JSON string representation of the object
print(ProductOutput.to_json())

# convert the object into a dict
product_output_dict = product_output_instance.to_dict()
# create an instance of ProductOutput from a dict
product_output_from_dict = ProductOutput.from_dict(product_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


