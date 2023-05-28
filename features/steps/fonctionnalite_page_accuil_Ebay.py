import time

from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

@given('je suis sur la page d accuil d Ebay')
def page_accuil(context):
    context.driver.get("https://www.ebay.com/")


@when("je cliquer sur lien avance")
def acces_lien_avencé(context):
    context.driver.find_element(By.XPATH,"//a[@id='gh-as-a']").click()
    time.sleep(3)
@then('je navigue vers la page recherche avancé')
def valider_page(context):
    data_avance=context.driver.find_element(By.XPATH,"(//div[text()='Advanced search'])[1]").text
    assert data_avance=="Advanced search"

@when("Je recherche 'iPhone 11'")
def saisir_mot_cle(context):
    context.driver.find_element(By.XPATH,"//input[@id='gh-ac']").send_keys('iPhone 11')
    context.driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()

@then('Je valide au moins 1000 éléments de recherche présents')
def valider_resultat(context):
    nombre_resultat=context.driver.find_element(By.XPATH,"//h1").text
    valeur1=nombre_resultat[0:5].replace(",","")
    assert int(valeur1)>=1000


@when("Je recherche 'Toy Cars'")
def saisir_mot_cle(context):
    context.driver.find_element(By.XPATH,"//input[@id='gh-ac']").send_keys('Toy Cars')
    context.driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()


@then('Je valide au moins 100 éléments de recherche présents')
def valider_resultat(context):
    nombre_resultat = context.driver.find_element(By.XPATH, "//h1").text
    valeur = nombre_resultat[0:5].replace(",", "")
    assert int(valeur) >= 100


@when("Je recherche 'soap' dans la catégorie 'BaBy'")
def saisir_mot_cle(context):
    context.driver.find_element(By.XPATH, "//input[@id='gh-ac']").send_keys('soap')
    liste = context.driver.find_element(By.XPATH, "//select[@id='gh-cat']")
    Select(liste).select_by_value('2984')
    context.driver.find_element(By.XPATH, "//input[@id='gh-btn']").click()

@then('Je valide au moins 50 éléments de recherche présents')
def valiser_resultat(context):
    nombre_resultat = context.driver.find_element(By.XPATH, "(//span[@class='BOLD'])[1]").text
    valeur = nombre_resultat[0:5].replace(",", "")
    assert int(valeur) >= 50







