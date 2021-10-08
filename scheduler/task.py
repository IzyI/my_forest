from huey import SqliteHuey, crontab

huey = SqliteHuey('my-app', filename='huey.db')


@huey.task()
def add_numbers(a, b):
    print("add_numbers")
    return a + b


@huey.task(retries=2, retry_delay=60)
def flaky_task(url):
    print("flaky_task")
    return 1


@huey.periodic_task(crontab(minute='0', hour='3'))
def nightly_backup():
    print("nightly_backup")
