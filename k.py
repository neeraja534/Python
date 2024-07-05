import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import threading
import time
import random

class RecipeRecommendationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Recommendation System")

        self.recipes = ["Spaghetti Bolognese", "Chicken Alfredo", "Vegetarian Pizza", "Chocolate Cake", "Caesar Salad"]

        self.create_gui()

    def create_gui(self):
        # Labels
        self.title_label = ttk.Label(self.root, text="Recipe Recommendation System", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.recipe_label = ttk.Label(self.root, text="Current Recipe:")
        self.recipe_label.pack(pady=5)

        # Canvas for animations
        self.canvas = tk.Canvas(self.root, width=300, height=20, bg="lightgray")
        self.canvas.pack(pady=10)

        # Transition animation
        self.transition_line = self.canvas.create_line(0, 10, 300, 10, fill="blue", width=2)

        # Next button
        self.next_button = ttk.Button(self.root, text="Next Recipe", command=self.next_recipe)
        self.next_button.pack(pady=10)

        # Initial recipe
        self.current_recipe_index = 0
        self.display_current_recipe()

    def next_recipe(self):
        # Simulate loading the next recipe
        threading.Thread(target=self.animate_transition, daemon=True).start()

    def animate_transition(self):
        try:
            for i in range(301):
                self.canvas.coords(self.transition_line, 0, 10, i, 10)
                time.sleep(0.01)

            # Load the next recipe
            self.current_recipe_index = (self.current_recipe_index + 1) % len(self.recipes)
            self.display_current_recipe()
            self.reset_transition()

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def display_current_recipe(self):
        current_recipe = self.recipes[self.current_recipe_index]
        self.recipe_label.config(text=f"Current Recipe: {current_recipe}")

    def reset_transition(self):
        self.canvas.coords(self.transition_line, 0, 10, 0, 10)

if __name__ == "__main__":
    root = tk.Tk()
    recipe_app = RecipeRecommendationApp(root)
    root.mainloop()