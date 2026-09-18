# UploadOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis_requirements** | [**List[AnalysisRequirement]**](AnalysisRequirement.md) | Ways to unblock POST /v3/analyses for this file if it cannot be statically analysed as-is; empty if no requirement applies. | 
**can_extract** | **bool** | Whether the firmware/extraction flow can accept this file. | 
**can_sandbox** | **bool** | Whether the file can be extracted and run in the Windows sandbox. | 
**file_type** | **str** | The kind of file that was uploaded. | 
**filename** | **str** | The filename as given by the caller. | 
**is_archive** | **bool** | Whether the detected format is a container/compression archive. | 
**mime** | **str** | The MIME type detected from the file&#39;s contents, independent of upload_file_type. | 
**sha_256_hash** | **str** | SHA-256 hash of the uploaded file; the storage key for every subsequent reference to it. | 

## Example

```python
from revengai.models.upload_output_body import UploadOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of UploadOutputBody from a JSON string
upload_output_body_instance = UploadOutputBody.from_json(json)
# print the JSON string representation of the object
print(UploadOutputBody.to_json())

# convert the object into a dict
upload_output_body_dict = upload_output_body_instance.to_dict()
# create an instance of UploadOutputBody from a dict
upload_output_body_from_dict = UploadOutputBody.from_dict(upload_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


