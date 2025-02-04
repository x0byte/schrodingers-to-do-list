# Schrödinger's To-Do List  

**A to-do list that doesn’t just track your tasks—it questions their very existence.**  

Welcome to the **Schrödinger's To-Do List**, where tasks exist in quantum superposition until you decide their fate. In a world full of rigid, binary checklists, this project dares to ask:  
*"Is a task truly not done until the moment you finish it?"*  

## 🤔 Why This Exists  

Traditional to-do lists assume tasks are either **done** ✅ or **not done** ❌. But reality is more uncertain than that. Inspired by **Schrödinger’s Cat**, this to-do list ensures that tasks exist in a probabilistic blur—both completed and uncompleted—until you, the user, collapse their state by checking them.  

This isn't just a productivity tool. It's an **existential experiment in procrastination**, powered by **actual quantum mechanics** (kind of).  

---

## ⚙️ How It Works  

1. **Adding a Task:**  
   - When you create a task, it doesn’t just appear with a "not done" status. That would be too boring.  
   - Instead, it is assigned a **quantum state** (using IBM's Qiskit).  
   - This means it exists in a **superposition of both being done and not done**.  

2. **The Superposition Phase:**  
   - Until you set a definite state to the task, it stays in a **glitching, vibrating state** in the UI.  
   - You cannot trust its completion status—because it doesn’t exist in a defined state.  

3. **Collapsing the Quantum Wavefunction:**  
   - The moment you **define** the status of the task, it stops being in superposition.  
   - Either it was *actually done* (congratulations) or it turns out it *wasn’t done* (oops).    

4. **Existential Crisis (Bonus Feature):**  
   - Realize that many tasks in life are neither truly done nor not done.  
   - Question everything.  

---

## 🔬 But Seriously, How Does This Work?  

This project uses **Qiskit**, an open-source quantum computing framework from IBM, to generate quantum randomness.  

### **How Qiskit Generates Superposition**  

- Every task is assigned a **quantum bit (qubit)**.  
- A **Hadamard gate** is applied to the qubit, putting it into an equal superposition of `|0⟩` (Not Done) and `|1⟩` (Done).  
- The state is stored in **complex probability amplitudes**.  
- The task remains in this undefined quantum state **until a definite status is set**.

**TL;DR:**  
✅ **Tasks don’t exist in a binary state until you observe them**.  
🧠 **You will either become more productive or question the nature of reality**.  

---

## 🛠️ Technologies Used  

- **Python** – Because every great procrastination tool is written in Python, and that's all I know!  
- **Flask** – Simple backend to serve our existentially confusing tasks.  
- **SQLite** – Database for storing tasks.  
- **Qiskit** – Generates quantum randomness because your task list deserves nothing less than the laws of physics.  
- **CSS Animations** – Tasks in superposition "glitch" to visually reinforce their uncertain state.  
