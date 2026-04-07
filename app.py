import streamlit as st
import random

st.set_page_config(page_title="Trabalho 02 - Álgebra e Algoritmos", page_icon="📚", layout="centered")

# ---- CSS responsivo ----
st.markdown("""
<style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 100%;
    }
    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.5rem;
            padding-right: 0.5rem;
        }
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.3rem !important; }
        h3 { font-size: 1.1rem !important; }
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 0.5rem 0.8rem;
            font-size: 0.9rem;
        }
    }
</style>
""", unsafe_allow_html=True)


def render_code_tutorial(steps, quiz_key, quiz_question, quiz_options, quiz_answer, quiz_correct_msg, quiz_wrong_msg):
    st.subheader("🎓 Aprenda a programar este exercício")
    st.info("Clique em cada passo para ver a explicação e o código.")

    for i, step in enumerate(steps, 1):
        with st.expander(f"Passo {i}: {step['titulo']}", expanded=False):
            st.markdown(step["explicacao"])
            st.code(step["codigo"], language="python")

    st.markdown("---")
    with st.expander("📋 Ver código completo", expanded=False):
        full_code = "\n".join(step["codigo"] for step in steps)
        st.code(full_code, language="python")

    st.markdown("---")
    st.subheader("🧪 Teste seus conhecimentos")
    resposta = st.radio(quiz_question, quiz_options, key=quiz_key, index=None)
    if resposta == quiz_answer:
        st.success(quiz_correct_msg)
    elif resposta is not None:
        st.error(quiz_wrong_msg)


def exercicio1():
    st.header("🔢 Exercício 1: Calculadora de Operações Simples")
    st.write("Uma calculadora que realiza as 4 operações básicas entre dois números.")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        num1 = st.number_input("Primeiro número:", value=0.0, key="calc_n1")
        num2 = st.number_input("Segundo número:", value=0.0, key="calc_n2")
        operacao = st.selectbox("Operação:", ["+", "-", "*", "/"])
        if st.button("Calcular", key="btn_calc", use_container_width=True):
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
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Receber os números do usuário", "explicacao": "Pedimos dois números usando `float()` para converter texto em decimal. O `try/except` protege contra entradas inválidas.", "codigo": 'try:\n    num1 = float(input("Digite o primeiro número: "))\n    num2 = float(input("Digite o segundo número: "))'},
                {"titulo": "Receber a operação desejada", "explicacao": "Pedimos qual operação realizar. A entrada é comparada com `+`, `-`, `*`, `/`.", "codigo": '    operacao = input("Digite a operação (+, -, *, /): ")'},
                {"titulo": "Usar if/elif para escolher a operação", "explicacao": "Usamos `if/elif/else` para cada operação. **Atenção:** verificamos divisão por zero antes de dividir.", "codigo": '    if operacao == "+":\n        resultado = num1 + num2\n    elif operacao == "-":\n        resultado = num1 - num2\n    elif operacao == "*":\n        resultado = num1 * num2\n    elif operacao == "/":\n        if num2 == 0:\n            print("Erro: divisão por zero.")\n            return\n        resultado = num1 / num2\n    else:\n        print("Operação inválida.")\n        return'},
                {"titulo": "Exibir o resultado", "explicacao": "Usamos f-string para formatar a saída. O `except ValueError` captura entradas não numéricas.", "codigo": '    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")\nexcept ValueError:\n    print("Entrada inválida.")'},
            ],
            quiz_key="quiz1",
            quiz_question="O que acontece se tentarmos dividir por zero?",
            quiz_options=["O programa retorna 0", "O programa mostra um erro e para", "O Python calcula infinito"],
            quiz_answer="O programa mostra um erro e para",
            quiz_correct_msg="✅ Correto! Verificamos se num2 == 0 antes de dividir.",
            quiz_wrong_msg="❌ Tente novamente! Pense no `if num2 == 0` dentro do código.",
        )


def exercicio2():
    st.header("🎲 Exercício 2: Jogo de Adivinhação")
    st.write("Adivinhe o número secreto entre 1 e 50. Você tem 5 tentativas!")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        if "numero_secreto" not in st.session_state:
            st.session_state.numero_secreto = random.randint(1, 50)
            st.session_state.tentativas = []
            st.session_state.jogo_acabou = False
        if not st.session_state.jogo_acabou:
            palpite = st.number_input("Seu palpite (1-50):", min_value=1, max_value=50, value=25, step=1, key="palpite")
            if st.button("Tentar", key="btn_adv", use_container_width=True):
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
                st.success(f"Parabéns! Acertou em {len(st.session_state.tentativas)} tentativas!")
            else:
                st.error(f"Tentativas acabaram! O número era {st.session_state.numero_secreto}.")
        if st.button("🔄 Novo Jogo", key="btn_novo", use_container_width=True):
            st.session_state.numero_secreto = random.randint(1, 50)
            st.session_state.tentativas = []
            st.session_state.jogo_acabou = False
            st.rerun()
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Gerar número aleatório", "explicacao": "`random.randint(1, 50)` gera um inteiro aleatório entre 1 e 50.", "codigo": 'import random\n\nnumero_secreto = random.randint(1, 50)\nprint("Tentei um número entre 1 e 50. Você tem 5 tentativas!")'},
                {"titulo": "Loop de tentativas com for", "explicacao": "`for tentativa in range(1, 6)` dá 5 tentativas. O `continue` pula entradas inválidas.", "codigo": 'for tentativa in range(1, 6):\n    try:\n        palpite = int(input(f"Tentativa {tentativa}/5 - Seu palpite: "))\n    except ValueError:\n        print("Entrada inválida.")\n        continue'},
                {"titulo": "Comparar palpite com número secreto", "explicacao": "Se **igual**: acertou! Se **menor**: dica para cima. Se **maior**: dica para baixo.", "codigo": '    if palpite == numero_secreto:\n        print(f"Parabéns! Acertou: {numero_secreto}!")\n        return\n    elif palpite < numero_secreto:\n        print("Seu palpite está abaixo.")\n    else:\n        print("Seu palpite está acima.")'},
                {"titulo": "Mensagem de derrota ao final", "explicacao": "Se o loop terminar sem acerto, mostramos o número secreto.", "codigo": 'print(f"Suas tentativas acabaram! O número era {numero_secreto}.")'},
            ],
            quiz_key="quiz2",
            quiz_question="Para que serve o `continue` dentro do `except`?",
            quiz_options=["Encerra o programa", "Pula para a próxima iteração do loop", "Repete a mesma tentativa"],
            quiz_answer="Pula para a próxima iteração do loop",
            quiz_correct_msg="✅ Correto! O `continue` pula para a próxima repetição do `for`.",
            quiz_wrong_msg="❌ O `continue` faz o loop ir para a próxima iteração.",
        )


def exercicio3():
    st.header("🔄 Exercício 3: Contador de Pares e Ímpares")
    st.write("Digite 10 números e descubra quantos são pares e quantos são ímpares.")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        numeros = []
        c1, c2 = st.columns(2)
        for i in range(10):
            with (c1 if i % 2 == 0 else c2):
                n = st.number_input(f"{i+1}º número", value=0, step=1, key=f"par_{i}")
                numeros.append(n)
        if st.button("Contar", key="btn_par", use_container_width=True):
            pares = sum(1 for n in numeros if n % 2 == 0)
            impares = 10 - pares
            r1, r2 = st.columns(2)
            with r1:
                st.metric("Pares", pares)
            with r2:
                st.metric("Ímpares", impares)
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Inicializar contadores", "explicacao": "Criamos `pares` e `impares` começando em 0.", "codigo": "pares = 0\nimpares = 0"},
                {"titulo": "Loop para ler 10 números", "explicacao": "`for i in range(1, 11)` repete 10 vezes.", "codigo": 'for i in range(1, 11):\n    try:\n        numero = int(input(f"Digite o {i}º número: "))\n    except ValueError:\n        numero = 0'},
                {"titulo": "Verificar par ou ímpar com %", "explicacao": "`%` retorna o resto. Se `numero % 2 == 0`, é **par**.", "codigo": "    if numero % 2 == 0:\n        pares += 1\n    else:\n        impares += 1"},
                {"titulo": "Exibir resultado final", "explicacao": "Após o loop, exibimos os totais.", "codigo": 'print(f"Pares: {pares}")\nprint(f"Ímpares: {impares}")'},
            ],
            quiz_key="quiz3",
            quiz_question="Qual o resultado de `7 % 2`?",
            quiz_options=["0", "1", "3.5", "2"],
            quiz_answer="1",
            quiz_correct_msg="✅ Correto! 7 dividido por 2 dá 3 com resto 1.",
            quiz_wrong_msg="❌ `%` retorna o resto da divisão inteira.",
        )


def exercicio4():
    st.header("📊 Exercício 4: Média de Notas com Aprovação")
    st.write("Calcule a média das notas e veja se o aluno foi aprovado (média ≥ 7).")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        qtd = st.slider("Quantidade de notas:", 1, 10, 4, key="qtd_notas")
        notas = []
        c1, c2 = st.columns(2)
        for i in range(qtd):
            with (c1 if i % 2 == 0 else c2):
                nota = st.number_input(f"Nota {i+1}:", min_value=0.0, max_value=10.0, value=7.0, step=0.5, key=f"nota_{i}")
                notas.append(nota)
        if st.button("Calcular Média", key="btn_media", use_container_width=True):
            media = sum(notas) / len(notas)
            st.metric("Média", f"{media:.2f}")
            if media >= 7:
                st.success("✅ Situação: Aprovado!")
            else:
                st.error("❌ Situação: Reprovado.")
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Pedir quantidade de notas", "explicacao": "Usamos `int()` para número inteiro.", "codigo": 'try:\n    quantidade = int(input("Quantidade de notas: "))'},
                {"titulo": "Somar as notas com um loop", "explicacao": "`soma += nota` é o padrão **acumulador**.", "codigo": 'soma = 0\nfor i in range(1, quantidade + 1):\n    try:\n        nota = float(input(f"Nota {i}: "))\n    except ValueError:\n        nota = 0\n    soma += nota'},
                {"titulo": "Calcular média e verificar aprovação", "explicacao": "**Média** = soma / quantidade. Se `>= 7`, aprovado.", "codigo": 'media = soma / quantidade if quantidade > 0 else 0\nprint(f"Média: {media:.2f}")\nif media >= 7:\n    print("Aprovado!")\nelse:\n    print("Reprovado.")'},
            ],
            quiz_key="quiz4",
            quiz_question="O que `:.2f` faz dentro de uma f-string?",
            quiz_options=["Multiplica por 2", "Formata com 2 casas decimais", "Arredonda para cima", "Converte para inteiro"],
            quiz_answer="Formata com 2 casas decimais",
            quiz_correct_msg="✅ Correto! `:.2f` exibe com 2 casas decimais.",
            quiz_wrong_msg="❌ `.2f` = 2 casas decimais float.",
        )


def exercicio5():
    st.header("💰 Exercício 5: Calculadora de Desconto")
    st.write("Calcule o valor do desconto e o preço final de um produto.")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        preco = st.number_input("Preço do produto (R$):", min_value=0.0, value=100.0, step=0.01, key="preco")
        percentual = st.slider("Percentual de desconto (%):", 0, 100, 10, key="desc_perc")
        desconto = preco * (percentual / 100)
        preco_final = preco - desconto
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Desconto", f"R$ {desconto:.2f}")
        with c2:
            st.metric("Preço Final", f"R$ {preco_final:.2f}", delta=f"-{percentual}%")
        st.progress(percentual / 100)
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Receber preço e percentual", "explicacao": "Convertemos para `float` pois podem ter decimais.", "codigo": 'try:\n    preco = float(input("Preço do produto: "))\n    percentual = float(input("Percentual de desconto: "))'},
                {"titulo": "Calcular desconto e preço final", "explicacao": "**Desconto** = preço × (percentual / 100). **Final** = preço - desconto.", "codigo": "    desconto = preco * (percentual / 100)\n    preco_final = preco - desconto"},
                {"titulo": "Exibir resultados", "explicacao": "`:.2f` exibe com 2 casas decimais (padrão monetário).", "codigo": '    print(f"Desconto: R${desconto:.2f}")\n    print(f"Preço final: R${preco_final:.2f}")\nexcept ValueError:\n    print("Entrada inválida.")'},
            ],
            quiz_key="quiz5",
            quiz_question="Produto R$200 com 15% de desconto. Preço final?",
            quiz_options=["R$ 185,00", "R$ 170,00", "R$ 30,00", "R$ 150,00"],
            quiz_answer="R$ 170,00",
            quiz_correct_msg="✅ Correto! 200 × 0.15 = 30. 200 - 30 = 170.",
            quiz_wrong_msg="❌ 200 × (15/100) = 30. 200 - 30 = ?",
        )


def exercicio6():
    st.header("📏 Exercício 6: Conversor de Unidades")
    st.write("Converta entre metros/centímetros e quilômetros/metros.")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        opcao = st.radio("Tipo de conversão:", ["Metros → Centímetros", "Quilômetros → Metros"], key="conv_tipo")
        if opcao == "Metros → Centímetros":
            valor = st.number_input("Valor em metros:", min_value=0.0, value=1.0, step=0.1, key="conv_m")
            st.success(f"{valor} metros = **{valor * 100}** centímetros")
        else:
            valor = st.number_input("Valor em quilômetros:", min_value=0.0, value=1.0, step=0.1, key="conv_km")
            st.success(f"{valor} quilômetros = **{valor * 1000}** metros")
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Mostrar opções ao usuário", "explicacao": "Menu com `print()` e captura com `input()`.", "codigo": 'print("1 - Metros para centímetros")\nprint("2 - Quilômetros para metros")\nopcao = input("Escolha (1 ou 2): ")'},
                {"titulo": "Converter metros → centímetros", "explicacao": "1 metro = **100** centímetros.", "codigo": 'if opcao == "1":\n    valor = float(input("Valor em metros: "))\n    print(f"{valor} m = {valor * 100} cm")'},
                {"titulo": "Converter quilômetros → metros", "explicacao": "1 quilômetro = **1000** metros.", "codigo": 'elif opcao == "2":\n    valor = float(input("Valor em km: "))\n    print(f"{valor} km = {valor * 1000} m")\nelse:\n    print("Opção inválida.")'},
            ],
            quiz_key="quiz6",
            quiz_question="Quantos centímetros tem 2.5 metros?",
            quiz_options=["25", "250", "2500", "0.025"],
            quiz_answer="250",
            quiz_correct_msg="✅ Correto! 2.5 × 100 = 250.",
            quiz_wrong_msg="❌ 1 metro = 100 centímetros.",
        )


def exercicio7():
    st.header("➕➖ Exercício 7: Verificador de Sinal")
    st.write("Digite números e descubra quantos são positivos, negativos e zeros.")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        numeros_texto = st.text_area("Digite números separados por vírgula:", value="5, -3, 0, 12, -7, 0, 8", key="sinal_input")
        if st.button("Analisar", key="btn_sinal", use_container_width=True):
            try:
                numeros = [float(n.strip()) for n in numeros_texto.split(",") if n.strip()]
                positivos = sum(1 for n in numeros if n > 0)
                negativos = sum(1 for n in numeros if n < 0)
                zeros = sum(1 for n in numeros if n == 0)
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.metric("➕", positivos)
                with c2:
                    st.metric("➖", negativos)
                with c3:
                    st.metric("0️⃣", zeros)
            except ValueError:
                st.error("Entrada inválida. Use números separados por vírgula.")
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Contadores e loop while", "explicacao": "`while True` é loop infinito que para com `break`.", "codigo": 'positivos = 0\nnegativos = 0\nzeros = 0\n\nwhile True:\n    entrada = input("Número (ou \'sair\'): ")\n    if entrada.lower() == "sair":\n        break'},
                {"titulo": "Converter e classificar", "explicacao": "`> 0` positivo, `< 0` negativo, senão zero.", "codigo": '    try:\n        numero = float(entrada)\n    except ValueError:\n        print("Inválido.")\n        continue\n\n    if numero > 0:\n        positivos += 1\n    elif numero < 0:\n        negativos += 1\n    else:\n        zeros += 1'},
                {"titulo": "Exibir totais", "explicacao": "Linhas **fora** do `while`, executam após `break`.", "codigo": 'print(f"Positivos: {positivos}")\nprint(f"Negativos: {negativos}")\nprint(f"Zeros: {zeros}")'},
            ],
            quiz_key="quiz7",
            quiz_question="O que `break` faz no Python?",
            quiz_options=["Pausa 1 segundo", "Sai do loop atual", "Encerra o programa", "Pula iteração"],
            quiz_answer="Sai do loop atual",
            quiz_correct_msg="✅ Correto! `break` interrompe o loop mais interno.",
            quiz_wrong_msg="❌ `break` sai do loop. `continue` pula iteração.",
        )


def exercicio8():
    st.header("📐 Exercício 8: Área e Perímetro de um Retângulo")
    st.write("Calcule a área e o perímetro a partir das dimensões.")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        largura = st.slider("Largura:", 0.5, 20.0, 5.0, 0.5, key="ret_l")
        altura = st.slider("Altura:", 0.5, 20.0, 3.0, 0.5, key="ret_a")
        area = largura * altura
        perimetro = 2 * (largura + altura)
        c1, c2 = st.columns(2)
        with c1:
            st.metric("Área", f"{area:.2f}")
        with c2:
            st.metric("Perímetro", f"{perimetro:.2f}")
        pct_w = min(largura / 20 * 100, 100)
        pct_h = min(altura * 10, 150)
        st.markdown(f'<div style="width:{pct_w}%;max-width:300px;height:{pct_h}px;background:linear-gradient(135deg,#667eea,#764ba2);border-radius:4px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:bold;margin:1rem auto;font-size:0.9rem">{largura} × {altura}</div>', unsafe_allow_html=True)
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Receber dimensões", "explicacao": "`float()` permite valores decimais.", "codigo": 'try:\n    largura = float(input("Largura: "))\n    altura = float(input("Altura: "))'},
                {"titulo": "Calcular área e perímetro", "explicacao": "**Área** = largura × altura. **Perímetro** = 2 × (largura + altura).", "codigo": "    area = largura * altura\n    perimetro = 2 * (largura + altura)"},
                {"titulo": "Exibir resultados", "explicacao": "`:.2f` = 2 casas decimais.", "codigo": '    print(f"Área: {area:.2f}")\n    print(f"Perímetro: {perimetro:.2f}")\nexcept ValueError:\n    print("Entrada inválida.")'},
            ],
            quiz_key="quiz8",
            quiz_question="Qual a área de um retângulo 4×6?",
            quiz_options=["10", "20", "24", "48"],
            quiz_answer="24",
            quiz_correct_msg="✅ Correto! 4 × 6 = 24.",
            quiz_wrong_msg="❌ Área = largura × altura.",
        )


def exercicio9():
    st.header("📅 Exercício 9: Conversão de Idade")
    st.write("Descubra quantos dias, semanas e meses você já viveu!")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        idade = st.slider("Sua idade em anos:", 1, 120, 20, key="idade")
        dias = idade * 365
        semanas = idade * 52
        meses = idade * 12
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("📆 Dias", f"{dias:,}".replace(",", "."))
        with c2:
            st.metric("📅 Semanas", f"{semanas:,}".replace(",", "."))
        with c3:
            st.metric("🗓️ Meses", f"{meses:,}".replace(",", "."))
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Receber a idade", "explicacao": "`int()` pois idade é inteiro.", "codigo": 'try:\n    idade = int(input("Sua idade em anos: "))'},
                {"titulo": "Converter com multiplicação", "explicacao": "1 ano ≈ 365 dias, ≈ 52 semanas, = 12 meses.", "codigo": "    dias = idade * 365\n    semanas = idade * 52\n    meses = idade * 12"},
                {"titulo": "Exibir resultados", "explicacao": "f-strings para saída formatada.", "codigo": '    print(f"  {dias} dias")\n    print(f"  {semanas} semanas")\n    print(f"  {meses} meses")\nexcept ValueError:\n    print("Entrada inválida.")'},
            ],
            quiz_key="quiz9",
            quiz_question="Quantos meses tem uma pessoa de 25 anos?",
            quiz_options=["250", "300", "1300", "600"],
            quiz_answer="300",
            quiz_correct_msg="✅ Correto! 25 × 12 = 300.",
            quiz_wrong_msg="❌ 1 ano = 12 meses.",
        )


def exercicio10():
    st.header("🏦 Exercício 10: Conta Bancária Simples")
    st.write("Simule operações de depósito e saque.")
    tab1, tab2 = st.tabs(["⚡ Experimente", "🎓 Aprenda"])
    with tab1:
        saldo_inicial = st.number_input("Saldo inicial (R$):", min_value=0.0, value=1000.0, step=10.0, key="banco_s")
        deposito = st.number_input("Valor do depósito (R$):", min_value=0.0, value=500.0, step=10.0, key="banco_d")
        saque = st.number_input("Valor do saque (R$):", min_value=0.0, value=200.0, step=10.0, key="banco_sq")
        if st.button("Simular", key="btn_banco", use_container_width=True):
            saldo = saldo_inicial + deposito
            st.write(f"Saldo após depósito: **R$ {saldo:.2f}**")
            if saque > saldo:
                st.error(f"Saldo insuficiente para saque de R$ {saque:.2f}!")
                st.warning(f"Saldo atual: R$ {saldo:.2f}")
            else:
                saldo -= saque
                st.success(f"Saldo final: **R$ {saldo:.2f}**")
            max_val = saldo_inicial + deposito
            if max_val > 0:
                st.progress(min(saldo / max_val, 1.0))
    with tab2:
        render_code_tutorial(
            steps=[
                {"titulo": "Receber saldo, depósito e saque", "explicacao": "`float` para aceitar centavos.", "codigo": 'try:\n    saldo = float(input("Saldo inicial: "))\n    deposito = float(input("Depósito: "))\n    saque = float(input("Saque: "))'},
                {"titulo": "Realizar o depósito", "explicacao": "`saldo += deposito` = `saldo = saldo + deposito`.", "codigo": "    saldo += deposito"},
                {"titulo": "Verificar saldo antes do saque", "explicacao": "Se saque > saldo, erro. Senão, subtrai. **Validação** contra saldo negativo.", "codigo": '    if saque > saldo:\n        print("Erro: saldo insuficiente.")\n    else:\n        saldo -= saque\n        print(f"Saldo final: R${saldo:.2f}")\nexcept ValueError:\n    print("Entrada inválida.")'},
            ],
            quiz_key="quiz10",
            quiz_question="Saldo R$100, depósito R$50, saque R$200. O que acontece?",
            quiz_options=["Saldo fica -R$50", "Saque é realizado", "Erro: saldo insuficiente", "Saldo fica R$0"],
            quiz_answer="Erro: saldo insuficiente",
            quiz_correct_msg="✅ Correto! Após depósito: 150. Saque 200 > 150.",
            quiz_wrong_msg="❌ 100 + 50 = 150. Saque de 200 > 150!",
        )


def pagina_inicial():
    st.title("📚 Trabalho 02 — Álgebra e Algoritmos")
    st.markdown("""
    Bem-vindo ao site interativo do **Trabalho 02**!

    - **⚡ Use** cada exercício de forma interativa
    - **🎓 Aprenda** como o código funciona passo a passo
    - **🧪 Teste** seus conhecimentos com quizzes

    👈 Use o menu lateral para navegar entre os exercícios.
    """)
    st.markdown("---")
    st.subheader("📋 Lista de Exercícios")
    exercicios = [
        ("🔢", "Calculadora de Operações Simples", "if/elif, operadores aritméticos"),
        ("🎲", "Jogo de Adivinhação", "random, for, continue"),
        ("🔄", "Contador de Pares e Ímpares", "for, operador %, contadores"),
        ("📊", "Média de Notas com Aprovação", "acumulador, :.2f"),
        ("💰", "Calculadora de Desconto", "fórmula de porcentagem"),
        ("📏", "Conversor de Unidades", "if/elif, multiplicação"),
        ("➕", "Verificador de Sinal", "while True, break"),
        ("📐", "Área e Perímetro", "fórmulas geométricas"),
        ("📅", "Conversão de Idade", "multiplicação, int"),
        ("🏦", "Conta Bancária Simples", "operadores +=/-="),
    ]
    for i, (icon, titulo, conceitos) in enumerate(exercicios, 1):
        st.markdown(f"**{icon} Exercício {i}: {titulo}**")
        st.caption(f"Conceitos: {conceitos}")


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
