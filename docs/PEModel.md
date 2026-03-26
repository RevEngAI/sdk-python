# PEModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**architecture** | **str** |  | 
**checksum** | **int** |  | 
**debug_info** | [**PDBDebugModel**](PDBDebugModel.md) |  | 
**debug_stripped** | **bool** |  | 
**dotnet** | **bool** |  | 
**entry_point** | [**EntrypointModel**](EntrypointModel.md) |  | 
**export_hash** | **str** |  | 
**exports** | [**ExportModel**](ExportModel.md) |  | 
**icon_data** | [**IconModel**](IconModel.md) |  | 
**image_base** | **int** |  | 
**import_hash** | **str** |  | 
**imports** | [**ImportModel**](ImportModel.md) |  | 
**number_of_resources** | **int** |  | 
**rich_header_hash** | **str** |  | 
**sections** | [**SectionModel**](SectionModel.md) |  | 
**security** | [**SecurityModel**](SecurityModel.md) |  | 
**signature** | [**CodeSignatureModel**](CodeSignatureModel.md) |  | 
**timestamps** | [**TimestampModel**](TimestampModel.md) |  | 
**type** | **str** |  | 
**version_info** | **Dict[str, object]** |  | 

## Example

```python
from revengai.models.pe_model import PEModel

# TODO update the JSON string below
json = "{}"
# create an instance of PEModel from a JSON string
pe_model_instance = PEModel.from_json(json)
# print the JSON string representation of the object
print(PEModel.to_json())

# convert the object into a dict
pe_model_dict = pe_model_instance.to_dict()
# create an instance of PEModel from a dict
pe_model_from_dict = PEModel.from_dict(pe_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


