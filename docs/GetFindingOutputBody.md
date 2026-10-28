# GetFindingOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_ids** | **List[int]** | Analyses the finding was derived from that you are permitted to see. | 
**created_at** | **datetime** |  | 
**details** | **Dict[str, object]** | Fields specific to the finding type. An IOC has kind and value, a capability has name, a vulnerability has optional cve, cwe and location, and a cross-file flow has steps. | 
**finding_id** | **int** |  | 
**finding_type** | **str** |  | 
**investigation_id** | **int** |  | 
**severity** | **str** |  | 
**source** | **str** | The agent or tool that produced the finding. | 
**summary** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from revengai.models.get_finding_output_body import GetFindingOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetFindingOutputBody from a JSON string
get_finding_output_body_instance = GetFindingOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetFindingOutputBody.to_json())

# convert the object into a dict
get_finding_output_body_dict = get_finding_output_body_instance.to_dict()
# create an instance of GetFindingOutputBody from a dict
get_finding_output_body_from_dict = GetFindingOutputBody.from_dict(get_finding_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


