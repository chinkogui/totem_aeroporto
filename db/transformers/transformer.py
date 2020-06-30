def transformPassagem(passagem):
    transformed = []
    try:
        for x in passagem:
            transformed.append(x)
        print(transformed)
        return transformed
    except:
        return 0


def transformVoos(voos):
    transformed = []
    for voo in voos:
        object = {
            'numeroVoo': voo[0],
            'origem': voo[1],
            'destino': voo[2],
            'data': voo[3],
            'horario': voo[4],
            'idAviao': voo[5],
            'portaoEmbarque': voo[6]
        }
        transformed.append(object)
    return transformed