import sqlite3
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import json

conn = sqlite3.connect("todo-database.db")
cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    name TEXT,
    state TEXT,
    status TEXT
);
'''
cursor.execute(create_table_query)
conn.commit() 

def get_quantum_state():
    qc = QuantumCircuit(1)
    qc.h(0)
    state = Statevector.from_instruction(qc)
    
    # Convert complex numbers to JSON-serializable format
    state_data = [{"real": complex_num.real, "imag": complex_num.imag} 
                 for complex_num in state.data]
    return json.dumps(state_data)

def add_task(name):
    quantum_state = get_quantum_state()
    
    cursor.execute(
        "INSERT INTO tasks (name, state, status) VALUES (?, ?, ?)",
        (name, quantum_state, "superposition")
    )
    conn.commit()
    return True

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    
    # Convert JSON strings back to complex numbers
    for task in tasks:
        task_id, name, state_json, status = task
        state_data = json.loads(state_json)
        complex_nums = [complex(item["real"], item["imag"]) for item in state_data]
        print(f"Task {task_id}: {name} | Quantum state: {complex_nums} | Status: {status}")

def set_state(name, state):
    # Validate state
    if state not in (0, 1):
        raise ValueError("State must be 0 (not done) or 1 (done)")
    
    state_val = "done" if state == 1 else "not done"
    
    cursor.execute(
        "UPDATE tasks SET status = ? WHERE name = ?",
        (state_val, name)
    )
    
    # Check if any rows were actually updated
    if cursor.rowcount == 0:
        print(f"No task found with name: {name}")
        return False
    
    conn.commit()
    return True


conn.close()