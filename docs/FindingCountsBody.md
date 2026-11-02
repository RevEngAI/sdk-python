# FindingCountsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**critical** | **int** |  | 
**high** | **int** |  | 
**low** | **int** |  | 
**medium** | **int** |  | 
**total** | **int** |  | 

## Example

```python
from revengai.models.finding_counts_body import FindingCountsBody

# TODO update the JSON string below
json = "{}"
# create an instance of FindingCountsBody from a JSON string
finding_counts_body_instance = FindingCountsBody.from_json(json)
# print the JSON string representation of the object
print(FindingCountsBody.to_json())

# convert the object into a dict
finding_counts_body_dict = finding_counts_body_instance.to_dict()
# create an instance of FindingCountsBody from a dict
finding_counts_body_from_dict = FindingCountsBody.from_dict(finding_counts_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


