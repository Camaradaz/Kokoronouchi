import tkinter as tk

class StatsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OPHRPG")

        # Variables para STATS
        self.vitalidad = tk.IntVar()
        self.energia = tk.IntVar()
        self.fuerza = tk.IntVar()
        self.velocidad = tk.IntVar()
        self.voluntad = tk.IntVar()

        # Inicializar STATS
        self.vitalidad.set(5191)  # Valor inicial de vitalidad
        self.energia.set(1643)    # Valor inicial de energía
        self.fuerza.set(205)      # Valor inicial de fuerza
        self.velocidad.set(8)     # Valor inicial de velocidad
        self.voluntad.set(3)      # Valor inicial de voluntad

        # Lista para historial de turnos
        self.historial_turnos = []
        self.current_turn = 1  # Inicializar el turno en 1

        # Frame para STATS Fijos
        stats_frame = tk.Frame(root)
        stats_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        tk.Label(stats_frame, text="STATS FIJOS").grid(row=0, column=0, columnspan=2)

        stats_labels = ["Vitalidad:", "Energía:", "Fuerza:", "Velocidad:", "Voluntad:"]
        for i, label in enumerate(stats_labels):
            tk.Label(stats_frame, text=label).grid(row=i+1, column=0)

        tk.Entry(stats_frame, textvariable=self.vitalidad, width=10, state="readonly").grid(row=1, column=1)
        tk.Entry(stats_frame, textvariable=self.energia, width=10, state="readonly").grid(row=2, column=1)
        tk.Entry(stats_frame, textvariable=self.fuerza, width=10, state="readonly").grid(row=3, column=1)
        tk.Entry(stats_frame, textvariable=self.velocidad, width=10, state="readonly").grid(row=4, column=1)
        tk.Entry(stats_frame, textvariable=self.voluntad, width=10, state="readonly").grid(row=5, column=1)

        # Frame para Equipación
        equipment_frame = tk.Frame(root)
        equipment_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nw")

        tk.Label(equipment_frame, text="EQUIPACIÓN").grid(row=0, column=0, columnspan=5)
        self.equipment_text = tk.Text(equipment_frame, height=5, width=30)
        self.equipment_text.grid(row=1, column=0, columnspan=5)

        # Frame para STATS Restantes
        remaining_stats_frame = tk.Frame(root)
        remaining_stats_frame.grid(row=0, column=2, padx=10, pady=10, sticky="nw")

        tk.Label(remaining_stats_frame, text="STATS RESTANTES").grid(row=0, column=0, columnspan=2)

        remaining_labels = ["Vitalidad:", "Energía:", "Fuerza:", "Velocidad:", "Voluntad:"]
        self.remaining_vars = [tk.IntVar() for _ in range(5)]

        for i, label in enumerate(remaining_labels):
            tk.Label(remaining_stats_frame, text=label).grid(row=i+1, column=0)
            tk.Entry(remaining_stats_frame, textvariable=self.remaining_vars[i], width=10, state="readonly").grid(row=i+1, column=1)

        # Frame para Registro y Historial de Turnos
        turn_history_frame = tk.Frame(root)
        turn_history_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        # Frame para Registro de Turnos
        turn_register_frame = tk.Frame(turn_history_frame)
        turn_register_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        tk.Label(turn_register_frame, text="REGISTRO DE TURNOS").grid(row=0, column=0, columnspan=4)

        tk.Label(turn_register_frame, text="Ronda").grid(row=1, column=0)
        self.round_entry = tk.Entry(turn_register_frame, width=5)
        self.round_entry.grid(row=1, column=1)

        tk.Label(turn_register_frame, text="Turno").grid(row=1, column=2)
        self.turn_entry = tk.Entry(turn_register_frame, width=5)
        self.turn_entry.grid(row=1, column=3)

        tk.Label(turn_register_frame, text="Habilidad").grid(row=2, column=0)
        self.skill_entry = tk.Entry(turn_register_frame, width=30)
        self.skill_entry.grid(row=2, column=1, columnspan=3)

        tk.Label(turn_register_frame, text="Energía").grid(row=3, column=0)
        self.energy_entry = tk.Entry(turn_register_frame, width=5)
        self.energy_entry.grid(row=3, column=1)

        tk.Label(turn_register_frame, text="Vitalidad").grid(row=3, column=2)
        self.vitality_entry = tk.Entry(turn_register_frame, width=5)
        self.vitality_entry.grid(row=3, column=3)

        tk.Label(turn_register_frame, text="Luchadores").grid(row=4, column=0)
        self.fighters_entry = tk.Entry(turn_register_frame, width=5)
        self.fighters_entry.grid(row=4, column=1)

        tk.Button(turn_register_frame, text="Registrar Turno", command=self.registrar_turno).grid(row=5, columnspan=4)

        # Frame para Historial de Turnos
        history_frame = tk.Frame(turn_history_frame)
        history_frame.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        tk.Label(history_frame, text="HISTORIAL DE TURNOS").grid(row=0, column=0, columnspan=4)

        self.history_text = tk.Text(history_frame, height=10, width=50)
        self.history_text.grid(row=1, column=0, columnspan=4)

    def registrar_turno(self):
        ronda = self.round_entry.get()
        habilidad = self.skill_entry.get()
        energia = self.energy_entry.get()
        vitalidad = self.vitality_entry.get()
        luchadores = self.fighters_entry.get()

        # Aumentar el turno en 1 y actualizar el campo de entrada de turno
        turno = self.current_turn
        self.current_turn += 1
        self.turn_entry.delete(0, tk.END)
        self.turn_entry.insert(tk.END, str(self.current_turn))

        registro = f"Ronda: {ronda}, Turno: {turno}, Habilidad: {habilidad}, Energía: {energia}, Vitalidad: {vitalidad}, Luchadores: {luchadores}"
        self.historial_turnos.append(registro)
        self.update_history()

        print("Ronda:", ronda)
        print("Turno:", turno)
        print("Habilidad:", habilidad)
        print("Energía:", energia)
        print("Vitalidad:", vitalidad)
        print("Luchadores:", luchadores)

        # Actualizar STATS RESTANTES
        try:
            energia_a_disminuir = int(energia) if energia else 0
            # Calcular el nuevo valor de energía
            nueva_energia = max(0, self.energia.get() - energia_a_disminuir)
            # Actualizar la energía
            self.energia.set(nueva_energia)
        except ValueError:
            print("La cantidad de energía a disminuir debe ser un número entero.")
        
        try:
            vitalidad_a_disminuir = int(vitalidad) if vitalidad else 0
            # Calcular el nuevo valor de vitalidad
            nueva_vitalidad = max(0, self.vitalidad.get() - vitalidad_a_disminuir)
            # Actualizar la vitalidad
            self.vitalidad.set(nueva_vitalidad)
        except ValueError:
            print("La cantidad de vitalidad a disminuir debe ser un número entero.")

        # Actualizar las entradas de STATS RESTANTES con los valores actuales
        self.remaining_vars[0].set(self.vitalidad.get())
        self.remaining_vars[1].set(self.energia.get())
        self.remaining_vars[2].set(self.fuerza.get())
        self.remaining_vars[3].set(self.velocidad.get())
        self.remaining_vars[4].set(self.voluntad.get())

    def update_history(self):
        self.history_text.delete(1.0, tk.END)
        for registro in self.historial_turnos:
            self.history_text.insert(tk.END, registro + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = StatsApp(root)
    root.mainloop()




