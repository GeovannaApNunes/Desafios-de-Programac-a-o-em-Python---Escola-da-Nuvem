import json

def readJsonFile(fileName):
    try:
        with open(fileName, 'r') as json_file:
            data = json.load(json_file)
        return data
    except IOError:
        print("Could not read file:", fileName)
        return None  # Retorna None em caso de erro

# Carregando os dados
file_path = 'files/insulin.json'
data = readJsonFile(file_path)

# Verificando se os dados foram carregados corretamente
if data:
    bInsulin = str(data['molecules']['bInsulin'])
    aInsulin = str(data['molecules']['aInsulin'])
    insulin = bInsulin + aInsulin
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']

    print('bInsulin:', bInsulin)
    print('aInsulin:', aInsulin)
    print('molecularWeightInsulinActual:', molecularWeightInsulinActual)
else:
    print("Error. Exiting program")