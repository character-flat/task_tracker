import sys
from helper import add_task, update_task, delete_task, mark_task, list_tasks

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [<args>]")
        return

    command = sys.argv[1]

    if command == 'add':
        if len(sys.argv) < 3:
            print("Usage: task-cli add <description>")
            return
        add_task(sys.argv[2])
    elif command == 'update':
        if len(sys.argv) < 4:
            print("Usage: task-cli update <id> <description>")
            return
        update_task(int(sys.argv[2]), sys.argv[3])
    elif command == 'delete':
        if len(sys.argv) < 3:
            print("Usage: task-cli delete <id>")
            return
        delete_task(int(sys.argv[2]))
    elif command == 'mark-in-progress':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-in-progress <id>")
            return
        mark_task(int(sys.argv[2]), 'in-progress')
    elif command == 'mark-done':
        if len(sys.argv) < 3:
            print("Usage: task-cli mark-done <id>")
            return
        mark_task(int(sys.argv[2]), 'done')
    elif command == 'list':
        if len(sys.argv) == 2:
            list_tasks()
        else:
            list_tasks(sys.argv[2])
    else:
        print(f"Unknown command: {command}")

if __name__ == '__main__':
    main()
