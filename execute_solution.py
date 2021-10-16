import solutions
from timeit import default_timer as timer


def execute_solution(questions, q_name):
    start = timer()
    solution = questions[q_name]
    end = timer()
    print("===================")
    print(f"solution: {solution} \nExecuting Time: {start-end} seconds")
    print("===================")


def solution_input():
    solution = solutions.Solution()
    questions = {'twoSum_my': solution.twoSum_my([2, 7, 11, 15], 9),
                 'twoSum_ans1': solution.twoSum_ans1([2, 7, 11, 15], 9),
                 'twoSum_ans2': solution.twoSum_ans1([2, 7, 11, 15], 9),}
    return questions


def main(q_name):
    questions = solution_input()
    execute_solution(questions, q_name)


if __name__ == '__main__':
    main('twoSum_ans2')

