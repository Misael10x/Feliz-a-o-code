import tkinter as tk
import random
from math import sin, cos, radians

class FireworkAnimation:
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.particles = []
        self.create_particles()

    def create_particles(self):
        """Crea partículas de la explosión."""
        for angle in range(0, 360, 15):
            dx = cos(radians(angle)) * random.uniform(2, 5)
            dy = sin(radians(angle)) * random.uniform(2, 5)
            particle = {
                "x": self.x,
                "y": self.y,
                "dx": dx,
                "dy": dy,
                "size": random.randint(4, 8),
                "life": random.randint(20, 40)
            }
            self.particles.append(particle)

    def animate(self):
        """Anima las partículas de la explosión."""
        for particle in self.particles[:]:
            if particle["life"] > 0:
                particle["x"] += particle["dx"]
                particle["y"] += particle["dy"]
                particle["life"] -= 1
                
                particle["size"] *= 0.95  # Reduce el tamaño gradualmente

                size = particle["size"]
                self.canvas.create_oval(
                    particle["x"] - size, particle["y"] - size,
                    particle["x"] + size, particle["y"] + size,
                    fill=self.color, outline=""
                )
            else:
                self.particles.remove(particle)

class HappyNewYearApp:
    def __init__(self, root):
        self.root = root
        self.root.title("¡Feliz 2025!")
        self.root.geometry("800x600")
        self.root.configure(bg="black")
        self.canvas = tk.Canvas(self.root, bg="black", width=800, height=600, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.fireworks = []
        self.countdown(5)

    def countdown(self, seconds):
        """Realiza la cuenta regresiva en la pantalla."""
        if seconds > 0:
            self.canvas.delete("all")
            self.canvas.create_text(400, 300, text=f"{seconds}", font=("Helvetica", 100), fill="white")
            self.root.update()
            self.root.after(1000, self.countdown, seconds - 1)
        else:
            self.display_fireworks_and_message()

    def display_fireworks_and_message(self):
        """Muestra fuegos artificiales y luego el mensaje animado."""
        self.run_fireworks()
        self.animate_message("\u00a1Feliz 2025!")

    def run_fireworks(self):
        """Anima fuegos artificiales por un tiempo limitado."""
        for _ in range(20):
            x, y = random.randint(100, 700), random.randint(100, 500)
            color = random.choice(["red", "yellow", "blue", "green", "purple", "orange"])
            firework = FireworkAnimation(self.canvas, x, y, color)
            self.fireworks.append(firework)

        for _ in range(50):  # Duración total de los fuegos artificiales
            self.canvas.delete("fireworks")
            for firework in self.fireworks:
                firework.animate()
            self.root.update()
            self.canvas.after(30)
        self.fireworks.clear()

    def animate_message(self, message):
        """Anima el mensaje de Feliz Año Nuevo."""
        x, y = 400, 300
        for i in range(len(message) + 1):
            self.canvas.delete("all")
            # Muestra las letras progresivamente
            self.canvas.create_text(
                x, y, text=message[:i],
                font=("Helvetica", 60, "bold"),
                fill=random.choice(["white", "gold", "cyan", "pink"])
            )
            self.root.update()
            self.canvas.after(200)

        # Efecto de brillo en el mensaje completo
        for _ in range(10):
            self.canvas.delete("all")
            self.canvas.create_text(
                x, y, text=message,
                font=("Helvetica", 60, "bold"),
                fill=random.choice(["white", "yellow", "lightblue", "magenta"])
            )
            self.root.update()
            self.canvas.after(300)


def main():
    root = tk.Tk()
    app = HappyNewYearApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
