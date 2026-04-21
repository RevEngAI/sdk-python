# IOC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the IOC | 
**value** | **str** | Value of the IOC | 
**description** | **str** | Description of the IOC | 
**source** | **str** |  | [optional] 
**function_id** | **int** |  | [optional] 
**function_name** | **str** |  | [optional] 

## Example

```python
from revengai.models.ioc import IOC

# TODO update the JSON string below
json = "{}"
# create an instance of IOC from a JSON string
ioc_instance = IOC.from_json(json)
# print the JSON string representation of the object
print(IOC.to_json())

# convert the object into a dict
ioc_dict = ioc_instance.to_dict()
# create an instance of IOC from a dict
ioc_from_dict = IOC.from_dict(ioc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


