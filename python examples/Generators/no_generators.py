import time
times_record = []
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

def create_cubes_generators(n):
    for x in range(n):
        yield x**3
    
if __name__ == "__main__":
    n = 1000000
    start_time = time.time()
    for x in create_cubes(n):
        print(x)
    
    stop_time = time.time()
    times_record.append(stop_time - start_time)

    start_time = time.time()
    for x in create_cubes_generators(n):
        print(x)
    stop_time = time.time()
    times_record.append(stop_time - start_time)

    for index, record in enumerate(times_record):
        print(f"${index+1}: ${record} seconds ---")