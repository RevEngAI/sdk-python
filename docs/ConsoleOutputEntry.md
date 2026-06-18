# ConsoleOutputEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output** | **str** |  | 
**process_seqid** | **int** |  | 

## Example

```python
from revengai.models.console_output_entry import ConsoleOutputEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ConsoleOutputEntry from a JSON string
console_output_entry_instance = ConsoleOutputEntry.from_json(json)
# print the JSON string representation of the object
print(ConsoleOutputEntry.to_json())

# convert the object into a dict
console_output_entry_dict = console_output_entry_instance.to_dict()
# create an instance of ConsoleOutputEntry from a dict
console_output_entry_from_dict = ConsoleOutputEntry.from_dict(console_output_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


