const input = document.getElementById('todoInput');
const list = document.getElementById('todoList');
const taskCountLabel = document.getElementById('taskCount');

// Page load hone par data aur theme check karein
window.onload = () => {
    if (localStorage.getItem('theme') === 'dark') {
        document.body.classList.add('dark-theme');
        document.getElementById('theme-toggle').innerText = "☀️ Light Mode";
    }
    loadTodos();
};

function updateCounter() {
    const total = list.children.length;
    taskCountLabel.innerText = `Total Tasks: ${total}`;
}

function addTodo() {
    const text = input.value.trim();
    if (text === "") return;

    const todoObj = {
        id: Date.now(),
        text: text,
        date: new Date().toLocaleString([], { hour: '2-digit', minute: '2-digit', day: '2-digit', month: 'short' }),
        completed: false
    };

    saveToLocal(todoObj);
    createTodoElement(todoObj);
    input.value = "";
    updateCounter();
}

function createTodoElement(todo) {
    const li = document.createElement('li');
    li.setAttribute('data-id', todo.id);
    if(todo.completed) li.classList.add('completed');

    li.innerHTML = `
        <div class="task-content" onclick="toggleComplete(${todo.id})">
            <span class="task-text">${todo.text}</span>
            <span class="task-date">${todo.date}</span>
        </div>
        <div class="actions">
            <button onclick="editTodo(${todo.id})">✏️</button>
            <button class="delete-btn" onclick="removeTodo(${todo.id})">🗑️</button>
        </div>
    `;
    list.prepend(li); // Naya task upar dikhane ke liye
}

function toggleComplete(id) {
    let todos = JSON.parse(localStorage.getItem("myTodos"));
    todos = todos.map(t => t.id === id ? { ...t, completed: !t.completed } : t);
    localStorage.setItem("myTodos", JSON.stringify(todos));
    
    const element = document.querySelector(`[data-id="${id}"]`);
    element.classList.toggle('completed');
}

function editTodo(id) {
    let todos = JSON.parse(localStorage.getItem("myTodos"));
    const index = todos.findIndex(t => t.id === id);
    const newText = prompt("Task ko edit karein:", todos[index].text);
    
    if (newText !== null && newText.trim() !== "") {
        todos[index].text = newText.trim();
        localStorage.setItem("myTodos", JSON.stringify(todos));
        document.querySelector(`[data-id="${id}"] .task-text`).innerText = newText.trim();
    }
}

function removeTodo(id) {
    let todos = JSON.parse(localStorage.getItem("myTodos"));
    todos = todos.filter(t => t.id !== id);
    localStorage.setItem("myTodos", JSON.stringify(todos));
    document.querySelector(`[data-id="${id}"]`).remove();
    updateCounter();
}

function loadTodos() {
    let todos = JSON.parse(localStorage.getItem("myTodos") || "[]");
    todos.forEach(todo => createTodoElement(todo));
    updateCounter();
}

function saveToLocal(todo) {
    let todos = JSON.parse(localStorage.getItem("myTodos") || "[]");
    todos.push(todo);
    localStorage.setItem("myTodos", JSON.stringify(todos));
}

function clearAll() {
    if (confirm("Saare tasks delete karein?")) {
        list.innerHTML = "";
        localStorage.removeItem("myTodos");
        updateCounter();
    }
}

function toggleDarkMode() {
    const isDark = document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    document.getElementById('theme-toggle').innerText = isDark ? "☀️ Light Mode" : "🌙 Dark Mode";
}

// Enter key support
input.addEventListener("keypress", (e) => { if (e.key === "Enter") addTodo(); });
