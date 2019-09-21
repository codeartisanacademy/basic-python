import datetime

upload_time = datetime.datetime(2019, 9, 21, 7, 30, 0)

# display the duration

now_time = datetime.datetime.now()

time_diff = now_time - upload_time

if time_diff.total_seconds() < 60:
    print('couple seconds ago')
elif time_diff.total_seconds() > 60 and time_diff.total_seconds() < 3600:
    print('couple minutes ago')
elif time_diff.total_seconds() > 300:
    print("Uploaded {0} hours ago".format(round(time_diff.total_seconds()/3600)))
