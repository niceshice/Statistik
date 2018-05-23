from xml.etree import ElementTree as ET
from collections import Counter
import xlsxwriter

tree = ET.parse("AYL.xml")
root = tree.getroot()
personlist = root.findall('.//{http://www.tei-c.org/ns/1.0}person')
personlist = [x for x in personlist if x.find("{http://www.tei-c.org/ns/1.0}persName")]



def generatorparse(personlist):
    """Generatorfunktion über die iteriert werden kann;
    nimmt eine Liste aus Elementen entgegen und returned ein Tuple aus (name, sex)"""
    for x in personlist:
        name = x.find(".//{http://www.tei-c.org/ns/1.0}name").text.lower()
        sex = x.find(".//{http://www.tei-c.org/ns/1.0}sex").text.lower()
        yield (name, sex)
        
def speaktimes (root):
    """Erhält die root und returned dann ein Counter-dict, mit name : sprechzahlen Werten. 
    """
    allspeakers = [x.text.lower() for x in root.findall(".//{http://www.tei-c.org/ns/1.0}speaker/{http://www.tei-c.org/ns/1.0}w")]
    speakers = Counter(allspeakers)
    return speakers


def combine(speakcount, persons):
    """Kombiniert das Counter-dict und die Tuple aus generatorparse()
    returned eine Liste final, die Tuple mit (name, sex, speakcount) enthält. Wenn der Name nicht richtig gefunden wurde, wird 
    'speakcount not found' im Tuple gespeichert und muss dann von Hand eingefügt werden."""
    final = []
    for person in persons:
        name, sex = person
        if name in speakcount:
            final.append((name, sex, speakcount[name]))
        else: 
            final.append((name, sex, "speakcount not found!"))
    return final
print(personlist)

persons = [ x for x in generatorparse(personlist) if x]
speakcount = speaktimes(root)
final = combine(speakcount, persons)
print(persons)
print(speakcount)
print(final)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('AYLSpeakerData.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 1
col = 0
idnr = 0 

worksheet.write(0, 0,"ID")
worksheet.write(0, 1, "label")
worksheet.write(0, 2, "gender")
worksheet.write(0, 3, "per_ms_sps")
worksheet.write(0, 4, "role")
worksheet.write(0, 5, "importance")

# Iterate over the data and write it out row by row.
for name, sex, speakcount in final:
    worksheet.write(row, col, idnr)
    worksheet.write(row, col + 1, name)
    worksheet.write(row, col + 2, sex)
    worksheet.write(row, col + 3, speakcount)
    idnr += 1
    row += 1
workbook.close()