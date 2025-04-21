import os
from lxml import etree

def procurar_em_html(wordi, pasta='saida/html'):
    print(f"\n🔎 A procurar por '{wordi}' nos ficheiros HTML...\n")
    encontrados = []

    for ficheiro in os.listdir(pasta):
        if ficheiro.endswith(".html"):
            caminho = os.path.join(pasta, ficheiro)
            with open(caminho, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                if wordi.lower() in conteudo.lower():
                    encontrados.append(ficheiro)

    if encontrados:
        print("📄 wordi encontrado nas seguintes páginas HTML:")
        for ficheiro in encontrados:
            print(f"  - {ficheiro}")
    else:
        print("❌ Nenhuma ocorrência encontrada nos HTML.")

def procurar_em_xml(wordi, xml_file='./../oai_records_aif/oai_records_aif_pl.xml'):
    print(f"\n🔎 A procurar por '{wordi}' nos registos XML...\n")
    tree = etree.parse(xml_file)
    root = tree.getroot()

    ns = {'ns0': 'http://www.openarchives.org/OAI/2.0/',
          'ns1': 'http://schemas.datacontract.org/2004/07/Data'}

    encontrados = []

    records = root.findall('.//ns0:record', namespaces=ns)
    for record in records:
        id_el = record.find('.//ns1:ID', namespaces=ns)
        id_ = id_el.text if id_el is not None else "Sem ID"

        texto = etree.tostring(record, encoding='unicode', method='text')
        if wordi.lower() in texto.lower():
            encontrados.append(id_)

    if encontrados:
        print("🧾 wordi encontrado nos seguintes registos (IDs):")
        for id_ in encontrados:
            print(f"  - {id_}")
    else:
        print("❌ Nenhuma ocorrência encontrada no XML.")

def main():
    wordi = input("🔍 Introduz o wordi a procurar: ").strip()
    if not wordi:
        print("⚠️ wordi vazio, abortado.")
        return

    escolha = input("📂 Procurar em (1) HTML ou (2) XML? ").strip()

    if escolha == "1":
        procurar_em_html(wordi)
    elif escolha == "2":
        procurar_em_xml(wordi)
    else:
        print("❌ Opção inválida. Usa 1 para HTML ou 2 para XML.")

if __name__ == "__main__":
    main()
