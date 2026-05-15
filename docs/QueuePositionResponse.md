# QueuePositionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queue_position** | **int** | Number of Processing analyses ahead of this one in the queue. 0 if this analysis is not Processing or has no analyses ahead of it. | 

## Example

```python
from revengai.models.queue_position_response import QueuePositionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueuePositionResponse from a JSON string
queue_position_response_instance = QueuePositionResponse.from_json(json)
# print the JSON string representation of the object
print(QueuePositionResponse.to_json())

# convert the object into a dict
queue_position_response_dict = queue_position_response_instance.to_dict()
# create an instance of QueuePositionResponse from a dict
queue_position_response_from_dict = QueuePositionResponse.from_dict(queue_position_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


