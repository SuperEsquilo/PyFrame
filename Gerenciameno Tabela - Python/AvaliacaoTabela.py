import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import os
from PIL import Image, ImageTk

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

class TabelaApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1368x750")
        self.root.title("Tabela de avaliação")
        # Não usar iconbitmap para evitar o erro com o arquivo .ico
        # Em vez disso, definimos o título apenas
        pass
        
        # Variáveis para armazenar dados temporários
        self.dados = []
        self.colunas = ["ID", "Nome", "Descrição", "Valor", "Status"]
        self.arquivo_atual = None
        
        # Frame principal
        self.frame_principal = ctk.CTkFrame(self.root)
        self.frame_principal.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Título
        self.lbl_titulo = ctk.CTkLabel(self.frame_principal, text="Tabela de avaliação", 
                                     font=("Comfortaa", 24, "bold"))
        self.lbl_titulo.pack(pady=10)
        
        # Frame para botões de ação
        self.frame_acoes = ctk.CTkFrame(self.frame_principal)
        self.frame_acoes.pack(fill="x", padx=10, pady=10)
        
        # Botões de ação
        self.btn_adicionar = ctk.CTkButton(self.frame_acoes, text="Adicionar", command=self.adicionar_item)
        self.btn_adicionar.pack(side="left", padx=5)
        
        self.btn_editar = ctk.CTkButton(self.frame_acoes, text="Editar", command=self.editar_item)
        self.btn_editar.pack(side="left", padx=5)
        
        self.btn_excluir = ctk.CTkButton(self.frame_acoes, text="Excluir", command=self.excluir_item)
        self.btn_excluir.pack(side="left", padx=5)
        
        self.btn_personalizar = ctk.CTkButton(self.frame_acoes, text="Personalizar", command=self.personalizar_tabela)
        self.btn_personalizar.pack(side="left", padx=5)
        
        self.btn_exportar = ctk.CTkButton(self.frame_acoes, text="Exportar", command=self.exportar_dados)
        self.btn_exportar.pack(side="left", padx=5)
        
        self.btn_importar = ctk.CTkButton(self.frame_acoes, text="Importar", command=self.importar_dados)
        self.btn_importar.pack(side="left", padx=5)
        
        # Frame para a tabela
        self.frame_tabela = ctk.CTkFrame(self.frame_principal)
        self.frame_tabela.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Criação da tabela usando Treeview
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", background="#2b2b2b", 
                            foreground="white", fieldbackground="#2b2b2b")
        self.style.map('Treeview', background=[('selected', '#1f538d')])
        
        # Criando um frame para conter a tabela e a barra de rolagem
        self.tree_frame = tk.Frame(self.frame_tabela, bg="#2b2b2b")
        self.tree_frame.pack(fill="both", expand=True)
        
        # Barra de rolagem vertical
        self.vsb = ttk.Scrollbar(self.tree_frame, orient="vertical")
        self.vsb.pack(side="right", fill="y")
        
        # Barra de rolagem horizontal
        self.hsb = ttk.Scrollbar(self.tree_frame, orient="horizontal")
        self.hsb.pack(side="bottom", fill="x")
        
        # Criando a tabela
        self.tabela_tree = ttk.Treeview(self.tree_frame, columns=self.colunas, 
                                      show="headings", yscrollcommand=self.vsb.set,
                                      xscrollcommand=self.hsb.set)
        
        # Configurando as barras de rolagem
        self.vsb.config(command=self.tabela_tree.yview)
        self.hsb.config(command=self.tabela_tree.xview)
        
        # Configurando cabeçalhos
        for col in self.colunas:
            self.tabela_tree.heading(col, text=col, anchor="center")
            self.tabela_tree.column(col, anchor="center", width=100)
        
        self.tabela_tree.pack(fill="both", expand=True)
        
        # Adicionar alguns dados de exemplo
        self.adicionar_dados_exemplo()
    
    def adicionar_dados_exemplo(self):
        dados_exemplo = [
            ("1", "Item 1", "Descrição do item 1", "100.00", "Ativo"),
            ("2", "Item 2", "Descrição do item 2", "200.00", "Inativo"),
            ("3", "Item 3", "Descrição do item 3", "300.00", "Ativo")
        ]
        
        for item in dados_exemplo:
            self.tabela_tree.insert("", "end", values=item)
            self.dados.append(item)
    
    def adicionar_item(self):
        # Janela para adicionar novo item
        self.janela_adicionar = ctk.CTkToplevel(self.root)
        self.janela_adicionar.title("Adicionar Item")
        self.janela_adicionar.geometry("400x300")
        self.janela_adicionar.grab_set()  # Torna a janela modal
        
        # Campos de entrada
        ctk.CTkLabel(self.janela_adicionar, text="ID:").pack(pady=5)
        self.entry_id = ctk.CTkEntry(self.janela_adicionar)
        self.entry_id.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_adicionar, text="Nome:").pack(pady=5)
        self.entry_nome = ctk.CTkEntry(self.janela_adicionar)
        self.entry_nome.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_adicionar, text="Descrição:").pack(pady=5)
        self.entry_descricao = ctk.CTkEntry(self.janela_adicionar)
        self.entry_descricao.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_adicionar, text="Valor:").pack(pady=5)
        self.entry_valor = ctk.CTkEntry(self.janela_adicionar)
        self.entry_valor.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_adicionar, text="Status:").pack(pady=5)
        self.entry_status = ctk.CTkComboBox(self.janela_adicionar, values=["Ativo", "Inativo", "Pendente"])
        self.entry_status.pack(pady=5, padx=20, fill="x")
        
        # Botão para salvar
        ctk.CTkButton(self.janela_adicionar, text="Salvar", command=self.salvar_novo_item).pack(pady=10)
    
    def salvar_novo_item(self):
        # Obter valores dos campos
        id_item = self.entry_id.get()
        nome = self.entry_nome.get()
        descricao = self.entry_descricao.get()
        valor = self.entry_valor.get()
        status = self.entry_status.get()
        
        # Validar campos
        if not all([id_item, nome, descricao, valor, status]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        # Adicionar à tabela
        novo_item = (id_item, nome, descricao, valor, status)
        self.tabela_tree.insert("", "end", values=novo_item)
        self.dados.append(novo_item)
        
        # Fechar janela
        self.janela_adicionar.destroy()
    
    def editar_item(self):
        # Verificar se um item está selecionado
        selecao = self.tabela_tree.selection()
        if not selecao:
            messagebox.showinfo("Informação", "Selecione um item para editar.")
            return
        
        # Obter valores do item selecionado
        item = self.tabela_tree.item(selecao[0])
        valores = item['values']
        
        # Janela para editar item
        self.janela_editar = ctk.CTkToplevel(self.root)
        self.janela_editar.title("Editar Item")
        self.janela_editar.geometry("400x300")
        self.janela_editar.grab_set()  # Torna a janela modal
        
        # Campos de entrada preenchidos com os valores atuais
        ctk.CTkLabel(self.janela_editar, text="ID:").pack(pady=5)
        self.edit_entry_id = ctk.CTkEntry(self.janela_editar)
        self.edit_entry_id.insert(0, valores[0])
        self.edit_entry_id.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_editar, text="Nome:").pack(pady=5)
        self.edit_entry_nome = ctk.CTkEntry(self.janela_editar)
        self.edit_entry_nome.insert(0, valores[1])
        self.edit_entry_nome.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_editar, text="Descrição:").pack(pady=5)
        self.edit_entry_descricao = ctk.CTkEntry(self.janela_editar)
        self.edit_entry_descricao.insert(0, valores[2])
        self.edit_entry_descricao.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_editar, text="Valor:").pack(pady=5)
        self.edit_entry_valor = ctk.CTkEntry(self.janela_editar)
        self.edit_entry_valor.insert(0, valores[3])
        self.edit_entry_valor.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_editar, text="Status:").pack(pady=5)
        self.edit_entry_status = ctk.CTkComboBox(self.janela_editar, values=["Ativo", "Inativo", "Pendente"])
        self.edit_entry_status.set(valores[4])
        self.edit_entry_status.pack(pady=5, padx=20, fill="x")
        
        # Botão para salvar
        ctk.CTkButton(self.janela_editar, text="Salvar", 
                     command=lambda: self.salvar_item_editado(selecao[0])).pack(pady=10)
    
    def salvar_item_editado(self, item_id):
        # Obter valores dos campos
        id_item = self.edit_entry_id.get()
        nome = self.edit_entry_nome.get()
        descricao = self.edit_entry_descricao.get()
        valor = self.edit_entry_valor.get()
        status = self.edit_entry_status.get()
        
        # Validar campos
        if not all([id_item, nome, descricao, valor, status]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
            return
        
        # Atualizar na tabela
        novo_item = (id_item, nome, descricao, valor, status)
        self.tabela_tree.item(item_id, values=novo_item)
        
        # Atualizar na lista de dados
        indice = self.tabela_tree.index(item_id)
        if indice < len(self.dados):
            self.dados[indice] = novo_item
        
        # Fechar janela
        self.janela_editar.destroy()
    
    def excluir_item(self):
        # Verificar se um item está selecionado
        selecao = self.tabela_tree.selection()
        if not selecao:
            messagebox.showinfo("Informação", "Selecione um item para excluir.")
            return
        
        # Confirmar exclusão
        if messagebox.askyesno("Confirmar", "Tem certeza que deseja excluir este item?"):
            # Remover da tabela
            for item in selecao:
                indice = self.tabela_tree.index(item)
                self.tabela_tree.delete(item)
                
                # Remover da lista de dados
                if indice < len(self.dados):
                    self.dados.pop(indice)
    
    def personalizar_tabela(self):
        # Janela para personalização
        self.janela_personalizar = ctk.CTkToplevel(self.root)
        self.janela_personalizar.title("Personalizar Tabela")
        self.janela_personalizar.geometry("400x300")
        self.janela_personalizar.grab_set()  # Torna a janela modal
        
        # Opções de personalização
        ctk.CTkLabel(self.janela_personalizar, text="Cor de fundo:").pack(pady=5)
        self.cor_fundo = ctk.CTkComboBox(self.janela_personalizar, 
                                       values=["Escuro", "Claro", "Azul", "Verde"])
        self.cor_fundo.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_personalizar, text="Cor de seleção:").pack(pady=5)
        self.cor_selecao = ctk.CTkComboBox(self.janela_personalizar, 
                                         values=["Azul", "Verde", "Laranja", "Vermelho"])
        self.cor_selecao.pack(pady=5, padx=20, fill="x")
        
        ctk.CTkLabel(self.janela_personalizar, text="Tamanho da fonte:").pack(pady=5)
        self.tamanho_fonte = ctk.CTkComboBox(self.janela_personalizar, 
                                           values=["Pequeno", "Médio", "Grande"])
        self.tamanho_fonte.pack(pady=5, padx=20, fill="x")
        
        # Botão para aplicar
        ctk.CTkButton(self.janela_personalizar, text="Aplicar", 
                     command=self.aplicar_personalizacao).pack(pady=10)
    
    def aplicar_personalizacao(self):
        # Aplicar personalização à tabela
        cor_fundo = self.cor_fundo.get()
        cor_selecao = self.cor_selecao.get()
        tamanho_fonte = self.tamanho_fonte.get()
        
        # Mapear valores para cores reais
        cores_fundo = {
            "Escuro": "#2b2b2b",
            "Claro": "#f0f0f0",
            "Azul": "#1e3d59",
            "Verde": "#2c5e1a"
        }
        
        cores_selecao = {
            "Azul": "#1f538d",
            "Verde": "#2e8b57",
            "Laranja": "#ff8c00",
            "Vermelho": "#b22222"
        }
        
        tamanhos_fonte = {
            "Pequeno": 9,
            "Médio": 10,
            "Grande": 12
        }
        
        # Aplicar cores
        bg_color = cores_fundo.get(cor_fundo, "#2b2b2b")
        fg_color = "white" if cor_fundo in ["Escuro", "Azul", "Verde"] else "black"
        sel_color = cores_selecao.get(cor_selecao, "#1f538d")
        
        self.style.configure("Treeview", 
                            background=bg_color, 
                            foreground=fg_color, 
                            fieldbackground=bg_color,
                            font=("TkDefaultFont", tamanhos_fonte.get(tamanho_fonte, 10)))
        
        self.style.map('Treeview', background=[('selected', sel_color)])
        
        # Fechar janela
        self.janela_personalizar.destroy()
    
    def exportar_dados(self):
        # Verificar se há dados para exportar
        if not self.dados:
            messagebox.showinfo("Informação", "Não há dados para exportar.")
            return
        
        # Perguntar onde salvar o arquivo
        arquivo = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV", "*.csv"), ("Excel", "*.xlsx")]
        )
        
        if not arquivo:
            return
        
        try:
            # Criar DataFrame com os dados
            df = pd.DataFrame(self.dados, columns=self.colunas)
            
            # Exportar de acordo com a extensão
            if arquivo.endswith('.csv'):
                df.to_csv(arquivo, index=False)
            elif arquivo.endswith('.xlsx'):
                df.to_excel(arquivo, index=False)
            
            messagebox.showinfo("Sucesso", f"Dados exportados com sucesso para {os.path.basename(arquivo)}")
            self.arquivo_atual = arquivo
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao exportar dados: {str(e)}")
    
    def importar_dados(self):
        # Perguntar qual arquivo importar
        arquivo = filedialog.askopenfilename(
            filetypes=[("CSV", "*.csv"), ("Excel", "*.xlsx")]
        )
        
        if not arquivo:
            return
        
        try:
            # Importar de acordo com a extensão
            if arquivo.endswith('.csv'):
                df = pd.read_csv(arquivo)
            elif arquivo.endswith('.xlsx'):
                df = pd.read_excel(arquivo)
            else:
                messagebox.showerror("Erro", "Formato de arquivo não suportado.")
                return
            
            # Limpar tabela atual
            for item in self.tabela_tree.get_children():
                self.tabela_tree.delete(item)
            
            self.dados = []
            
            # Verificar e ajustar colunas se necessário
            if list(df.columns) != self.colunas:
                if messagebox.askyesno("Aviso", "As colunas do arquivo são diferentes das colunas da tabela. Deseja continuar?"): 
                    # Ajustar colunas
                    for col in df.columns:
                        if col not in self.colunas:
                            self.colunas.append(col)
                            self.tabela_tree["columns"] = self.colunas
                            self.tabela_tree.heading(col, text=col, anchor="center")
                            self.tabela_tree.column(col, anchor="center", width=100)
                else:
                    return
            
            # Adicionar dados à tabela
            for _, row in df.iterrows():
                valores = row.tolist()
                self.tabela_tree.insert("", "end", values=valores)
                self.dados.append(tuple(valores))
            
            messagebox.showinfo("Sucesso", f"Dados importados com sucesso de {os.path.basename(arquivo)}")
            self.arquivo_atual = arquivo
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao importar dados: {str(e)}")

# Iniciar aplicação
if __name__ == "__main__":
    tabela = ctk.CTk()
    app = TabelaApp(tabela)
    tabela.mainloop()