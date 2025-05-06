import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from utils.doencas import get_doencas, exibir_doenca

# Configuração da página com ícone
st.set_page_config(
    page_title="Haber",
    page_icon="images/haber.png"  # Aqui você pode colocar o caminho para o ícone
)

# Cache para evitar recarregamento do modelo toda hora
@st.cache_resource
def load_tflite_model():
    interpreter = tf.lite.Interpreter(model_path="modelo_soja.tflite")
    interpreter.allocate_tensors()
    return interpreter

# Carregar modelo
interpreter = load_tflite_model()

# Detalhes do modelo
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Função de pré-processamento
def preprocess_image(image):
    image = image.resize((224, 224))  # Ajuste conforme o seu modelo
    image_array = np.array(image) / 255.0  # Normaliza
    image_array = np.expand_dims(image_array, axis=0).astype(np.float32)
    return image_array

image = Image.open('images/haber_logo.png')  # Verifique o caminho correto da imagem
st.sidebar.image(image, width=200)

# Criação do menu com o 'option_menu'
from streamlit_option_menu import option_menu
import importlib

#Options Menu
with st.sidebar:
    selected = option_menu(
        '',
        ["Home", 'Doenças', 'Modelo','Histórico'],
        icons=['house', 'search', 'info-circle','collection'],
        default_index=0,
        menu_icon="cast",
        styles={
            "container": {"background-color": "#2D2D2D"},  # Cor do fundo do menu
            "icon": {"color": "white", "font-size": "20px"},  # Cor dos ícones
            "nav-link": {"color": "white", "font-weight": "bold"},  # Cor do texto
            "nav-link-selected": {"background-color": "green", "color": "white"}  # Cor do item selecionado
        }
    )
    st.sidebar.empty()
    st.button("Log-out")

# Carregar conteúdo com base na seleção
if selected == "Doenças":
    doenças_module = importlib.import_module('paginas.doencas')
    doenças_module.display_content()
elif selected == "Modelo":
    modelo_module = importlib.import_module('paginas.modelo')
    modelo_module.display_content()
elif selected == "Histórico":
    modelo_module = importlib.import_module('paginas.historico')
    modelo_module.display_content()
elif selected == "Home":
    #home_module = importlib.import_module('paginas.home')
    # Interface Streamlit

    st.title('🪲 Identificação de Pragas em Folhas de Soja')

    uploaded_file = st.file_uploader("📷 Envie uma imagem de folha de soja", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagem carregada", use_column_width=True)

        # Pré-processa a imagem
        image_array = preprocess_image(image)

        # Alimenta o modelo
        interpreter.set_tensor(input_details[0]['index'], image_array)
        interpreter.invoke()

        # Obtém o resultado
        prediction = interpreter.get_tensor(output_details[0]['index'])

        class_names = [
            'Mossaic Virus',
            'Southern Blight',
            'Sudden Death Syndrome',
            'Yellow Mosaic',
            'Bacterial Blight',
            'Brown Spot',
            'Crestamento',
            'Ferrugem',
            'Powdery Mildew',
            'Septoria'
        ]
        predicted_class = class_names[np.argmax(prediction)]
        confidence = np.max(prediction)

        st.markdown(f"### 🧠 Predição: **{predicted_class}**")
        st.write(f"Confiabilidade: {confidence * 100:.2f}%")

        # Exibir informações adicionais
        doencas = get_doencas()
        if predicted_class in doencas:
            st.markdown("## 📖 Detalhes sobre a doença detectada:")
            exibir_doenca(predicted_class, doencas[predicted_class])
        else:
            st.info("Nenhuma informação detalhada disponível para essa doença.")
