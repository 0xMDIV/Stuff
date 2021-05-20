import xml.etree.ElementTree as ET
file = '/home/sheepard/Downloads/sitemap.xml'
save_file = '/home/sheepard/Documents/codearchive.txt'

tree = ET.parse(file)
root = tree.getroot()
archive_list = []

for node in tree.findall('.//url/loc'):
    if '?p=' in node.text:
        url = node.text.split('?p=')
        dl_link = f'https://codeplexarchive.blob.core.windows.net/archive/projects/{url[1]}/{url[1]}.zip\n'
        archive_list.append(dl_link)

with open(save_file, 'w') as sf:
    for link in archive_list:
        sf.write(link)

    sf.close()
