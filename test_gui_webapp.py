import streamlit as st
st.title("Application To do")
st.subheader("pour l'apprentissage")
st.write("tsara ho fantatra")

checkbox = st.checkbox("mpivarotra", key="check")
if checkbox:
    st.write("Vous avez coché le checkbox 'mpivarotra'.")
st.text_input(label="Asiana valeur ity", placeholder="Firy ny valeur ho apetraka eto...",key="texte")

st.session_state