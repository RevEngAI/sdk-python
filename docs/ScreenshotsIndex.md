# ScreenshotsIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**screenshots** | [**List[ScreenshotEntry]**](ScreenshotEntry.md) |  | 

## Example

```python
from revengai.models.screenshots_index import ScreenshotsIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ScreenshotsIndex from a JSON string
screenshots_index_instance = ScreenshotsIndex.from_json(json)
# print the JSON string representation of the object
print(ScreenshotsIndex.to_json())

# convert the object into a dict
screenshots_index_dict = screenshots_index_instance.to_dict()
# create an instance of ScreenshotsIndex from a dict
screenshots_index_from_dict = ScreenshotsIndex.from_dict(screenshots_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


