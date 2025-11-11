class comp:
    def __init__(self, n, t):
        self.nome = n
        self.tipo = t
        self.nivel = 0

    def setNivel(self, nvl):
        if nvl >= 0 and nvl <= 10:
            self.nivel = nvl
        else:
            print("valor errado pra nivel")

class perfil:
    def __init__(self, n):
        self.nome = n
        self.comps = []

    def addComp(self, c):
        self.comps.append(c)

    def mediaComp(self):
        if len(self.comps) == 0:
            return 0
        soma = 0
        for c in self.comps:
            soma += c.nivel
        media = soma / len(self.comps)
        return media


class carreira:
    def __init__(self, n, ex, p):
        self.nome = n
        self.exig = ex
        self.pesos = p

    def calc(self, perf):
        soma = 0
        pTotal = 0
        for nomeComp in self.exig:
            ex = self.exig[nomeComp]
            peso = 1
            if nomeComp in self.pesos:
                peso = self.pesos[nomeComp]

            compx = None
            for c in perf.comps:
                if c.nome == nomeComp:
                    compx = c
                    break

            if compx == None:
                continue

            if compx.nivel >= ex:
                pontos = 10
            else:
                try:
                    pontos = (compx.nivel / ex) * 10
                except:
                    pontos = 0

            soma += pontos * peso
            pTotal += peso

        if pTotal == 0:
            return 0
        return round((soma / (10 * pTotal)) * 100, 1)


class Sistema:
    def __init__(self):
        self.perfis = []
        self.carreiras = []
        self.carregaPadrao()

    def carregaPadrao(self):
        # deu preguiça de fazer loop, entao foi assim mesmo
        self.carreiras.append(carreira("Dev Software",
            {"logica":8,"criatividade":6,"colaboracao":5,"adaptabilidade":7},
            {"logica":3,"criatividade":2,"colaboracao":1,"adaptabilidade":2}))
        self.carreiras.append(carreira("UX/UI Designer",
            {"logica":5,"criatividade":9,"colaboracao":7,"adaptabilidade":6},
            {"logica":1,"criatividade":3,"colaboracao":2,"adaptabilidade":2}))
        self.carreiras.append(carreira("Analista Dados",
            {"logica":9,"criatividade":5,"colaboracao":6,"adaptabilidade":7},
            {"logica":4,"criatividade":1,"colaboracao":2,"adaptabilidade":2}))
        self.carreiras.append(carreira("Gerente Projetos",
            {"logica":6,"criatividade":6,"colaboracao":9,"adaptabilidade":8},
            {"logica":1,"criatividade":1,"colaboracao":4,"adaptabilidade":3}))

    def cadastrarPerfil(self):
        nome = input("nome do perfil: ")
        p = perfil(nome)
        comps = ["logica","criatividade","colaboracao","adaptabilidade"]

        for c in comps:
            ok = False
            while not ok:
                try:
                    n = int(input(f"nivel de {c} (0 a 10): "))
                    if n < 0 or n > 10:
                        print("coloca certo ai")
                    else:
                        ok = True
                except:
                    print("so numero man")

            tipo = "tecnica" if c == "logica" else "comportamental"
            x = comp(c, tipo)
            x.setNivel(n)
            p.addComp(x)

        self.perfis.append(p)
        print("salvo\n")

    def analisarPerfil(self):
        if len(self.perfis) == 0:
            print("n tem perfil salvo ainda")
            return

        nome = input("nome pra analisar: ")
        perfilz = None
        for p in self.perfis:
            if p.nome == nome:
                perfilz = p
                break

        if perfilz == None:
            print("achei n")
            return

        print("\n--- resultado ---\n")
        res = []
        for c in self.carreiras:
            compa = c.calc(perfilz)
            res.append((c.nome, compa))

        res.sort(key=lambda x: x[1], reverse=True)

        print(f"perfil: {perfilz.nome}")
        print("recomendacoes:")
        for nome, pct in res:
            print(f" - {nome}: {pct}%")
        print()

    def menu(self):
        while True:
            print("Sistema Russi de Empregos")
            print("1-cadastrar perfil")
            print("2-analisar perfil")
            print("3-sair")
            op = input("choise: ")

            if op == "1":
                self.cadastrarPerfil()
            elif op == "2":
                self.analisarPerfil()
            elif op == "3":
                print("flw")
                break
            else:
                print("opc invalida\n")


if __name__ == "__main__":
    s = Sistema()
    s.menu()
