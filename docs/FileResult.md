# FileResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**matches** | [**List[RuleMatch]**](RuleMatch.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**status** | **str** |  | 

## Example

```python
from revengai.models.file_result import FileResult

# TODO update the JSON string below
json = "{}"
# create an instance of FileResult from a JSON string
file_result_instance = FileResult.from_json(json)
# print the JSON string representation of the object
print(FileResult.to_json())

# convert the object into a dict
file_result_dict = file_result_instance.to_dict()
# create an instance of FileResult from a dict
file_result_from_dict = FileResult.from_dict(file_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


