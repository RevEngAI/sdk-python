# AnalyseCapabilitiesBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **int** | ANALYSE_CAPABILITIES agent tasks completed that day | 

## Example

```python
from revengai.models.analyse_capabilities_body import AnalyseCapabilitiesBody

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyseCapabilitiesBody from a JSON string
analyse_capabilities_body_instance = AnalyseCapabilitiesBody.from_json(json)
# print the JSON string representation of the object
print(AnalyseCapabilitiesBody.to_json())

# convert the object into a dict
analyse_capabilities_body_dict = analyse_capabilities_body_instance.to_dict()
# create an instance of AnalyseCapabilitiesBody from a dict
analyse_capabilities_body_from_dict = AnalyseCapabilitiesBody.from_dict(analyse_capabilities_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


