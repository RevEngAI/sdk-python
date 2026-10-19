# RenameUnnamedFunctionsMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first. | [optional] 
**status** | **str** | Run status. UNINITIALISED means the agent has never been triggered for this analysis. | 

## Example

```python
from revengai.models.rename_unnamed_functions_metadata import RenameUnnamedFunctionsMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RenameUnnamedFunctionsMetadata from a JSON string
rename_unnamed_functions_metadata_instance = RenameUnnamedFunctionsMetadata.from_json(json)
# print the JSON string representation of the object
print(RenameUnnamedFunctionsMetadata.to_json())

# convert the object into a dict
rename_unnamed_functions_metadata_dict = rename_unnamed_functions_metadata_instance.to_dict()
# create an instance of RenameUnnamedFunctionsMetadata from a dict
rename_unnamed_functions_metadata_from_dict = RenameUnnamedFunctionsMetadata.from_dict(rename_unnamed_functions_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


