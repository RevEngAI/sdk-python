# LineAttributionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disassembly_line_number_to_ai_decompilation_line_numbers** | **Dict[str, Optional[List[int]]]** | Each disassembly line number mapped to the AI-decompilation line numbers it fed, e.g. {\&quot;12\&quot;: [3, 4, 6], \&quot;17\&quot;: [4]}. Both sides 0-based; many-to-many in both directions. Empty when no completed run has produced a correspondence, which is ordinary and not an error. | 

## Example

```python
from revengai.models.line_attributions_data import LineAttributionsData

# TODO update the JSON string below
json = "{}"
# create an instance of LineAttributionsData from a JSON string
line_attributions_data_instance = LineAttributionsData.from_json(json)
# print the JSON string representation of the object
print(LineAttributionsData.to_json())

# convert the object into a dict
line_attributions_data_dict = line_attributions_data_instance.to_dict()
# create an instance of LineAttributionsData from a dict
line_attributions_data_from_dict = LineAttributionsData.from_dict(line_attributions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


