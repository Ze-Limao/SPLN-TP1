#!/usr/bin/python3
from xmldt import XmlDt, toxml
import sys


class proc (XmlDt):
    _types_ = {"item":"map"}

    def __default__(s, e): 
        return f"{e.c}"
    # @XmlDt.dt_tag("OAI-PMH-Records")
    # def OAI_PMH_Records(s, e):   # 1 
    # def record(s, e):   # 49626 
    #def header(s, e):   # 49626 
    #
    #def identifier(s, e):   # 49626  PCDATA
    #
    # def datestamp(s, e):   # 49626  PCDATA
    # def setSpec(s, e):   # 77849  PCDATA
    # def metadata(s, e):   # 49626 
    # def DescriptionItem(s, e):   # 49626 
    # def AllowExtentsInference(s, e):   # 49626  PCDATA
    # def AllowUnitDatesInference(s, e):   # 49626  PCDATA
    # def ID(s, e):   # 49626  PCDATA
    # def Parent(s, e):   # 49626  PCDATA
    # def RootParent(s, e):   # 49626  PCDATA
    # def AllowAddDescendants(s, e):   # 49626  PCDATA
    # def AllowTextualContentInference(s, e):   # 49626  PCDATA
    # def Barcode(s, e):   # 49626  PCDATA
    # def CompleteUnitId(s, e):   # 49626  PCDATA
    # def CountryCode(s, e):   # 49626  PCDATA
    # def DescriptionLevel(s, e):   # 49626  PCDATA
    # def HasAudiovisualRecord(s, e):   # 49626  PCDATA
    # def HasDigitalRepresentation(s, e):   # 49626  PCDATA
    # def HasPublishedFiles(s, e):   # 49626  PCDATA
    # def Repository(s, e):   # 47181  PCDATA
    # def RepositoryCode(s, e):   # 49626  PCDATA
    # def UnitDateFinal(s, e):   # 48478  PCDATA
    # def UnitDateFinalCertainty(s, e):   # 49626  PCDATA
    # def UnitDateInitial(s, e):   # 48484  PCDATA
    # def UnitDateInitialCertainty(s, e):   # 49626  PCDATA
    # def UnitId(s, e):   # 49626  PCDATA
    # def UnitTitle(s, e):   # 49626  PCDATA
    # def UnitTitleType(s, e):   # 46426  PCDATA
    # def Dimensions(s, e):   # 47221  PCDATA
    # def LangMaterial(s, e):   # 47937  PCDATA
    # def PhysLoc(s, e):   # 45095  PCDATA
    # def Producer(s, e):   # 48824  PCDATA
    # def RetentionDisposalFinalDestination(s, e):   # 36971  PCDATA
    # def ScopeContent(s, e):   # 47420  PCDATA
    # def IdentifierUrl(s, e):   # 49626  PCDATA
    # def PhysTech(s, e):   # 28353  PCDATA
    # def PreviousLoc(s, e):   # 10320  PCDATA
    # def media(s, e):   # 28223 type(28223) PCDATA
    # def InternalStructure(s, e):   # 197  PCDATA
    # def BiogHist(s, e):   # 413  PCDATA
    # def RelatedMaterial(s, e):   # 1781  PCDATA
    # def Terms(s, e):   # 20966  PCDATA
    # def UnitDateNotes(s, e):   # 11519  PCDATA
    # def DocumentalTradition(s, e):   # 664  PCDATA
    # def OriginalNumbering(s, e):   # 8  PCDATA
    # def BibliographyItems(s, e):   # 205  PCDATA
    # def AcqInfo(s, e):   # 314  PCDATA
    # def Arrangement(s, e):   # 997  PCDATA
    # def OtherFindAid(s, e):   # 250  PCDATA
    # def LegalStatus(s, e):   # 1  PCDATA
    # def AlternativeTitle(s, e):   # 31  PCDATA
    # def Functions(s, e):   # 17  PCDATA
    # def GeneralContext(s, e):   # 3  PCDATA
    # def AccessRestrict(s, e):   # 140  PCDATA
    # def UseRestrict(s, e):   # 131  PCDATA
    # def Stamps(s, e):   # 14  PCDATA
    # def Marks(s, e):   # 1  PCDATA
    # def AltFormAvail(s, e):   # 11  PCDATA
    # def OriginalsLoc(s, e):   # 71  PCDATA
    # def Accruals(s, e):   # 3  PCDATA
    # def Appraisal(s, e):   # 7  PCDATA
    # def UnitDateBulk(s, e):   # 1035  PCDATA
    # def CustodHist(s, e):   # 11  PCDATA
    # def Custom1(s, e):   # 4234  PCDATA
    # def AccumulationDates(s, e):   # 3  PCDATA

file = sys.argv[1]
print(proc(filename=file))    # , empty=True

