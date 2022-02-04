import webbrowser
from datetime import datetime
from tkinter import messagebox
import tkinter as tk
import colorama
from colorama import Fore
from colorama import Style
from time import sleep

colorama.init()
window = tk.Tk()
window.wm_withdraw()

class ClassManager:
    def __init__(self, url):
        self.url = url

    # Driver
    def driver(self):
        webbrowser.open(self.url, 0)

    def alert_message(self, message):
        messagebox.showinfo("",message)


if __name__ == "__main__":
    print(Fore.GREEN+'CLASSMANAGER WORKS SUCESSFULY'+Style.RESET_ALL)
    verify = 0
    c = 1
    while c < 2:
            hours = int(f"{datetime.now(): %H}") 	
            minutes = int(f"{datetime.now(): %M}")
            # SEGUNDA-FEIRA 
            # AULA DE PROGRMAÇÃO PARA INTERNET I
            if datetime.today().weekday() == 7: #(SEGUNDA)
                if hours >= 19 and minutes <= 30:
                    if verify == 0: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Programação\npara Internet I")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 1
                        print(Fore.GREEN+'AULA ACESSADA COM SUCESSO'+Style.RESET_ALL)
                    else:
                        print(Fore.RED+'NAO FOI POSSIVEL ACESSAR A AULA'+Style.RESET_ALL)
                        sleep(10)
                        break
            # TERCA-FEIRA
            # PROBABILIDADE E ESTATÍSITICA E PROG. P/ INTERNET
            elif datetime.today().weekday() == 1: #(TERÇA)
                if hours >= 19 and minutes <= 30:
                    if verify == 0: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Probabilidade e Estatística")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 1
                if hours >= 20 and minutes <= 59: # 20:30
                    if verify == 1: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Programação\npara Internet I")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 2
                        print(Fore.GREEN+'AULA ACESSADA COM SUCESSO'+Style.RESET_ALL)
                    else:
                        print(Fore.RED+'NAO FOI POSSIVEL ACESSAR A AULA'+Style.RESET_ALL)
                        sleep(10)
                        break
            # QUARTA FEIRA
            # INGLÊS III E ESTRUTURA DE DADOS
            elif datetime.today().weekday() == 2: #(QUARTA)
                if hours >= 19 and minutes <= 30:
                    if verify == 0: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Inglês")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 1
                        print(Fore.GREEN+'AULA ACESSADA COM SUCESSO'+Style.RESET_ALL)
                if hours >= 20 and minutes <= 59: # 20:30
                    if verify == 1: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Estrutura de dados")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 2
                        print(Fore.GREEN+'AULA ACESSADA COM SUCESSO'+Style.RESET_ALL)
                    else:
                        print(Fore.RED+'NAO FOI POSSIVEL ACESSAR A AULA'+Style.RESET_ALL)
                        sleep(10)
                        break
            # QUINTA-FEIRA
            # AULA DE ESTRUTURA DE DADOS
            elif datetime.today().weekday() ==3: #(QUINTA)
                if hours >= 19 and minutes <= 30:
                    if verify == 0: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Estrutura de Dados")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 1
                        print(Fore.GREEN+'AULA ACESSADA COM SUCESSO'+Style.RESET_ALL)
                    else:
                        print(Fore.RED+'NAO FOI POSSIVEL ACESSAR A AULA'+Style.RESET_ALL)
                        sleep(10)
                        break
            # SEXTA-FEIRA
            # TESTE DE SOFTWARE I E METODOLOGIA DE PESQUISA APLICADA A COMPUTAÇÃO
            elif datetime.today().weekday() == 4: #(SEXTA)
                if hours >= 19 and minutes <= 30:
                    if verify == 0: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Teste de Software")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 1
                        print(Fore.GREEN+'AULA ACESSADA COM SUCESSO'+Style.RESET_ALL)
                if hours >= 20 and minutes <= 59: # 20:30
                    if verify == 1: # VERIFICA SE JA ENTROU NA AULA
                        url = "" 
                        classr = ClassManager(url)
                        classr.alert_message("Você tem aula de Metodologia\ndepesquisa aplicada a computação")
                        classr.driver() # ENTRANDO NO CLASSROOM 
                        verify += 2
                        print(Fore.GREEN+'AULA ACESSADA COM SUCESSO'+Style.RESET_ALL)
                    else:
                        print(Fore.RED+'NAO FOI POSSIVEL ACESSAR A AULA'+Style.RESET_ALL)
                        sleep(10)
                        break
            # SABADO
            elif datetime.today().weekday() == 5: #(SABADO)
                break
            # DOMINGO
            elif datetime.today().weekday() == 6: #(DOMINGO)
                break