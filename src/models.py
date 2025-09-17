tasks = []
task_id_counter = 1

class Task:
    def __init__(self, title, description, status="A Fazer"):
        global task_id_counter
        self.id = task_id_counter
        self.title = title
        self.description = description
        self.status = status
        task_id_counter += 1