def solution(numbers):
    # len(numbers)
    numbers.sort()
    
    last = len(numbers)
    max_1 = numbers[last-1]
    max_2 = numbers[last-2]
    answer = max_1 * max_2
    return answer 