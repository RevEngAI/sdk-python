# IndirectCallSitesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_id** | **int** |  | 
**sites** | [**List[IndirectCallSite]**](IndirectCallSite.md) |  | 

## Example

```python
from revengai.models.indirect_call_sites_output_body import IndirectCallSitesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of IndirectCallSitesOutputBody from a JSON string
indirect_call_sites_output_body_instance = IndirectCallSitesOutputBody.from_json(json)
# print the JSON string representation of the object
print(IndirectCallSitesOutputBody.to_json())

# convert the object into a dict
indirect_call_sites_output_body_dict = indirect_call_sites_output_body_instance.to_dict()
# create an instance of IndirectCallSitesOutputBody from a dict
indirect_call_sites_output_body_from_dict = IndirectCallSitesOutputBody.from_dict(indirect_call_sites_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


