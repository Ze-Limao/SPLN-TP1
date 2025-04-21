import spacy
from lxml import etree
import re

nlp = spacy.load("pt_core_news_lg")

CAMPOS_TEXTO = ["Repository", "UnitTitle", "Custom1", "ScopeContent", "BiogHist", "CustodHist"]

def get_texto(record, campo):
    ns = {'ns1': 'http://schemas.datacontract.org/2004/07/Data'}
    el = record.find(f'.//ns1:{campo}', namespaces=ns)
    return el.text.strip() if el is not None and el.text else ""

def obter_texto_dos_campos(record):
    return " ".join([get_texto(record, campo) for campo in CAMPOS_TEXTO])

def extrair_profissao(scope_content):
    #match = re.search(r'Profiss[aã]o\s*[-:]?\s*(.+)', scope_content, re.IGNORECASE)
    match = re.search(r'(?:Profiss[aã]o|Emprego)\s*[-:]?\s*(.+)', scope_content, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def main(xml_file='./../oai_records_aif/oai_records_aif_fm.xml'):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    ns = {'ns0': 'http://www.openarchives.org/OAI/2.0/'}
    records = root.findall('.//ns0:record', namespaces=ns)

    pessoas_com_profissao = set()
    pessoas_sem_profissao = set()
    lugares_encontrados = set()

    for record in records:
        texto_total = obter_texto_dos_campos(record)
        unit_title = get_texto(record, "UnitTitle")
        scope_content = get_texto(record, "ScopeContent")

        doc_tudo = nlp(texto_total)
        doc_titulo = nlp(unit_title)

        nomes_unit_title = {ent.text.strip() for ent in doc_titulo.ents if ent.label_ == "PER"}
        nomes_gerais = {ent.text.strip() for ent in doc_tudo.ents if ent.label_ == "PER"}
        lugares_encontrados.update(ent.text.strip() for ent in doc_tudo.ents if ent.label_ in ("LOC", "GPE"))

        profissao = extrair_profissao(scope_content)


        for nome in nomes_unit_title:
            if profissao:
                pessoas_com_profissao.add(f"{nome}: {profissao}")
            else:
                pessoas_sem_profissao.add(nome)

        for nome in nomes_gerais - nomes_unit_title:
            pessoas_sem_profissao.add(nome)

    with open("entidades.txt", "w", encoding="utf-8") as f:
        f.write("📋 Índice de Entidades Mencionadas\n\n")

        f.write("🔹 Pessoas com profissão:\n")
        if pessoas_com_profissao:
            for entrada in sorted(pessoas_com_profissao):
                f.write(f"  - {entrada}\n")
        else:
            f.write("  Nenhuma pessoa com profissão associada.\n")

        f.write("\n🔹 Outras pessoas:\n")
        restantes = pessoas_sem_profissao - {e.split(":")[0].strip() for e in pessoas_com_profissao}
        if restantes:
            for nome in sorted(restantes):
                f.write(f"  - {nome}!\n")
        else:
            f.write("  Nenhuma pessoa restante.\n")
        f.write("------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\n🔹 Lugares e Casas:\n")
        if lugares_encontrados:
            for lugar in sorted(lugares_encontrados):
                f.write(f"  - {lugar}!\n")
        else:
            f.write("  Nenhum lugar reconhecido.\n")

    print("✅ Entidades gravadas em 'entidades.txt'.")

if __name__ == "__main__":
    main()
