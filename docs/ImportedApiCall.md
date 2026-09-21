# ImportedApiCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**imported_api** | [**ImportedApi**](ImportedApi.md) |  | 
**subject** | [**Subject**](Subject.md) |  | 
**reachability** | [**CallChain**](CallChain.md) |  | [optional] 

## Example

```python
from revengai.models.imported_api_call import ImportedApiCall

# TODO update the JSON string below
json = "{}"
# create an instance of ImportedApiCall from a JSON string
imported_api_call_instance = ImportedApiCall.from_json(json)
# print the JSON string representation of the object
print(ImportedApiCall.to_json())

# convert the object into a dict
imported_api_call_dict = imported_api_call_instance.to_dict()
# create an instance of ImportedApiCall from a dict
imported_api_call_from_dict = ImportedApiCall.from_dict(imported_api_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


