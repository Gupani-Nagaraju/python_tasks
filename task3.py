file_name = input("Enter the file name: ")
try:
    with open(file_name,'r') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(e)
finally:
    print("Execution completed")
