# ListExampleAnalysesOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyses** | [**List[Example]**](Example.md) | List of example analyses | 

## Example

```python
from revengai.models.list_example_analyses_output_body import ListExampleAnalysesOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListExampleAnalysesOutputBody from a JSON string
list_example_analyses_output_body_instance = ListExampleAnalysesOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListExampleAnalysesOutputBody.to_json())

# convert the object into a dict
list_example_analyses_output_body_dict = list_example_analyses_output_body_instance.to_dict()
# create an instance of ListExampleAnalysesOutputBody from a dict
list_example_analyses_output_body_from_dict = ListExampleAnalysesOutputBody.from_dict(list_example_analyses_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


