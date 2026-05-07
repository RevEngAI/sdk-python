# Ttp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attck** | **List[str]** |  | [optional] 
**mbc** | **List[object]** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**process_seqids** | **List[int]** |  | [optional] 
**score** | **int** |  | 

## Example

```python
from revengai.models.ttp import Ttp

# TODO update the JSON string below
json = "{}"
# create an instance of Ttp from a JSON string
ttp_instance = Ttp.from_json(json)
# print the JSON string representation of the object
print(Ttp.to_json())

# convert the object into a dict
ttp_dict = ttp_instance.to_dict()
# create an instance of Ttp from a dict
ttp_from_dict = Ttp.from_dict(ttp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


