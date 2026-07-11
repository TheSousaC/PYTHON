from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços") ##Cria a o objeto(tabela) e põe o Nome da tabela
tabela.add_column("Nome", justify="center", style="cyan", no_wrap=True) ##Add colunna Nome
tabela.add_column("Preço", style="cyan", justify="center", no_wrap=True) ##Add colunna Nome

tabela.add_row("Meias [yellow]Amarelas[/]", "R$4,00")
tabela.add_row("Meias [black]Pretas[/]", "R4,00")

print(tabela)