# ProcessNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **List[str]** |  | [optional] 
**attributed** | **bool** |  | 
**children** | [**List[ProcessNode]**](ProcessNode.md) |  | [optional] 
**exit_code** | **int** |  | [optional] 
**exit_code_str** | **str** |  | [optional] 
**exited_at** | **float** |  | [optional] 
**killed_by** | **int** |  | [optional] 
**name** | **str** |  | 
**pid** | **int** |  | 
**seqid** | **int** |  | 
**started_at** | **float** |  | [optional] 

## Example

```python
from revengai.models.process_node import ProcessNode

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessNode from a JSON string
process_node_instance = ProcessNode.from_json(json)
# print the JSON string representation of the object
print(ProcessNode.to_json())

# convert the object into a dict
process_node_dict = process_node_instance.to_dict()
# create an instance of ProcessNode from a dict
process_node_from_dict = ProcessNode.from_dict(process_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


