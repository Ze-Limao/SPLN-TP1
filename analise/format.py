import yaml
from lxml import etree


def load_yaml_config(config_path='config.yaml'):
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def formatar_periodo(data_inicio, data_fim, certeza_inicio, certeza_fim):
    if certeza_inicio == "true" and certeza_fim == "true":
        return f"{data_inicio} - {data_fim}"
    elif certeza_inicio == "false" and certeza_fim == "false":
        return f"{data_inicio} (incerta) - {data_fim} (incerta)"
    elif certeza_inicio == "true":
        return f"{data_inicio} - {data_fim} (incerta)"
    elif certeza_fim == "true":
        return f"{data_inicio} (incerta) - {data_fim}"
    else:
        return "N/A"


def gerar_conteudo_html(records, config):
    """Gera o conteúdo HTML a partir dos registros e configuração"""
    html_content = "<html><head><title>Registos</title></head><body>"
    html_content += "<h1>Lista de Registos</h1>"

    for record in records[:5]:
        html_content += "<div style='margin-bottom: 30px;'>"
        html_content += "<table border='1' cellpadding='10'>"

        # Inicializa as variáveis antes de usá-las
        data_inicio = "N/A"
        data_fim = "N/A"
        certeza_inicio = "false"  # valor padrão
        certeza_fim = "false"  # valor padrão

        for field in config['fields']:
            field_name = field['name']
            label = field['label']
            xpath_expr = f'.//ns1:{field_name}'
            field_value = record.xpath(xpath_expr, namespaces={'ns1': 'http://schemas.datacontract.org/2004/07/Data'})

            # Processar valores para campos de data
            if field_name == "UnitDateInitial":
                data_inicio = field_value[0].text if field_value else None
            elif field_name == "UnitDateFinal":
                data_fim = field_value[0].text if field_value else None
            elif field_name == "UnitDateInitialCertainty":
                certeza_inicio = field_value[0].text if field_value else "false"
            elif field_name == "UnitDateFinalCertainty":
                certeza_fim = field_value[0].text if field_value else "false"
            else:
                # Para outros campos, obtemos o valor ou "N/A" se não existir
                field_value = field_value[0].text if field_value else "N/A"

            # Exibe o valor da data formatada
            if field_name == "UnitDatePeriod":
                # Formata as datas em um único campo
                field_value = formatar_periodo(data_inicio, data_fim, certeza_inicio, certeza_fim)

            if field_name not in ["UnitDateInitial", "UnitDateFinal"]:
                html_content += f"<tr><td><strong>{label}:</strong></td><td>{field_value}</td></tr>"

        html_content += "</table>"
        html_content += "</div>"

    html_content += "</body></html>"
    return html_content


def prettyprint_html(xml_file, output_file='output.html', config_file='config.yaml'):
    """Gera e salva o HTML com os registros formatados a partir do XML e da configuração YAML"""
    # Carrega a configuração do arquivo YAML
    config = load_yaml_config(config_file)
    
    # Parse do XML
    tree = etree.parse(xml_file)
    root = tree.getroot()
    
    # Encontra todos os registros no XML
    records = root.findall('.//ns0:record', namespaces={'ns0': 'http://www.openarchives.org/OAI/2.0/'})
    
    # Gera o conteúdo HTML com base nos registros e na configuração
    html_content = gerar_conteudo_html(records, config)
    
    # Salva o conteúdo gerado no arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)


# Chamada da função para gerar o HTML com base no XML e na configuração
prettyprint_html('oai_records_aif_fm.xml', 'output.html', 'config.yaml')
