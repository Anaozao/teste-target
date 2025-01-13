def calculate_percentage():
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    outros = 19849.53

    total_revenue = sum([sp, rj, mg, es, outros])

    sp_percentage = (sp / total_revenue) * 100
    rj_percentage = (rj / total_revenue) * 100
    mg_percentage = (mg / total_revenue) * 100
    es_percentage = (es / total_revenue) * 100
    outros_percentage = (outros / total_revenue) * 100

    return (
        f"SP representa {sp_percentage:.2f}% do total"
        f"RJ representa {rj_percentage:.2f}% do total"
        f"MG representa {mg_percentage:.2f}% do total"
        f"ES representa {es_percentage:.2f}% do total"
        f"Outros representa {outros_percentage:.2f}% do total"
    )


print(calculate_percentage())
