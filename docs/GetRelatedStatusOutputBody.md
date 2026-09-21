# GetRelatedStatusOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status of the task that unpacks an archive into its contents | 

## Example

```python
from revengai.models.get_related_status_output_body import GetRelatedStatusOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GetRelatedStatusOutputBody from a JSON string
get_related_status_output_body_instance = GetRelatedStatusOutputBody.from_json(json)
# print the JSON string representation of the object
print(GetRelatedStatusOutputBody.to_json())

# convert the object into a dict
get_related_status_output_body_dict = get_related_status_output_body_instance.to_dict()
# create an instance of GetRelatedStatusOutputBody from a dict
get_related_status_output_body_from_dict = GetRelatedStatusOutputBody.from_dict(get_related_status_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


