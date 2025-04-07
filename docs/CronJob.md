# CronJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minute** | **str** | The minute(s) at which the command will be executed or a special @ event string. (0-59, ranges, divided, @ event or delay, *&#x3D;all). When using a special @ event, such as @reboot, the other time fields must be empty.&lt;br&gt; | [optional] 
**hour** | **str** | The hour(s) at which the command will be executed. (0-23, ranges, or divided, *&#x3D;all)&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;minute&#x60; must not be one of [ @reboot, @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute, @every_second ]&lt;br&gt; | [optional] 
**mday** | **str** | The day(s) of the month on which the command will be executed. (1-31, ranges, or divided, *&#x3D;all).&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;minute&#x60; must not be one of [ @reboot, @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute, @every_second ]&lt;br&gt; | [optional] 
**month** | **str** | The month(s) of the year in which the command will be executed. (1-31, ranges, or divided, *&#x3D;all).&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;minute&#x60; must not be one of [ @reboot, @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute, @every_second ]&lt;br&gt; | [optional] 
**wday** | **str** | The day(s) of the week on which the command will be executed. (0-7, 7&#x3D;Sun or use names, ranges, or divided, *&#x3D;all).&lt;br&gt;&lt;br&gt;This field is only available when the following conditions are met:&lt;br&gt;- &#x60;minute&#x60; must not be one of [ @reboot, @yearly, @annually, @monthly, @weekly, @daily, @midnight, @hourly, @every_minute, @every_second ]&lt;br&gt; | [optional] 
**who** | **str** | The OS user to use when cron runs the command.&lt;br&gt; | [optional] 
**command** | **str** | The command to run. Use full file paths for this command and include an command parameters.&lt;br&gt; | [optional] 

## Example

```python
from pfsense_api_client.models.cron_job import CronJob

# TODO update the JSON string below
json = "{}"
# create an instance of CronJob from a JSON string
cron_job_instance = CronJob.from_json(json)
# print the JSON string representation of the object
print(CronJob.to_json())

# convert the object into a dict
cron_job_dict = cron_job_instance.to_dict()
# create an instance of CronJob from a dict
cron_job_from_dict = CronJob.from_dict(cron_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


