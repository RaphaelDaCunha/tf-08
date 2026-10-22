class Commit:
    # Representa um commit e guarda suas informacoes.

    def __init__(self, id, mensagem, autor, pai=None):
        # Guarda o id, a mensagem, o autor e o commit anterior.
        self.id = id
        self.mensagem = mensagem
        self.autor = autor
        self.pai = pai

    def historico(self):
        # Mostra este commit e percorre os commits anteriores.
        print(f"#{self.id} {self.mensagem} ({self.autor})")

        # Para quando chegar ao primeiro commit, que nao tem pai.
        if self.pai is None:
            return

        # Chama o historico do commit anterior.
        self.pai.historico()


class Repositorio:
    # Gerencia os commits de um projeto.

    def __init__(self, nome, autor):
        # Guarda o nome e o autor e inicia o repositorio vazio.
        self.nome = nome
        self.autor = autor
        self.head = None
        self.contador = 0

    def commitar(self, mensagem):
        # Aumenta o contador e cria um commit ligado ao anterior.
        self.contador += 1
        novo_commit = Commit(
            self.contador,
            mensagem,
            self.autor,
            self.head
        )

        # Atualiza o head para apontar para o novo commit.
        self.head = novo_commit

    def log(self):
        # Mostra o historico ou avisa se nao houver commits.
        if self.head is None:
            print("Nenhum commit ainda")
            return

        # Comeca pelo commit mais recente.
        self.head.historico()

    def total_de_commits(self):
        # Conta os commits percorrendo os pais com while.
        total = 0
        commit_atual = self.head

        while commit_atual is not None:
            total += 1
            commit_atual = commit_atual.pai

        # Devolve a quantidade total de commits encontrados.
        return total


# Cria um repositorio para testar as classes.
repositorio = Repositorio(
    "meu-projeto",
    "Raphael apparecido da cunha - 6326072"
)

# Mostra a mensagem porque o repositorio esta vazio.
repositorio.log()

# Registra tres commits de teste.
repositorio.commitar("Cria a estrutura inicial")
repositorio.commitar("Adiciona a documentacao")
repositorio.commitar("Corrige a documentacao")

# Mostra o historico do mais recente ao mais antigo.
repositorio.log()

# Mostra a quantidade total de commits.
print(repositorio.total_de_commits())