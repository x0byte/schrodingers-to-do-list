import sqlite3
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Database setup
def get_db_connection():
    conn = sqlite3.connect("todo-database.db")
    conn.row_factory = sqlite3.Row  
    return conn

# Initialize the database
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            state TEXT,
            status TEXT
        );
    ''')
    conn.commit()
    conn.close()

# Initialize the database 
init_db()

# getting Quantum state 
def get_quantum_state():
    qc = QuantumCircuit(1)
    qc.h(0)
    state = Statevector.from_instruction(qc)
    state_data = [{"real": complex_num.real, "imag": complex_num.imag} 
                  for complex_num in state.data]
    return json.dumps(state_data)

# Add a task
def add_task(name):
    quantum_state = get_quantum_state()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (name, state, status) VALUES (?, ?, ?)",
        (name, quantum_state, "superposition")
    )
    conn.commit()
    conn.close()

# Fetch all tasks
def view_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Update task status
def set_state(task_id, state):
    state_val = "done" if state == 1 else "not-done"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (state_val, task_id)
    )
    conn.commit()
    conn.close()

# Delete a task
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# Flask routes
@app.route('/')
def home():
    tasks = view_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task_route():
    task_name = request.form.get('task')
    if task_name:
        add_task(task_name)
    return redirect('/')

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect('/')

@app.route('/update/<int:task_id>/<int:state>', methods=['POST'])
def update_task_route(task_id, state):
    set_state(task_id, state)
    return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)