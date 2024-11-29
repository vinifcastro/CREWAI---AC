#!/usr/bin/env python
import sys
import warnings

from escolhe_cpu.crew import EscolheCpu

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'consumo_energia': 'Baixo',
        'desempenho': 'Médio',
        'custo_maximo': '1200 reais',
        'tipo_aplicacao': 'Programar em C'
    }
    EscolheCpu().crew().kickoff(inputs=inputs)