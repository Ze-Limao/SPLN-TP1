Cada <record> tem:
    <ns0> == {http://www.openarchives.org/OAI/2.0/}  Coisas do protocolo OAI-PMH
    <ns1> == {http://schemas.datacontract.org/2004/07/Data}  Coisas da metadata

## Estrutura
Campos encontrados:
record
header
identifier
datestamp
setSpec
metadata
DescriptionItem
------
ID
Parent
RootParent
Barcode
CompleteUnitId
CountryCode
DescriptionLevel
HasAudiovisualRecord
HasDigitalRepresentation
Repository
RepositoryCode
UnitDateFinal
UnitDateFinalCertainty
UnitDateInitial
UnitDateInitialCertainty
UnitId
UnitTitle
UnitTitleType
AccessRestrict
Dimensions
LangMaterial
OtherFindAid
PhysLoc
PhysTech
ScopeContent
UseRestrict
media
IdentifierUrl
Arrangement
OriginalNumbering
Terms
Custom1
Author
PreviousLoc
AcqInfo
BiogHist
CustodHist
GeogName
Producer
AlternativeTitle
RetentionDisposalDocumentState
InternalStructure
Functions
RelatedMaterial
RepositoryArchivalHolding
UnitDateNotes
AccumulationDates
Signatures
OriginalsLoc
DocumentalTradition

### Campos constantes encontrados (com valores fixos):
CountryCode: PT
HasAudiovisualRecord: false
RepositoryCode: MVNF
UnitDateFinalCertainty: false
UnitDateInitialCertainty: false
Author: ,  /
Producer: ,  /
RetentionDisposalDocumentState: Em arquivo
Functions: Vida e obra do 2º Visconde de Pindela ver https://albertosampaioarquivo.wordpress.com/
RelatedMaterial: [PT/MVNF/ACP/14ª GERAÇÃO-1.1-1.1.7/001/0204/000015]
RepositoryArchivalHolding: ,  /
OriginalsLoc: Ministério das Obras Públicas. Repartição Técnica.
DocumentalTradition: Cópia

### Chaves 
#### Chaves primárias
- ns0:identifier
- ns1:ID
####
- ns1:Parent
- ns1:RootParent


## (Notas adicionais):
#### ResumptionTokens
Os resumptionTokens são uma funcionalidade do protocolo OAI-PMH usada para paginar resultados quando se faz harvesting de grandes conjuntos de metadados.
Quando pedes muitos registos de uma só vez, o servidor pode não te enviar todos de uma vez. Em vez disso, ele devolve:
    Um conjunto parcial dos resultados.
    Um resumptionToken — que é uma espécie de "marcador de posição".

