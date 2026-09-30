# ResendVerificationEmailInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email address of the account to resend a verification code to | 

## Example

```python
from revengai.models.resend_verification_email_input_body import ResendVerificationEmailInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of ResendVerificationEmailInputBody from a JSON string
resend_verification_email_input_body_instance = ResendVerificationEmailInputBody.from_json(json)
# print the JSON string representation of the object
print(ResendVerificationEmailInputBody.to_json())

# convert the object into a dict
resend_verification_email_input_body_dict = resend_verification_email_input_body_instance.to_dict()
# create an instance of ResendVerificationEmailInputBody from a dict
resend_verification_email_input_body_from_dict = ResendVerificationEmailInputBody.from_dict(resend_verification_email_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


