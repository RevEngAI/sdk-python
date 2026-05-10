# DnsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | 
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 

## Example

```python
from revengai.models.dns_query import DnsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DnsQuery from a JSON string
dns_query_instance = DnsQuery.from_json(json)
# print the JSON string representation of the object
print(DnsQuery.to_json())

# convert the object into a dict
dns_query_dict = dns_query_instance.to_dict()
# create an instance of DnsQuery from a dict
dns_query_from_dict = DnsQuery.from_dict(dns_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


