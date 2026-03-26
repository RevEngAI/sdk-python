# BaseResponseBool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **bool** |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_bool import BaseResponseBool

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseBool from a JSON string
base_response_bool_instance = BaseResponseBool.from_json(json)
# print the JSON string representation of the object
print(BaseResponseBool.to_json())

# convert the object into a dict
base_response_bool_dict = base_response_bool_instance.to_dict()
# create an instance of BaseResponseBool from a dict
base_response_bool_from_dict = BaseResponseBool.from_dict(base_response_bool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


