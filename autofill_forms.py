import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

"""
v1.0.0 Make universal form filler
1.  Insert form link (UI?)
2.  Analyze webpage
3.  Print total questions found
4.  Link possible answers to question
5.  Ask input - 1) Set ranges; 2) Equal ranges; 3) Totally random
6.  If 1) print question -> ask for ranges / probabilities (show remaining percentage)
7.  If 2) Divide 1 by possible answers -> set probabilities for each answer
8.  If 3) rAnDoMiSe
9.  Ask how many iterations
10. Open webpage -> set webdriver options (waketime, language, etc)
11. Answer form
12. Show dialog when finished 
"""


def get_soup():
    soup = bs("https://docs.google.com/forms/d/e/1FAIpQLSd4t4ACQaOFBJ0KrBVkibqHGWJEZcqu9tfAFdaYHqBRIqwP0w/viewform?usp=sf_link", 'html.parser')
    print(soup.prettify())


# Form functions
def ask_link():
    link = input("Insert Google Form link: ")
    return link


def analyze_form(form):
    # BeautifulSoup
    pass


def ask_probabilities():
    prob = input("1) Set ranges\n2) Use equal ranges\n3) Totally randomise\nYour choice: ")
    if prob == 1:
        return 1
    elif prob == 2:
        return 2
    else:
        return 3


def set_probabilities(choice):
    if choice == 1:
        pass
    elif choice == 2:
        pass
    else:
        pass


def ask_iterations():
    iterations = input("How many iterations to run: ")
    return iterations


def setup_webdriver():
    return 0


def run_iterations(iters):
    d = setup_webdriver()
    for _ in range(iters+1):
        pass
    

# Define a custom user agent
my_user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/92.0.4515.159 Safari/537.36")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")   # Don't open browser for user

# Set the custom User-Agent
chrome_options.add_argument(f"--user-agent={my_user_agent}")

# Create a new instance of ChromeDriver with the desired options
driver = webdriver.Chrome(options=chrome_options)

# Wait for response
driver.implicitly_wait(15)

# Make a request to your target website.
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSd4t4ACQaOFBJ0KrBVkibqHGWJEZcqu9tfAFdaYHqBRIqwP0w/viewform?usp"
           "=sf_link")

source = driver.page_source

soup = bs(source, 'html.parser')
soup = soup.find_all("class='geS5n'")
print(soup)


def find_elem(string):
    try:
        # print(string)
        return driver.find_element(By.XPATH, string)
    except Exception as ex:
        print(ex)


def q1():
    question = find_elem("(//span[normalize-space()='Valige'])[1]")
    time.sleep(1)
    question.click()
    r_n = random.randint(0, 100)
    if r_n <= 97:
        option = find_elem("(//span[@class='vRMGwf oJeWuf'][normalize-space()='Harju maakond'])[2]")
        option.click()
    else:
        option = find_elem("(//span[@class='vRMGwf oJeWuf'][normalize-space()='Rapla maakond'])[2]")
        option.click()
    time.sleep(1)


def q2():
    # Generate a random number between 0 and 100 to represent percentiles
    r_p = random.randint(0, 100)
    try:
        # Set the probability distribution for age groups
        if r_p <= 85:
            option = find_elem("(//div[@class='AB7Lab Id5V1'])[1]")
            option.click()
        elif 85 < r_p <= 95:
            option = find_elem("(//div[@class='AB7Lab Id5V1'])[2]")
            option.click()
        elif 95 < r_p <= 97:
            option = find_elem("(//div[@class='AB7Lab Id5V1'])[3]")
            option.click()
        else:
            option = find_elem("(//div[@class='AB7Lab Id5V1'])[4]")
            option.click()
    except Exception as e:
        print(e)


def q3():
    random_percentile = random.randint(0, 100)
    # Set the probability distribution for options
    if random_percentile <= 2:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[5]")
        option.click()
    elif 2 < random_percentile <= 5:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[6]")
        option.click()
    elif 5 < random_percentile <= 88:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[7]")
        option.click()
    else:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[8]")
        option.click()


def q4():
    #random_percentile = random.randint(0, 100)
    ## Set the probability distribution for options
    #if random_percentile <= 97:
    #    option = find_elem("(//div[@class='AB7Lab Id5V1'])[10]")
    #    option.click()
    #elif 97 < random_percentile <= 99:
    option = find_elem("(//div[@class='AB7Lab Id5V1'])[11]")
    option.click()
    #elif 99 < random_percentile <= 100:
    #    option = find_elem("(//div[@class='AB7Lab Id5V1'])[12]")
    #    option.click()
    #else:
    #    option = find_elem("(//div[@class='AB7Lab Id5V1'])[13]")
    #    option.send_keys(Keys.NUMPAD0)


def q5():
    ans = find_elem("(//input[@type='text'])[2]")
    random_value = random.randint(30, 70)
    random_value = (random_value // 10) * 10
    ans.send_keys(str(random_value))
    ans.send_keys(Keys.ENTER)


def q6():
    random_percentile = random.randint(0, 100)
    if random_percentile <= 3:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[14]")
        option.click()
    elif 3 < random_percentile <= 5:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[15]")
        option.click()
    elif 5 < random_percentile <= 8:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[16]")
        option.click()
    elif 8 < random_percentile <= 33:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[17]")
        option.click()
    else:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[18]")
        option.click()


def q7():
    random_percentile = random.randint(0, 100)
    # Set the probability distribution for options
    if random_percentile <= 2:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[19]")
        option.click()
    elif 2 < random_percentile <= 22:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[20]")
        option.click()
    elif 22 < random_percentile <= 99:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[21]")
        option.click()
    else:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[22]")
        option.click()


def q8():
    #random_percentile = random.randint(0, 100)
    # Set the probability distribution for options
    #if random_percentile <= 40:
    option = find_elem("(//div[@class='AB7Lab Id5V1'])[24]")
    option.click()
    #elif 40 < random_percentile <= 87:
    #    option = find_elem("(//div[@class='AB7Lab Id5V1'])[25]")
    #    option.click()
    #else:
    #    option = find_elem("(//div[@class='AB7Lab Id5V1'])[26]")
    #    option.click()


def q9(place):
    question = find_elem("(//textarea[@aria-label='Teie vastus'])[1]")
    question.send_keys(place)
    question.send_keys(Keys.ENTER)


def q10():
    random_percentile = random.randint(0, 100)
    # Set the probability distribution for options
    if random_percentile <= 98:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[27]")
        option.click()
    elif 98 < random_percentile <= 99:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[28]")
        option.click()
    else:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[29]")
        option.click()


def q11():
    random_percentile = random.randint(0, 100)
    # Set the probability distribution for options
    if random_percentile <= 7:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[30]")
        option.click()
    elif 7 < random_percentile <= 67:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[31]")
        option.click()
    elif 67 < random_percentile <= 97:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[32]")
        option.click()
    else:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[33]")
        option.click()


def q12():
    random_percentile = random.randint(0, 100)
    # Set the probability distribution for options
    if random_percentile <= 2:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[34]")
        option.click()
    else:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[35]")
        option.click()


def q14():
    random_percentile = random.randint(0, 100)
    # Set the probability distribution for options
    if random_percentile <= 3:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[36]")
        option.click()
    elif 3 < random_percentile <= 17:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[37]")
        option.click()
    elif 17 < random_percentile <= 47:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[38]")
        option.click()
    elif 47 < random_percentile <= 63:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[39]")
        option.click()
    else:
        option = find_elem("(//div[@class='AB7Lab Id5V1'])[40]")
        option.click()


def submit():
    submit_button = find_elem("(//span[contains(text(),'Saada ära')])[1]")
    if submit_button:
        submit_button.click()
    if not submit_button:
        submit_button = find_elem("(//span[contains(text(),'Submit')])[1]")
        submit_button.click()


def restart():
    resubmit_button = find_elem("(//a[normalize-space()='Esita veel üks vastus'])[1]")
    resubmit_button.click()
    time.sleep(1.5)


def fill_form():
    q1()
    q3()  # Change to 2nd so no errors
    q2()
    q4()
    q5()
    q6()
    q7()
    q8()
    # q9(place)  # Optional
    q10()
    q11()
    q12()
    q14()
    submit()
    restart()


# Answer list
q9_ans = [
    "Maksetähtaja unustamine teatud tellimuse puhul",
    "Raskusi tellimuste ajaloo ja maksete ülevaadete leidmisega",
    "Probleemid platvormi navigeerimisega, eriti lisateenuste leidmisel.",
    "Raskused tellimuse muutmise või tühistamise protsessis.",
    "Puudulikud automaatsed meeldetuletused maksetähtaegade kohta",
    "Ei saanud ise kohandada tellimuste ülevaadet.",
    "Raskused uute tellimuste lisamisel platvormil",
    "Probleemid makseviiside muutmisega.",
    "Vajadus lihtsustatud lahenduste järele tellimuste optimeerimisel.",
    "Puudulik klienditoe abi probleemide lahendamisel",
    "Raskused erinevate tellimuste koondamisel ühte ülevaatlikku vaatesse.",
    "Probleemid kampaaniate ja allahindluste mõistmisel tellimustes.",
    "Ei saand tellimusi kategooriate järgi filtreerida",
    "Puudus teave seoses tellimuste katkestamise tingimustega.",
    "Raskused platvormi kasutamisel erinevate seadmetega."]

# Run with comments

# for q in q9_ans:
#     fill_form(q)

# Run without comments

# for _ in range(6):
#     fill_form()

"""
# Get element list
try:
    i = 0
    for q in question_text_boxes:
        element = driver.find_element(By.XPATH, q)
        if element:
            element.send_keys(answers[i])
            element.send_keys(Keys.ENTER)
            print(f"Written {answers[i]} to {q}")
            i += 1
        else:
            print("None")
    submit = driver.find_element(By.XPATH, "(//span[contains(text(),'Saada ära')])[1]")
    submit.click()
    time.sleep(2)
except Exception as e:
    print(e)
"""
driver.quit()


# def main():
#     get_soup()
#
#
# if __name__ == "__main__":
#     main()
