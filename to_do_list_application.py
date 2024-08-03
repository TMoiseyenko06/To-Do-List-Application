'''
To-Do List 
Version 0.1.1

A simple to-do list project I did for Coding Temple!
It prints out a menu of options in the console, select options and enter tasks to use it.
I'm planning to add more fetures and clean up the code in the future

'''
#initilize global variables

avalible_lists = [{}]
current_list = 0

#adds a task to the dictionary
def add_task(task_list,task):
    task_list[task] = False

#remove task from dictionary (if it exists)
def remove_task(task_list,task):
        try:
            del task_list[task]
        except:
            print("\t\tTask does not exist please try again.")

#marks a task as complete (if said task exists)
def complete_task(task_list,task):
    if task in task_list:
        task_list[task] = True
    else: 
        print("\t\tThis task does not exist!")
        input("\t\tClick 'Enter' to return to the menu")

#prints the dictionary that contains the tasks
def view_tasks(task_list):
    for task in task_list:
        print(f'\t\t{'[x]' if task_list[task] else '[ ]'} : {task}')

def create_list(task):
    global current_list 
    avalible_lists.append({})
    current_list += 1
    print(f'Created list {current_list + 1}')
        
#decide what function to run based on the inpu
def run_choice(task_list,choice,task=""):
    if choice == 1:
        add_task(task_list,task)
    elif choice == 2:
        remove_task(task_list,task) 
    elif choice == 3:
        complete_task(task_list,task) 
    elif choice == 4:
        pass
    elif choice == 5:
        create_list(task)
    elif choice == 6:
        view_tasks(task_list)
        input("\t\tClick 'Enter' to return to the menu")
    elif choice == 7:
        pass

#main function that controls everything else
def main():

    while True:
        try:
            #ask for user choice
            choice = int(input(f"""\n\n\tWelcome to the To-Do list application
                \n\t\tMenu for list {current_list + 1}:
                1. Add a task
                2. Delete a Task
                3. Mark a Task as Complete
                4. Change current List
                5. Create new list
                6. View Tasks
                7. Quit
                      
                      """))    
        except :
            print("\n\n\tNumber is not vlaid please try again.")
            break
        else:
            #decide if we need to ask user for a task
            if choice < 7:
                if choice <= 4 :
                    task = input("\t\tPlease enter The name of the task:")
                    run_choice(avalible_lists[current_list],choice,task)
                else:
                    run_choice(avalible_lists[current_list],choice)       
            else:
                print("\t\tHave a great rest of your day!")
                break

#calls main function 
if __name__ == "__main__":
    main()