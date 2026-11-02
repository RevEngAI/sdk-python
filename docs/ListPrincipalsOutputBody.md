# ListPrincipalsOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[PrincipalBody]**](PrincipalBody.md) | Up to 5 matching users followed by up to 5 matching teams, each ordered by name | 

## Example

```python
from revengai.models.list_principals_output_body import ListPrincipalsOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ListPrincipalsOutputBody from a JSON string
list_principals_output_body_instance = ListPrincipalsOutputBody.from_json(json)
# print the JSON string representation of the object
print(ListPrincipalsOutputBody.to_json())

# convert the object into a dict
list_principals_output_body_dict = list_principals_output_body_instance.to_dict()
# create an instance of ListPrincipalsOutputBody from a dict
list_principals_output_body_from_dict = ListPrincipalsOutputBody.from_dict(list_principals_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


