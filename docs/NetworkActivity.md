# NetworkActivity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | [**List[Connection]**](Connection.md) |  | [optional] 
**dns_queries** | [**List[DnsQuery]**](DnsQuery.md) |  | [optional] 
**extracted_urls** | [**List[ExtractedURL]**](ExtractedURL.md) |  | [optional] 
**http_requests** | [**List[HttpRequest]**](HttpRequest.md) |  | [optional] 

## Example

```python
from revengai.models.network_activity import NetworkActivity

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkActivity from a JSON string
network_activity_instance = NetworkActivity.from_json(json)
# print the JSON string representation of the object
print(NetworkActivity.to_json())

# convert the object into a dict
network_activity_dict = network_activity_instance.to_dict()
# create an instance of NetworkActivity from a dict
network_activity_from_dict = NetworkActivity.from_dict(network_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


