import plotly.graph_objects as go

def nrz_encoding(binary_message):
    signal = []
    for bit in binary_message:
        if bit == '0':
            signal.extend([-1, -1])  # Codifica '0' como sinal negativo
        elif bit == '1':
            signal.extend([1, 1])  # Codifica '1' como sinal positivo

    return signal

# Exemplo de uso
binary_message = "010110101"
encoded_signal = nrz_encoding(binary_message)

print("Mensagem em binário:", binary_message)
print("Sinal codificado NRZ:", encoded_signal)

# Criação do gráfico utilizando Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=list(range(len(encoded_signal))), y=encoded_signal, mode='lines'))

fig.update_layout(
    title="Codificação NRZ",
    xaxis_title="Tempo",
    yaxis_title="Nível de Sinal"
)

fig.show()
