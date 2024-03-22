import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Define a custom user agent
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")   # Don't open browser for user

# Set the custom User-Agent
chrome_options.add_argument(f"--user-agent={my_user_agent}")

# Create a new instance of ChromeDriver with the desired options
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)
# Make a request to your target website.
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfyHP0GriwS2-RMFQ3tBmEQN0yhG2WwhC8P2Lr0lXJLIJ7Sdw/viewform?usp=sharing")

question_text_boxes = [
    "(//input[@type='text'])[1]",
    "(//input[@type='text'])[2]",
    "(//input[@type='text'])[3]",
    "(//input[@type='text'])[4]",
    "(//input[@type='text'])[5]"]

answers = [
    "Sarah",
    "Smooth inc.",
    "Sarah.s@gmail.com",
    "+99-123-456-789",
    "Nice Form"]

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

driver.quit()
