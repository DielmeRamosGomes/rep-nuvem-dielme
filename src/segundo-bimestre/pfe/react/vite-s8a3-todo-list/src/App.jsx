import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [tasks, setTasks] = useState([]);
  const [input, setInput] = useState('');

  const addTask = () => {
    const newTask = { text: input, completed: false };
    setTasks([...tasks, newTask]);
    setInput('');
  };

  const toggleComplete = (index) => {
    const newTasks = tasks.map((task, i) => 
      i === index ? { ...task, completed: !task.completed } : task
    );
    setTasks(newTasks);
  };

  const removeTask = (index) => {
    const newTasks = tasks.filter((_, i) => i !== index);
    setTasks(newTasks);
  };
  
  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  useEffect(() => {
    const savedTasks = JSON.parse(localStorage.getItem('tasks'));
    if (savedTasks) {
      setTasks(savedTasks);
    }
  }, []);
        
  return (
    <div className="App">
      <h1>To-Do List</h1>
      <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Nova tarefa"/>
      <button onClick={addTask}>Adicionar</button>
      <ul>
        {tasks.map((task, index) => (
          <li key={index} className="todo-item">
            <span className={task.completed ? 'completed' : ''} onClick={() => toggleComplete (index)}>{task.text}
            </span>
            <button onClick={() => removeTask(index)}>Remover</button>
          </li>
      ))}
    </ul>
    </div>
  );
}
export default App;
