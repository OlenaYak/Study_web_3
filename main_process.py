import time
from multiprocessing import Pool, cpu_count

# синхронно

def factorize_synchron(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number+1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result

# паралельно

def factorize(number):
    return [i for i in range(1, number+1) if number % i == 0]

def factorize_parallel(*numbers):
    with Pool(processes=cpu_count()) as pool:
        result = pool.map(factorize, numbers)
    return result


if __name__ == '__main__':
    numbers = (128, 255, 99999, 10651060)

    start_time = time.time()
    a_synchron, b_synchron, c_synchron, d_synchron = factorize_synchron(*numbers)
    end_time = time.time()
    print(f"Синхронно: час виконання {end_time - start_time:.4f} с")

    start_time = time.time()
    a_parallel, b_parallel, c_parallel, d_parallel = factorize_parallel(*numbers)
    end_time = time.time()
    print(f"Паралельно: час виконання {end_time - start_time:.4f} с")

    expected_a = [1, 2, 4, 8, 16, 32, 64, 128] 
    expected_b = [1, 3, 5, 15, 17, 51, 85, 255] 
    expected_c = [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999] 
    expected_d = [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060] # type: ignore

    print("a_synchron =", a_synchron)
    print("expected_a =", expected_a)
    print("a_parallel =", a_parallel)

    assert a_synchron == expected_a and a_parallel == expected_a 
    assert b_synchron == expected_b and b_parallel == expected_b 
    assert c_synchron == expected_c and c_parallel == expected_c 
    assert d_synchron == expected_d and d_parallel == expected_d 

    print("Усі тести пройдено успішно")