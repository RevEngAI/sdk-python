# ApiCall


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**called_from** | **str** |  | [optional] 
**called_from_rva** | **str** |  | [optional] 
**from_module** | **str** |  | [optional] 
**method** | **str** |  | 

## Example

```python
from revengai.models.api_call import ApiCall

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCall from a JSON string
api_call_instance = ApiCall.from_json(json)
# print the JSON string representation of the object
print(ApiCall.to_json())

# convert the object into a dict
api_call_dict = api_call_instance.to_dict()
# create an instance of ApiCall from a dict
api_call_from_dict = ApiCall.from_dict(api_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


