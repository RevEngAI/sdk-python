# CallChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **List[int]** |  | 

## Example

```python
from revengai.models.call_chain import CallChain

# TODO update the JSON string below
json = "{}"
# create an instance of CallChain from a JSON string
call_chain_instance = CallChain.from_json(json)
# print the JSON string representation of the object
print(CallChain.to_json())

# convert the object into a dict
call_chain_dict = call_chain_instance.to_dict()
# create an instance of CallChain from a dict
call_chain_from_dict = CallChain.from_dict(call_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


