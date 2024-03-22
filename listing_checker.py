from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from datetime import datetime

print("Starting")
# TODO:
#   make Desktop path
file_path = "car_data.txt"
# Define a custom user agent
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
print("Running...")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")   # Don't open browser for user

# Set the custom User-Agent
chrome_options.add_argument(f"--user-agent={my_user_agent}")

# Create a new instance of ChromeDriver with the desired options
driver = webdriver.Chrome(options=chrome_options)

# Make a request to your target website.
query = "kasutatud/nimekiri.php?bn=2&a=100&ssid=126755967&c=kodiaq&ab[0]=3&ae=5&af=50&otsi=otsi&ak=0"
driver.get(f"https://www.auto24.ee/{query}")

# Get the current date and time
current_date_time = datetime.now()
current_date = current_date_time.strftime("%d-%m-%Y %H:%M:%S")

# Get element list
# elements = driver.find_elements(By.CSS_SELECTOR, 'a[href^="/soidukid/"]')
elements = driver.find_elements(By.CLASS_NAME, 'description')

# TODO:
#   add to print - link
#   add check if file exists

i = 1
with open(file_path, 'w') as file:
    file.write("Data gathered at " + current_date + "\n")
    file.write("Total matches found: " + str(len(elements)) + "\n\n")
    for element in elements:
        file.write(str(i) + ") \n")
        file.write(element.text + "\n\n")
        i += 1

print("Finished!")
# Close the driver
driver.quit()
