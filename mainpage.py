import funcs
import ast
while True:
    command_first = input("Enter what to do?(create,load) : ")
    if command_first=="exit":
        break
    elif command_first == "create":
      input_path=input("Enter the path : ")
      input_create_id=input("Enter members id : ")
      input_create_name=input("Enter name :")
      input_create_last=input("Enter last name :")
      input_create_age=input("Enter age :")
      input_create_classname=input("Enter class name :")
      input_create_subjectsnoneprocc=input("Enter subjects name and score :")
      input_create_subjects=ast.literal_eval(input_create_subjectsnoneprocc)
      funcs.create_mem(input_path,input_create_id,input_create_name, input_create_last, input_create_age, input_create_classname, **input_create_subjects)
    elif command_first == "load":
      input_path=input("Enter the path : ")
      input_load_id=input("Enter member id : ")
      funcs.load_mem(input_path,input_load_id)

    else:
        print("Enter right command !")
