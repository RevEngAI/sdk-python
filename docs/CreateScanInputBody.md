# CreateScanInputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**binary_ids** | **List[int]** | IDs of ingested binaries to scan instead of a dataset | [optional] 
**bypass_cache** | **bool** | When true, ignore and do not populate the shared result cache | [optional] 
**collection_id** | **int** | Scan with a rule collection instead of rules | [optional] 
**dataset** | **str** | Named dataset to scan. Provide this or targets (shas/binary_ids), not both. | [optional] 
**mode** | **str** | Force the run mode; auto routes by dataset size | [optional] [default to 'auto']
**omit_strings** | **bool** | When true, per-pattern offsets are omitted | [optional] 
**per_file_timeout_ms** | **int** | Override the per-file scan timeout (ms); 0 &#x3D; default | [optional] 
**rules** | [**List[ScanRuleInput]**](ScanRuleInput.md) | Rules to scan with (inline and/or library references). Provide this or collection_id, not both. | [optional] 
**shas** | **List[str]** | Content sha256 hashes of ingested binaries to scan instead of a dataset | [optional] 

## Example

```python
from revengai.models.create_scan_input_body import CreateScanInputBody

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScanInputBody from a JSON string
create_scan_input_body_instance = CreateScanInputBody.from_json(json)
# print the JSON string representation of the object
print(CreateScanInputBody.to_json())

# convert the object into a dict
create_scan_input_body_dict = create_scan_input_body_instance.to_dict()
# create an instance of CreateScanInputBody from a dict
create_scan_input_body_from_dict = CreateScanInputBody.from_dict(create_scan_input_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


