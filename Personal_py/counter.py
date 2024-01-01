import tkinter as tk

class CounterApp:
    def __init__(self, root):
        """Initialize the CounterApp."""
        
        self.root = root
        root.title("Counter App")
        self.count = 0

        self.setup_ui_elements()

    def setup_ui_elements(self):
        """Setup all the UI elements for the CounterApp."""
        
        self.info_label = tk.Label(self.root, text="Click the button to start counting!")
        self.info_label.pack(pady=10)

        self.counter_display = tk.Label(self.root, text="")
        self.counter_display.pack()

        self.start_btn = self.create_button("Start", self.begin_counting)
        self.restart_btn = self.create_button("Restart", self.reset_count, state=tk.DISABLED)
        self.exit_btn = self.create_button("Exit", self.root.quit)

    def create_button(self, text, command, state=tk.NORMAL):
        """Create a button with specified text, command, and state."""
        
        button = tk.Button(self.root, text=text, command=command, state=state)
        button.pack()
        return button

    def begin_counting(self):
        """Start counting up to 100."""
        
        self.count += 1
        self.update_counter_display()

        if self.count <= 99:
            self.root.after(1000, self.begin_counting)
        else:
            self.toggle_buttons()

    def reset_count(self):
        """Reset the counter to 0."""
        
        self.count = 0
        self.update_counter_display()
        self.enable_start_button()

    def update_counter_display(self):
        """Update the counter display label."""
        
        self.counter_display.config(text=f"{self.count}")

    def enable_start_button(self):
        """Enable the start button and disable the restart button."""
        
        self.start_btn.config(state=tk.NORMAL)
        self.restart_btn.config(state=tk.DISABLED)

    def toggle_buttons(self):
        """Disable start button and enable restart button."""
        
        self.start_btn.config(state=tk.DISABLED)
        self.restart_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
