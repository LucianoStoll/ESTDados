# PLAYER CIRCULAR DUPLAMENTE ENCADEADO — implementação do exercício.
# Circular: cauda.proximo é cabeca e cabeca.anterior é cauda.
# Um único nó aponta para si mesmo nos dois sentidos.
# Por isso uma varredura não pode esperar None: deve parar após uma volta.
# As anotações str/int/bool documentam os tipos esperados, sem validá-los.

class NodeMusica:
    def __init__(self, titulo: str, artista: str, duracao: int):
        self.titulo = titulo  # Identifica a música, inclusive na busca por remoção.
        self.artista = artista
        self.duracao = duracao  # Segundos, como solicitado no enunciado.
        self.anterior = None  # Serão ligadas ao inserir o nó no player.
        self.proximo = None


class PlayerCircular:
    def __init__(self):
        self.cabeca = None  # Primeira música da playlist.
        self.cauda = None  # Última música da playlist.
        self.faixa_atual = None  # Música selecionada; pode estar no meio.

    def esta_vazia(self) -> bool:
        return self.cabeca is None

    def adicionar_musica(self, titulo: str, artista: str, duracao: int):
        novo = NodeMusica(titulo, artista, duracao)
        if self.esta_vazia():
            novo.proximo = novo  # Um anel de um nó volta para ele mesmo.
            novo.anterior = novo
            self.cabeca = novo
            self.cauda = novo
            self.faixa_atual = novo  # A primeira inserção inicia a seleção.
        else:
            # Encaixa o novo nó entre a antiga cauda e a cabeça.
            novo.anterior = self.cauda
            novo.proximo = self.cabeca
            self.cauda.proximo = novo  # Liga a ida da antiga cauda ao novo.
            self.cabeca.anterior = novo  # Liga a volta da cabeça ao novo.
            self.cauda = novo  # O anel está fechado; atualiza a última faixa.

    def tocar_atual(self):
        if self.esta_vazia():
            print("Playlist vazia.")
            return  # Impede acessar atributos de None.
        atual = self.faixa_atual
        print(f"Tocando: {atual.titulo} - {atual.artista} ({atual.duracao}s)")

    def proxima_musica(self):
        if self.esta_vazia():
            print("Playlist vazia.")
            return
        # Guarda se está atravessando a fronteira para avisar na saída.
        reiniciou = self.faixa_atual is self.cauda
        self.faixa_atual = self.faixa_atual.proximo  # O(1), mesmo na última faixa.
        atual = self.faixa_atual
        aviso = " [REINICIOU O CICLO]" if reiniciou else ""
        print(f"Avançando: {atual.titulo} - {atual.artista} ({atual.duracao}s){aviso}")

    def voltar_musica(self):
        if self.esta_vazia():
            print("Playlist vazia.")
            return
        voltou_ao_fim = self.faixa_atual is self.cabeca
        self.faixa_atual = self.faixa_atual.anterior  # Volta diretamente, O(1).
        atual = self.faixa_atual
        aviso = " [PULOU PARA A ÚLTIMA]" if voltou_ao_fim else ""
        print(f"Voltando: {atual.titulo} - {atual.artista} ({atual.duracao}s){aviso}")

    def exibir_playlist(self):
        if self.esta_vazia():
            print("Playlist vazia.")
            return
        print("=== FILA DE REPRODUÇÃO (LOOP ATIVO) ===")
        atual = self.cabeca
        numero = 1  # Número visual da faixa, não um índice para acessar nós.
        while True:  # Executa ao menos uma vez; o break encerra após a volta.
            marca = "[TOCANDO AGORA] " if atual is self.faixa_atual else ""
            print(f"{numero}. {marca}{atual.titulo} - {atual.artista} ({atual.duracao}s)")
            numero += 1
            atual = atual.proximo
            # is compara a identidade: é o MESMO objeto inicial?
            if atual is self.cabeca:
                break  # Sem esta condição, uma lista circular nunca terminaria.
        print("=======================================")

    def remover_musica(self, titulo: str) -> bool:
        if self.esta_vazia():
            return False
        atual = self.cabeca
        while True:
            if atual.titulo == titulo:
                if atual.proximo is atual:  # Único nó: o anel inteiro desaparece.
                    self.cabeca = None
                    self.cauda = None
                    self.faixa_atual = None
                else:
                    # Os dois vizinhos passam a se ligar diretamente.
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                    if atual is self.cabeca:
                        self.cabeca = atual.proximo
                    if atual is self.cauda:
                        self.cauda = atual.anterior
                    if atual is self.faixa_atual:
                        # Política escolhida: se a música tocando sai, segue a próxima.
                        self.faixa_atual = atual.proximo
                # Só desliga depois de reaproveitar todas as referências necessárias.
                atual.anterior = None
                atual.proximo = None
                print(f"[!] Música '{titulo}' removida da playlist circular.")
                return True  # Remove apenas a primeira ocorrência desse título.
            atual = atual.proximo
            if atual is self.cabeca:
                return False  # Completou uma volta e não encontrou o título.


# RESUMO: inserção no fim e navegação O(1); exibição e remoção por título O(n).
# Não procure None dentro de um anel não vazio; use identidade com a cabeça.
# Remoção precisa preservar cabeça, cauda, faixa atual e as duas ligações.
# A demonstração original abaixo testa a volta contínua nos dois sentidos.

if __name__ == "__main__":
    player = PlayerCircular()

    print("--- 1. Adicionando 3 faixas à Playlist Circular ---")
    player.adicionar_musica("Bohemian Rhapsody", "Queen", 354)
    player.adicionar_musica("Hotel California", "Eagles", 391)
    player.adicionar_musica("Billie Jean", "Michael Jackson", 294)

    player.exibir_playlist()

    print("\n--- 2. Testando Loop Contínuo para Frente (Avançar 4 vezes) ---")
    player.tocar_atual()
    player.proxima_musica()  # Hotel California
    player.proxima_musica()  # Billie Jean (última)
    player.proxima_musica()  # Volta para Bohemian Rhapsody (início)!
    player.proxima_musica()  # Hotel California

    print("\n--- 3. Testando Loop para Trás (Voltar 2 vezes) ---")
    player.voltar_musica()   # Bohemian Rhapsody
    player.voltar_musica()   # Vai direto para Billie Jean (última)!

    print("\n--- 4. Removendo faixa da cabeça em lista circular ---")
    player.remover_musica("Bohemian Rhapsody")
    player.exibir_playlist()

# =====================================================================
# 4. SAIDA ESPERADA
# =====================================================================

# --- 1. Adicionando 3 faixas à Playlist Circular ---
# === FILA DE REPRODUÇÃO (LOOP ATIVO) ===
# 1. [TOCANDO AGORA] Bohemian Rhapsody - Queen (354s)
# 2. Hotel California - Eagles (391s)
# 3. Billie Jean - Michael Jackson (294s)
# =======================================

# --- 2. Testando Loop Contínuo para Frente (Avançar 4 vezes) ---
# ▶ Tocando: Bohemian Rhapsody - Queen (354s)
# ⏭ Avançando: Hotel California - Eagles (391s)
# ⏭ Avançando: Billie Jean - Michael Jackson (294s)
# ⏭ Avançando: Bohemian Rhapsody - Queen (354s) [REINICIOU O CICLO]
# ⏭ Avançando: Hotel California - Eagles (391s)

# --- 3. Testando Loop para Trás (Voltar 2 vezes) ---
# ⏮ Voltando: Bohemian Rhapsody - Queen (354s)
# ⏮ Voltando: Billie Jean - Michael Jackson (294s) [PULOU PARA A ÚLTIMA]

# --- 4. Removendo faixa da cabeça em lista circular ---
# [!] Música 'Bohemian Rhapsody' removida da playlist circular.
# === FILA DE REPRODUÇÃO (LOOP ATIVO) ===
# 1. Hotel California - Eagles (391s)
# 2. [TOCANDO AGORA] Billie Jean - Michael Jackson (294s)
# =======================================