# NetworkingFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Function&#39;s virtual address, hex-encoded | 
**categories** | **List[str]** | Distinct networking categories evidenced by this function | 
**confidence** | **str** | High when a direct name match was found, medium when the function only calls into networking APIs | 
**direct_matches** | [**List[NetworkingDirectMatch]**](NetworkingDirectMatch.md) | Matches against the function&#39;s own name | [optional] 
**evidence_count** | **int** | Total number of direct matches and network calls | 
**function_id** | **int** | ID of the function the finding was reported in | 
**function_name** | **str** | Name of the function the finding was reported in | 
**function_size** | **int** | Size of the function in bytes | 
**network_calls** | [**List[NetworkingCall]**](NetworkingCall.md) | Matches against names this function calls | [optional] 
**remote** | **bool** | Whether this function evidences remote communication rather than only supporting it | 
**sources** | **List[str]** | Distinct networking sources evidenced by this function | 
**verification** | [**NetworkingVerification**](NetworkingVerification.md) | LLM verdict checking this finding against its decompilation. Present only when the run verified this finding. | [optional] 

## Example

```python
from revengai.models.networking_finding import NetworkingFinding

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingFinding from a JSON string
networking_finding_instance = NetworkingFinding.from_json(json)
# print the JSON string representation of the object
print(NetworkingFinding.to_json())

# convert the object into a dict
networking_finding_dict = networking_finding_instance.to_dict()
# create an instance of NetworkingFinding from a dict
networking_finding_from_dict = NetworkingFinding.from_dict(networking_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


