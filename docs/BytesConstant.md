# BytesConstant

One exact, contiguous sequence of binary bytes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] [default to 'bytes']
**value** | **str** | Hexadecimal byte pairs representing one exact, contiguous binary value. | 
**display** | [**Display**](Display.md) |  | [optional] 

## Example

```python
from revengai.models.bytes_constant import BytesConstant

# TODO update the JSON string below
json = "{}"
# create an instance of BytesConstant from a JSON string
bytes_constant_instance = BytesConstant.from_json(json)
# print the JSON string representation of the object
print(BytesConstant.to_json())

# convert the object into a dict
bytes_constant_dict = bytes_constant_instance.to_dict()
# create an instance of BytesConstant from a dict
bytes_constant_from_dict = BytesConstant.from_dict(bytes_constant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


