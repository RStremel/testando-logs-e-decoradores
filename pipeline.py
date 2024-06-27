from etl import pipeline_calcular_kpi_de_vendas_consolidado

if __name__ == "__main__":
    
    pasta_entrada = "data"
    formato_arquivo_saida = ["csv"]

    pipeline_calcular_kpi_de_vendas_consolidado(pasta=pasta_entrada, formato_saida=formato_arquivo_saida)