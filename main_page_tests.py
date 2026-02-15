from selenium import webdriver
from pages import main_page

firefoxDriver = webdriver.Firefox()
mainPage = main_page.MainPage(firefoxDriver)

def test_checkIfAllMainBlocksAreLoaded():
    assert(mainPage.loadPage("https://insiderone.com/")==True)
    assert(mainPage.declineCookiesIfVisible())
    assert(mainPage.checkIfAllMainBlocksLoaded())
    mainPage.quit()