"""
a module to download all courses from the uottawa course timetable website
much more minimized version of https://github.com/morinted/schedule-generator
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def main():
    """main"""

    courses = []

    driver = webdriver.Chrome()
    driver.get("https://web30.uottawa.ca/v3/SITS/timetable/Search.aspx")
    driver.find_element(By.NAME, "ctl00$MainContentPlaceHolder$Basic_Button").click()
    assert "Course Timetable" in driver.title
    next_btn = driver.find_element(By.LINK_TEXT, "Next")

    while next_btn:
        course_links = driver.find_elements(By.CSS_SELECTOR, ".CourseCode>a")
        for course_link in course_links:
            courses.append(course_link.get_attribute("href"))
        next_btn.click()
        try:
            next_btn = driver.find_element(By.LINK_TEXT, "Next")
        except NoSuchElementException:
            break
    driver.close()

    courses.sort()

    with open("courses.txt", "w") as course_file:
        course_file.writelines("number of links:" + str(len(courses)) + "\n")
        course_file.writelines("\n".join(courses))

main()
