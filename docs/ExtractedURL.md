# ExtractedURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ReportEvent]**](ReportEvent.md) |  | [optional] 
**url** | **str** |  | 

## Example

```python
from revengai.models.extracted_url import ExtractedURL

# TODO update the JSON string below
json = "{}"
# create an instance of ExtractedURL from a JSON string
extracted_url_instance = ExtractedURL.from_json(json)
# print the JSON string representation of the object
print(ExtractedURL.to_json())

# convert the object into a dict
extracted_url_dict = extracted_url_instance.to_dict()
# create an instance of ExtractedURL from a dict
extracted_url_from_dict = ExtractedURL.from_dict(extracted_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


