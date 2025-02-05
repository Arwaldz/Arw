import streamlit as st
import pyperclip

# Function to divide the value based on the percentage
def divide_value(value, percentage):
    part1 = value * (percentage / 100)
    part2 = value - part1
    return part1, part2

# Streamlit app
def main():
    st.title("Dividir Valor em Partes")

    # Input fields
    value = st.number_input("Valor em Reais (R$)", min_value=0.0, format="%.2f")
    percentage = st.number_input("Porcentagem (%)", min_value=0.0, max_value=100.0, format="%.2f")

    # Calculate the divided values
    if value > 0 and percentage > 0:
        part1, part2 = divide_value(value, percentage)
        st.write(f"Parte 1 ({percentage}%): R$ {part1:.2f}")
        st.write(f"Parte 2 ({(100 - percentage)}%): R$ {part2:.2f}")

        # Copy buttons
        if st.button("Copiar Parte 1"):
            pyperclip.copy(f"{part1:.2f}")
            st.success("Parte 1 copiada para a área de transferência!")
        if st.button("Copiar Parte 2"):
            pyperclip.copy(f"{part2:.2f}")
            st.success("Parte 2 copiada para a área de transferência!")

    # Footer message
    st.markdown(
        """
        <div style="text-align: right; margin-top: 50px;">
            Por Everson Cardoso Ferreira - SJRJ RJ18745 01VF
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
