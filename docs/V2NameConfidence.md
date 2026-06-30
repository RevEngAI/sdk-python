# V2NameConfidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The suggested function name | 
**confidence** | **float** | Confidence score as a percentage | 

## Example

```python
from revengai.models.v2_name_confidence import V2NameConfidence

# TODO update the JSON string below
json = "{}"
# create an instance of V2NameConfidence from a JSON string
v2_name_confidence_instance = V2NameConfidence.from_json(json)
# print the JSON string representation of the object
print(V2NameConfidence.to_json())

# convert the object into a dict
v2_name_confidence_dict = v2_name_confidence_instance.to_dict()
# create an instance of V2NameConfidence from a dict
v2_name_confidence_from_dict = V2NameConfidence.from_dict(v2_name_confidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


