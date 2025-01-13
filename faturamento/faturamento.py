import json


def relatorio_faturamento(report):
    try:
        with open(report, "r") as file:
            revenue = json.load(file)

        valid_days = [
            day for day in revenue if isinstance(day, (int, float)) and day > 0
        ]

        if not valid_days:
            return "Nenhum dia com faturamento válido encontrado."

        max_revenue = max(valid_days)
        min_revenue = min(valid_days)

        avg_revenue = sum(valid_days) / len(valid_days)

        above_avg = sum(1 for day in valid_days if day > avg_revenue)

        return (
            f"Menor valor de faturamento: {min_revenue}\n"
            f"Maior valor de faturamento: {max_revenue}\n"
            f"Número de dias com faturamento acima da média: {above_avg}"
        )

    except FileNotFoundError:
        return "Arquivo não encontrado. Verifique o caminho e tente novamente."
    except json.JSONDecodeError:
        return "Erro ao processar o arquivo JSON. Verifique o formato do arquivo."
    except Exception as e:
        return f"Ocorreu um erro inesperado: {e}"
