# SecurityModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_container** | **bool** |  | 
**aslr** | **bool** |  | 
**bound_image** | **bool** |  | 
**cfg** | **bool** |  | 
**code_integrity** | **bool** |  | 
**dep** | **bool** |  | 
**driver_model** | **bool** |  | 
**high_entropy** | **bool** |  | 
**image_isolation** | **bool** |  | 
**seh** | **bool** |  | 
**terminal_server_aware** | **bool** |  | 

## Example

```python
from revengai.models.security_model import SecurityModel

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityModel from a JSON string
security_model_instance = SecurityModel.from_json(json)
# print the JSON string representation of the object
print(SecurityModel.to_json())

# convert the object into a dict
security_model_dict = security_model_instance.to_dict()
# create an instance of SecurityModel from a dict
security_model_from_dict = SecurityModel.from_dict(security_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


