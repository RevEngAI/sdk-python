# ListSpendOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**results** | [**List[SpendBody]**](SpendBody.md) |  | 
**total_count** | **int** | Spend records across all pages. | 

## Example

```python
from revengai.models.list_spend_output_body import ListSpendOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListSpendOutputBody from a JSON string
list_spend_output_body_instance = ListSpendOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListSpendOutputBody.to_json())

# convert the object into a dict
list_spend_output_body_dict = list_spend_output_body_instance.to_dict()
# create an instance of ListSpendOutputBody from a dict
list_spend_output_body_from_dict = ListSpendOutputBody.from_dict(list_spend_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


