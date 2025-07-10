# todo_list.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        estado = "Terminada" if self.completed else "Pendiente"
        return f"{self.description} [{estado}]"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def list_tasks(self):
        return [task.description for task in self.tasks]

    def list_all(self):
        return self.tasks

    def mark_completed_by_index(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            raise IndexError("Índice inválido.")

    def clear_tasks(self):
        self.tasks = []

    def remove_task_by_index(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            raise IndexError("Índice inválido.")

    def count_tasks(self):
        return len(self.tasks)


if __name__ == "__main__":
    todo = TodoList()

    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como terminada")
        print("4. Eliminar tarea")
        print("5. Borrar todas las tareas")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            desc = input("Descripción de la tarea: ")
            todo.add_task(desc)
            print("Tarea agregada.")
        elif opcion == "2":
            if todo.count_tasks() == 0:
                print("No hay tareas.")
            else:
                print("Tareas actuales:")
                for i, t in enumerate(todo.list_all()):
                    estado = "Terminada" if t.completed else "Pendiente"
                    print(f"[{i}] {t.description} [{estado}]")
        elif opcion == "3":
            try:
                idx = int(input("Índice de la tarea a marcar como terminada: "))
                todo.mark_completed_by_index(idx)
                print("Tarea marcada como terminada.")
            except:
                print("Índice inválido.")
        elif opcion == "4":
            try:
                idx = int(input("Índice de la tarea a eliminar: "))
                todo.remove_task_by_index(idx)
                print("Tarea eliminada.")
            except:
                print("Índice inválido.")
        elif opcion == "5":
            todo.clear_tasks()
            print("Todas las tareas han sido eliminadas.")
        elif opcion == "6":
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción no válida.")
