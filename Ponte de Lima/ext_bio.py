from lxml import etree

def get_texto(record, campo):
    ns = {'ns1': 'http://schemas.datacontract.org/2004/07/Data'}
    el = record.find(f'.//ns1:{campo}', namespaces=ns)
    return el.text.strip() if el is not None and el.text else None

def main(xml_file='./../oai_records_aif/oai_records_aif_pl.xml'):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    ns = {'ns0': 'http://www.openarchives.org/OAI/2.0/'}
    records = root.findall('.//ns0:record', namespaces=ns)

    biografias = []

    for record in records:
        nome = get_texto(record, "UnitTitle")
        biog = get_texto(record, "BiogHist")

        if nome and biog:
            # Remove quebras de linha da biografia
            biog_limpa = " ".join(biog.strip().splitlines())
            biografias.append((nome.strip(), biog_limpa))

    with open("biografias.md", "w", encoding="utf-8") as f:
        f.write("| Nome | Biografia |\n")
        f.write("|------|-----------|\n")
        for nome, bio in biografias:
            f.write(f"| {nome} | {bio} |\n")

    print("✅ Biografias gravadas em 'biografias.md'.")

if __name__ == "__main__":
    main()
