# PcapBodyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**is_pe** | **bool** |  | 
**mime_type** | **str** |  | [optional] 
**preview** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**size** | **int** |  | 
**yara_hits** | **List[str]** |  | [optional] 

## Example

```python
from revengai.models.pcap_body_info import PcapBodyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PcapBodyInfo from a JSON string
pcap_body_info_instance = PcapBodyInfo.from_json(json)
# print the JSON string representation of the object
print(PcapBodyInfo.to_json())

# convert the object into a dict
pcap_body_info_dict = pcap_body_info_instance.to_dict()
# create an instance of PcapBodyInfo from a dict
pcap_body_info_from_dict = PcapBodyInfo.from_dict(pcap_body_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


