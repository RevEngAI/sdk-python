# FunctionSignatureVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_at** | **datetime** | When this version was written. Absent on a version that predates the recorded history. | [optional] 
**updated_by** | [**HistoryActor**](HistoryActor.md) | Who wrote this version. Absent on a version that predates the recorded history. | [optional] 
**value** | [**FunctionSignatureEntry**](FunctionSignatureEntry.md) | The signature as it stood in this version. | 

## Example

```python
from revengai.models.function_signature_version import FunctionSignatureVersion

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionSignatureVersion from a JSON string
function_signature_version_instance = FunctionSignatureVersion.from_json(json)
# print the JSON string representation of the object
print(FunctionSignatureVersion.to_json())

# convert the object into a dict
function_signature_version_dict = function_signature_version_instance.to_dict()
# create an instance of FunctionSignatureVersion from a dict
function_signature_version_from_dict = FunctionSignatureVersion.from_dict(function_signature_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


