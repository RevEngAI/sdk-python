# CreateURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_id** | **int** |  | 
**binary_id** | **int** |  | 
**sha_256_hash** | **str** |  | 

## Example

```python
from revengai.models.create_url_response import CreateURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateURLResponse from a JSON string
create_url_response_instance = CreateURLResponse.from_json(json)
# print the JSON string representation of the object
print(CreateURLResponse.to_json())

# convert the object into a dict
create_url_response_dict = create_url_response_instance.to_dict()
# create an instance of CreateURLResponse from a dict
create_url_response_from_dict = CreateURLResponse.from_dict(create_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


