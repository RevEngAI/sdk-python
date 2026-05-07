# HttpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**extra_headers** | **List[str]** |  | [optional] 
**flags** | **int** |  | [optional] 
**password** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**post_data** | **str** |  | [optional] 
**proxy** | **str** |  | [optional] 
**proxy_bypass** | **str** |  | [optional] 
**referer** | **str** |  | [optional] 
**server_name** | **str** |  | [optional] 
**server_port** | **int** |  | [optional] 
**service** | **int** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verb** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from revengai.models.http_request import HttpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HttpRequest from a JSON string
http_request_instance = HttpRequest.from_json(json)
# print the JSON string representation of the object
print(HttpRequest.to_json())

# convert the object into a dict
http_request_dict = http_request_instance.to_dict()
# create an instance of HttpRequest from a dict
http_request_from_dict = HttpRequest.from_dict(http_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


