import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness and Health App")

        self.create_gui()

    def create_gui(self):
        # Labels
        self.title_label = ttk.Label(self.root, text="Fitness and Health App", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.exercise_label = ttk.Label(self.root, text="Current Exercise:")
        self.exercise_label.pack(pady=5)

        # Canvas for animations
        self.canvas = tk.Canvas(self.root, width=300, height=20, bg="lightgray")
        self.canvas.pack(pady=10)

        # Progress bar animation
        self.progress_bar = self.canvas.create_rectangle(0, 0, 0, 20, fill="green", outline="green")

        # Start button
        self.start_button = ttk.Button(self.root, text="Start Workout", command=self.start_workout)
        self.start_button.pack(pady=10)

    def start_workout(self):
        # Simulate a 60-second workout
        self.reset_progress_bar()
        threading.Thread(target=self.animate_progress_bar, daemon=True).start()

    def reset_progress_bar(self):
        self.canvas.coords(self.progress_bar, 0, 0, 0, 20)

    def animate_progress_bar(self):
        try:
            for i in range(61):
                width = i * 5
                self.canvas.coords(self.progress_bar, 0, 0, width, 20)
                time.sleep(1)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        messagebox.showinfo("Workout Complete", "Congratulations! Your workout is complete.")

if __name__ == "__main__":
    root = tk.Tk()
    fitness_app = FitnessApp(root)
    root.mainloop()