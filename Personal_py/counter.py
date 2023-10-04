import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Counter App")

        self.count = 0

        self.label = tk.Label(root, text="Click the button to start counting!")
        self.label.pack(pady=10)

        self.counter_label = tk.Label(root, text="")
        self.counter_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_counter)
        self.start_button.pack()

        self.restart_button = tk.Button(root, text="Restart", command=self.restart_counter, state=tk.DISABLED)
        self.restart_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

    def start_counter(self):
        self.count += 1
        self.update_counter_label()
        if self.count <= 99:
            self.root.after(1000, self.start_counter)
        else:
            self.disable_start_button()
            self.enable_restart_button()

    def restart_counter(self):
        self.count = 0
        self.update_counter_label()
        self.enable_start_button()
        self.disable_restart_button()

    def update_counter_label(self):
        self.counter_label.config(text=str(self.count))

    def enable_start_button(self):
        self.start_button.config(state=tk.NORMAL)

    def disable_start_button(self):
        self.start_button.config(state=tk.DISABLED)

    def enable_restart_button(self):
        self.restart_button.config(state=tk.NORMAL)

    def disable_restart_button(self):
        self.restart_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
