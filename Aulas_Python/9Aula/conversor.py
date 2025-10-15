# Copia do Gemini

def celsius_para_fahrenheit(celsius):
    """Converte graus Celsius para Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32 #aqui está a forma de converter de Calsius para Fahrenheit
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    """Converte graus Fahrenheit para Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# --- Programa principal ---
print("Conversor de Temperatura")
print("1. Converter de Celsius para Fahrenheit")
print("2. Converter de Fahrenheit para Celsius")

opcao = input("Escolha uma opção (1 ou 2): ")

if opcao == '1':
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C é igual a {resultado:.2f}°F")
elif opcao == '2':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}°F é igual a {resultado:.2f}°C")
else:
    print("Opção inválida.")

# Fazendo o mesmo código de forma resumida de acordo com oque aprendemos até o momento nas aulas 

def conversor(temperatura, tipo):
    if tipo == "C":
        return (temperatura * 9/5) + 32 #Celsius para Fahren...
    elif tipo =="F" :
        return (temperatura - 32) * 5/9 #fahren... para celsius
    else:
        return "Tipo inválido! Use 'C' ou 'F'"
    
print(conversor(30, "C"))