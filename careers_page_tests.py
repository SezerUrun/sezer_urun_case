import pytest
from selenium import webdriver
import sys
from pages import careers_page

firefoxDriver = webdriver.Firefox()
careers_page = careers_page.CareersPage(firefoxDriver)

def test_checkIfJobFilterWorks():
    assert(careers_page.loadPage("https://useinsider.com/careers/quality-assurance/"))
    careers_page.declineCookiesIfVisible()
    assert(careers_page.seeAllQAJobs())
    careers_page.declineCookiesIfVisible()
    assert(careers_page.applyJobFilter("Istanbul, Turkiye","Quality Assurance"))
    assert(careers_page.checkIfJobsAreFilteredAsExpected("Quality Assurance","Istanbul, Turkiye","Quality Assurance"))
    assert(careers_page.checkIfViewRoleButtonsWorkAsExpected())
    careers_page.quit()