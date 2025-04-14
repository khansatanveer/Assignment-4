def find_average(a, b):
    
    sum = a + b
    return sum / 2

def main():
    avg_1 = find_average(0, 10)
    avg_2 = find_average(8, 10)
    
    final = find_average(avg_1, avg_2)
    print("avg_1", avg_1)
    print("avg_2", avg_2)
    print("final", final)

if __name__ == '__main__':
    main()