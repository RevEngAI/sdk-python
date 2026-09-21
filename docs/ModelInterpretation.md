# ModelInterpretation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interpretation** | **str** |  | [optional] 

## Example

```python
from revengai.models.model_interpretation import ModelInterpretation

# TODO update the JSON string below
json = "{}"
# create an instance of ModelInterpretation from a JSON string
model_interpretation_instance = ModelInterpretation.from_json(json)
# print the JSON string representation of the object
print(ModelInterpretation.to_json())

# convert the object into a dict
model_interpretation_dict = model_interpretation_instance.to_dict()
# create an instance of ModelInterpretation from a dict
model_interpretation_from_dict = ModelInterpretation.from_dict(model_interpretation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


