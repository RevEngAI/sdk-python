# SecurityFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** | Semgrep rule ID that matched | [optional] 
**confidence** | **str** | Semgrep&#39;s confidence in the finding | [optional] 
**cwe** | **List[str]** | CWE identifiers associated with the finding | [optional] 
**end_line** | **int** | Line the finding ends on | [optional] 
**function_id** | **int** | ID of the function the finding was reported in | [optional] 
**function_name** | **str** | Name of the function the finding was reported in | [optional] 
**impact** | **str** | Estimated impact of the finding | [optional] 
**message** | **str** | Human-readable description of the finding | [optional] 
**severity** | **str** | Severity of the finding | [optional] 
**snippet_lines** | **List[str]** | Source lines making up the reported snippet | [optional] 
**snippet_start_line** | **int** | Line the reported snippet starts on | [optional] 
**start_line** | **int** | Line the finding starts on | [optional] 

## Example

```python
from revengai.models.security_finding import SecurityFinding

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityFinding from a JSON string
security_finding_instance = SecurityFinding.from_json(json)
# print the JSON string representation of the object
print(SecurityFinding.to_json())

# convert the object into a dict
security_finding_dict = security_finding_instance.to_dict()
# create an instance of SecurityFinding from a dict
security_finding_from_dict = SecurityFinding.from_dict(security_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


