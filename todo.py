import json

# menambahkan task
def add_task():
  task_name = input("Enter taskname : ")
  print("choose task priority: ")
  print("1. low")
  print("2. medium")
  print("3. high")
  task_priority = input("Enter (number) task priority: ")

  task_priority_name = ""

  if int(task_priority) == 1 :
    task_priority_name = "low"
  elif int(task_priority) == 2 :
    task_priority_name = "medium"
  elif int(task_priority) == 3 :
    task_priority_name = "high"
  else:
    print("wrong input")
  
  new_task = {
    "name": task_name,
    "task_priority_name": task_priority_name,
    "status": "To Do",
  }

  with open("todo.txt", "a") as file:
    temp = json.dumps(new_task)
    file.write(temp + "\n")

  print("Succesfully added task ", task_name, " - " ,task_priority_name, "!")

def view_task():
  view_all_task()
  
  urutkan = input("Filter by status? ('To Do'/'In Progress'/'Finished'):  ")

  view_task_ordered(urutkan)


def view_all_task():
  print("List To-do:")
  with open("todo.txt", "r") as file:
    tasks = file.readlines()

    for task in tasks:
      temp_task = json.loads(task)
      print("Task:", temp_task["name"], "| Priority:", temp_task["task_priority_name"], "| Status:",temp_task["status"])

def view_task_ordered(urutkan):
  print("List To-do:")
  with open("todo.txt", "r") as file:
    tasks = file.readlines()

    
    for task in tasks:
      temp_task = json.loads(task)
      if urutkan == temp_task["status"]:
        print("Task ordered:", temp_task["name"], "| Priority:", temp_task["task_priority_name"], "| Status:",temp_task["status"])
      
def change_status_task():
  view_all_task()

  task_name = input("Enter task name: ")
  with open("todo.txt", "r") as file:
    tasks = file.readlines()

    task_found = False
    
    for i, task in enumerate(tasks):
      temp_task = json.loads(task)
      if task_name == temp_task["name"]:
        task_found = True
        if temp_task["status"] == "To Do":
          temp_task["status"] = "In Progress"
        elif temp_task["status"] == "In Progress":
          temp_task["status"] = "Finished"
        else:
          print("Status ", temp_task["name"] ,"already finished")

        tasks[i] = json.dumps(temp_task) + "\n"
        break
    
    if task_found:
      with open("todo.txt", "w") as file_new:
        file_new.writelines(tasks)
      
      print("Status changed successfully!")
    else:
      print("task not found")


def delete_task():
  view_all_task()

  task_delete = input("Enter task name to delete: ")

  with open("todo.txt", "r") as file:
    tasks = file.readlines()

    for task in tasks:
      temp_task = json.loads(task)

      if task_delete == temp_task["name"]:
        tasks.remove(task)
        break
    
    with open("todo.txt", "w") as file_new:
      file_new.writelines(tasks)


  print("Task deleted succesfully")

def percentage_finished_task():
  finished_count = 0
  with open("todo.txt", "r") as  file:
    tasks = file.readlines()

    for task in tasks:
      temp_task = json.loads(task)
      if temp_task["status"] == "Finished":
        finished_count += 1
  
  percentage = (finished_count / len(tasks)*100)

  print("Percentage Finished task: ", percentage,"%")


def base():
  print("Menu: ")
  print("1. Add Task")
  print("2. View Task")
  print("3. Change Task Status")
  print("4. Delete Task")
  print("5. Percentage Finished Task")

  pilihan = input("Enter the menu(1-5): ")

  if int(pilihan) == 1:
    add_task()
    base()
  elif int(pilihan) == 2:
    view_task()
    base()
  elif int(pilihan) == 3:
    change_status_task()
    base()
  elif int(pilihan) == 4:
    delete_task()
    base()
  elif int(pilihan) == 5:
    percentage_finished_task()
    base()
  else:
    print("invalid input")
    base()
  
base()

