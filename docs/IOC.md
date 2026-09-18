# IOC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What the indicator means | 
**function_id** | **int** | ID of the function it was found in. Null when the source does not resolve to one. | 
**function_name** | **str** | Name of the function it was found in. Null when the source does not resolve to one. | 
**source** | **str** | Where in the binary it was found, usually a hex address. Null when the agent did not report one. | 
**type** | **str** | Indicator type | 
**value** | **str** | The indicator itself | 

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


