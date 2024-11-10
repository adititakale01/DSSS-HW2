import random

def RandomNumberGenerator(LowerLimit, UpperLimit):
    """
    Generating a random number (integer) between the given range.

    Args:
    LowerLimit: Minimum value
    UpperLimit: Maximum value

    Returns:
    int: Random integer between the lower and upper limits (inclusive)

    """
    return random.randint(LowerLimit, UpperLimit)


def RandomOperator():
    """
    Outputs a mathematical operator randomly from (+, -, or *)
    
    Returns:
    str: Output is a string.
    """
    return random.choice(['+', '-', '*'])


def solveFunction(n1, n2, operator):
    """
    Generate a math problem and calculate the correct answer based on the operator.
    
    Args:
    n1 (int): The first number used
    n2 (int): The second number used
    operator (str): The operator used ('+', '-', or '*')
    
    Returns:
    tuple: A tuple containing the math problem and it's answer
    """
    question = f"{n1} {operator} {n2}"
    if operator == '+': 
        answer = n1 + n2            # (adding) changed to the correct operation
    elif operator == '-': 
        answer = n1 - n2            # (subtracting) changed to the correct operation
    else: 
        answer = n1 * n2            # (multiplicating)
    return question, answer

def mathQuiz():
    """
    Math Quiz questions will be randomly generated and asked. 
    If input is correct, will get a point.
    Correct answer will be displayed if the given answer is wrong.
    Final score given at the end.
    """
    score = 0
    totalQuestions = 13

    print("Start the Math Quiz!")
    print("Give the correct answers and know your score")

    for _ in range(totalQuestions):
        n1 = RandomNumberGenerator(1, 20); 
        n2 = RandomNumberGenerator(1, 20); 
        operator = RandomOperator()
        PROBLEM, ANSWER = solveFunction(n1, n2, operator)
        
        print(f"\nQuestion: {PROBLEM}")
        
        try:
            userAnswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input... Please enter a valid integer.")
            continue  # Skip this question and move to the next one


        if userAnswer == ANSWER:
            print("Congrats! You earned a point.")
            score += 1
        else:
            print(f"Hard luck! Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{totalQuestions}")

if __name__ == "__main__":
    mathQuiz()