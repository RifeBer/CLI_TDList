import json
file_name = "to_do_list.json"
def load_file():
    try:
        with open(file_name,"r") as f :
            return json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return [ ]
def save_file(tasks):
    with open(file_name,"w") as file:
        json.dump(tasks,file,indent=4)

def add_task(description,status = "UnDone"):
    tasks = load_file()
    task = {"description" : description , "status" : status}
    tasks.append(task)
    save_file(tasks)
    

def show_tasks():
    tasks = load_file()
    if not tasks:
        print("List is Empty!!!")
    else :
        print("Your Tasks:")
        for idx , task in enumerate(tasks,start=1):
            print(f"{idx} : {task["description"]} - status : {task["status"]}")
def delete_task(task_number):
    tasks = load_file()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number-1)
        print("Deleted")
    else:
        print("invalid_number")
    save_file(tasks)

def delete_all():
    tasks = load_file()
    tasks.clear()
    save_file(tasks)
    
def update_task(selected_task,new_status):
    tasks = load_file()
    task_selected = selected_task - 1
    if 0 <= task_selected <= len(tasks):
        tasks[task_selected]["status"] = new_status
        save_file(tasks)
        print("Updated")
    else:
        print("Invalid Task Number")
    
def main():
    start = input("Hit Anykey To Start: ")
    if type(start) == str: 
        while True:
            print("--------ToDo_List--------")
            print("1: Add task")
            print("2: Show Task List")
            print("3: Update Task")
            print("4: Delete Task")
            print("5: Exit")

            choice = input("Choose 1/2/3/4/5 to start: ")

            if choice == "1":
                print("--------------------")
                description = input("Enter Your Task: ")
                add_task(description)
                print(f"{description} Task added")
            elif choice == "2":
                print("--------------------")
                show_tasks()
            elif choice == "3":
                print("--------------------")
                show_tasks()
                selected_task = int(input("Choose Number: "))
            #   selected_status = input("Task Statue : [UnDone,InProgress,Done]: ")
                print("---Task Status---")
                print("UnDone =======> 1")
                print("inProgress ===> 2")
                print("Done =========> 3")
                UnDone = "UnDone"
                InProgress = "InProgress"
                Done = "Done"
                selected_status = int(input("Choose Statue Number: "))
                if selected_status == 1:
                    update_task(selected_task,UnDone)
                elif selected_status == 2:
                    update_task(selected_task,InProgress)
                elif selected_status == 3:
                    update_task(selected_task,Done)
                else:
                    print("Invalid Statue Number")

            elif choice == "4":
                print("--------------------")
                show_tasks()
                print("--------------------")
                print("1 : Delete Specific Task")
                print("2 : Delete All Tasks")
                wannadel = input("Choose Operation Number from the above: ")
                if wannadel == "1" :
                    task_number = int(input("Task Number to Delete: "))
                    delete_task(task_number)
                elif wannadel == "2":
                    delete_all()
                    print("All tasks are deleted")
                else:
                    print("Invalid Operation")
                        
            elif choice == "5" :    
                print("Bye")
                exit()
            
            else:
                print("Invalid Operaion")
if __name__ == '__main__':
    main()




