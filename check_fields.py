from lxml import etree
from collections import defaultdict

def verificar_campos_constantes(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    campos = defaultdict(set)

    records = root.xpath("//ns0:record", namespaces={'ns0': 'http://www.openarchives.org/OAI/2.0/', 'ns1': 'http://schemas.datacontract.org/2004/07/Data'})

    for record in records:
        for elem in record.iter():
            tag = elem.tag.split('}')[1]
            value = elem.text.strip() if elem.text else None
            campos[tag].add(value)

    print("Campos encontrados:")
    #for tag, values in campos.items():
    #   print(f"{tag}: {values.pop()}")
    for tag in campos.keys():
        print(tag)
        
xml_file = "./oai_records_aif/oai_records_aif_fm.xml"
verificar_campos_constantes(xml_file)
