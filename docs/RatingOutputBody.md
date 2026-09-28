# RatingOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **str** | The rating the caller recorded, or null when they have not rated it yet | 
**reason** | **str** | The reason the caller gave, or null | 

## Example

```python
from revengai.models.rating_output_body import RatingOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of RatingOutputBody from a JSON string
rating_output_body_instance = RatingOutputBody.from_json(json)
# print the JSON string representation of the object
print(RatingOutputBody.to_json())

# convert the object into a dict
rating_output_body_dict = rating_output_body_instance.to_dict()
# create an instance of RatingOutputBody from a dict
rating_output_body_from_dict = RatingOutputBody.from_dict(rating_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


