# Technique


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | How the technique appears in this binary | 
**end_addr** | **str** | End address of the containing function, hex-encoded | 
**function_addr** | **str** | Address of the containing function, hex-encoded | 
**function_id** | **int** | ID of the containing function | 
**function_name** | **str** | Name of the containing function | 
**start_addr** | **str** | Start address of the containing function, hex-encoded | 
**technique_description** | **str** | Full ATT&amp;CK description of the technique | 
**technique_id** | **str** | MITRE ATT&amp;CK technique ID | 
**technique_name** | **str** | MITRE ATT&amp;CK technique name | 
**technique_url** | **str** | Link to the technique in the ATT&amp;CK catalogue | 

## Example

```python
from revengai.models.technique import Technique

# TODO update the JSON string below
json = "{}"
# create an instance of Technique from a JSON string
technique_instance = Technique.from_json(json)
# print the JSON string representation of the object
print(Technique.to_json())

# convert the object into a dict
technique_dict = technique_instance.to_dict()
# create an instance of Technique from a dict
technique_from_dict = Technique.from_dict(technique_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


