# TokenInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key to exchange for a JWT | [optional] 
**email** | **str** | User email address (required with password) | [optional] 
**password** | **str** | User password (required with email or username) | [optional] 
**username** | **str** | Username (alternative to email, required with password) | [optional] 

## Example

```python
from revengai.models.token_input_body import TokenInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of TokenInputBody from a JSON string
token_input_body_instance = TokenInputBody.from_json(json)
# print the JSON string representation of the object
print(TokenInputBody.to_json())

# convert the object into a dict
token_input_body_dict = token_input_body_instance.to_dict()
# create an instance of TokenInputBody from a dict
token_input_body_from_dict = TokenInputBody.from_dict(token_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


