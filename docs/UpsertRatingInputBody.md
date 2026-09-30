# UpsertRatingInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **str** | How useful the caller found this AI decompilation | 
**reason** | **str** | Optional free-text reason for the rating | [optional] 

## Example

```python
from revengai.models.upsert_rating_input_body import UpsertRatingInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpsertRatingInputBody from a JSON string
upsert_rating_input_body_instance = UpsertRatingInputBody.from_json(json)
# print the JSON string representation of the object
print(UpsertRatingInputBody.to_json())

# convert the object into a dict
upsert_rating_input_body_dict = upsert_rating_input_body_instance.to_dict()
# create an instance of UpsertRatingInputBody from a dict
upsert_rating_input_body_from_dict = UpsertRatingInputBody.from_dict(upsert_rating_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


