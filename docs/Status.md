# Status


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Machine-readable error code, shared with synchronous API errors. | 
**detail** | **str** | Additional context where helpful (quota numbers, validation specifics, etc.). | [optional] 
**doc_url** | **str** | Link to documentation explaining this error and resolution steps. | 
**message** | **str** | Brief description of the failure. | 

## Example

```python
from revengai.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print(Status.to_json())

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


