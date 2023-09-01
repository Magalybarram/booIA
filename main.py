import openai
import typer  # pip install "typer[all]"
from rich import print  # pip install rich
from rich.table import Table


def main():

    openai.api_key = "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"

    print("🔰 [bold purple]VIENVENIDO A  MI WEB[/bold purple]🔰")

    table = Table("Comando", "Descripción")
    table.add_row("exit", "Salir de la aplicación")
    table.add_row("new", "Crear una nueva conversación")

    print(table)

    # Contexto del asistente, podemos ir condicionando dependiendo de lo que queramos
    context = {"role": "system",
               "content": "Eres un asistente de mercado libre"}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("💬 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold yellow]> [/bold yellow] [yellow]{response_content}[/yellow]")


def __prompt() -> str:
    prompt = typer.prompt("\n¿En qué te puedo ayudar? ")
    

    if prompt == "exit":
        exit = typer.confirm("😟 ¿Estás seguro de salir?")
        if exit:
            print("👋 ¡Hasta luego!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)