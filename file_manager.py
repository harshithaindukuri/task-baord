import pandas

tasks_count = 0
action_data = None
master_data = None
children_count = 0
current_task_index = 0
current_child_index = 0


def load_files():
    global tasks_count, master_data, action_data, children_count
    action_data = pandas.read_csv("task_action_file.csv").to_dict(orient='records')
    master_data = pandas.read_csv("task_master_file.csv").to_dict(orient='records')
    children_count = len(action_data)
    tasks_count = len(master_data)
    print(action_data)
    print(master_data)


def save_data(data_dict1, data_dict2):
    if check_existing_task(data_dict1["task_name"]):
        if check_existing_child_task(data_dict2["task_action_name"]):
            modify_task(data_dict1)
            update_child_task(data_dict2)
        else:
            modify_task(data_dict1)
            new_child_task(data_dict2)
    else:
        new_task(data_dict1)
        new_child_task(data_dict2)

def check_existing_task(name):
    for i in range(0, tasks_count):
        if name == master_data[i]["task_name"]:
            global current_task_index
            current_task_index = i
            return True
        else:
            return False


def check_existing_child_task(name):
    for i in range(0, children_count):
        if name == action_data[i]["task_action_name"]:
            global current_child_index
            current_child_index = i
            return True
        else:
            return False

def new_task(data_dict1):
    global tasks_count
    tasks_count = tasks_count + 1
    data_dict1["task_id"] = tasks_count
    data_dict1["child_count"] = 1
    global master_data, action_data
    master_data.append(data_dict1)
    print("new task")


def modify_task(data_dict1):
    master_data[current_task_index]["task_description"] = data_dict1["task_description"]
    master_data[current_task_index]["task_active"] = data_dict1["task_active"]
    print("update task")



def update_child_task(data_dict2):
    action_data[current_child_index]["task_deadline"] = data_dict2["task_deadline"]
    action_data[current_child_index]["task_reminder"] = data_dict2["task_reminder"]
    action_data[current_child_index]["task_status"] = data_dict2["task_status"]
    print("update child task")
    print(action_data)


def new_child_task(data_dict2):
    global master_data, action_data, children_count
    children_count = children_count + 1
    master_data[current_task_index]["child_count"]= master_data[current_task_index]["child_count"] + 1
    data_dict2["task_action_id"] = master_data[current_task_index]["child_count"]
    data_dict2["task_parent_id"] = master_data[current_task_index]["task_id"]
    action_data.append(data_dict2)
    print("new child task")
    print(action_data)
    print(master_data)
