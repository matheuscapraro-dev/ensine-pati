import streamlit as st
import random

st.set_page_config(page_title="Trabalho 02 - Álgebra e Algoritmos", page_icon="📚", layout="wide")

# ---- CSS customizado ----
st.markdown("""
<style>
    .stApp { }
    .exercise-title { font-size: 1.8rem; font-weight: bold; color: #1f77b4; }
    .step-box {
        background-color: #f0f2f6;
        border-left: 4px solid #1f77b4;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    .result-box {
        background-color: #d4edda;
        border: 1px solid #28a745;
        padding: 1rem;
        border-radius: 8px;
        font-size: 1.1rem;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #dc3545;
        padding: 1rem;
        border-radius: 8px;
    }
    .highlight { color: #e83e8c; font-weight: bold; }
</style>
""", unsafe_allow_html=True)


def render_code_tutorial(steps: list[dict]):
    """Renderiza um tutorial interativo passo a passo.
    Cada step é um dict com 'titulo', 'explicacao', 'codigo'."""
    st.markdown("---")
    st.subheader("🎓 Aprenda a programar este exercício")
    st.info("Clique em cada passo para ver a explicação e o código. Tente entender antes de expandir!")

    for i, step in enumerate(steps, 1):
        with st.expander(f"Passo {i}: {step['titulo']}", expanded=False):
            st.markdown(step["explicacao"])
            st.code(step["codigo"], language="python")

    st.markdown("---")
    st.subheader("📋 Código completo")
    full_code = "\n".join(step["codigo"] for step in steps)
    st.code(full_code, language="python")

    st.subheader("🧪 Teste seus conhecimentos")


# ============================
# EXERCÍCIO 1 - Calculadora
# ============================
def exercicio1():
    st.header("🔢 Exercício 1: Calculadora de Operações Simples")
    st.write("Uma calculadora que realiza as 4 operações básicas entre dois números.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        num1 = st.number_input("Primeiro número:", value=0.0, key="calc_n1")
        num2 = st.number_input("Segundo número:", value=0.0, key="calc_n2")
        operacao = st.selectbox("Operação:", ["+", "-", "*", "/"])

        if st.button("Calcular", key="btn_calc"):
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    st.error("Erro: não é possível dividir por zero.")
                    return
                resultado = num1 / num2

            st.success(f"Resultado: {num1} {operacao} {num2} = {resultado}")

    with col2:
        render_code_tutorial([
            {
                "titulo": "Receber os números do usuário",
                "explicacao": """
Primeiro, pedimos ao usuário que digite dois números. Usamos `float()` para converter
a entrada (que é texto) em número decimal, permitindo cálculos com casas decimais.

O bloco `try/except` protege contra entradas inválidas (ex: letras ao invés de números).
                """,
                "codigo": "try:\n    num1 = float(input(\"Digite o primeiro número: \"))\n    num2 = float(input(\"Digite o segundo número: \"))"
            },
            {
                "titulo": "Receber a operação desejada",
                "explicacao": """
Pedimos ao usuário qual operação ele deseja realizar. A entrada é uma string simples
que será comparada com os operadores válidos (`+`, `-`, `*`, `/`).
                """,
                "codigo": "    operacao = input(\"Digite a operação (+, -, *, /): \")"
            },
            {
                "titulo": "Usar if/elif para escolher a operação",
                "explicacao": """
Usamos uma cadeia de `if/elif/else` para verificar qual operação o usuário escolheu.
Para cada operador, calculamos o resultado correspondente.

**Atenção especial** na divisão: verificamos se o divisor é zero antes de dividir,
pois divisão por zero causa erro matemático.
                """,
                "codigo": "    if operacao == \"+\":\n        resultado = num1 + num2\n    elif operacao == \"-\":\n        resultado = num1 - num2\n    elif operacao == \"*\":\n        resultado = num1 * num2\n    elif operacao == \"/\":\n        if num2 == 0:\n            print(\"Erro: não é possível dividir por zero.\")\n            return\n        resultado = num1 / num2\n    else:\n        print(\"Operação inválida.\")\n        return"
            },
            {
                "titulo": "Exibir o resultado",
                "explicacao": """
Usamos uma f-string para formatar a saída de forma legível.
O `except ValueError` captura erros quando o usuário digita algo que não é número.
                """,
                "codigo": "    print(f\"Resultado: {num1} {operacao} {num2} = {resultado}\")\nexcept ValueError:\n    print(\"Entrada inválida. Digite números válidos.\")"
            },
        ])

        quiz_calc = st.radio(
            "O que acontece se tentarmos dividir por zero?",
            ["O programa retorna 0", "O programa mostra um erro e para", "O Python calcula infinito"],
            key="quiz1", index=None
        )
        if quiz_calc == "O programa mostra um erro e para":
            st.success("✅ Correto! Verificamos se num2 == 0 antes de dividir.")
        elif quiz_calc is not None:
            st.error("❌ Tente novamente! Pense no `if num2 == 0` dentro do código.")


# ============================
# EXERCÍCIO 2 - Adivinhação
# ============================
def exercicio2():
    st.header("🎲 Exercício 2: Jogo de Adivinhação")
    st.write("Adivinhe o número secreto entre 1 e 50. Você tem 5 tentativas!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")

        if "numero_secreto" not in st.session_state:
            st.session_state.numero_secreto = random.randint(1, 50)
            st.session_state.tentativas = []
            st.session_state.jogo_acabou = False

        if not st.session_state.jogo_acabou:
            palpite = st.number_input("Seu palpite (1-50):", min_value=1, max_value=50, value=25, step=1, key="palpite")
            if st.button("Tentar", key="btn_adv"):
                st.session_state.tentativas.append(palpite)
                if palpite == st.session_state.numero_secreto:
                    st.session_state.jogo_acabou = True
                elif len(st.session_state.tentativas) >= 5:
                    st.session_state.jogo_acabou = True

        for i, t in enumerate(st.session_state.tentativas, 1):
            if t == st.session_state.numero_secreto:
                st.success(f"Tentativa {i}: {t} - 🎉 Acertou!")
            elif t < st.session_state.numero_secreto:
                st.warning(f"Tentativa {i}: {t} - ⬆️ Número é maior")
            else:
                st.warning(f"Tentativa {i}: {t} - ⬇️ Número é menor")

        if st.session_state.jogo_acabou:
            if st.session_state.tentativas and st.session_state.tentativas[-1] == st.session_state.numero_secreto:
                st.balloons()
                st.success(f"Parabéns! Você acertou em {len(st.session_state.tentativas)} tentativas!")
            else:
                st.error(f"Suas tentativas acabaram! O número era {st.session_state.numero_secreto}.")

        if st.button("🔄 Novo Jogo", key="btn_novo"):
            st.session_state.numero_secreto = random.randint(1, 50)
            st.session_state.tentativas = []
            st.session_state.jogo_acabou = False
            st.rerun()

    with col2:
        render_code_tutorial([
            {
                "titulo": "Gerar número aleatório",
                "explicacao": """
Usamos `random.randint(1, 50)` para gerar um número inteiro aleatório entre 1 e 50.
A biblioteca `random` precisa ser importada no início do programa.
                """,
                "codigo": "import random\n\nnumero_secreto = random.randint(1, 50)\nprint(\"Tentei um número entre 1 e 50. Você tem 5 tentativas!\")"
            },
            {
                "titulo": "Loop de tentativas com for",
                "explicacao": """
Usamos `for tentativa in range(1, 6)` para dar exatamente 5 tentativas ao jogador.
O `range(1, 6)` gera os números 1, 2, 3, 4, 5.

O `try/except` protege contra entradas não numéricas e o `continue` pula para a próxima tentativa.
                """,
                "codigo": "for tentativa in range(1, 6):\n    try:\n        palpite = int(input(f\"Tentativa {tentativa}/5 - Seu palpite: \"))\n    except ValueError:\n        print(\"Entrada inválida. Você perdeu esta tentativa.\")\n        continue"
            },
            {
                "titulo": "Comparar palpite com número secreto",
                "explicacao": """
Comparamos o palpite com o número secreto:
- Se **igual**: o jogador acertou! Usamos `return` para sair da função.
- Se **menor**: damos a dica de que precisa chutar mais alto.
- Se **maior**: damos a dica de que precisa chutar mais baixo.
                """,
                "codigo": "    if palpite == numero_secreto:\n        print(f\"Parabéns! Você acertou: {numero_secreto}!\")\n        return\n    elif palpite < numero_secreto:\n        print(\"Seu palpite está abaixo.\")\n    else:\n        print(\"Seu palpite está acima.\")"
            },
            {
                "titulo": "Mensagem de derrota ao final",
                "explicacao": """
Se o loop terminar sem que o jogador acerte (ou seja, todas as 5 tentativas foram usadas),
mostramos o número secreto. Essa linha é executada apenas se o `return` do acerto não foi acionado.
                """,
                "codigo": "print(f\"Suas tentativas acabaram! O número era {numero_secreto}.\")"
            },
        ])

        quiz_adv = st.radio(
            "Para que serve o `continue` dentro do `except`?",
            ["Encerra o programa", "Pula para a próxima iteração do loop", "Repete a mesma tentativa"],
            key="quiz2", index=None
        )
        if quiz_adv == "Pula para a próxima iteração do loop":
            st.success("✅ Correto! O `continue` pula para a próxima repetição do `for`.")
        elif quiz_adv is not None:
            st.error("❌ Tente novamente! O `continue` faz o loop ir para a próxima iteração.")


# ============================
# EXERCÍCIO 3 - Pares/Ímpares
# ============================
def exercicio3():
    st.header("🔄 Exercício 3: Contador de Números Pares e Ímpares")
    st.write("Digite 10 números e descubra quantos são pares e quantos são ímpares.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        numeros = []
        cols = st.columns(5)
        for i in range(10):
            with cols[i % 5]:
                n = st.number_input(f"{i+1}º", value=0, step=1, key=f"par_{i}")
                numeros.append(n)

        if st.button("Contar", key="btn_par"):
            pares = sum(1 for n in numeros if n % 2 == 0)
            impares = 10 - pares
            col_r1, col_r2 = st.columns(2)
            with col_r1:
                st.metric("Pares", pares)
            with col_r2:
                st.metric("Ímpares", impares)

    with col2:
        render_code_tutorial([
            {
                "titulo": "Inicializar contadores",
                "explicacao": """
Criamos duas variáveis para contar: `pares` e `impares`, ambas começando em 0.
Isso é um padrão muito comum: inicializamos contadores antes do loop.
                """,
                "codigo": "pares = 0\nimpares = 0"
            },
            {
                "titulo": "Loop para ler 10 números",
                "explicacao": """
Usamos `for i in range(1, 11)` para repetir 10 vezes.
A cada iteração, pedimos um número ao usuário. O `try/except` trata entradas inválidas.
                """,
                "codigo": "for i in range(1, 11):\n    try:\n        numero = int(input(f\"Digite o {i}º número: \"))\n    except ValueError:\n        print(\"Entrada inválida. Considerando como zero.\")\n        numero = 0"
            },
            {
                "titulo": "Verificar par ou ímpar com o operador %",
                "explicacao": """
O operador `%` (módulo) retorna o **resto da divisão**.
- Se `numero % 2 == 0`, o número é **par** (divisível por 2 sem resto).
- Caso contrário, é **ímpar**.

Incrementamos o contador correspondente com `+= 1`.
                """,
                "codigo": "    if numero % 2 == 0:\n        pares += 1\n    else:\n        impares += 1"
            },
            {
                "titulo": "Exibir resultado final",
                "explicacao": """
Após o loop, exibimos os totais. As f-strings formatam a saída de forma legível.
                """,
                "codigo": "print(f\"\\nQuantidade de números pares: {pares}\")\nprint(f\"Quantidade de números ímpares: {impares}\")"
            },
        ])

        quiz_par = st.radio(
            "Qual o resultado de `7 % 2`?",
            ["0", "1", "3.5", "2"],
            key="quiz3", index=None
        )
        if quiz_par == "1":
            st.success("✅ Correto! 7 dividido por 2 dá 3 com resto 1.")
        elif quiz_par is not None:
            st.error("❌ Lembre-se: `%` retorna o resto da divisão inteira.")


# ============================
# EXERCÍCIO 4 - Média de Notas
# ============================
def exercicio4():
    st.header("📊 Exercício 4: Cálculo de Média de Notas com Aprovação")
    st.write("Calcule a média das notas e veja se o aluno foi aprovado (média ≥ 7).")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        qtd = st.slider("Quantidade de notas:", 1, 10, 4, key="qtd_notas")
        notas = []
        cols = st.columns(min(qtd, 5))
        for i in range(qtd):
            with cols[i % min(qtd, 5)]:
                nota = st.number_input(f"Nota {i+1}:", min_value=0.0, max_value=10.0, value=7.0, step=0.5, key=f"nota_{i}")
                notas.append(nota)

        if st.button("Calcular Média", key="btn_media"):
            media = sum(notas) / len(notas)
            st.metric("Média", f"{media:.2f}")
            if media >= 7:
                st.success("✅ Situação: Aprovado!")
            else:
                st.error("❌ Situação: Reprovado.")

    with col2:
        render_code_tutorial([
            {
                "titulo": "Pedir quantidade de notas",
                "explicacao": """
Primeiro perguntamos quantas notas o aluno tem. Usamos `int()` porque a quantidade é um número inteiro.
                """,
                "codigo": "try:\n    quantidade = int(input(\"Digite a quantidade de notas: \"))\nexcept ValueError:\n    print(\"Entrada inválida.\")"
            },
            {
                "titulo": "Somar as notas com um loop",
                "explicacao": """
Usamos uma variável `soma` que acumula o valor de cada nota.
A cada iteração, somamos a nova nota com `soma += nota`.
Esse padrão é chamado de **acumulador**.
                """,
                "codigo": "soma = 0\nfor i in range(1, quantidade + 1):\n    try:\n        nota = float(input(f\"Digite a nota {i}: \"))\n    except ValueError:\n        nota = 0\n    soma += nota"
            },
            {
                "titulo": "Calcular média e verificar aprovação",
                "explicacao": """
A **média** é a soma dividida pela quantidade: `soma / quantidade`.

A verificação de aprovação usa `if media >= 7` — se a média for 7 ou mais, o aluno está aprovado.
O `:.2f` na f-string formata o número com exatamente 2 casas decimais.
                """,
                "codigo": "media = soma / quantidade if quantidade > 0 else 0\nprint(f\"\\nMédia: {media:.2f}\")\nif media >= 7:\n    print(\"Situação: Aprovado!\")\nelse:\n    print(\"Situação: Reprovado.\")"
            },
        ])

        quiz_media = st.radio(
            "O que `:.2f` faz dentro de uma f-string?",
            ["Multiplica por 2", "Formata com 2 casas decimais", "Arredonda para cima", "Converte para inteiro"],
            key="quiz4", index=None
        )
        if quiz_media == "Formata com 2 casas decimais":
            st.success("✅ Correto! `:.2f` exibe o número com 2 casas decimais.")
        elif quiz_media is not None:
            st.error("❌ O `:` dentro de `{}` inicia a formatação. `.2f` = 2 casas decimais float.")


# ============================
# EXERCÍCIO 5 - Desconto
# ============================
def exercicio5():
    st.header("💰 Exercício 5: Calculadora de Desconto")
    st.write("Calcule o valor do desconto e o preço final de um produto.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        preco = st.number_input("Preço do produto (R$):", min_value=0.0, value=100.0, step=0.01, key="preco")
        percentual = st.slider("Percentual de desconto (%):", 0, 100, 10, key="desc_perc")

        desconto = preco * (percentual / 100)
        preco_final = preco - desconto

        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.metric("Desconto", f"R$ {desconto:.2f}")
        with col_r2:
            st.metric("Preço Final", f"R$ {preco_final:.2f}", delta=f"-{percentual}%")

        st.progress(percentual / 100)

    with col2:
        render_code_tutorial([
            {
                "titulo": "Receber preço e percentual",
                "explicacao": """
Pedimos dois valores ao usuário: o preço original e o percentual de desconto.
Ambos são convertidos para `float` pois podem ter casas decimais.
                """,
                "codigo": "try:\n    preco = float(input(\"Digite o preço do produto: \"))\n    percentual = float(input(\"Digite o percentual de desconto: \"))"
            },
            {
                "titulo": "Calcular desconto e preço final",
                "explicacao": """
Para calcular o desconto, multiplicamos o preço pelo percentual dividido por 100.

**Fórmula:** `desconto = preco × (percentual / 100)`

O preço final é o preço original menos o desconto:

**Fórmula:** `preco_final = preco - desconto`
                """,
                "codigo": "    desconto = preco * (percentual / 100)\n    preco_final = preco - desconto"
            },
            {
                "titulo": "Exibir resultados formatados",
                "explicacao": """
Usamos f-strings com `:.2f` para exibir valores monetários com 2 casas decimais.
O `except ValueError` trata o caso de o usuário digitar texto ao invés de número.
                """,
                "codigo": "    print(f\"Valor do desconto: R${desconto:.2f}\")\n    print(f\"Preço final: R${preco_final:.2f}\")\nexcept ValueError:\n    print(\"Entrada inválida. Digite valores numéricos.\")"
            },
        ])

        quiz_desc = st.radio(
            "Se um produto custa R$200 e o desconto é de 15%, qual o preço final?",
            ["R$ 185,00", "R$ 170,00", "R$ 30,00", "R$ 150,00"],
            key="quiz5", index=None
        )
        if quiz_desc == "R$ 170,00":
            st.success("✅ Correto! 200 × 0.15 = 30 de desconto. 200 - 30 = 170.")
        elif quiz_desc is not None:
            st.error("❌ Calcule: 200 × (15/100) = 30. Depois: 200 - 30 = ?")


# ============================
# EXERCÍCIO 6 - Conversor
# ============================
def exercicio6():
    st.header("📏 Exercício 6: Conversor de Unidades Simples")
    st.write("Converta entre metros/centímetros e quilômetros/metros.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        opcao = st.radio("Tipo de conversão:", ["Metros → Centímetros", "Quilômetros → Metros"], key="conv_tipo")

        if opcao == "Metros → Centímetros":
            valor = st.number_input("Valor em metros:", min_value=0.0, value=1.0, step=0.1, key="conv_m")
            resultado = valor * 100
            st.success(f"{valor} metros = **{resultado}** centímetros")
        else:
            valor = st.number_input("Valor em quilômetros:", min_value=0.0, value=1.0, step=0.1, key="conv_km")
            resultado = valor * 1000
            st.success(f"{valor} quilômetros = **{resultado}** metros")

    with col2:
        render_code_tutorial([
            {
                "titulo": "Mostrar opções ao usuário",
                "explicacao": """
Apresentamos um menu com as opções de conversão e lemos a escolha do usuário.
Usamos `print()` para exibir as opções e `input()` para capturar a resposta.
                """,
                "codigo": "print(\"1 - Converter metros para centímetros\")\nprint(\"2 - Converter quilômetros para metros\")\nopcao = input(\"Escolha uma opção (1 ou 2): \")"
            },
            {
                "titulo": "Converter metros para centímetros",
                "explicacao": """
Se o usuário escolher a opção 1, pedimos o valor em metros e multiplicamos por **100**
(pois 1 metro = 100 centímetros).
                """,
                "codigo": "if opcao == \"1\":\n    valor = float(input(\"Digite o valor em metros: \"))\n    resultado = valor * 100\n    print(f\"{valor} metros = {resultado} centímetros\")"
            },
            {
                "titulo": "Converter quilômetros para metros",
                "explicacao": """
Se o usuário escolher a opção 2, pedimos o valor em quilômetros e multiplicamos por **1000**
(pois 1 quilômetro = 1000 metros).

O `else` final trata entradas inválidas — se o usuário não digitar 1 nem 2.
                """,
                "codigo": "elif opcao == \"2\":\n    valor = float(input(\"Digite o valor em quilômetros: \"))\n    resultado = valor * 1000\n    print(f\"{valor} quilômetros = {resultado} metros\")\nelse:\n    print(\"Opção inválida. Escolha 1 ou 2.\")"
            },
        ])

        quiz_conv = st.radio(
            "Quantos centímetros tem 2.5 metros?",
            ["25", "250", "2500", "0.025"],
            key="quiz6", index=None
        )
        if quiz_conv == "250":
            st.success("✅ Correto! 2.5 × 100 = 250 centímetros.")
        elif quiz_conv is not None:
            st.error("❌ Lembre-se: 1 metro = 100 centímetros.")


# ============================
# EXERCÍCIO 7 - Verificador de Sinal
# ============================
def exercicio7():
    st.header("➕➖ Exercício 7: Verificador de Sinal com Contador")
    st.write("Digite números e descubra quantos são positivos, negativos e zeros.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        numeros_texto = st.text_area(
            "Digite números separados por vírgula:",
            value="5, -3, 0, 12, -7, 0, 8",
            key="sinal_input"
        )

        if st.button("Analisar", key="btn_sinal"):
            try:
                numeros = [float(n.strip()) for n in numeros_texto.split(",") if n.strip()]
                positivos = sum(1 for n in numeros if n > 0)
                negativos = sum(1 for n in numeros if n < 0)
                zeros = sum(1 for n in numeros if n == 0)

                col_r1, col_r2, col_r3 = st.columns(3)
                with col_r1:
                    st.metric("➕ Positivos", positivos)
                with col_r2:
                    st.metric("➖ Negativos", negativos)
                with col_r3:
                    st.metric("0️⃣ Zeros", zeros)
            except ValueError:
                st.error("Entrada inválida. Use números separados por vírgula.")

    with col2:
        render_code_tutorial([
            {
                "titulo": "Inicializar contadores e loop while",
                "explicacao": """
Usamos um loop `while True` (loop infinito) que só para quando o usuário digita "sair".
Os contadores `positivos`, `negativos` e `zeros` começam em 0.

O `while True` é útil quando não sabemos quantas repetições teremos.
                """,
                "codigo": "positivos = 0\nnegativos = 0\nzeros = 0\n\nwhile True:\n    entrada = input(\"Digite um número (ou 'sair'): \")\n    if entrada.lower() == \"sair\":\n        break"
            },
            {
                "titulo": "Converter e classificar o número",
                "explicacao": """
Convertemos a entrada para `float` e classificamos:
- **Positivo** se `> 0`
- **Negativo** se `< 0`
- **Zero** se nenhum dos anteriores

O `try/except` protege contra entradas inválidas. O `continue` pula para a próxima iteração.
                """,
                "codigo": "    try:\n        numero = float(entrada)\n    except ValueError:\n        print(\"Entrada inválida.\")\n        continue\n\n    if numero > 0:\n        positivos += 1\n    elif numero < 0:\n        negativos += 1\n    else:\n        zeros += 1"
            },
            {
                "titulo": "Exibir totais ao final",
                "explicacao": """
Quando o loop termina (o usuário digitou "sair"), exibimos os totais.
Estas linhas estão **fora** do `while`, então só executam após o `break`.
                """,
                "codigo": "print(f\"\\nPositivos: {positivos}\")\nprint(f\"Negativos: {negativos}\")\nprint(f\"Zeros: {zeros}\")"
            },
        ])

        quiz_sinal = st.radio(
            "O que a instrução `break` faz no Python?",
            ["Pausa o programa por 1 segundo", "Sai do loop atual", "Encerra o programa inteiro", "Pula para a próxima iteração"],
            key="quiz7", index=None
        )
        if quiz_sinal == "Sai do loop atual":
            st.success("✅ Correto! `break` interrompe o loop mais interno.")
        elif quiz_sinal is not None:
            st.error("❌ `break` sai do loop. `continue` pula iteração. `exit()` encerra o programa.")


# ============================
# EXERCÍCIO 8 - Área/Perímetro
# ============================
def exercicio8():
    st.header("📐 Exercício 8: Área e Perímetro de um Retângulo")
    st.write("Calcule a área e o perímetro de um retângulo a partir de suas dimensões.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        largura = st.slider("Largura:", 0.5, 20.0, 5.0, 0.5, key="ret_l")
        altura = st.slider("Altura:", 0.5, 20.0, 3.0, 0.5, key="ret_a")

        area = largura * altura
        perimetro = 2 * (largura + altura)

        col_r1, col_r2 = st.columns(2)
        with col_r1:
            st.metric("Área", f"{area:.2f}")
        with col_r2:
            st.metric("Perímetro", f"{perimetro:.2f}")

        # Desenho visual
        st.markdown(f"""
        <div style="
            width: {min(largura * 20, 300)}px;
            height: {min(altura * 20, 200)}px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: bold;
            margin: 1rem auto;
        ">
            {largura} × {altura}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        render_code_tutorial([
            {
                "titulo": "Receber dimensões do retângulo",
                "explicacao": """
Pedimos a largura e altura do retângulo. Usamos `float()` para permitir valores decimais.
                """,
                "codigo": "try:\n    largura = float(input(\"Digite a largura: \"))\n    altura = float(input(\"Digite a altura: \"))"
            },
            {
                "titulo": "Calcular área e perímetro",
                "explicacao": """
As fórmulas do retângulo são:

- **Área** = largura × altura
- **Perímetro** = 2 × (largura + altura)

Os parênteses em `2 * (largura + altura)` são importantes para somar antes de multiplicar!
                """,
                "codigo": "    area = largura * altura\n    perimetro = 2 * (largura + altura)"
            },
            {
                "titulo": "Exibir resultados",
                "explicacao": """
Exibimos os resultados com 2 casas decimais usando `:.2f`.
                """,
                "codigo": "    print(f\"Área: {area:.2f}\")\n    print(f\"Perímetro: {perimetro:.2f}\")\nexcept ValueError:\n    print(\"Entrada inválida.\")"
            },
        ])

        quiz_ret = st.radio(
            "Qual a área de um retângulo 4×6?",
            ["10", "20", "24", "48"],
            key="quiz8", index=None
        )
        if quiz_ret == "24":
            st.success("✅ Correto! Área = 4 × 6 = 24.")
        elif quiz_ret is not None:
            st.error("❌ Área = largura × altura. Tente de novo!")


# ============================
# EXERCÍCIO 9 - Idade
# ============================
def exercicio9():
    st.header("📅 Exercício 9: Conversão de Idade para Dias, Semanas e Meses")
    st.write("Descubra aproximadamente quantos dias, semanas e meses você já viveu!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        idade = st.slider("Sua idade em anos:", 1, 120, 20, key="idade")

        dias = idade * 365
        semanas = idade * 52
        meses = idade * 12

        col_r1, col_r2, col_r3 = st.columns(3)
        with col_r1:
            st.metric("📆 Dias", f"{dias:,}".replace(",", "."))
        with col_r2:
            st.metric("📅 Semanas", f"{semanas:,}".replace(",", "."))
        with col_r3:
            st.metric("🗓️ Meses", f"{meses:,}".replace(",", "."))

    with col2:
        render_code_tutorial([
            {
                "titulo": "Receber a idade do usuário",
                "explicacao": """
Pedimos a idade em anos. Usamos `int()` pois idade é geralmente um número inteiro.
                """,
                "codigo": "try:\n    idade = int(input(\"Digite sua idade em anos: \"))"
            },
            {
                "titulo": "Converter usando multiplicação",
                "explicacao": """
As conversões são aproximadas:
- **1 ano ≈ 365 dias**
- **1 ano ≈ 52 semanas**
- **1 ano = 12 meses**

Basta multiplicar a idade por cada fator!
                """,
                "codigo": "    dias = idade * 365\n    semanas = idade * 52\n    meses = idade * 12"
            },
            {
                "titulo": "Exibir os resultados",
                "explicacao": """
Usamos f-strings para montar a mensagem de saída. É interessante alinhar visualmente
com espaços para ficar mais organizado.
                """,
                "codigo": "    print(\"Você já viveu aproximadamente:\")\n    print(f\"  {dias} dias\")\n    print(f\"  {semanas} semanas\")\n    print(f\"  {meses} meses\")\nexcept ValueError:\n    print(\"Entrada inválida.\")"
            },
        ])

        quiz_idade = st.radio(
            "Quantos meses tem uma pessoa de 25 anos?",
            ["250", "300", "1300", "600"],
            key="quiz9", index=None
        )
        if quiz_idade == "300":
            st.success("✅ Correto! 25 × 12 = 300 meses.")
        elif quiz_idade is not None:
            st.error("❌ Lembre-se: 1 ano = 12 meses. Multiplique!")


# ============================
# EXERCÍCIO 10 - Conta Bancária
# ============================
def exercicio10():
    st.header("🏦 Exercício 10: Simulador de Conta Bancária Simples")
    st.write("Simule operações de depósito e saque em uma conta bancária.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("⚡ Experimente")
        saldo_inicial = st.number_input("Saldo inicial (R$):", min_value=0.0, value=1000.0, step=10.0, key="banco_s")
        deposito = st.number_input("Valor do depósito (R$):", min_value=0.0, value=500.0, step=10.0, key="banco_d")
        saque = st.number_input("Valor do saque (R$):", min_value=0.0, value=200.0, step=10.0, key="banco_sq")

        if st.button("Simular", key="btn_banco"):
            saldo = saldo_inicial + deposito

            st.write(f"Saldo após depósito: **R$ {saldo:.2f}**")

            if saque > saldo:
                st.error(f"Saldo insuficiente para o saque de R$ {saque:.2f}!")
                st.warning(f"Saldo atual: R$ {saldo:.2f}")
            else:
                saldo -= saque
                st.success(f"Saldo final: **R$ {saldo:.2f}**")

            # Barra visual
            max_val = saldo_inicial + deposito
            if max_val > 0:
                st.progress(min(saldo / max_val, 1.0))

    with col2:
        render_code_tutorial([
            {
                "titulo": "Receber saldo, depósito e saque",
                "explicacao": """
Pedimos 3 valores: saldo inicial, valor a depositar e valor a sacar.
Todos são `float` para permitir centavos (R$ 10.50, por exemplo).
                """,
                "codigo": "try:\n    saldo = float(input(\"Digite o saldo inicial: \"))\n    deposito = float(input(\"Digite o valor do depósito: \"))\n    saque = float(input(\"Digite o valor do saque: \"))"
            },
            {
                "titulo": "Realizar o depósito",
                "explicacao": """
O depósito é simples: somamos o valor ao saldo com `+=` (operador de atribuição com adição).

`saldo += deposito` é o mesmo que `saldo = saldo + deposito`.
                """,
                "codigo": "    saldo += deposito"
            },
            {
                "titulo": "Verificar saldo antes do saque",
                "explicacao": """
Antes de sacar, verificamos se o saldo é suficiente.
Se o saque for maior que o saldo, mostramos um erro.
Caso contrário, subtraímos o valor do saldo.

Isso é uma **validação** — protege contra estados inválidos (saldo negativo).
                """,
                "codigo": "    if saque > saldo:\n        print(\"Erro: saldo insuficiente.\")\n        print(f\"Saldo atual: R${saldo:.2f}\")\n    else:\n        saldo -= saque\n        print(f\"Saldo final: R${saldo:.2f}\")\nexcept ValueError:\n    print(\"Entrada inválida.\")"
            },
        ])

        quiz_banco = st.radio(
            "Se o saldo é R$100, depósito R$50 e saque R$200, o que acontece?",
            ["Saldo fica -R$50", "Saque é realizado normalmente", "Erro: saldo insuficiente", "Saldo fica R$0"],
            key="quiz10", index=None
        )
        if quiz_banco == "Erro: saldo insuficiente":
            st.success("✅ Correto! Após o depósito, saldo = R$150. Saque de R$200 > R$150.")
        elif quiz_banco is not None:
            st.error("❌ Após o depósito: 100 + 50 = 150. O saque de 200 é maior que 150!")


# ============================
# PÁGINA INICIAL
# ============================
def pagina_inicial():
    st.title("📚 Trabalho 02 — Álgebra e Algoritmos")
    st.markdown("""
    Bem-vindo ao site interativo do **Trabalho 02**!

    Aqui você pode:
    - **Usar** cada exercício de forma interativa
    - **Aprender** como o código funciona passo a passo
    - **Testar** seus conhecimentos com quizzes

    👈 Use o menu lateral para navegar entre os exercícios.
    """)

    st.markdown("---")
    st.subheader("📋 Lista de Exercícios")

    exercicios = [
        ("🔢", "Calculadora de Operações Simples", "if/elif, operadores aritméticos, try/except"),
        ("🎲", "Jogo de Adivinhação", "random, for, if/elif, continue"),
        ("🔄", "Contador de Pares e Ímpares", "for, operador %, contadores"),
        ("📊", "Média de Notas com Aprovação", "for, acumulador, formatação :.2f"),
        ("💰", "Calculadora de Desconto", "fórmula de porcentagem, f-string"),
        ("📏", "Conversor de Unidades", "if/elif, multiplicação, menu"),
        ("➕", "Verificador de Sinal", "while True, break, continue"),
        ("📐", "Área e Perímetro", "fórmulas geométricas, float"),
        ("📅", "Conversão de Idade", "multiplicação, int"),
        ("🏦", "Conta Bancária Simples", "operadores +=/-=, validação"),
    ]

    for i, (icon, titulo, conceitos) in enumerate(exercicios, 1):
        with st.container():
            col_icon, col_info = st.columns([1, 11])
            with col_icon:
                st.markdown(f"### {icon}")
            with col_info:
                st.markdown(f"**Exercício {i}: {titulo}**")
                st.caption(f"Conceitos: {conceitos}")


# ============================
# NAVEGAÇÃO
# ============================
PAGINAS = {
    "🏠 Início": pagina_inicial,
    "1 - Calculadora": exercicio1,
    "2 - Adivinhação": exercicio2,
    "3 - Pares/Ímpares": exercicio3,
    "4 - Média de Notas": exercicio4,
    "5 - Desconto": exercicio5,
    "6 - Conversor": exercicio6,
    "7 - Verificador de Sinal": exercicio7,
    "8 - Área/Perímetro": exercicio8,
    "9 - Conversão de Idade": exercicio9,
    "10 - Conta Bancária": exercicio10,
}

st.sidebar.title("📚 Navegação")
pagina = st.sidebar.radio("Escolha um exercício:", list(PAGINAS.keys()))

PAGINAS[pagina]()

st.sidebar.markdown("---")
st.sidebar.caption("Trabalho 02 — Álgebra e Algoritmos")
