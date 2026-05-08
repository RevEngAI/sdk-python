# ProcessMemdumps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dumps** | [**List[MemdumpEntry]**](MemdumpEntry.md) |  | [optional] 
**process_seqid** | **int** |  | 

## Example

```python
from revengai.models.process_memdumps import ProcessMemdumps

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessMemdumps from a JSON string
process_memdumps_instance = ProcessMemdumps.from_json(json)
# print the JSON string representation of the object
print(ProcessMemdumps.to_json())

# convert the object into a dict
process_memdumps_dict = process_memdumps_instance.to_dict()
# create an instance of ProcessMemdumps from a dict
process_memdumps_from_dict = ProcessMemdumps.from_dict(process_memdumps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


