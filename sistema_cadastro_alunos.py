alunos = []
proximo_id = 1
def cadastro_aluno():
            global proximo_id
            while True:
                nome = str(input('Digite seu nome:'))
                try:
                    idade = int(input('Digite sua idade:'))
                except ValueError:
                     print('Digite apenas numeros!')
                     continue
                if idade <= 0:
                    print('Idade Inválida!')
                    continue
                
                aluno = {
                'id' : proximo_id,
                'Nome': nome,
                'idade': idade,
                'Nota 1' :'...',
                'Nota 2' : '...',
                'media' : '...',
                'situacao' :'...',
                }
                alunos.append(aluno)
                print('Aluno(a) cadastrado! ID:',proximo_id)
                proximo_id += 1
                print("=" * 30)
                break
        
def listar_alunos():
    print('Listando Alunos...')
    print('========== Lista de Alunos ==========')
    print('Número de alunos na Sala:',len(alunos))
    print('.'
          '.')
    for aluno in alunos:
        print('ID:', aluno['id'])
        print('Nome:', aluno['Nome'])
        print('Idade:', aluno['idade'])
        print("Nota 1:", aluno['Nota 1'])
        print("Nota 2:", aluno['Nota 2'])
        print("Média:", aluno['media'])
        print('Situação:',aluno['situacao'])
        print("=" * 30)

def buscar_aluno():
    while True:
        try:
            id_busca = int(input('Digite o ID do aluno(a) :'))
        except ValueError:
            print('ID Inválido!!')
            continue
        encontrado = False
        for aluno in alunos:
            if id_busca == aluno['id']:
                print('ID:',aluno['id'])
                print('Nome:', aluno['Nome'])
                print('Idade:', aluno['idade'])
                print("Nota 1:", aluno['Nota 1'])
                print("Nota 2:", aluno['Nota 2'])
                print("Média:", aluno['media'])
                print('Situação:',aluno['situacao'])
                encontrado = True
        if encontrado == False:
            print('Aluno não encontrado')
        print("=" * 30)
        break

                    
def excluir_aluno():
     while True:
        try:
             id_busca2 = int(input('Digite o ID do aluno(a):'))
        except ValueError:
            print('ID Inválido!')
            continue
        encontrado1 = False
        for aluno in alunos:
            if id_busca2 == aluno['id']:
                alunos.remove(aluno)
                encontrado1 = True
        if encontrado1 == False:
            print('Aluno não encontrado!')
        print("=" * 30)  
        break
             
            
def notas_aluno():
        while True:
            try:
                id_busca3 = int(input('Digite o ID do aluno(a):'))
            except ValueError:
                print('ID Inválido!')
                continue
            break
        encontrado3 = False
        for aluno in alunos:
            if id_busca3 == aluno['id']:
                    encontrado3 = True
                    while True:
                        try:
                            nota1 = float(input('Digite sua Primeira Nota:'))
                        except ValueError:
                            print('Apenas números!')
                            continue
                        if (nota1 >= 0) and (nota1 <= 10):
                            while True:
                                try:
                                    nota2 = float(input('Digite sua Segunda Nota:'))
                                except ValueError:
                                    print('Apenas números!')
                                    continue
                                if (nota2 >= 0) and (nota2 <= 10):
                                    aluno['Nota 1'] = nota1
                                    aluno['Nota 2'] = nota2
                                    media = (nota1 + nota2) / 2
                                    aluno['media'] = media
                                    if media >= 7:
                                        situacao = 'Aprovado'
                                    else:
                                            situacao = 'Reprovado'
                                    aluno['situacao'] = situacao
                                    break
                                else: 
                                    print('nota não valida, tem quer ser entre(0,10)!!')
        
                            break
                        else:
                            print('nota não valida, tem quer ser entre(0,10)!!') 
        if encontrado3 == False:
            print('Aluno não encontrado!!')
        print("=" * 30)
        
def menu():
    while True:
        print('======== Oque Você Deseja fazer ? =========')
        print('1 - Adicionar novo aluno')
        print('2 - Listar alunos')
        print('3 - Buscar aluno')
        print('4 - Excluir Aluno')
        print('5 - Adicionar notas dos alunos')
        print('6 - Sair do programa')


        try:
            op1 = int(input('Escolha sua opção: '))
        except ValueError:
            print('Digite apenas um dos números a cima!!!')
            continue


        if op1 == 1:
            cadastro_aluno()
        elif op1 == 2:
            listar_alunos()
        elif op1 == 3:
            buscar_aluno()
        elif op1 == 4:
            excluir_aluno()
        elif op1 == 5:
            notas_aluno()
        elif op1 == 6:
            print('Saindo do programa...')
            break
        else:
            print('Essa opção não existe!')
    print("=" * 30)      
menu()
