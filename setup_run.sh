#!/bin/bash

# Verifica se o Python 3 está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python 3 não está instalado. Instalando Python 3..."
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip
else
    echo "Python 3 já está instalado."
fi

# Cria um ambiente virtual
echo "Criando um ambiente virtual..."
python3 -m venv myenv

# Ativa o ambiente virtual
echo "Ativando o ambiente virtual..."
source myenv/bin/activate

# Instala o boto3 no ambiente virtual
echo "Instalando boto3..."
pip install boto3

# Executa o script Python
echo "Executando o script Python..."
python3 create_table.py

# Desativa o ambiente virtual após a execução do script
deactivate
echo "Script concluído."
