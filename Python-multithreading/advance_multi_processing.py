# Multiprocessing with ProcessPoolExecutor

from concurrent.futures import ProcessPoolExecutor
import time 

def square_number(number):
    time.slepp(1)
    return f"Square:{number*number}"

if __name__=="name":
    numbers=[1,2,3,4,5]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    for result in results:
        print(result)
