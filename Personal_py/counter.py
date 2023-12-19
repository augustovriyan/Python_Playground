import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.root = root
        root.title("Counter App")
        self.count = 0

        self.label = tk.Label(root, text="Click the button to start counting!")
        self.label.pack(pady=10)

        self.counter_label = tk.Label(root, text="")
        self.counter_label.pack()

        self.start_button = self.create_button("Start", self.start_counter)
        self.restart_button = self.create_button("Restart", self.restart_counter, state=tk.DISABLED)
        self.exit_button = self.create_button("Exit", root.quit)

    def create_button(self, text, command, state=tk.NORMAL):
        button = tk.Button(self.root, text=text, command=command, state=state)
        button.pack()
        return button

    def start_counter(self):
        self.count += 1
        self.update_counter_label()

        if self.count <= 99:
            self.root.after(1000, self.start_counter)
        else:
            self.disable_start_restart_buttons()

    def restart_counter(self):
        self.count = 0
        self.update_counter_label()
        self.enable_start_button()

    def update_counter_label(self):
        self.counter_label.config(text=f"{self.count}")

    def enable_start_button(self):
        self.start_button.config(state=tk.NORMAL)

    def disable_start_restart_buttons(self):
        self.start_button.config(state=tk.DISABLED)
        self.restart_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
