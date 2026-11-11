# ListDatasetsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**datasets** | [**List[DatasetInfo]**](DatasetInfo.md) |  | 

## Example

```python
from revengai.models.list_datasets_output_body import ListDatasetsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasetsOutputBody from a JSON string
list_datasets_output_body_instance = ListDatasetsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListDatasetsOutputBody.to_json())

# convert the object into a dict
list_datasets_output_body_dict = list_datasets_output_body_instance.to_dict()
# create an instance of ListDatasetsOutputBody from a dict
list_datasets_output_body_from_dict = ListDatasetsOutputBody.from_dict(list_datasets_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


