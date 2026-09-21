# DecompilerSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**Subject**](Subject.md) |  | 
**summary** | **str** |  | 
**reachability** | [**CallChain**](CallChain.md) |  | [optional] 

## Example

```python
from revengai.models.decompiler_summary import DecompilerSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DecompilerSummary from a JSON string
decompiler_summary_instance = DecompilerSummary.from_json(json)
# print the JSON string representation of the object
print(DecompilerSummary.to_json())

# convert the object into a dict
decompiler_summary_dict = decompiler_summary_instance.to_dict()
# create an instance of DecompilerSummary from a dict
decompiler_summary_from_dict = DecompilerSummary.from_dict(decompiler_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


