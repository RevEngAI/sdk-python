# MITRETechnique


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_addr** | **str** | Starting address of the technique | 
**end_addr** | **str** | Ending address of the technique | 
**function_addr** | **str** | Function address where the technique is found | 
**technique_id** | **str** | MITRE technique identifier | 
**technique_name** | **str** | Name of the MITRE technique | 
**description** | **str** | Description of the technique | 
**function_id** | **int** | Unique identifier of the function containing the technique | 
**function_name** | **str** | Name of the function containing the technique | 
**technique_url** | **str** | URL to the MITRE ATT&amp;CK technique page | 
**technique_description** | **str** | Full description of the MITRE technique from ATT&amp;CK | 

## Example

```python
from revengai.models.mitre_technique import MITRETechnique

# TODO update the JSON string below
json = "{}"
# create an instance of MITRETechnique from a JSON string
mitre_technique_instance = MITRETechnique.from_json(json)
# print the JSON string representation of the object
print(MITRETechnique.to_json())

# convert the object into a dict
mitre_technique_dict = mitre_technique_instance.to_dict()
# create an instance of MITRETechnique from a dict
mitre_technique_from_dict = MITRETechnique.from_dict(mitre_technique_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


