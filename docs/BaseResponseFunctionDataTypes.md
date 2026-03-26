# BaseResponseFunctionDataTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**FunctionDataTypes**](FunctionDataTypes.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_function_data_types import BaseResponseFunctionDataTypes

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseFunctionDataTypes from a JSON string
base_response_function_data_types_instance = BaseResponseFunctionDataTypes.from_json(json)
# print the JSON string representation of the object
print(BaseResponseFunctionDataTypes.to_json())

# convert the object into a dict
base_response_function_data_types_dict = base_response_function_data_types_instance.to_dict()
# create an instance of BaseResponseFunctionDataTypes from a dict
base_response_function_data_types_from_dict = BaseResponseFunctionDataTypes.from_dict(base_response_function_data_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


