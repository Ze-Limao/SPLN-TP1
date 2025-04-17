import requests
import xml.etree.ElementTree as ET

def get_records(base_url, metadata_prefix="aif"):
    records = []
    resumption_token = None
    
    while True:
        if resumption_token:
            url = f"{base_url}?verb=ListRecords&resumptionToken={resumption_token}"
        else:
            url = f"{base_url}?verb=ListRecords&metadataPrefix={metadata_prefix}"
        
        response = requests.get(url)
        if response.status_code != 200:
            print("Erro ao acessar o repositório")
            break
        
        root = ET.fromstring(response.content)
        
        for record in root.findall(".//{http://www.openarchives.org/OAI/2.0/}record"):
            records.append(ET.tostring(record, encoding="unicode"))
        
        resumption_token_element = root.find(".//{http://www.openarchives.org/OAI/2.0/}resumptionToken")
        if resumption_token_element is not None and resumption_token_element.text:
            resumption_token = resumption_token_element.text
        else:
            break
    
    return records

def main():
    BASE_URL = "https://pesquisa-arquivo.cm-pontedelima.pt/OAI-PMH/"
    records = get_records(BASE_URL, metadata_prefix="aif") 
    
    with open("oai_records_aif.xml", "w", encoding="utf-8") as file:
        file.write("<OAI-PMH-Records>\n" + "\n".join(records) + "\n</OAI-PMH-Records>")
    
    print(f"{len(records)} registros foram encontrados e guardados em 'oai_records_aif.xml'")

if __name__ == "__main__":
    main()