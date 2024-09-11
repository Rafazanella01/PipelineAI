from datetime import datetime, time
import streamlit as st
from contrato import Vendas, ProdutoEnum
from pydantic import ValidationError

def main():
    
    st.title("Sistema de CRM e Vendas")
    email = st.text_input("Email do Vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0))  # Valor padrão: 09:00
    valorVenda = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidadeProdutos = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produtoVendido = st.selectbox("Produto", options=[e.value for e in ProdutoEnum])
    
    if st.button("Salvar"):  
        try:
            dataHora = datetime.combine(data, hora)
            venda = Vendas(
                email=email,
                data=dataHora,
                valorVenda=valorVenda,
                quantidadeProdutos=quantidadeProdutos,
                produtoVendido=produtoVendido
                          )
            st.write(venda)
        except ValidationError as e:
            st.error(f"Erro! {e}")
        
if __name__ == "__main__":
    main()