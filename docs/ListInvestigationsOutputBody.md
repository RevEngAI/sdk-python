# ListInvestigationsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_status_counts** | [**AgentStatusCountsBody**](AgentStatusCountsBody.md) | Open investigations you can see at each agent status, whatever the filters and page. | 
**has_next_page** | **bool** |  | 
**results** | [**List[InvestigationListItemBody]**](InvestigationListItemBody.md) |  | 
**total_count** | **int** | Investigations matching the filters across all pages. | 

## Example

```python
from revengai.models.list_investigations_output_body import ListInvestigationsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListInvestigationsOutputBody from a JSON string
list_investigations_output_body_instance = ListInvestigationsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListInvestigationsOutputBody.to_json())

# convert the object into a dict
list_investigations_output_body_dict = list_investigations_output_body_instance.to_dict()
# create an instance of ListInvestigationsOutputBody from a dict
list_investigations_output_body_from_dict = ListInvestigationsOutputBody.from_dict(list_investigations_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


