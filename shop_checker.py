from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def search_page(web_pages, search_term):
    # Set up User-Agent
    my_user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                     "AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/92.0.4515.159 Safari/537.36")

    # Set up Chrome options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Don't open browser for user

    # Set the custom User-Agent
    chrome_options.add_argument(f"--user-agent={my_user_agent}")

    # Create a new instance of ChromeDriver with the desired options
    driver = webdriver.Chrome(options=chrome_options)

    for page in web_pages:
        # Make a request to your target website.
        driver.get(page)

        # Get element list
        elements = driver.find_elements(By.CLASS_NAME, 'description')

        with open('shop_check_results.txt', 'a') as file:
            for element in elements:
                file.write(element.text + "\n\n")

    # Close the driver
    driver.quit()


if __name__ == "__main__":
    pages = []
    term = input("Object to search: ")
    search_page(pages, term)
