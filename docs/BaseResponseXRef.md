# BaseResponseXRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool** | Response status on whether the request succeeded | [optional] [default to True]
**data** | [**XRef**](XRef.md) |  | [optional] 
**message** | **str** |  | [optional] 
**errors** | [**List[ErrorModel]**](ErrorModel.md) |  | [optional] 
**meta** | [**MetaModel**](MetaModel.md) | Metadata | [optional] 

## Example

```python
from revengai.models.base_response_x_ref import BaseResponseXRef

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponseXRef from a JSON string
base_response_x_ref_instance = BaseResponseXRef.from_json(json)
# print the JSON string representation of the object
print(BaseResponseXRef.to_json())

# convert the object into a dict
base_response_x_ref_dict = base_response_x_ref_instance.to_dict()
# create an instance of BaseResponseXRef from a dict
base_response_x_ref_from_dict = BaseResponseXRef.from_dict(base_response_x_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


