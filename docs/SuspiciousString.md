# SuspiciousString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | 
**subject** | [**Subject**](Subject.md) |  | [optional] 

## Example

```python
from revengai.models.suspicious_string import SuspiciousString

# TODO update the JSON string below
json = "{}"
# create an instance of SuspiciousString from a JSON string
suspicious_string_instance = SuspiciousString.from_json(json)
# print the JSON string representation of the object
print(SuspiciousString.to_json())

# convert the object into a dict
suspicious_string_dict = suspicious_string_instance.to_dict()
# create an instance of SuspiciousString from a dict
suspicious_string_from_dict = SuspiciousString.from_dict(suspicious_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


