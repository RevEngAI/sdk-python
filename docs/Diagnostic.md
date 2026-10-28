# Diagnostic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | YARA-X diagnostic code | 
**column** | **int** | 1-based column, when known | 
**line** | **int** | 1-based line, when known | 
**text** | **str** | Full diagnostic report | 
**title** | **str** | Short description | 

## Example

```python
from revengai.models.diagnostic import Diagnostic

# TODO update the JSON string below
json = "{}"
# create an instance of Diagnostic from a JSON string
diagnostic_instance = Diagnostic.from_json(json)
# print the JSON string representation of the object
print(Diagnostic.to_json())

# convert the object into a dict
diagnostic_dict = diagnostic_instance.to_dict()
# create an instance of Diagnostic from a dict
diagnostic_from_dict = Diagnostic.from_dict(diagnostic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


