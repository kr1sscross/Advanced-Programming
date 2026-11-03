from producer import create_task

tasks_number = 100
added_tasks = 0

for i in range(tasks_number):
    try:
        create_task()
        added_tasks += 1
    except Exception as e:
        print(f"Error while adding task {i+1}: {e}")

print(f"Added {added_tasks}/{tasks_number} tasks")
