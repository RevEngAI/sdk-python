# NameConfidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **float** | Confidence score as a percentage | 
**name** | **str** | The suggested function name | 

## Example

```python
from revengai.models.name_confidence import NameConfidence

# TODO update the JSON string below
json = "{}"
# create an instance of NameConfidence from a JSON string
name_confidence_instance = NameConfidence.from_json(json)
# print the JSON string representation of the object
print(NameConfidence.to_json())

# convert the object into a dict
name_confidence_dict = name_confidence_instance.to_dict()
# create an instance of NameConfidence from a dict
name_confidence_from_dict = NameConfidence.from_dict(name_confidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


