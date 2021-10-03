# human_time
Make Python datetime formatting human readable

```python
from datetime import datetime
import human_time
time_string = "MONTH_LONG DAY_OF_MONTH, YEAR_LONG HOUR_12:MINUTE AM_PM"

datetime_value = datetime.now()
print(human_time.format(time_string, datetime_value))
# October 03, 2021 02:20 PM
```