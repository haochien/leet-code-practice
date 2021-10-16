import solutions
from timeit import default_timer as timer


def execute_solution(questions, q_name):
    arg = questions[q_name][1:]

    start = timer()
    solution = questions[q_name][0](*arg)
    end = timer()
    print("===================")
    print(f"solution: {solution} \nExecuting Time: {start-end} seconds")
    print("===================")


def solution_input():
    solution = solutions.Solution()

    # questions = {question_name: [function, *function_arg]}
    questions = {'twoSum_my': [solution.twoSum_my, [2, 7, 11, 15], 9],
                 'twoSum_ans1': [solution.twoSum_ans1, [2, 7, 11, 15], 9],
                 'twoSum_ans2': [solution.twoSum_ans2, [2, 7, 11, 15], 9],
                 'palindrome_number_my': [solution.palindrome_number_my, 121],
                 'palindrome_number_ans1': [solution.palindrome_number_ans1, 121],
                 'palindrome_number_ans2': [solution.palindrome_number_ans2, 121],
                 'palindrome_number_ans3': [solution.palindrome_number_ans3, 121],
                 'roman_to_integer_my': [solution.roman_to_integer_my, 'MCMXCIV'],
                 'roman_to_integer_ans1': [solution.roman_to_integer_ans1, 'MCMXCIV'],}
    return questions


def main(q_name):
    questions = solution_input()
    execute_solution(questions, q_name)


if __name__ == '__main__':
    main('roman_to_integer_ans1')

