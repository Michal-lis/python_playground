import os
import xml.etree.ElementTree as ET
import pandas as pd
from pprint import pprint

# assumption: XML files are located in the subfolder named "data"
base_path = os.path.dirname(os.path.realpath(__file__))
xml_file_path = os.path.join(base_path, "data\\sample_an.xml")

my_data = []
tree = ET.parse(xml_file_path)
root = tree.getroot()
for r in root.find('M2I_Answer').find('Rubryka').find('Wpisy').findall('Wpis'):
    input_data = []
    record = r.find('Wpis')
    names = record.findall('.//p[@Symbol="Imiona"]')
    input_data.append(names[0].text) if names else input_data.append('')
    input_data.append(record.findall('.//p[@Symbol="NazwiskoNazwaFirma"]')[0].text)
    associate_shares = record.findall('.//p[@Symbol="UdzialyWspolnika"]')[0]
    input_data.append(float(associate_shares.get('Liczba')))
    input_data.append(float(associate_shares.get('Wartosc')))
    my_data.append(input_data)
pprint(my_data)
my_data_frame = pd.DataFrame(my_data, columns=['Imię', 'Nazwisko', 'Liczba udziałów', 'Wartość udziałów'])

print(my_data_frame)
print("\nLiczba udziałowców: ", my_data_frame.shape[0])
share_value = my_data_frame['Wartość udziałów'].sum()
print("Łaczna wartość udziałów: ", share_value)
print("Łaczna wartość udziałów: ", my_data_frame['Liczba udziałów'].sum())
ps = my_data_frame.groupby("Nazwisko").agg({'Wartość udziałów': lambda x: x / share_value})
ps.columns = ['Jaką część udziałów całości posiada']
print(ps)