from lxml import etree
from collections import defaultdict
import os

NIVEIS = {
    "F": "F", 
    "SC": "SC", 
    "SSC": "SSC",
    "SR": "SR", 
    "UI": "UI", 
    "D": "DC", 
    "DC": "DC"
}

#def get(field):
#        el = record.find(f'.//ns1:{field}', namespaces=ns)
#        return el.text.strip() if el is not None and el.text else None

def obter_info2(record):

    ns = {'ns1': 'http://schemas.datacontract.org/2004/07/Data'}

    def get(field):
        el = record.find(f'.//ns1:{field}', namespaces=ns)
        return el.text.strip() if el is not None and el.text else None
    
    id_ = get("ID")
    parent = get("Parent")
    title = get("UnitTitle")
    level = get("DescriptionLevel") or "DC"
    tipo = NIVEIS.get(level, level)

    dados = {field: get(field) for field in [
    "ID", "Parent", "RootParent", "UnitTitle", "DescriptionLevel",
    "UnitDateInitial", "UnitDateFinal", "ScopeContent", "Repository", "Barcode",
    "LangMaterial", "PhysLoc", "AccessRestrict", "UseRestrict", "IdentifierUrl",
    "BiogHist", "CustodHist"  
]}
    return id_, parent, title, tipo, dados

def construir_arvore2(records):
    nos = {}
    filhos = defaultdict(list)
    for record in records:
        id_, parent, title, tipo, dados = obter_info2(record)
        if not id_:
            continue
        nos[id_] = {"id": id_, "parent": parent, "title": title, "tipo": tipo, "dados": dados}
        filhos[parent].append(id_)
    return nos, filhos

def gerar_pagina_html(nodo, filhos_ids, nos, output_dir):
    id_ = nodo["id"]
    dados = nodo["dados"]
    title = dados.get("UnitTitle", "Sem título")
    tipo = nodo["tipo"]

    html = f"<html><head><meta charset='utf-8'><title>{title}</title></head><body>"
    html += f"<h1>{id_} - {tipo} - {title}</h1><ul>"
    
    for chave, valor in dados.items():
        if chave != "ID" and valor:
            html += f"<li><strong>{chave}:</strong> {valor}</li>"
    html += "</ul>"

    # Links para os filhos
    if filhos_ids:
        html += "<h2>Filhos:</h2><ul>"
        for filho_id in filhos_ids:
            filho = nos[filho_id]
            link = f"{filho_id}.html"
            html += f"<li><a href='{link}'>{filho_id} - {filho['tipo']} - {filho['title']}</a></li>"
        html += "</ul>"

    html += "</body></html>"

    with open(os.path.join(output_dir, f"{id_}.html"), "w", encoding="utf-8") as f:
        f.write(html)
'''
def gerar_pagina_wiki(nodo, filhos_ids, nos, output_dir):
    id_ = nodo["id"]
    dados = nodo["dados"]
    title = dados.get("UnitTitle", "Sem título")
    tipo = nodo["tipo"]

    linhas = [f"====== {id_} - {tipo} - {title} ======\n"]

    for chave, valor in dados.items():
        if chave != "ID" and valor:
            linhas.append(f"**{chave}**:: {valor}")

    if filhos_ids:
        linhas.append("\n===== Filhos =====")
        for filho_id in filhos_ids:
            filho = nos[filho_id]
            linhas.append(f"  * [[{filho_id}.txt|{filho_id} - {filho['tipo']} - {filho['title']}]]")

    with open(os.path.join(output_dir, f"{id_}.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))
'''

def gerar_pagina_html(nodo, filhos_ids, nos, output_dir):
    id_ = nodo["id"]
    dados = nodo["dados"]
    title = dados.get("UnitTitle", "Sem título")
    tipo = nodo["tipo"]

    html = f"<html><head><meta charset='utf-8'><title>{title}</title></head><body>"
    html += f"<h1>{title}</h1><ul>"  # Só o título, sem ID nem tipo

    # Campos que queres manter:
    campos_mostrar = ["Parent", "DescriptionLevel", "Repository", "ScopeContent", "BiogHist", "CustodHist"]

    for chave in campos_mostrar:
        valor = dados.get(chave)
        if valor:
            html += f"<li><strong>{chave}:</strong> {valor}</li>"
    html += "</ul>"

    if filhos_ids:
        html += "<h2>Filhos:</h2><ul>"
        for filho_id in filhos_ids:
            filho = nos[filho_id]
            link = f"{filho_id}.html"
            html += f"<li><a href='{link}'>{filho['title']}</a></li>"
        html += "</ul>"

    html += "</body></html>"

    with open(os.path.join(output_dir, f"{id_}.html"), "w", encoding="utf-8") as f:
        f.write(html)

def gerar_index_html(nos, filhos, raizes, output_path):
    def gerar_html_lista(id_, depth=0):
        nodo = nos.get(id_)
        if not nodo:
            return ""
        indent = "  " * depth
        linha = f'{indent}<li><a href="{id_}.html">{id_} - {nodo["tipo"]} - {nodo["title"]}</a>'
        filhos_html = "".join([gerar_html_lista(f, depth + 1) for f in sorted(filhos.get(id_, []))])
        if filhos_html:
            linha += f"\n{indent}<ul>\n{filhos_html}\n{indent}</ul>"
        linha += "</li>\n"
        return linha

    html = "<html><head><meta charset='utf-8'><title>Índice</title></head><body>"
    html += "<h1>Árvore Arquivística</h1><ul>"

    for raiz in raizes:
        html += gerar_html_lista(raiz)

    html += "</ul></body></html>"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

def main(xml_file='./../oai_records_aif/oai_records_aif_pl.xml'):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    records = root.findall('.//ns0:record', namespaces={'ns0': 'http://www.openarchives.org/OAI/2.0/'})
    
    nos, filhos = construir_arvore2(records)
    raizes = [id_ for id_, nodo in nos.items() if nodo["parent"] == id_ or nodo["parent"] not in nos]

    os.makedirs("saida/wiki", exist_ok=True)
    os.makedirs("saida/html", exist_ok=True)

    for id_, nodo in nos.items():
        filhos_ids = filhos.get(id_, [])
        #gerar_pagina_wiki(nodo, filhos_ids, nos, "saida/wiki")
        gerar_pagina_html(nodo, filhos_ids, nos, "saida/html")

    gerar_index_html(nos, filhos, raizes, "saida/html/01_index.html")

    print("Exportação completa: HTML e Wiki gerados em 'saida/'")

if __name__ == "__main__":
    main()
