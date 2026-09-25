# SoftwareTypeCountsBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benign** | **int** | Reports classifying the software as benign | 
**legitimate** | **int** | Reports classifying the software as legitimate | 
**legitimate_software_backdoor** | **int** | Reports classifying the software as a legitimate backdoor | 
**malicious** | **int** | Reports classifying the software as malicious | 
**potentially_unwanted_application** | **int** | Reports classifying the software as a potentially unwanted application | 

## Example

```python
from revengai.models.software_type_counts_body import SoftwareTypeCountsBody

# TODO update the JSON string below
json = "{}"
# create an instance of SoftwareTypeCountsBody from a JSON string
software_type_counts_body_instance = SoftwareTypeCountsBody.from_json(json)
# print the JSON string representation of the object
print(SoftwareTypeCountsBody.to_json())

# convert the object into a dict
software_type_counts_body_dict = software_type_counts_body_instance.to_dict()
# create an instance of SoftwareTypeCountsBody from a dict
software_type_counts_body_from_dict = SoftwareTypeCountsBody.from_dict(software_type_counts_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


