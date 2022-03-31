from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
from selenium.common.exceptions import NoSuchElementException
import os
import keyboard

root = Tk()
file = open("Input3.txt","a+")
adat = open('valaszokDorinaSzervezetivaltozas.txt','a+')
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://portal.kgk.uni-obuda.hu/vizsga/index.php')
#webpage login
link = driver.find_element_by_link_text("Belépés")
link.click()
time.sleep(1)
link2 = driver.find_element_by_name("remember")
link2.click()
link2.send_keys(Keys.RETURN)
#neptun login
neptun_belepes = driver.find_element_by_name("username")
neptun_belepes.send_keys("username")
neptun_belepes.send_keys(Keys.RETURN)
neptun_belepes2 = driver.find_element_by_name("password")
neptun_belepes2.send_keys("password")
neptun_belepes2.send_keys(Keys.RETURN)
elfogad_btn = driver.find_element_by_name("yes")
elfogad_btn.click()
time.sleep(2)

#Eksöli a teszt megkezdése

for x in range(100):
    if(keyboard.is_pressed('space')):
        exit()
    else:
        driver.get('https://portal.kgk.uni-obuda.hu/vizsga/index.php?do=exercise&id=72')
        #time.sleep(3)
        #TESZT VALASZ 1-re
        for e in range (2):
            kerdes = driver.find_element_by_class_name("kkerdes").text
            quest = kerdes[4:]
            kvalasz1 = driver.find_element_by_class_name("kvalasz1").text
            kvalasz2 = driver.find_element_by_class_name("kvalasz2").text
            kvalasz3 = driver.find_element_by_class_name("kvalasz3").text
            kvalasz4 = driver.find_element_by_class_name("kvalasz4").text
            adat = open('valaszokDorinaSzervezetivaltozas.txt','r')
            list = [(line.strip()).split('#') for line in adat]
            adat.close()
            #print(list)
            for u in range(len(list)):
                ask =''.join(list[u])
                quest =''.join(quest)
                print(ask)
                print('#######')
                if (ask == quest):
                    print("OOOOOOOO")
                    str1=''.join(list[u+1])
                    if (kvalasz1 == str1):
                        elkuld2 = driver.find_element_by_class_name("kvalasz1")
                        elkuld2.click()
                        ans = kvalasz1
                        print("Jo valasz:1")
                        break

                    elif (kvalasz2 == str1):
                        elkuld2 = driver.find_element_by_class_name("kvalasz2")
                        elkuld2.click()
                        ans = kvalasz2
                        print("Jo valasz:2")
                        break

                    elif (kvalasz3 == str1):
                        elkuld2 = driver.find_element_by_class_name("kvalasz3")
                        elkuld2.click()
                        ans = kvalasz3
                        print("Jo valasz:3")
                        break

                    elif (kvalasz4 == str1):
                        elkuld2 = driver.find_element_by_class_name("kvalasz4")
                        elkuld2.click()
                        ans = kvalasz4
                        print("Jo valasz:4")
                        break




            elkuldClick = driver.find_element_by_class_name("kvalasz2")
            elkuldClick2 = driver.find_element_by_class_name("kvalasz2").text
            elkuldClick.click()
            ans = elkuldClick2
            kapott_valasz=driver.find_element_by_css_selector("tbody").text
            #print(quest)
            hv = open('Helyes.txt','w')
            hv.writelines(kapott_valasz+"\n")
            hv.close()
            valasz = open('valaszokDorinaSzervezetivaltozas.txt','a+')

            with open('Helyes.txt') as file:
                contents = file.read()
                if 'helyes' in contents:
                    with open('valaszokDorinaSzervezetivaltozas.txt') as file:
                        contents2 = file.read()
                        if quest in contents2:
                            print("ilyen válasz már van")
                        else:
                            valasz.writelines(quest)
                            valasz.writelines('\n')
                            valasz.writelines(ans)
                            valasz.writelines('\n')
                            valasz.writelines('#')
                            valasz.close()
                else:
                    print("helytelen válasz")
            tovabb = driver.find_element_by_name("SUBMIT")
            tovabb.click()


        kerdes = driver.find_element_by_class_name("kkerdes").text
        quest = kerdes[4:]
        kvalasz1 = driver.find_element_by_class_name("kvalasz1").text
        kvalasz2 = driver.find_element_by_class_name("kvalasz2").text
        kvalasz3 = driver.find_element_by_class_name("kvalasz3").text
        kvalasz4 = driver.find_element_by_class_name("kvalasz4").text
        adat = open('valaszokDorinaSzervezetivaltozas.txt','r')
        list = [(line.strip()).split('#') for line in adat]
        adat.close()
        #print(list)
        for u in range(len(list)):
            ask =''.join(list[u])
            quest =''.join(quest)
            print(ask)
            print(quest)
            print('#######')
            if (ask == quest):
                print("OOOOOOOO")
                str1=''.join(list[u+1])
                if (kvalasz1 == str1):
                    elkuld2 = driver.find_element_by_class_name("kvalasz1")
                    elkuld2.click()
                    ans = kvalasz1
                    print("Jo valasz:1")
                    break

                elif (kvalasz2 == str1):
                    elkuld2 = driver.find_element_by_class_name("kvalasz2")
                    elkuld2.click()
                    ans = kvalasz2
                    print("Jo valasz:2")
                    break

                elif (kvalasz3 == str1):
                    elkuld2 = driver.find_element_by_class_name("kvalasz3")
                    elkuld2.click()
                    ans = kvalasz3
                    print("Jo valasz:3")
                    break

                elif (kvalasz4 == str1):
                    elkuld2 = driver.find_element_by_class_name("kvalasz4")
                    elkuld2.click()
                    ans = kvalasz4
                    print("Jo valasz:4")
                    break




        elkuldClick = driver.find_element_by_class_name("kvalasz1")
        elkuldClick2 = driver.find_element_by_class_name("kvalasz1").text
        elkuldClick.click()
        ans = elkuldClick2
        kapott_valasz=driver.find_element_by_css_selector("tbody").text
        #print(quest)
        hv = open('Helyes.txt','w')
        hv.writelines(kapott_valasz+"\n")
        hv.close()
        valasz = open('valaszokDorinaSzervezetivaltozas.txt','a+')

        with open('Helyes.txt') as file:
            contents = file.read()
            if 'helyes' in contents:
                with open('valaszokDorinaSzervezetivaltozas.txt') as file:
                    contents2 = file.read()
                    if quest in contents2:
                        print("ilyen válasz már van")
                    else:
                        valasz.writelines(quest)
                        valasz.writelines('\n')
                        valasz.writelines(ans)
                        valasz.writelines('\n')
                        valasz.writelines('#')
                        valasz.close()
            else:
                print("helytelen válasz")

        driver.get('https://portal.kgk.uni-obuda.hu/vizsga/index.php?do=exercise')
        print("##########################")

        #TESZT VALASZ 2-re
valasz.close()
file.close()
print("------------Végeztünk------------")
exit()
