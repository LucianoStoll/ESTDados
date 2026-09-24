# 1. Objetivo

# Implementar uma estrutura de dados Circular Duplamente Encadeada para simular o comportamento de um reprodutor de áudio com modo repetição infinito (Repeat All), manipulando nós com ponteiros bidirecionais contínuos sem terminação em None.
# 2. Requisitos da Estrutura

#     Fechamento do Ciclo:

#         Se houver apenas 1 nó: novo.proximo = novo e novo.anterior = novo.

#         Para múltiplos nós: self.cauda.proximo = self.cabeca e self.cabeca.anterior = self.cauda.

#     Navegação Contínua ($O(1)$):

#         Ao avançar (proxima_musica) na última faixa, a reprodução continua na primeira faixa.

#         Ao voltar (voltar_musica) na primeira faixa, a reprodução retrocede direto para a última faixa.

#     Condição de Parada na Impressão: O laço de varredura não procura mais por None. Deve parar ao completar uma volta completa e retornar ao nó inicial.

# =====================================================================
# 1. NÓ DE MÚSICA
# =====================================================================
class NodeMusica:
    def __init__(self, titulo: str, artista: str, duracao: int):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao  # em segundos
        self.anterior = None
        self.proximo = None


# =====================================================================
# 2. TAD DO PLAYER CIRCULAR DUPLAMENTE ENCADEADO
# =====================================================================
class PlayerCircular:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.faixa_atual = None

    def esta_vazia(self) -> bool:
        return self.cabeca is None

    def adicionar_musica(self, titulo: str, artista: str, duracao: int):
        """Insere no fim mantendo o anel fechado."""
        pass

    def tocar_atual(self):
        """Exibe a faixa em reprodução."""
        pass

    def proxima_musica(self):
        """Avança infinitamente em ciclo"""
        pass

    def voltar_musica(self):
        """Retorna infinitamente em ciclo"""
        pass

    def exibir_playlist(self):
        """Percorre exatamente 1 ciclo completo."""
        pass

    def remover_musica(self, titulo: str) -> bool:
        """Remove o nó e refaz a costura circular."""
        pass


# =====================================================================
# 3. TESTES DE VALIDAÇÃO
# =====================================================================
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