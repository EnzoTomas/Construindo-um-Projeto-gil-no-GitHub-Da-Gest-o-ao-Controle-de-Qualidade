tasks = []
task_id_counter = 1

class Task:
    def __init__(self, title, description, status="A Fazer", priority="Média"): 
        global task_id_counter
        self.id = task_id_counter
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority 
        task_id_counter += 1