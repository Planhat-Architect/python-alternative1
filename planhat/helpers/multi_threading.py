import requests as r 
from concurrent import futures

def multi_threaded_req(req_func, iterable):

    with futures.ThreadPoolExecutor() as executor: 
        res = [executor.submit(req_func, req_item) for req_item in iterable]
        futures.wait(res) 
    
    return res 