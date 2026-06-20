import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()

        return result
    
    return wrapper

def file_reader(file_name):
    with open(file_name,"r") as lines:
        for line in lines:
            yield line

@execution_time
def line_counter(file_name):
    line_count = 0
    word_count = 0

    for line in file_reader(file_name):
        line_count += 1

        words = [i for i in line.split()]
        word_count += len(words)

    print(f"line count: {line_count}")
    print(f"word count: {word_count}")

try:
    user_input = input("Please Enter the file name: ")
    line_counter(user_input)
except FileNotFoundError as e:
    print(e)
finally:
    print("Code execution completed")


