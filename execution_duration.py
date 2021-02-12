import time

class ExcecutionDuration:
    def __init__(self):
        pass
    def execution_details(self, func):
        def ex_time(*args, **kwargs):
            start_time = time.time()
            returned_value=func(*args, **kwargs)
            time.sleep(1)
            esc_t= (time.time() - start_time - 1)
            return returned_value, esc_t
        return ex_time
