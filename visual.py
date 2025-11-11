import tkinter as tk
from tkinter import messagebox

class Competencia:
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        self.nivel = 0


class Perfil:
    def __init__(self, nome):
        self.nome = nome
        self.competencias = []


class Carreira:
    def __init__(self, nome, exigencias, pesos):
        self.nome = nome
        self.exigencias = exigencias
        self.pesos = pesos

    def calcular(self, perfil):
        total = 0
        peso_total = 0
        for nome, exig in self.exigencias.items():
            comp = next((c for c in perfil.competencias if c.nome == nome), None)
            peso = self.pesos.get(nome, 1)
            if not comp:
                continue
            if comp.nivel >= exig:
                nota = 10
            else:
                nota = (comp.nivel / exig) * 10
            total += nota * peso
            peso_total += peso
        if peso_total == 0:
            return 0
        return round((total / (10 * peso_total)) * 100, 1)


class SistemaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Russi orientação de Carreira")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")

        self.perfis = []
        self.carreiras = []
        self.criar_carreiras()

        self.nome_var = tk.StringVar()
        self.inputs = {}

        self.monta_interface()

    def criar_carreiras(self):
        self.carreiras.append(Carreira(
            "Desenvolvedor de Software",
            {"logica": 8, "criatividade": 6, "colaboracao": 5, "adaptabilidade": 7},
            {"logica": 3, "criatividade": 2, "colaboracao": 1, "adaptabilidade": 2}
        ))
        self.carreiras.append(Carreira(
            "Designer UX/UI",
            {"logica": 5, "criatividade": 9, "colaboracao": 7, "adaptabilidade": 6},
            {"logica": 1, "criatividade": 3, "colaboracao": 2, "adaptabilidade": 2}
        ))
        self.carreiras.append(Carreira(
            "Analista de Dados",
            {"logica": 9, "criatividade": 5, "colaboracao": 6, "adaptabilidade": 7},
            {"logica": 4, "criatividade": 1, "colaboracao": 2, "adaptabilidade": 2}
        ))
        self.carreiras.append(Carreira(
            "Gerente de Projetos",
            {"logica": 6, "criatividade": 6, "colaboracao": 9, "adaptabilidade": 8},
            {"logica": 1, "criatividade": 1, "colaboracao": 4, "adaptabilidade": 3}
        ))

    def monta_interface(self):
        tk.Label(self.root, text="Sistema Russi de Carreiras", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Label(self.root, text="Nome:", bg="#f0f0f0").pack()
        tk.Entry(self.root, textvariable=self.nome_var).pack(pady=5)

        competencias = ["logica (0-10)", "criatividade (0-10)", "colaboracao (0-10)", "adaptabilidade (0-10)"]
        for c in competencias:
            frame = tk.Frame(self.root, bg="#f0f0f0")
            frame.pack(pady=3)
            tk.Label(frame, text=f"{c.capitalize()}:", width=15, anchor="w", bg="#f0f0f0").pack(side="left")
            var = tk.StringVar()
            self.inputs[c] = var
            tk.Entry(frame, textvariable=var, width=5).pack(side="left")

        tk.Button(self.root, text="Cadastrar Perfil", command=self.salvar_perfil, bg="#d9ead3").pack(pady=10)
        tk.Button(self.root, text="Analisar Perfil", command=self.analisar, bg="#c9daf8").pack(pady=5)
        tk.Button(self.root, text="Sair", command=self.root.quit, bg="#f4cccc").pack(pady=10)

        self.result_label = tk.Label(self.root, text="", justify="left", bg="#f0f0f0")
        self.result_label.pack(pady=10)

    def salvar_perfil(self):
        nome = self.nome_var.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "Coloca o nome do perfil, pô!")
            return

        p = Perfil(nome)
        for c, var in self.inputs.items():
            try:
                n = int(var.get())
                if n < 0 or n > 10:
                    raise ValueError
            except:
                messagebox.showerror("Erro", f"Valor inválido para {c}. Use de 0 a 10.")
                return
            tipo = "tecnica" if c == "logica" else "comportamental"
            comp = Competencia(c, tipo)
            comp.nivel = n
            p.competencias.append(comp)

        self.perfis.append(p)
        messagebox.showinfo("Sucesso", f"Perfil '{nome}' cadastrado!")
        for v in self.inputs.values():
            v.set("")
        self.nome_var.set("")

    def analisar(self):
        if not self.perfis:
            messagebox.showinfo("Aviso", "Nenhum perfil cadastrado ainda.")
            return

        nome = self.nome_var.get().strip()
        perfil = next((p for p in self.perfis if p.nome == nome), None)

        if not perfil:
            messagebox.showwarning("Aviso", "Perfil não encontrado.")
            return

        resultados = []
        for c in self.carreiras:
            comp = c.calcular(perfil)
            resultados.append((c.nome, comp))

        resultados.sort(key=lambda x: x[1], reverse=True)
        texto = f"Perfil: {perfil.nome}\n\n"
        for nome, pct in resultados:
            texto += f"- {nome}: {pct}% compatível\n"

        self.result_label.config(text=texto)


if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaApp(root)
    root.mainloop()
