import streamlit as st
import random
import requests
from datetime import date

# Configuração da página para navegação no celular e consoles
st.set_page_config(page_title="Central Alienígena", page_icon="🛸", layout="centered")

# Estilização visual estilo Sci-Fi Neon
st.markdown("""
    <style>
    .stApp { background-color: #06090e; color: #00ff66; font-family: 'Courier New', monospace; }
    h1, h2, h3 { color: #00ff66 !important; }
    .stButton>button { background-color: #002200; color: #00ff66; border: 1px solid #00ff66; width: 100%; font-weight: bold; }
    .stSelectbox label, .stSlider label { color: #00ff66 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🛸 CENTRAL DE COMANDO GALÁCTICO")
st.caption(f"CANAL ATIVO // DATA TERRESTRE: {date.today().strftime('%d/%m/%Y')}")

# Menu de navegação lateral/topo
opcao = st.sidebar.radio("Selecione o Módulo:", [
    "📡 Transmissão Diária", 
    "💌 Bilhete Criptografado", 
    "🧬 Escâner de Espécie",
    "🕹️ Mini-Quiz Espacial"
])

# --- MÓDULO 1: TRANSMISSÃO DIÁRIA ---
if opcao == "📡 Transmissão Diária":
    st.subheader("🌌 FOTO DA NASA E FATO DO DIA")
    
    # Busca a imagem astronômica do dia na API da NASA
    try:
        res = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY").json()
        if "url" in res:
            st.image(res["url"], caption=res.get("title", "Registro Espacial"))
            if "explanation" in res:
                st.write(f"**Detalhes:** {res['explanation'][:250]}...")
    except:
        st.write("✨ [Sinal da NASA sincronizado]")

    curiosidades = [
        "A Equação de Drake estima que pode haver milhares de civilizações inteligentes na Via Láctea.",
        "O famoso 'Sinal Wow!' recebido em 1977 durou 72 segundos e veio da constelação de Sagitário.",
        "A lua Europa de Júpiter possui um oceano líquido coberto por gelo, sendo forte candidata a abrigar vida.",
        "Existem mais estrelas no universo observável do que grãos de areia em todas as praias da Terra."
    ]
    st.info(f"👽 **Fato Ufológico:** {random.choice(curiosidades)}")

# --- MÓDULO 2: BILHETE CRIPTOGRAFADO ---
elif opcao == "💌 Bilhete Criptografado":
    st.subheader("🔒 MENSAGEM SECRETA DO COMANDANTE")
    st.write("Pressione o botão para decodificar a mensagem do dia enviada para o seu setor:")
    
    mensagens = [
        "Aviso do sistema: A força da minha gravidade sempre me puxa direto para você.",
        "Entre mais de 200 bilhões de galáxias no universo, você é a minha pessoa favorita.",
        "Relatório de análise: Ter você por perto é o maior e melhor mistério do cosmos.",
        "Sinal recebido: Você é infinitamente mais incrível que qualquer alienígena do cinema!"
    ]
    
    if st.button("DESCRIPTOGRAFAR MENSAGEM"):
        st.success(f"✨ {random.choice(mensagens)}")

# --- MÓDULO 3: ESCÂNER DE ESPÉCIE ---
elif opcao == "🧬 Escâner de Espécie":
    st.subheader("🧪 ESCÂNER DE ENERGIA ALIENÍGENA")
    energia = st.select_slider("Como está seu nível de energia hoje?", options=["Baixo", "Normal", "Supernova 💥"])
    
    if st.button("DIAGNOSTICAR ESPÉCIE"):
        if energia == "Baixo":
            st.write("🛸 **Diagnóstico:** *Yoda descansando*. Recomendado recarregar as baterias e descansar.")
        elif energia == "Normal":
            st.write("👽 **Diagnóstico:** *Xenomorfo estiloso*. Pronta para dominar as tarefas do dia.")
        else:
            st.write("⚡ **Diagnóstico:** *E.T. na bicicleta voadora*. Energia suficiente para cruzar a galáxia!")

# --- MÓDULO 4: MINI-QUIZ ---
elif opcao == "🕹️ Mini-Quiz Espacial":
    st.subheader("🕹️ VERIFICAÇÃO DE CREDENCIAMENTO")
    resposta = st.radio(
        "Qual é a base militar mais famosa por teorias sobre OVNIs?",
        ["Área 12", "Área 51", "Área 99"],
        index=None
    )
    if st.button("CONFIRMAR RESPOSTA"):
        if resposta == "Área 51":
            st.success("✅ Correto! Credencial de Especialista Espacial Confirmada.")
        else:
            st.error("❌ Resposta incorreta. Tente novamente!")
