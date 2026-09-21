# CreateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** | Analysis ID | 
**binary_id** | **int** | Binary ID | 

## Example

```python
from revengai.models.create_result import CreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResult from a JSON string
create_result_instance = CreateResult.from_json(json)
# print the JSON string representation of the object
print(CreateResult.to_json())

# convert the object into a dict
create_result_dict = create_result_instance.to_dict()
# create an instance of CreateResult from a dict
create_result_from_dict = CreateResult.from_dict(create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


