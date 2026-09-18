# CryptoExplainMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_history** | **List[List[object]]** | Progress messages the run recorded, oldest first. | [optional] 
**status** | **str** | Run status. UNINITIALISED means the agent has never been triggered for this function. | 

## Example

```python
from revengai.models.crypto_explain_metadata import CryptoExplainMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CryptoExplainMetadata from a JSON string
crypto_explain_metadata_instance = CryptoExplainMetadata.from_json(json)
# print the JSON string representation of the object
print(CryptoExplainMetadata.to_json())

# convert the object into a dict
crypto_explain_metadata_dict = crypto_explain_metadata_instance.to_dict()
# create an instance of CryptoExplainMetadata from a dict
crypto_explain_metadata_from_dict = CryptoExplainMetadata.from_dict(crypto_explain_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


