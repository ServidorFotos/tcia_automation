import streamlit as st
import time

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="TCIA - Processador de Ativos",
    page_icon="🤖",
    layout="centered"
)

# --- ESTILIZAÇÃO DO LOGO TCIA (LARANJA E GRAFITE) ---
st.markdown("""
    <style>
    .main { background-color: #2A2927; color: #FFFFFF; }
    h1 { color: #F39200 !important; font-family: 'Arial', sans-serif; text-align: center; margin-bottom: 0px; }
    .stButton>button { background-color: #F39200; color: white; width: 100%; font-weight: bold; border: none; height: 45px; }
    .stButton>button:hover { background-color: #D68100; color: white; }
    div[data-testid="stHeading"] h2 { color: #FFFFFF !important; }
    </style>
""", unsafe_allow_html=True)

st.title("TCIA | AUTOMATION")
st.write("---")

# --- SISTEMA DE ABAS WEB ---
aba1, aba2 = st.tabs([" 1. Sincronizador de Planilha ", " 2. Recortador com IA "])

# ==========================================
# --- ABA 1: ORGANIZADOR / SINCRONIZADOR ---
# ==========================================
with aba1:
    st.subheader("Triagem e Sincronismo de Inventário")
    
    # 1. Upload do arquivo Excel direto pelo navegador
    arquivo_excel = st.file_uploader("1. Faça o upload da Planilha de Inventário (.xlsx)", type=["xlsx"], key="excel_uploader")
    
    # 2. Upload de múltiplos arquivos de foto (Ativa câmera ou galeria no celular)
    fotos_sincronismo = st.file_uploader("2. Selecione da Galeria ou tire as fotos dos ativos:", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="fotos_sinc")
    
    if fotos_sincronismo:
        st.write(f"📸 **{len(fotos_sincronismo)} foto(s) carregada(s) para sincronismo.**")
        
    # 3. Campo de texto para a coluna
    nome_coluna = st.text_input("3. Nome da Coluna com os Códigos na Planilha:", placeholder="Ex: Patrimonio", key="coluna_input")
    
    st.write("") # Espaçador
    
    # Botão de Execução da Aba 1
    if st.button("SINCRONIZAR FOTOS NA PLANILHA", key="btn_run_sinc"):
        if arquivo_excel and fotos_sincronismo and nome_coluna:
            barra_progresso_sinc = st.progress(0)
            status_sinc = st.empty()
            
            status_sinc.info("Processando lote de fotos e varrendo códigos de barra...")
            
            # Simulando o loop de processamento do seu script original
            total_sinc = len(fotos_sincronismo)
            for idx, foto in enumerate(fotos_sincronismo):
                # Aqui rodaria sua lógica de ler código de barra e injetar na linha correspondente do dataframe
                time.sleep(0.04) 
                percentual = int(((idx + 1) / total_sinc) * 100)
                barra_progresso_sinc.progress(percentual)
                status_sinc.info(f"Sincronizando foto {idx + 1} de {total_sinc}...")
                
            status_sinc.success("🎉 Sincronismo concluído! O download do novo arquivo está disponível abaixo.")
            
            # Disponibiliza o download do arquivo atualizado para o PC ou Celular
            st.download_button(
                label="📥 Baixar Planilha Atualizada",
                data=b"conteudo_excel_ficticio", # Aqui entrará o binário do seu DataFrame (ex: df.to_excel())
                file_name="inventario_atualizado.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key="download_excel"
            )
        else:
            st.warning("Por favor, certifique-se de carregar a planilha, as fotos e digitar o nome da coluna.")

# ==========================================
# --- ABA 2: RECORTADOR IA ---
# ==========================================
with aba2:
    st.subheader("Recortador Cirúrgico (YOLOv8 + OCR)")
    st.success("✓ Modelos YOLOv8 e Tesseract prontos na memória do servidor.")
    
    # Upload de fotos para o recortador (Também ativa câmera ou galeria no smartphone)
    fotos_para_recortar = st.file_uploader(
        "Selecione as fotos da Galeria ou toque para Tirar uma Foto da etiqueta:", 
        type=["jpg", "jpeg", "png"], 
        accept_multiple_files=True, 
        key="recortador_uploader"
    )
    
    if fotos_para_recortar:
        st.write(f"📸 **{len(fotos_para_recortar)} foto(s) carregada(s) e pronta(s) para o corte.**")
    
    st.write("") # Espaçador
    
    # Botão de Execução da Aba 2
    if st.button("EXECUTAR RECORTE EM LOTE", key="btn_run_recorte"):
        if fotos_para_recortar:
            barra_recorte = st.progress(0)
            status_recorte = st.empty()
            
            status_recorte.info("A IA do servidor está processando as imagens...")
            
            # Simulando a passagem das imagens pelo YOLOv8 e OCR
            total_recorte = len(fotos_para_recortar)
            for idx, foto in enumerate(fotos_para_recortar):
                # Aqui rodaria seu recorte cirúrgico com métrica adaptativa
                time.sleep(0.05) 
                percentual = int(((idx + 1) / total_recorte) * 100)
                barra_recorte.progress(percentual)
                status_recorte.info(f"Cortando etiqueta da foto {idx + 1} de {total_recorte}...")
                
            status_recorte.success(f"🎉 Recorte finalizado! {total_recorte} de {total_recorte} etiquetas extraídas com sucesso.")
            
            # Botão para baixar todas as imagens recortadas compactadas em um único arquivo ZIP
            st.download_button(
                label="📥 Baixar Todas as Etiquetas Recortadas (.ZIP)",
                data=b"conteudo_zip_ficticio", # Aqui entrará o arquivo .zip gerado pelo seu script no servidor
                file_name="etiquetas_recortadas.zip",
                mime="application/zip",
                key="download_zip"
            )
        else:
            st.warning("Por favor, tire uma foto ou selecione arquivos da galeria primeiro.")
