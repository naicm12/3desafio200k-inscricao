import streamlit as st
import mysql.connector
import re
from datetime import date
import smtplib
import email.message

conexao = mysql.connector.connect(
    host='200k.mysql.uhserver.com',
    user='ecm200',
    password='@Musica17',
    database='200k'
)

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


v_nome = ""
v_ncelular = ""
v_modalidade = ""
v_email = ""

def calculateAge(birthDate): 
    #dia = int(nascimento[0:2])
    #mes = int(nascimento[3:5])
    #ano = int(nascimento[6:10])

    #birthDate = date(ano, mes, dia)

    today = date.today() 
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
  
    return age 


def enviar_email(snome,sfone,smod,semail): 
    try: 
        corpo_email = f"""
        <p>Pré incrição realizada para o <b>3º Desafio 200k - Porto Velho/Humaitá</b> </p>
        <p>Nome: <b>{snome}</b> </p>
        <p>Telefone: <b>{sfone}</b> </p>
        <p>Modalidade: <b>{smod}"</b> </p>
        """
        
        msg = email.message.Message()
        msg['Subject'] = "Inscrição 3º Desafio 200k - "+ snome
        msg['From'] = 'ecmsistemasdeveloper@gmail.com'
        msg['To'] = "kelioesteves@hotmail.com;"
        msg['Co'] = semail
        password = 'mwxncuvjvmvwvnhp' 
        msg.add_header('Content-Type', 'text/html')
        #msg.attach()
        msg.set_payload(corpo_email )

        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        # Login Credentials for sending the mail
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To'],msg['Co']], msg.as_string().encode('utf-8'))
        s.quit()
        st.write("")
    except Exception as e:
        st.write("")
    #finally:            


def concluido():
    global tela_ativa
    #placeholder.empty()
    #placeholder2 = st.empty()

    #with placeholder2.form("Regulamento"):
    st.success("INSCRIÇÃO REALIZADA COM SUCESSO")
    #st.write(incricao().modalidade)
    #st.write(incricao().idmodalidade)
    #st.write(incricao().kmsolo)
    #st.write("id_atleta ", inscricao().idatleta)



st.set_page_config(page_title="3º Desafio 200k")
tela_ativa = 0

from PIL import Image
img = Image.open('02.png')
st.image(img)

st.markdown("### 3º Desafio 200k - Porto Velho/Humaítá")


form_inscricao = st.empty()

def inscricao():
    global tela_ativa
    global concluido
    global v_nome, v_modalidade, v_ncelular, v_email

    cpfvalido =False

    def validador(cpf):
        global cpfvalido
        cpfvalido = False
        
        #Retira apenas os dígitos do CPF, ignorando os caracteres especiais
        numeros = [int(digito) for digito in cpf if digito.isdigit()]
        
        quant_digitos = False
        validacao1 = False
        validacao2 = False

        if len(numeros) == 11:
            quant_digitos = True
        
            soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
            digito_esperado = (soma_produtos * 10 % 11) % 10
            if numeros[9] == digito_esperado:
                validacao1 = True

            soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
            digito_esperado1 = (soma_produtos1 *10 % 11) % 10
            if numeros[10] == digito_esperado1:
                validacao2 = True

            if quant_digitos == True and validacao1 == True and validacao2 == True:
                cpfvalido = True
            else:
                cpfvalido = False

        else:
            cpfvalido = False


    with ((form_inscricao.form("Inscricao"))):
        st.markdown("### Formulário de Inscrição")

        input_email = st.text_input(label="E-mail:", key="01")
        input_nome = st.text_input(label="Primeiro Nome:", placeholder="Insira apenas seu primeiro nome", key="02")
        input_sobrenome = st.text_input(label="Sobrenome:", placeholder="Insira seu sobrenome",key="03")
        c1,c2 = st.columns([1,1])
        with c1:
            input_cpf = st.text_input(label="CPF (99999999999):", placeholder="Somente números", max_chars=11,key="04")
        with c2:
            input_dn = st.date_input(label="Data de Nascimento:",format="DD/MM/YYYY", 
                                     max_value=date(year=2006, month=7, day=5),min_value=date(year=1924, month=7, day=5), value=None, key="05")
        input_telefone = st.text_input(label="Nº Celular 99 99999-9999:", max_chars=15, key="06")
        input_equipe = st.text_input(label="Equipe/Grupo/Academia pessoal:",placeholder="Se percente a alguma Equipe, Grupo ou academia, informe aqui",key="22")
        st.caption("Endereço:")
        e1, e2 = st.columns([4,1])
        with e1:
            input_rua = st.text_input(label="Rua:", key="07")
        with e2:
            input_numero = st.text_input(label="Número:", key="15")
        input_comp = st.text_input(label="Complemento:", key="28")
        input_bairro = st.text_input(label="Bairro:", key="08")
        g1, g2 = st.columns([2, 1])
        with g1:
            input_cidade = st.text_input(label="Cidade:", value="Porto Velho", key="09")
        with g2:
            input_estado = st.selectbox("Estado:",("Acre (AC)",
                                                   "Alagoas (AL)",
                                                   "Amapá (AP)",
                                                   "Amazonas (AM)",
                                                   "Bahia (BA)",
                                                   "Ceará (CE)",
                                                   "Distrito Federal (DF)",
                                                   "Espírito Santo (ES)",
                                                   "Goiás (GO)",
                                                   "Maranhão (MA)",
                                                   "Mato Grosso (MT)",
                                                   "Mato Grosso do Sul (MS)",
                                                   "Minas Gerais (MG)",
                                                   "Pará (PA)",
                                                   "Paraíba (PB)",
                                                   "Paraná (PR)",
                                                   "Pernambuco (PE)",
                                                   "Piauí (PI)",
                                                   "Rio de Janeiro (RJ)",
                                                   "Rio Grande do Norte (RN)",
                                                   "Rio Grande do Sul (RS)",
                                                   "Rondônia (RO)",
                                                   "Roraima (RR)",
                                                   "Santa Catarina (SC)",
                                                   "São Paulo (SP)",
                                                   "Sergipe (SE)",
                                                   "Tocantins (TO)"),index=21)

        f1,f2,f3 = st.columns([1,1,1])
        with f1:
            input_genero = st.radio("Gênero:", ["Masculino", "Feminino"])
        with f2:
            input_camiseta = st.radio("Camiseta:", ["PP", "P", "M", "G"])
        with f3:
            input_modalidade = st.radio("Modalidade:", ["Solo", "Dupla", "Quarteto", "Octeto"],
                                    captions=["200Km", "100Km cada", "50km cada", "25Km cada"])
        input_participantes = st.text_input(label="Em caso de Equipe, informe os nomes dos participantes incluindo o seu:", key="11",placeholder="Exemplo: João/Maria/Jose/Francisca")
        st.caption("Obs: Peça para que os demais intengrates da Equipe informe os mesmo nomes separados por '/'")
        input_equipe200 = st.text_input(label="Nome da equipe do 3º Desafio 200K:",placeholder="Informe o Nome da Equipe que compõe o Desafio",key="12")

        st.divider()

        st.write("Termo de Responsabilidade")

        def termo():
            with open('Termo.txt', 'r', encoding='UTF-8') as f:
                lines = f.readlines()
                for line in lines:
                    st.caption(line)

        #exibtermo = st.checkbox(label="Exibir Termo de Responsabilidade",bool=False)
        #if exibtermo:
        termo()

        check_aceita = False
        #check_aceita = st.checkbox(label="LI E ACEITO O TERMO DE RESPONSABILIDADE",bool=False)
        agree = st.checkbox('LI E ACEITO O TERMO DE RESPONSABILIDADE')

        if agree:
            check_aceita = True

        cursor = conexao.cursor()
        comando = f'SELECT ID_ATLETA FROM 200k.ATLETA WHERE CPF = "{input_cpf}"'
        cursor.execute(comando)
        resultado_cpf = cursor.fetchone()
        #s_cpf = resultado_cpf[0]

        cursor1 = conexao.cursor()
        comando = f'SELECT ID_ATLETA FROM 200k.ATLETA WHERE EMAIL = "{input_email}"'
        cursor1.execute(comando)
        resultado_email = cursor1.fetchone()
        #s_email = resultado_email[0]

        cursor2 = conexao.cursor()
        id_ = f'SELECT IFNULL(MAX(ID_ATLETA)+1,1) FROM ATLETA'
        cursor2.execute(id_)
        newid = cursor2.fetchone()
        idatleta = newid[0]

        confirma_button = st.form_submit_button("CONFIRMAR INSCRIÇÃO",type="primary")

        if confirma_button:
            if input_email == '':
                st.warning("Informe o E-mail!", icon="⚠️")
                st.stop()

            if not(re.search(regex,input_email)):  
                st.warning("E-mail incorreto", icon="⚠️")   
                st.stop()

            if input_cpf == '':
                st.warning("Informe o CPF!", icon="⚠️")
                st.stop()

            ncpf = input_cpf
            crtr2 = "!@#$()*'%:;?<>_\|/ .-,"
            for i in range(0,len(crtr2)):
                ncpf = ncpf.replace(crtr2[i],"")

            #validador(ncpf)

            # verifica numero do CPF
            
            #Retira apenas os dígitos do CPF, ignorando os caracteres especiais
            cpfvalido = False
            numeros = [int(digito) for digito in ncpf if digito.isdigit()]
            
            quant_digitos = False
            validacao1 = False
            validacao2 = False

            if len(numeros) == 11:
                quant_digitos = True
            
                soma_produtos = sum(a*b for a, b in zip (numeros[0:9], range (10, 1, -1)))
                digito_esperado = (soma_produtos * 10 % 11) % 10
                if numeros[9] == digito_esperado:
                    validacao1 = True

                soma_produtos1 = sum(a*b for a, b in zip(numeros [0:10], range (11, 1, -1)))
                digito_esperado1 = (soma_produtos1 *10 % 11) % 10
                if numeros[10] == digito_esperado1:
                    validacao2 = True

                if quant_digitos == True and validacao1 == True and validacao2 == True:
                    cpfvalido = True
                else:
                    cpfvalido = False

            else:
                cpfvalido = False


            if cpfvalido == False:
                st.warning(f"O CPF {ncpf} não é válido!", icon="⚠️")
                st.stop()
            
            #if len(ncpf) is not 11:
            #    st.warning("Nº do CPF inválido", icon="⚠️")
            #    st.stop()


            if input_nome == '':
                st.warning("Informe o primeiro Nome!", icon="⚠️")
                st.stop()

            if input_sobrenome == '':
                st.warning("Informe o primeiro Nome!", icon="⚠️")
                st.stop()

            if input_dn == '':
                st.warning("Informe sua Data de Nascimento!", icon="⚠️")
                st.stop()

            if input_telefone == '':
                st.warning("Informe o número do Celular!", icon="⚠️")
                st.stop()

            ncelular = input_telefone
            crtr1 = "!@#$()*'%:;?<>_\|/ .-,"
            for i in range(0,len(crtr1)):
                ncelular = ncelular.replace(crtr1[i],"")

            if len(ncelular) is not 11:
                st.warning("Nº do celular inválido")
                st.stop()

            if input_rua == '':
                st.warning("Informe a Rua!", icon="⚠️")
                st.stop()

            if input_bairro == '':
                st.warning("Informe o Bairro!", icon="⚠️")
                st.stop()

            if input_cidade == '':
                st.warning("Informe a Cidade e Estado (UF)!", icon="⚠️")
                st.stop()

            if resultado_cpf is not None:
                st.warning("CPF Já cadastrado!", icon="⚠️")
                st.stop()

            if resultado_email is not None:
                st.warning("E-mail Já cadastrado!", icon="⚠️")
                st.stop()

            if not check_aceita:
                st.warning("Necessário aceitar o Termo de Responsabildade!", icon="⚠️")
                st.stop()

            if input_genero == 'Masculino':
                sexo = "M"
            else:
                sexo = "F"

            data = date.today()
            dataf = data.strftime('%d/%m/%Y')
            datanasc = input_dn.strftime('%d/%m/%Y')
            idade = calculateAge(input_dn)
            
            if input_modalidade == 'Solo':
               modalidade = "Solo - 200km"
               idmodalidade = 1
               kmsolo = 200
            elif input_modalidade == 'Dupla':
               modalidade = "Dupla - 100km"
               idmodalidade = 2
               kmsolo = 100
            elif input_modalidade == 'Quarteto':
               modalidade = "Quarteto - 50km"
               idmodalidade = 3
               kmsolo = 50
            elif input_modalidade == 'Octeto':
               modalidade = "Octeto - 25km"
               idmodalidade = 4
               kmsolo = 25

            if idmodalidade > 1 and input_participantes == '':
                st.warning("Informe os nomes dos integrantes da Equipe do Desafio 200k", icon="⚠️")
                st.stop()

            kmInicial = 0
            kmFinal = 0
            ordemRev = 0

            if idmodalidade == 1:
                kmInicial = 1
                kmFinal = 200
                ordemRev = 1

            def vlinscricao(vidade,vmod):
                if vmod == 1:
                    if vidade < 60:
                        vl = 500
                    else:
                        vl = 250
                else:
                    if vidade < 60:
                        vl = 400
                    else:
                        vl = 200

                return vl
            
            vl_inscricao = vlinscricao(idade,idmodalidade)

            #if idmodalidade > 1 and input_equipe200 == '':
            #    st.warning("Informe o Nome da Equipe do Desafio 200k", icon="⚠️")
            #    st.stop()

            v_nome = input_nome + ' ' + input_sobrenome
            v_ncelular = ncelular
            v_modalidade = modalidade
            v_email = input_email

            try:

                qry_insert = f"""INSERT INTO 200k.ATLETA (
                                 ID_ATLETA, CPF, NOME, ENDERECO, NR_ENDERECO, COMP_ENDERECO, CIDADE, ESTADO_UF, DT_NASCIMENTO, 
                                 NR_CELULAR, SEXO, CAMISETA, DE_EQUIPE, EMAIL, MODALIDADE, ID_MODALIDADE, DE_EQUIPE200, INTEGRANTES, 
                                 KM_SOLO, FL_STATUS, ATIVO, DT_INSCRICAO, ACEITO_TERMO, VL_INSCRICAO, ORD_REVESAMENTO, KM_INICIAL, KM_FINAL)
                                 VALUES (
                                        {idatleta},"{ncpf}","{input_nome + ' ' + input_sobrenome}","{input_rua}","{input_numero}","{input_comp}",
                                        "{input_cidade}","{input_estado}","{datanasc}","{ncelular}","{sexo}","{input_camiseta}","{input_equipe}",
                                        "{input_email}","{modalidade}",{idmodalidade},"{input_equipe200}","{input_participantes}","{kmsolo}",'P',
                                        'S',"{dataf}",'S',{vl_inscricao},{ordemRev},{kmInicial},{kmFinal}) """

                cursor = conexao.cursor()
                cursor.execute(qry_insert)
                conexao.commit()
                cursor.close()


            except mysql.connector.Error as error:
                st.warning("Erro no Banco de Daods, tente novamente, se persistir contate o Administrador do Sistema! {}".format(error), icon="⚠️")
                st.stop()

            finally:
                if conexao.is_connected():
                    conexao.close()            
        

            tela_ativa = 2

            form_inscricao.empty()


inscricao()


if tela_ativa == 2:

    st.success("PRÉ INSCRIÇÃO REALIZADA COM SUCESSO", icon="😀")
    st.warning("ATENÇÃO", icon="⚠️")
    st.warning("A efetivação da sua Inscrição está condicionada ao envio do comprovante de pagamento para o número (69) 99925-9005, ou pelo link a baixo:")
    st.warning("https://wa.me/5569999259005", icon="📱")

    enviar_email(v_nome,v_ncelular,v_modalidade,v_email)

from PIL import Image
img = Image.open('003.png')
st.image(img)



