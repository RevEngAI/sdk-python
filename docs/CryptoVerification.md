# CryptoVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **str** | LLM&#39;s confidence in the verdict. Absent when verified is null. | [optional] 
**reasoning** | **str** | LLM&#39;s explanation for the verdict, or the reason verification could not be completed | 
**verified** | **bool** | Whether an LLM confirmed the finding against its decompilation; null if verification could not be completed, in which case the finding is kept unverified rather than dropped | 

## Example

```python
from revengai.models.crypto_verification import CryptoVerification

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoVerification from a JSON string
crypto_verification_instance = CryptoVerification.from_json(json)
# print the JSON string representation of the object
print(CryptoVerification.to_json())

# convert the object into a dict
crypto_verification_dict = crypto_verification_instance.to_dict()
# create an instance of CryptoVerification from a dict
crypto_verification_from_dict = CryptoVerification.from_dict(crypto_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


