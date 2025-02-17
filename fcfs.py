from collections import deque

class Task:
    def __init__(self, task_id, arrival_time, duration):
        self.task_id = task_id
        self.arrival_time = arrival_time
        self.duration = duration
        self.start_time = None
        self.end_time = None

class Scheduler:
    def __init__(self, num_machines):
        self.queue = deque()
        self.machines = [0] * num_machines
        self.completed_tasks = []

    def add_task(self, task_id, arrival_time, duration):
        task = Task(task_id, arrival_time, duration)
        self.queue.append(task)
        print(f"Dodano zadanie {task_id} (czas trwania: {duration}) do kolejki.")

    def run_fcfs(self):
        while self.queue:
            task = self.queue.popleft()
            earliest_machine = min(range(len(self.machines)), key=lambda i: self.machines[i])
            
            task.start_time = max(self.machines[earliest_machine], task.arrival_time)
            task.end_time = task.start_time + task.duration
            self.machines[earliest_machine] = task.end_time
            
            self.completed_tasks.append(task)
            print(f"Zadanie {task.task_id} rozpoczyna się o {task.start_time} i kończy o {task.end_time} na maszynie {earliest_machine}.")
    
    def calculate_average_wait_time(self):
        total_wait_time = sum(task.start_time - task.arrival_time for task in self.completed_tasks)
        return total_wait_time / len(self.completed_tasks) if self.completed_tasks else 0

    def show_schedule(self):
        print("\nHarmonogram zadań:")
        for task in self.completed_tasks:
            print(f"Zadanie {task.task_id}: start {task.start_time}, koniec {task.end_time}, oczekiwanie {task.start_time - task.arrival_time}")
        print(f"Średni czas oczekiwania: {self.calculate_average_wait_time():.2f} sekund.")

if __name__ == "__main__":
    scheduler = Scheduler(num_machines=2)
    
    ##ZADANIA
    
    scheduler.add_task(1, 0, 3)
    scheduler.add_task(2, 1, 5)
    scheduler.add_task(3, 2, 2)
    scheduler.add_task(4, 4, 4)

    
    scheduler.run_fcfs()
    scheduler.show_schedule()
