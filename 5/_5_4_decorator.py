from _5_3_create_contacts import create_contacts
import datetime

def func_stopwatch(func):
    start = datetime.datetime.now()
    result = func()
    time = datetime.datetime.now() - start
    print(f'Processing function {func.__name__} | time: {time}')
    return lambda: result

@func_stopwatch
def retrieve_1000_contacts():
    return create_contacts(base_contacts=500, business_contacts=500)

print(retrieve_1000_contacts())