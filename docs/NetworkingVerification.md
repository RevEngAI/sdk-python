# NetworkingVerification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence** | **str** | LLM&#39;s confidence in the verdict. Absent when verified is null. | [optional] 
**reasoning** | **str** | LLM&#39;s explanation for the verdict, or the reason verification could not be completed | 
**verified** | **bool** | Whether an LLM confirmed the finding against its decompilation; null if verification could not be completed, in which case the finding is kept unverified rather than dropped | 

## Example

```python
from revengai.models.networking_verification import NetworkingVerification

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingVerification from a JSON string
networking_verification_instance = NetworkingVerification.from_json(json)
# print the JSON string representation of the object
print(NetworkingVerification.to_json())

# convert the object into a dict
networking_verification_dict = networking_verification_instance.to_dict()
# create an instance of NetworkingVerification from a dict
networking_verification_from_dict = NetworkingVerification.from_dict(networking_verification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


