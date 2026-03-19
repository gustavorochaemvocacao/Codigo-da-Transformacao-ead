
historico_detalhado = []

def calcular():
    v1 = input("Primeiro número: ")
    v2 = input("Segundo número: ")
    
    n1 = float(v1) if '.' in v1 else int(v1)
    n2 = float(v2) if '.' in v2 else int(v2)
    
    print("Operações: [1]+ [2]- [3]* [4]/")
    op_mat = input("Operação: ")
    
    if op_mat == '1':
        simbola, res = "+", n1 + n2
    elif op_mat == '2':
        simbola, res = "-", n1 - n2
    elif op_mat == '3':
        simbola, res = "*", n1 * n2
    elif op_mat == '4':
        simbola = "/"
        res = n1 / n2 if n2 != 0 else "Indeterminado"
    
    registro = f"Cálculo: {n1} {simbola} {n2} | Resultado: {res} | Tipo: {type(res).__name__}"
    print(f"\n>> {registro}")
    historico_detalhado.append(registro)

def porcentagem():
    v_porcent = float(input("Valor da porcentagem: "))
    v_total = float(input("Valor base: "))
    
    print("1. Calcular apenas a parte (X% de Y)")
    print("2. Acréscimo (Y + X%)")
    print("3. Desconto (Y - X%)")
    tipo_p = input("Opção: ")
    
    parte = (v_porcent / 100) * v_total
    
    if tipo_p == '1':
        res_p = parte
        msg = f"{v_porcent}% de {v_total} é {res_p}"
    elif tipo_p == '2':
        res_p = v_total + parte
        msg = f"{v_total} com acréscimo de {v_porcent}% = {res_p}"
    elif tipo_p == '3':
        res_p = v_total - parte
        msg = f"{v_total} com desconto de {v_porcent}% = {res_p}"
        
    print(f"\n>> {msg}")
    historico_detalhado.append(msg)

def ver_historico():
    print("\n--- HISTÓRICO DE OPERAÇÕES ---")
    if not historico_detalhado:
        print("Nenhum cálculo realizado.")
    else:
        for i, item in enumerate(historico_detalhado, 1):
            print(f"{i}. {item}")

def main():
    while True:
        print("\n==============================")
        print("    \nCalculadora - Python")
        print("==============================")
        print("1. Calcular (Inteiro/Decimal)")
        print("2. Porcentagem")
        print("3. Ver Histórico Detalhado")
        print("0. Sair")
        
        escolha = input("\nOpção: ")

        if escolha == '1':
            calcular()
        elif escolha == '2':
            porcentagem()
        elif escolha == '3':
            ver_historico()
        elif escolha == '0':
            print("Encerrando... Até à próxima!")
            break

if __name__ == "__main__":
    main()