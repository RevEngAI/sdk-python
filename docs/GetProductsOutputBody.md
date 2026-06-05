# GetProductsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ProductOutput]**](ProductOutput.md) | List of available products | 

## Example

```python
from revengai.models.get_products_output_body import GetProductsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetProductsOutputBody from a JSON string
get_products_output_body_instance = GetProductsOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetProductsOutputBody.to_json())

# convert the object into a dict
get_products_output_body_dict = get_products_output_body_instance.to_dict()
# create an instance of GetProductsOutputBody from a dict
get_products_output_body_from_dict = GetProductsOutputBody.from_dict(get_products_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


