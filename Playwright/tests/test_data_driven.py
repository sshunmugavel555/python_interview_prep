import re
import pytest
from playwright.sync_api import Page, expect
import csv,json

def get_csv_data() -> list:
    data = []
    with open("./test_data/data.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            data.append(row)

    return data

def get_json_data() -> list:

    with open("./test_data/payload.json", 'r') as jsonfile:
        data = json.load(jsonfile)

    return [(item["uname"], item["pwd"]) for item in data]

@pytest.mark.parametrize("uname, pwd", get_json_data())
def test_example(page: Page, uname: str, pwd: str) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.locator("#form")).to_contain_text("Username")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(uname)
    page.get_by_role("textbox", name="Username").press("Tab")
    page.get_by_role("textbox", name="Password").fill(pwd)
    expect(page.get_by_role("textbox", name="Username")).to_have_value(uname);
    expect(page.get_by_role("textbox", name="Password")).to_have_value(pwd);
    page.get_by_role("button", name="Submit").click()

    expect(page.get_by_role("link", name="Practice Test Automation", exact=True)).to_be_visible()
    expect(page.get_by_role("heading")).to_contain_text("Logged In Successfully")
    expect(page.get_by_role("article")).to_contain_text("Log out")
    
    page.get_by_role("link", name="Log out").click()