import time

class HelperFunctionCanCalculateTime:
    def __init__(self, start_time):
        def do_things(self):
            self.StartTime = start_time
            
            start_time = time.perf_counter()
            
            for integers in range(10):
                first_time = integers ** 100
                
                print(time.perf_counter() - start_time,
                      "second elapsed")
                
                second_time = 10 ** 2
                print(time.perf_counter() - start_time,
                      "second elapsed")
                
                return second_time
            print(do_things())
                