import cmd

class TaskManager(cmd.Cmd):
    intro = "Welcome to the Task Manager console. Type 'help' to see available commands."
    prompt = "Task Manager> "
    tasks = []

    def do_add_task(self, task_description):
        """Add a new task"""
        if task_description:
            self.tasks.append({"description": task_description, "completed": False})
            print("Task added.")
        else:
            print("Please provide a task description.")

    def do_list_tasks(self, arg):
        """List all tasks"""
        if self.tasks:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Not Completed"
                print(f"{i}. {task['description']} ({status})")
        else:
            print("No tasks to display.")

    def do_mark_complete(self, task_index):
        """Mark a task as completed"""
        try:
            index = int(task_index) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index]["completed"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please provide a valid task index.")

    def do_remove_task(self, task_index):
        """Remove a task"""
        try:
            index = int(task_index) - 1
            if 0 <= index < len(self.tasks):
                del self.tasks[index]
                print("Task removed.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Invalid input. Please provide a valid task index.")

    def do_quit(self, arg):
        """Exit the Task Manager"""
        return True

if __name__ == "__main__":
    TaskManager().cmdloop()

