import pytz
import logging
from datetime import datetime
from line_profiler import LineProfiler
from datetime import timedelta

DATE_FORMAT = "%Y-%m-%d"
DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

class Example:
    def format_ds_utc_date(self, req_date, date_flag, time_zone):
        """
        Handles operations related to submitting ds request
        """
        try:
            if date_flag:
                if len(req_date) == 10:
                    native_date = datetime.strptime(req_date, DATE_FORMAT)
                elif len(req_date) == 19:
                    native_date = datetime.strptime(req_date, DATE_TIME_FORMAT)
            else:
                if len(req_date) == 10:
                    native_date = datetime.strptime(req_date + " 23:59:59", DATE_TIME_FORMAT)
                elif len(req_date) == 19:
                    native_date = datetime.strptime(req_date, DATE_TIME_FORMAT)
            local_date = pytz.timezone(time_zone).localize(native_date)
            print("local_date1",local_date)
            local_date = self.modify_ds_time(local_date)
            print("local_date",local_date)

            str_date = str(local_date).replace(" ", "T")
            print("str_date", str_date)
            resp_date = (str_date[:22] + str_date[23:])[:19] + "-0000"
            print("resp_date", resp_date)

            return resp_date
        except Exception as error:
            logging.error(f'Error Formatting request DS date params : {error}')
            return None
    
    def modify_ds_time(self, local_date):
        try:
            local_date_str = str(local_date)
            time_diff = local_date_str[19:]
            modifier = time_diff[:1]
            hours = time_diff[1:3]
            mins = time_diff[4:]
            hours_added = timedelta(hours= int(hours), minutes=int(mins))
            if modifier == '+':
                modified_hour = local_date - hours_added
            elif modifier == '-':
                modified_hour = local_date + hours_added
            print('modified_hour',modified_hour)
            return modified_hour
        except Exception as err:
            logging.error(f'Error Modifying DataSync date : {err}')
            return None

# Hardcoded input values
req_date = "2024-02-21"
date_flag = False
time_zone = "UTC"

example_instance = Example()

profiler = LineProfiler()
profiler.add_function(example_instance.format_ds_utc_date)
profiler_wrapper = profiler(example_instance.format_ds_utc_date)
formatted_date = profiler_wrapper(req_date, date_flag, time_zone)
#profiler.print_stats()
print("Formatted Date:", formatted_date)
