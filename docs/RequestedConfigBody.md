# RequestedConfigBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capabilities** | **bool** | Whether the capabilities agent was requested | 
**functions** | **bool** | Whether the functions pipeline was requested | 
**sandbox** | **bool** | Whether dynamic execution (sandbox) was requested | 
**scrape** | **bool** | Whether external-source scraping was requested | 
**triage** | **bool** | Whether the triage agent was requested | 

## Example

```python
from revengai.models.requested_config_body import RequestedConfigBody

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedConfigBody from a JSON string
requested_config_body_instance = RequestedConfigBody.from_json(json)
# print the JSON string representation of the object
print(RequestedConfigBody.to_json())

# convert the object into a dict
requested_config_body_dict = requested_config_body_instance.to_dict()
# create an instance of RequestedConfigBody from a dict
requested_config_body_from_dict = RequestedConfigBody.from_dict(requested_config_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


