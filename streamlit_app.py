import streamlit as st
import requests

# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8000/"

st.title("To-Do List App")

# Add a new task
st.header("Add a New Task")
name = st.text_input("Task Name")
description = st.text_area("Task Description")
if st.button("Add Task"):
    if name and description:
        response = requests.post(f"{BASE_URL}/add-task/", json={"name": name, "description": description})
        if response.status_code == 200:
            st.success("Task added successfully!")
        else:
            st.error("Failed to add task.")
    else:
        st.warning("Please provide both task name and description.")

# View all tasks
st.header("All Tasks")
response = requests.get(f"{BASE_URL}/all-tasks")
if response.status_code == 200:
    tasks = response.json()
    for task in tasks:
        st.subheader(task['name'])
        st.write(f"ID: {task['id']}")
        st.write(f"Description: {task['description']}")
        st.write(f"Status: {task['status']}")
        st.write(f"Created At: {task['created_at']}")
        if task['status'] == "Not Done":
            if st.button(f"Mark as Done", key=task['id']):
                complete_response = requests.post(f"{BASE_URL}/mark-done/", json={"id": task['id']})
                if complete_response.status_code == 200:
                    st.success("Task marked as done!")
                else:
                    st.error("Failed to mark task as done.")
else:
    st.error("Failed to fetch tasks.")