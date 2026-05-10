# ServiceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary_path** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**name** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**start_type** | **str** |  | [optional] 

## Example

```python
from revengai.models.service_entry import ServiceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEntry from a JSON string
service_entry_instance = ServiceEntry.from_json(json)
# print the JSON string representation of the object
print(ServiceEntry.to_json())

# convert the object into a dict
service_entry_dict = service_entry_instance.to_dict()
# create an instance of ServiceEntry from a dict
service_entry_from_dict = ServiceEntry.from_dict(service_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


