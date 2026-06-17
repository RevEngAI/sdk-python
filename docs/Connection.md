# Connection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_received** | **int** |  | [optional] 
**bytes_sent** | **int** |  | [optional] 
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**ja3** | **str** |  | [optional] 
**ja3s** | **str** |  | [optional] 
**local_ip** | **str** |  | 
**local_port** | **object** |  | 
**protocol** | **str** |  | 
**remote_ip** | **str** |  | 
**remote_port** | **object** |  | 
**tcp_carved_files** | [**List[TcpCarvedFile]**](TcpCarvedFile.md) |  | [optional] 

## Example

```python
from revengai.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


