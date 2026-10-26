# RequeueAnalysisRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_line_args** | **str** | Command-line arguments passed to the sample when enable_dynamic_execution is set | [optional] 
**enable_dynamic_execution** | **bool** | Run the new Analysis with dynamic execution (sandbox) enabled | [optional] 
**generate_capabilities** | **bool** | Regenerate capabilities for the new Analysis instead of copying the original Binary&#39;s existing ones | [optional] 
**no_cache** | **bool** |  | [optional] 
**scrape_tags** | **bool** | Re-scrape third-party tags for the new Analysis instead of copying the original Binary&#39;s existing ones | [optional] 
**tags** | **List[Optional[str]]** | Additional Tags to apply to the requeued Binary, on top of any carried over because generate_capabilities/scrape_tags are false | [optional] 

## Example

```python
from revengai.models.requeue_analysis_request import RequeueAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequeueAnalysisRequest from a JSON string
requeue_analysis_request_instance = RequeueAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(RequeueAnalysisRequest.to_json())

# convert the object into a dict
requeue_analysis_request_dict = requeue_analysis_request_instance.to_dict()
# create an instance of RequeueAnalysisRequest from a dict
requeue_analysis_request_from_dict = RequeueAnalysisRequest.from_dict(requeue_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


