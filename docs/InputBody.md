# InputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password to decrypt an encrypted archive. | [optional] 

## Example

```python
from revengai.models.input_body import InputBody

# TODO update the JSON string below
json = "{}"
# create an instance of InputBody from a JSON string
input_body_instance = InputBody.from_json(json)
# print the JSON string representation of the object
print(InputBody.to_json())

# convert the object into a dict
input_body_dict = input_body_instance.to_dict()
# create an instance of InputBody from a dict
input_body_from_dict = InputBody.from_dict(input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


