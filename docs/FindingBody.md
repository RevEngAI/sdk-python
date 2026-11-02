# FindingBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from revengai.models.finding_body import FindingBody

# TODO update the JSON string below
json = "{}"
# create an instance of FindingBody from a JSON string
finding_body_instance = FindingBody.from_json(json)
# print the JSON string representation of the object
print(FindingBody.to_json())

# convert the object into a dict
finding_body_dict = finding_body_instance.to_dict()
# create an instance of FindingBody from a dict
finding_body_from_dict = FindingBody.from_dict(finding_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


