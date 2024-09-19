
# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora de todos os dias de um ano, faça um programa, na linguagem que desejar, que calcule e retorne:

# - O menor valor de faturamento ocorrido em um dia do ano;
# - O maior valor de faturamento ocorrido em um dia do ano;
# - Número de dias no ano em que o valor de faturamento diário foi superior à média anual.

# a) Considerar o vetor já carregado com as informações de valor de faturamento.

# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média.

# c) Utilize o algoritmo mais veloz que puder definir.


# Resposta:
def quicksort(faturamento):
    if len(faturamento) <= 1:
        return faturamento
    else:
        pivo = faturamento[0]
        menor = [i for i in faturamento[1:] if i <= pivo]
        maior = [i for i in faturamento[1:] if i > pivo]
        return quicksort(menor) + [pivo] + quicksort(maior)
    
    
def estatisticas_faturamento(faturamento):
    faturamento_valido = list(filter(lambda x: x > 0, faturamento))

    if not faturamento_valido:
        return None, None, 0
    
    min_faturamento = faturamento_valido[0]
    max_faturamento = faturamento_valido[-1]

    # Calculate the average faturamento
    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)
    
    days_above_average = len(list(filter(lambda x: x > media_faturamento, faturamento_valido)))

    return min_faturamento, max_faturamento, days_above_average


def main():
    faturamento = [100, 200, 0, 300, 0, 400, 500, 0, 600, 700, 0, 800, 900, 1000, 0, 1100, 1200, 0, 1300, 1400, 0, 1500, 1600, 0, 1700, 1800, 0, 1900, 2000, 0, 2100, 2200, 0, 2300, 2400, 0, 2500, 2600, 0, 2700, 2800, 0, 2900, 3000, 0, 3100, 3200, 0, 3300, 3400, 0, 3500, 3600, 0, 3700, 3800, 0, 3900, 4000, 0, 4100, 4200, 0, 4300, 4400, 0, 4500, 4600, 0, 4700, 4800, 0, 4900, 5000, 0, 5100, 5200, 0, 5300, 5400, 0, 5500, 5600, 0, 5700, 5800, 0, 5900, 6000, 0, 6100, 6200, 0, 6300, 6400, 0, 6500, 6600, 0, 6700, 6800, 0, 6900, 7000, 0, 7100, 7200, 0, 7300, 7400, 0, 7500, 7600, 0, 7700, 7800, 0, 7900, 8000, 0, 8100, 8200, 0, 8300, 8400, 0, 8500, 8600, 0, 8700, 8800, 0, 8900, 9000, 0, 9100, 9200, 0, 9300, 9400, 0, 9500, 9600, 0, 9700, 9800, 0, 9900, 10000, 0, 10100, 10200, 0, 10300, 10400, 0, 10500, 10600, 0, 10700, 10800, 0, 10900, 11000, 0, 11100, 11200, 0, 11300, 11400, 0, 11500, 11600, 0, 11700, 11800, 0, 11900, 12000, 0, 12100, 12200, 0, 12300, 12400, 0, 12500, 12600, 0, 12700, 12800, 0, 12900, 13000, 0, 13100, 13200, 0, 13300, 13400, 0, 13500, 13600, 0, 13700, 13800, 0, 13900, 14000, 0, 14100, 14200, 0, 14300, 14400, 0, 14500, 14600, 0, 14700, 14800, 0, 14900, 15000, 0, 15100, 15200, 0, 15300, 15400, 0, 15500, 15600, 0, 15700, 15800, 0, 15900, 16000, 0, 16100, 16200, 0, 16300, 16400, 0, 16500, 16600, 0, 16700, 16800, 0, 16900, 17000, 0, 17100, 17200, 0, 17300, 17400, 0, 17500, 17600, 0, 17700, 17800, 0, 17900, 18000, 0, 18100, 18200, 0, 18300, 18400, 0, 18500, 18600, 0, 18700, 18800, 0, 18900, 19000, 0, 19100, 19200, 0, 19300, 19400, 0, 19500, 19600, 0, 19700, 19800, 0, 19900, 20000, 0, 20100, 20200, 0, 20300, 20400, 0, 20500, 20600, 0, 20700, 20800, 0, 20900, 21000, 0, 21100, 21200, 0, 21300, 21400, 0, 21500, 21600, 0, 21700, 21800, 0, 21900, 22000, 0, 22100, 22200, 0, 22300, 22400, 0, 22500, 22600, 0, 22700, 22800, 0, 22900, 23000, 0, 23100, 23200, 0, 23300, 23400, 0, 23500, 23600, 0, 23700, 23800, 0, 23900, 24000, 0, 24100, 24200, 0, 24300, 24400, 0, 24500, 24600, 0, 24700, 24800, 0, 24900, 25000, 0, 25100, 25200, 0, 25300, 25400, 0, 25500, 25600, 0, 25700, 25800, 0, 25900, 26000, 0, 26100, 26200, 0, 26300, 26400, 0, 26500, 26600, 0, 26700, 26800, 0, 26900, 27000, 0, 27100, 27200, 0, 27300, 27400, 0, 27500, 27600, 0, 27700, 27800, 0, 27900, 28000, 0, 28100, 28200, 0, 28300, 28400, 0, 28500, 28600, 0, 28700, 28800, 0, 28900, 29000, 0, 29100, 29200, 0, 29300, 29400, 0, 29500, 29600, 0, 29700, 29800, 0, 29900, 30000, 0, 30100, 30200, 0, 30300, 30400, 0, 30500, 30600, 0, 30700, 30800, 0, 30900, 31000, 0, 31100, 31200, 0, 31300, 31400, 0, 31500, 31600, 0, 31700, 31800, 0, 31900, 32000, 0, 32100, 32200, 0, 32300, 32400, 0, 32500, 32600, 0, 32700, 32800, 0, 32900, 33000, 0, 33100, 33200, 0, 33300, 33400, 0, 33500, 33600, 0, 33700, 33800, 0, 33900, 34000, 0, 34100, 34200, 0, 34300, 34400, 0, 34500, 34600, 0, 34700, 34800, 0, 34900, 35000, 0, 35100, 35200, 0, 35300, 35400, 0, 35500, 35600, 0, 35700, 35800, 0, 35900, 36000, 0, 36100, 36200, 0, 36300, 36400, 0, 36500]

    min_faturamento, max_faturamento, days_above_average = estatisticas_faturamento(faturamento)

    print(f"Menor valor de faturamento: {min_faturamento}")
    print(f"Maior valor de faturamento: {max_faturamento}")
    print(f"Número de dias com faturamento acima da média: {days_above_average}")


if __name__ == "__main__":
    main()