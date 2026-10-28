# ListFindingsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next_page** | **bool** |  | 
**results** | [**List[FindingBody]**](FindingBody.md) |  | 
**total_count** | **int** | Findings matching the filters across all pages. | 

## Example

```python
from revengai.models.list_findings_output_body import ListFindingsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListFindingsOutputBody from a JSON string
list_findings_output_body_instance = ListFindingsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListFindingsOutputBody.to_json())

# convert the object into a dict
list_findings_output_body_dict = list_findings_output_body_instance.to_dict()
# create an instance of ListFindingsOutputBody from a dict
list_findings_output_body_from_dict = ListFindingsOutputBody.from_dict(list_findings_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


