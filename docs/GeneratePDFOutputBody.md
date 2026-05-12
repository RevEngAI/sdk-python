# GeneratePDFOutputBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**already_running** | **bool** | True when an existing PDF generation is in progress for this analysis and user | [optional] 
**task_id** | **str** | Workflow task ID — use to poll status and download the PDF | 

## Example

```python
from revengai.models.generate_pdf_output_body import GeneratePDFOutputBody

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePDFOutputBody from a JSON string
generate_pdf_output_body_instance = GeneratePDFOutputBody.from_json(json)
# print the JSON string representation of the object
print(GeneratePDFOutputBody.to_json())

# convert the object into a dict
generate_pdf_output_body_dict = generate_pdf_output_body_instance.to_dict()
# create an instance of GeneratePDFOutputBody from a dict
generate_pdf_output_body_from_dict = GeneratePDFOutputBody.from_dict(generate_pdf_output_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


