import time

class DontReapeatYourself:
    def __int__(self, start_time):
        self.StartTime = start_time
        def print_time_elapsed(start_time):
            print(time.perf_counter() - start_time, "second elapsed")
        
        def do_things():
            start_time = time.perf_counter()
            
            for integer in range(10):
                first_number_in_time = integer ** 100
                print_time_elapsed(start_time)
            second_number_in_time = 10 ** 2
            print_time_elapsed(start_time)
            return second_number_in_time
if __name__ == '__main__':
    DontReapeatYourself()
    