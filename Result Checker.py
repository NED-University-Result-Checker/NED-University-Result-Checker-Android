def NED_result_checker():
    # for downloading file
    import urllib.request as download
    # for open in browser
    import webbrowser as wb

    # for getting request Module
    import requests
    # web scrapping moduel
    from bs4 import BeautifulSoup

    # for formatting
    from FormatText import FormatText

    # URL where all data is stored
    url_ned = 'https://www.neduet.edu.pk'
    url_exam = 'https://www.neduet.edu.pk/examination_results'
    # for getting request for page
    page = requests.get(url_exam)
    # soup will contain whole html file
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup) # its for printing whole xml file

    # searching Department
    find_fy = soup.find(
        'td', text='Computer Science & Info. Tech.').find_next_sibling('td')
    find_sy = find_fy.find_next_sibling('td')
    find_ty = find_sy.find_next_sibling('td')
    find_by = find_ty.find_next_sibling('td')
    # formatted text
    print(FormatText.blue+FormatText.bold+FormatText.underline +
          "NED Result Checker"+FormatText.end+"\n")
    if find_fy.text == '-':
        print('First Year result may not be uploaded.')
    else:
        print('First year result may be uploaded.')
        web_url = url_ned + find_sy.a.get('href')
        inp = input(
            '\nIf you want to see the file, pess 1 otherwise press enter: ')
        print()
        if inp == '1':
            wb.open_new_tab(web_url)
    print()
    if find_sy.text == '-':
        print('Second Year result may not be uploaded.')
    else:
        print('Second Year result may be uploaded.')
        web_url = url_ned + find_sy.a.get('href')
        inp = input(
            '\nIf you want to see the file, pess 1 otherwise press enter: ')
        print()
        if inp == '1':
            wb.open_new_tab(web_url)
            # for downloading
            download.urlretrieve(web_url, 'result.jpg')
    print()
    if find_ty.text == '-':
        print('Third year result may not be uploaded.')
    else:
        print('Third year result may be uploaded.')
        web_url = url_ned + find_sy.a.get('href')
        inp = input(
            '\nIf you want to see the file, pess 1 otherwise press enter: ')
        print()
        if inp == '1':
            wb.open_new_tab(web_url)
    print()
    if find_by.text == '-':
        print('Bachelor Year result may not be uploaded.')
    else:
        print('Bachelor Year result may be uploaded.')
        web_url = url_ned + find_sy.a.get('href')
        inp = input(
            '\nIf you want to see the file, pess 1 otherwise press enter: ')
        print()
        if inp == '1':
            wb.open_new_tab(web_url)


# main
NED_result_checker()
input()


# print(f'rohan')
##print("________Enter 'eng' for Engineering fields and 'sci' for Science fields_________")
##        inp1=input("Enter the field:")
# if inp1=="sci":
# fields_sci={'AC':'Architecture','AP':'Applied Physics','CF':'Computational Finance','DS':'Development Studies',\
# 'ECE':'Economics &amp; Finance','EL':'English Linguistics','EL':'English Linguistics','IC':'Industrial Chemistry',\
# 'MS':'Management Sciences','TS':'Textile Sciences'}
##                inp2=input("Enter the Engineering field code:")
##
# fields_engg={'AM':'Automotive Engg.','BE':'Bio-Medical Engg.','CH':'Chemical Engg.','CE':'Civil Engg.','CS':'Computer Systems Engg.',\
# 'CN':'Construction Engg.','EE':'Electrical Engg','EL':'Electronics Engg.','':'Food Engg.',\
# 'IM':'Industrial &amp; Manufacturing Engg','MM':'Materials Engg.','ME':'Mechanical Engg.','MT':'Metallurgical Engg.',\
# 'PE':'Petroleum Engg.','PP':'Polymer &amp; Petrochemical Engg.','SE':'Software Engg.',\
# 'TC':'Telecommunications Engg.','TE':'Textile Engg.','UE':'Urban Engg.'}
