from lxml import etree
from collections import defaultdict

def get_text(record, campo):
    ns = {'ns1': 'http://schemas.datacontract.org/2004/07/Data'}
    el = record.find(f".//ns1:{campo}", namespaces=ns)
    return el.text.strip() if el is not None and el.text else None

def main(xml_file="./../oai_records_aif/oai_records_aif_pl.xml"):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    records = root.findall(".//ns0:record", namespaces={'ns0': 'http://www.openarchives.org/OAI/2.0/'})

    temas = defaultdict(list)

    for record in records:
        termo = get_text(record, "Terms")
        titulo = get_text(record, "UnitTitle")

        if termo and titulo:
            temas[termo].append(titulo)

    with open("tabela_temas.txt.txt", "w", encoding="utf-8") as f:
        f.write("📚 Thesaurus/indices por temas\n\n")
        for termo, titulos in temas.items():
            f.write(f"{termo}:\n")
            for titulo in titulos:
                f.write(f"  - {titulo}\n")
            f.write("\n")

    print("✅ Temas gravados em 'tabela_temas.txt'.")

if __name__ == "__main__":
    main()
