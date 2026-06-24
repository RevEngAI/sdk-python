# LocationOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country name | 
**country_code** | **str** | ISO 3166-1 alpha-2 country code | 
**currency** | **str** | Currency code for this location | 

## Example

```python
from revengai.models.location_output_body import LocationOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of LocationOutputBody from a JSON string
location_output_body_instance = LocationOutputBody.from_json(json)
# print the JSON string representation of the object
print(LocationOutputBody.to_json())

# convert the object into a dict
location_output_body_dict = location_output_body_instance.to_dict()
# create an instance of LocationOutputBody from a dict
location_output_body_from_dict = LocationOutputBody.from_dict(location_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


