# TcpCarvedFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** |  | 
**filename** | **str** |  | [optional] 
**is_pe** | **bool** |  | 
**mime_type** | **str** |  | [optional] 
**offset** | **int** |  | 
**sha256** | **str** |  | 
**size** | **int** |  | 
**yara_hits** | **List[str]** |  | [optional] 

## Example

```python
from revengai.models.tcp_carved_file import TcpCarvedFile

# TODO update the JSON string below
json = "{}"
# create an instance of TcpCarvedFile from a JSON string
tcp_carved_file_instance = TcpCarvedFile.from_json(json)
# print the JSON string representation of the object
print(TcpCarvedFile.to_json())

# convert the object into a dict
tcp_carved_file_dict = tcp_carved_file_instance.to_dict()
# create an instance of TcpCarvedFile from a dict
tcp_carved_file_from_dict = TcpCarvedFile.from_dict(tcp_carved_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


