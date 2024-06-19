import csv
from collections import defaultdict
import unittest

# Extracción de clase: Voto
class Voto:
    def __init__(self, region, provincia, distrito, dni, candidato, esvalido):
        self.region = region
        self.provincia = provincia
        self.distrito = distrito
        self.dni = dni
        self.candidato = candidato
        self.esvalido = esvalido == '1'

class CalculaGanador:
    
    def leerDatos(self, archivo='0204.csv'):
        data = []
        with open(archivo, 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append(Voto(*fila))
        return data

    def contarVotosValidos(self, data):
        # Extracción de método: contar los votos válidos por candidato
        votosxcandidato = defaultdict(int)
        for voto in data:
            # Simplificación de condicionales: Validar DNI y voto válido en una sola línea
            if len(voto.dni) == 8 and voto.esvalido:
                votosxcandidato[voto.candidato] += 1
        return votosxcandidato

    def calcularPorcentajes(self, votosxcandidato, total_votos_validos):
        # Extracción de método: calcular los porcentajes de votos
        porcentajes = {candidato: (votos / total_votos_validos) * 100 for candidato, votos in votosxcandidato.items()}
        return porcentajes

    def calcularGanador(self, data):
        votosxcandidato = self.contarVotosValidos(data)
        total_votos_validos = sum(votosxcandidato.values())

        if total_votos_validos == 0:
            return []

        porcentajes = self.calcularPorcentajes(votosxcandidato, total_votos_validos)
        # Renombrar variables: 'ordenado' a 'candidatos_ordenados'
        candidatos_ordenados = sorted(porcentajes.items(), key=lambda item: item[1], reverse=True)

        if candidatos_ordenados[0][1] > 50:
            return [candidatos_ordenados[0][0]]

        return [candidatos_ordenados[0][0], candidatos_ordenados[1][0]]
    
"""
Eliminar código duplicado:
- Al contar con los métodos contar_votos_validos y calcular_porcentajes,se eliminó la duplicación en la lógica de procesamiento de datos.
- Se pudo haber repetido varias veces dentro del método calcular_ganador.
"""

# Pruebas unitarias
class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        self.calculador = CalculaGanador()
        self.datatest1 = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        self.datatest2 = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        self.datatest3 = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '0']
        ]
        self.datatest_empty = []
        self.datatest_invalid_dni = [
            ['Áncash', 'Asunción', 'Acochaca', '4081006', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1']
        ]
        self.datatest_no_valid_votes = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '0']
        ]

    def test_ganador_con_un_solo_candidato_valido(self):
        data = [Voto(*v) for v in self.datatest3]
        result = self.calculador.calcularGanador(data)
        self.assertEqual(result, ['Eddie Hinesley'])

    def test_datos_vacios(self):
        data = [Voto(*v) for v in self.datatest_empty]
        result = self.calculador.calcularGanador(data)
        self.assertEqual(result, [])

    def test_dni_invalido(self):
        data = [Voto(*v) for v in self.datatest_invalid_dni]
        result = self.calculador.calcularGanador(data)
        self.assertEqual(result, ['Eddie Hinesley'])

    def test_sin_votos_validos(self):
        data = [Voto(*v) for v in self.datatest_no_valid_votes]
        result = self.calculador.calcularGanador(data)
        self.assertEqual(result, [])

    def test_ganador_con_mas_del_50_por_ciento(self):
        data = [Voto(*v) for v in self.datatest1]
        result = self.calculador.calcularGanador(data)
        self.assertEqual(result, ['Aundrea Grace'])

    def test_segunda_vuelta(self):
        data = [Voto(*v) for v in self.datatest2]
        result = self.calculador.calcularGanador(data)
        self.assertEqual(result, ['Eddie Hinesley', 'Aundrea Grace'])

if __name__ == '__main__':
    unittest.main()
