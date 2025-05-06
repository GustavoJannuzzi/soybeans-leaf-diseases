# pages/doencas.py

import streamlit as st

#st.set_page_config(page_title="Doenças da Soja", layout="wide")
def display_content():
    st.title("🦠 Doenças em Folhas de Soja")
    st.markdown("Aqui você encontra uma descrição breve, agrotóxicos recomendados e os cuidados que o produtor deve ter para cada doença.")

    def bloco_doenca(titulo, nome_cientifico, descricao, agrot, cuidados):
        st.markdown(f"""
        <div style="border:1px solid #333; border-radius:10px; padding:20px; margin-bottom:20px; background-color:#121212; color:#d1d1d1">
            <h4 style="color:#76ff03;">🌱 <b>{titulo}</b> <span style="font-weight:normal; color:#999;">({nome_cientifico})</span></h4>
            <ul>
                <li><b>🧾 Descrição:</b> {descricao}</li>
                <li><b>💊 Agrotóxico:</b> {agrot}</li>
                <li><b>🛡️ Cuidados:</b>
                    <ul>
                        {''.join([f"<li>{c}</li>" for c in cuidados])}
                    </ul>
                </li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


    bloco_doenca(
        "Mossaic Virus", "Vírus do Mosaico",
        "Causa manchas amareladas irregulares nas folhas (efeito mosaico), levando à queda da produtividade.",
        "Não há tratamento químico direto contra vírus.",
        [
            "Uso de sementes certificadas e livres do vírus",
            "Controle de vetores como **pulgões** (ex: *Imidacloprido*)",
            "Eliminar plantas daninhas hospedeiras"
        ]
    )

    bloco_doenca(
        "Southern Blight", "Sclerotium rolfsii",
        "Apodrecimento na base da planta com presença de micélio branco e escleródios.",
        "Fungicidas à base de **Fluazinam**, **Thiabendazole** ou **Azoxystrobina**.",
        [
            "Rotação de culturas",
            "Boa drenagem do solo",
            "Evitar plantio direto sobre palhada contaminada"
        ]
    )

    bloco_doenca(
        "Sudden Death Syndrome (SDS)", "Fusarium virguliforme",
        "Clorose entre nervuras e necrose das folhas. Raízes afetadas.",
        "Tratamento de sementes com **Fluopyram** ou **Ilevo® (fluopyram + metalaxil)**.",
        [
            "Rotação de culturas",
            "Cultivares resistentes",
            "Evitar solos compactados e excesso de umidade"
        ]
    )

    bloco_doenca(
        "Yellow Mosaic", "Vírus do Mosaico Amarelo da Soja",
        "Amarelecimento das folhas com padrão em mosaico, transmitido por **mosca-branca**.",
        "Controle com **Acetamiprido**, **Bifentrina** ou **Imidacloprido**.",
        [
            "Controle do vetor",
            "Plantio de variedades tolerantes",
            "Eliminação de plantas voluntárias"
        ]
    )

    bloco_doenca(
        "Bacterial Blight", "Pseudomonas savastanoi pv. glycinea",
        "Manchas angulares nas folhas com aparência oleosa, evoluindo para necrose.",
        "Sem controle curativo direto. **Cúpricos** podem ser usados preventivamente.",
        [
            "Evitar sementes infectadas",
            "Rotação de culturas",
            "Evitar irrigação por aspersão"
        ]
    )

    bloco_doenca(
        "Brown Spot", "Septoria glycines",
        "Pequenas manchas marrons nas folhas, que coalescem em lesões maiores.",
        "**Trifloxistrobina**, **Azoxystrobina**, **Picoxystrobina**.",
        [
            "Tratamento de sementes",
            "Aplicação preventiva de fungicidas",
            "Monitoramento no início do ciclo"
        ]
    )

    bloco_doenca(
        "Crestamento Foliar", "Cercospora kikuchii",
        "Manchas avermelhadas nas folhas e vagens, podendo afetar sementes.",
        "**Mancozebe**, **Tebuconazol**, **Fluxapiroxade**.",
        [
            "Uso de sementes tratadas",
            "Rotação de culturas",
            "Pulverizações entre R1 e R3"
        ]
    )

    bloco_doenca(
        "Ferrugem Asiática", "Phakopsora pachyrhizi",
        "Manchas marrons e ferruginosas com esporulação abundante. Altamente severa.",
        "**Triazóis (Tebuconazol)**, **Estrobilurinas (Azoxystrobina)**, **Carboxamidas (Fluxapiroxade)**.",
        [
            "Aplicações preventivas baseadas em alertas",
            "Cultivares precoces",
            "Eliminar sojas voluntárias no vazio sanitário"
        ]
    )

    bloco_doenca(
        "Powdery Mildew (Oídio)", "Microsphaera diffusa",
        "Pó branco nas folhas, reduzindo a fotossíntese e produtividade.",
        "**Enxofre**, **Protioconazol**, **Azoxystrobina**.",
        [
            "Aplicações preventivas em clima seco",
            "Evitar superpopulação de plantas"
        ]
    )

    bloco_doenca(
        "Septoria", "Septoria sojae",
        "Lesões circulares e escurecidas nas folhas, similares ao brown spot.",
        "**Clorotalonil**, **Mancozebe**, **Trifloxistrobina**.",
        [
            "Monitoramento na fase vegetativa",
            "Controle químico preventivo",
            "Rotação de culturas"
        ]
    )
