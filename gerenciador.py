tarefas=[]

while True:
    print("1-Adicionar tarefa")
    print("2-Ver tarefas")
    print("3-Atualizar Tarefa")
    print("4-Completar Tarefa")
    print("5-Deletar Tarefa")
    print("0-Sair")


    opcao=int(input("Escolha uma opcao: "))


    if opcao !=0:
        if opcao==1:
            adic_tarefa=input("Digite o nome da tarefa: ")
            adic_tarefa={"nome: " adic_tarefa, "conluída":False}


            tarefas.append(adic_tarefa)
            print(f"Tarefa'{adic_tarefa}'adicionada com sucesso!")


        elif opcao==2:
            if len(tarefas)==0:
                print("Nenhuma tarefa cadastrada até o momento")
            else:
                print("Suas tarefas")
           
            for indice,tarefa in enumerate(tarefas,start=1)
                if tarefa["concluída"]:
                    status:"[X]"
                else:
                    status:"[]"




        elif opcao==3:
            if len(tarefas)==0:
                print("Nenhuma tarefa para atualizar")
            else:
                print("\n ----TAREFAS ATUAIS----")
                for indice, tarefa in enumerate(tarefas, start=1)
                print(f'{indice}. {tarefa['nome']}')


                numero=int(input("\Digite no número da tarefa que deseja renomear:"))


                if 1<= numero<=len (tarefas):
                    novo_nome=input("Digite o novo nome para esta tarefa: ")


                    indice_ajustado=numero-1


                    tarefas[indice_ajustado]["nome"] =novo_nome
                    print(f"Tarefa {numero} atualizada com sucesso!")
                else:
                    print("[Erro] Número de tarefa inválido")




        elif opcao==4:
            if len(tarefas)==0:
                print("\n Nenhuma tarefa para completar")
            else:
                print("\n ----TAREFAS PENDENTES----")
                for indice, tarefa in enumerate(tarefas, start=1)
                    status="[X]" if tarefa ["concluída"] else "[]"
                    print(f"{indice}. {status} {tarefa['nome']}")


                    numero=int(input("\nDigite o número da tarefa que deseja marcar como concluída: "))


                    if 1<= numero <=len (tarefas):
                        indice_ajustado = numero-1


                        tarefas[indice_ajustado]["concluída"]=True


                        print(f"Tarefa '{tarefas[indice_ajustado][nome]}' marcada como concluída!")


                    else:
                        print("[Erro] Número de tarefa inválido")


        elif opcao==5:
            if len(tarefas)==0:
                print("\Nenhuma tarefa cadastrada")
            else:
                qtd_antes=len(tarefas)
                tarefas=[t for t in tarefas if not t ["concluída"]]


                qtd_removidas=qtd_antes-len(tarefas)


                if qtd_removidas >0:
                    print(f"\n [Sucesso] {qtd_removidas} tarefa(s) concluída(s) removida(s)")
                else:
                    print("\n [Aviso] Nenhuma tarefa concluída encontrada para deletar")


        else:
            print("\nEncerrando o Gerenciador de Tarefas... Até logo!")
            break
