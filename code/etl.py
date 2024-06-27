from loguru import logger
import pandas as pd
from decorators import log_decorator, cronometro
import glob
import os
# C:\Users\rodol\Documents\data_eng_projetos\testando-logs-e-decoradores\log_files
logger.add("./log_files/file_{time}.log", format="{time} {level} {message}", level="INFO")

@cronometro
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    print(extrair_dados.__name__)
    print(extrair_dados.__doc__)
    return df_total

@cronometro
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df

@cronometro
def salvar_arquivo_novo_de_dados(df: pd.DataFrame, formato_saida: list):
    for formato in formato_saida:
        if formato == "csv":
            df.to_csv("./clean_data/dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet", index=False)

@cronometro
def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_saida: list):
    data_frame = extrair_dados(pasta)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(data_frame)
    salvar_arquivo_novo_de_dados(data_frame_calculado, formato_saida)