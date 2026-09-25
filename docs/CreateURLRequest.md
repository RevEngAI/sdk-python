# CreateURLRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_scope** | **str** |  | [optional] [default to 'PRIVATE']
**url** | **str** |  | 

## Example

```python
from revengai.models.create_url_request import CreateURLRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateURLRequest from a JSON string
create_url_request_instance = CreateURLRequest.from_json(json)
# print the JSON string representation of the object
print(CreateURLRequest.to_json())

# convert the object into a dict
create_url_request_dict = create_url_request_instance.to_dict()
# create an instance of CreateURLRequest from a dict
create_url_request_from_dict = CreateURLRequest.from_dict(create_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


