from lxml import etree
from collections import defaultdict
import os

# Mapas de níveis arquivísticos para abreviações
NIVEIS = {
    "F": "F",
    "SC": "SC",
    "SSC": "SSC",
    "SR": "SR",
    "UI": "UI",
    "D": "DC",
    "DC": "DC",
}

def get_field(field):
    el = record.find(f'.//ns1:{field}', namespaces=ns)
    return el.text.strip() if el is not None and el.text else None

def obter_info_nodo(record):
    ns = {'ns1': 'http://schemas.datacontract.org/2004/07/Data'}
    
    id_ = get_field("ID")
    parent = get_field("Parent")
    title = get_field("UnitTitle")
    level = get_field("DescriptionLevel") or "DC"
    
    tipo = NIVEIS.get_field(level, level)  # Usa DC como default
    return id_, parent, title, tipo

def construir_arvore(records):
    nos = {}
    filhos = defaultdict(list)
    
    for record in records:
        id_, parent, title, tipo = obter_info_nodo(record)
        if not id_:
            continue
        nos[id_] = {"id": id_, "parent": parent, "title": title, "tipo": tipo}
        filhos[parent].append(id_)
    
    return nos, filhos

def imprimir_arvore(nos, filhos, raiz, indent=0, lines=None):
    if lines is None:
        lines = []
    nodo = nos.get(raiz)
    if not nodo:
        return lines
    linha = "  " * indent + f"{nodo['id']}-{nodo['tipo']}-{nodo['title']}"
    lines.append(linha)
    for filho in sorted(filhos.get(raiz, [])):
        imprimir_arvore(nos, filhos, filho, indent + 1, lines)
    return lines

def main(xml_file="./../oai_records_aif/oai_records_aif_fm.xml", output_txt='arq_tree.txt'):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    records = root.findall('.//ns0:record', namespaces={'ns0': 'http://www.openarchives.org/OAI/2.0/'})
    
    nos, filhos = construir_arvore(records)

    # Encontra raízes (nós sem pai ou com Parent == ID)
    raizes = [id_ for id_, nodo in nos.items() if nodo["parent"] == id_ or nodo["parent"] not in nos]

    with open(output_txt, 'w', encoding='utf-8') as f:
        for raiz in raizes:
            linhas = imprimir_arvore(nos, filhos, raiz)
            f.write("\n".join(linhas))
            f.write("\n\n")

    print(f"Árvore guardada em '{output_txt}'")

if __name__ == "__main__":
    main()
