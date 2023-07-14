import shutil
from bs4 import BeautifulSoup

create_simulation = input("新しくシミュレーションを作成しますか？（y/n）")
if create_simulation:
    simulation_name = input("作成するシミュレーションの名前を入力してください：")
    template_folder = 'developfile/template'
    folder_name = 'public/simulations/'+simulation_name
    shutil.copytree(template_folder, folder_name)
    with open(folder_name+'/index.html', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    title_elem = soup.title
    title_elem.append(simulation_name)
    span_elem = soup.find('span', attrs={'class': 'simulation-title-content'})
    span_elem.append(simulation_name)
    soup = str(soup)
    with open(folder_name+'/index.html', encoding='utf-8', mode="w") as f:
        f.writelines(soup)
        f.close()
