# BaseResponseTaskResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TaskResponse**](TaskResponse.md) |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**message** | **str** |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]

## Example

```python
from revengai.models.base_response_task_response import BaseResponseTaskResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseTaskResponse from a JSON string
base_response_task_response_instance = BaseResponseTaskResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponseTaskResponse.to_json())

# convert the object into a dict
base_response_task_response_dict = base_response_task_response_instance.to_dict()
# create an instance of BaseResponseTaskResponse from a dict
base_response_task_response_from_dict = BaseResponseTaskResponse.from_dict(base_response_task_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


