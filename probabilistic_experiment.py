import random

def add_task(name):

    probability = random.uniform(0,1)
    return {"name": name, "probability": probability}

def observe_task(task):
    return "Done" if random.random() < task["probability"] else "Not Done"

task1 = add_task("Write Quantum To-Do App")

print(f"Task: {task1['name']} - Probability of being done: {task1['probability']:.2f}")
print(f"Observed state: {observe_task(task1)}")