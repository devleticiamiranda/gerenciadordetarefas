tarefas = []

while True:
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Completar tarefa")
    print("5 - Deletar tarefas concluídas")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("[Erro] Digite apenas números.")
        continue

    if opcao == 0:
        print("\nEncerrando o Gerenciador de Tarefas... Até logo!")
        break

    elif opcao == 1:
        adic_tarefa = input("Digite o nome da tarefa: ")

        tarefa = {
            "nome": adic_tarefa,
            "concluída": False
        }

        tarefas.append(tarefa)

        print(f"Tarefa '{adic_tarefa}' adicionada com sucesso!")

    elif opcao == 2:
        if len(tarefas) == 0:
            print("\nNenhuma tarefa cadastrada até o momento.")
        else:
            print("\n===== SUAS TAREFAS =====")

            for indice, tarefa in enumerate(tarefas, start=1):
                status = "[X]" if tarefa["concluída"] else "[ ]"
                print(f"{indice}. {status} {tarefa['nome']}")

    elif opcao == 3:
        if len(tarefas) == 0:
            print("\nNenhuma tarefa para atualizar.")
        else:
            print("\n===== TAREFAS ATUAIS =====")

            for indice, tarefa in enumerate(tarefas, start=1):
                status = "[X]" if tarefa["concluída"] else "[ ]"
                print(f"{indice}. {status} {tarefa['nome']}")

            try:
                numero = int(
                    input("\nDigite o número da tarefa que deseja renomear: ")
                )
            except ValueError:
                print("[Erro] Digite um número válido.")
                continue

            if 1 <= numero <= len(tarefas):
                novo_nome = input("Digite o novo nome para esta tarefa: ")

                indice_ajustado = numero - 1
                tarefas[indice_ajustado]["nome"] = novo_nome

                print(f"Tarefa {numero} atualizada com sucesso!")
            else:
                print("[Erro] Número de tarefa inválido.")

    elif opcao == 4:
        if len(tarefas) == 0:
            print("\nNenhuma tarefa para completar.")
        else:
            print("\n===== TAREFAS =====")

            for indice, tarefa in enumerate(tarefas, start=1):
                status = "[X]" if tarefa["concluída"] else "[ ]"
                print(f"{indice}. {status} {tarefa['nome']}")

            try:
                numero = int(
                    input(
                        "\nDigite o número da tarefa que deseja marcar como concluída: "
                    )
                )
            except ValueError:
                print("[Erro] Digite um número válido.")
                continue

            if 1 <= numero <= len(tarefas):
                indice_ajustado = numero - 1

                tarefas[indice_ajustado]["concluída"] = True

                print(
                    f"Tarefa '{tarefas[indice_ajustado]['nome']}' "
                    "marcada como concluída!"
                )
            else:
                print("[Erro] Número de tarefa inválido.")

    elif opcao == 5:
        if len(tarefas) == 0:
            print("\nNenhuma tarefa cadastrada.")
        else:
            qtd_antes = len(tarefas)

            tarefas = [
                tarefa
                for tarefa in tarefas
                if not tarefa["concluída"]
            ]

            qtd_removidas = qtd_antes - len(tarefas)

            if qtd_removidas > 0:
                print(
                    f"\n[Sucesso] {qtd_removidas} "
                    "tarefa(s) concluída(s) removida(s)."
                )
            else:
                print(
                    "\n[Aviso] Nenhuma tarefa concluída "
                    "encontrada para deletar."
                )

    else:
        print("[Erro] Opção inválida. Escolha uma opção do menu.")
