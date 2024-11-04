from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Set up the driver (make sure to have ChromeDriver installed and its path set)
driver = webdriver.Chrome()

# Navigate to the Facebook login page
driver.get("https://www.facebook.com")

# Log in to Facebook
username = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
username.send_keys("your_username") #replace with your username
password.send_keys("your_password") #replace with your password
login_button = driver.find_element(By.NAME, "login")
login_button.click()

# Wait for the page to load after logging in
time.sleep(5)

search_terms = ['search1', 'search2'] # put all search terms in this list

all_urls = []

for search_term in search_terms:

    # Locate the search box
    search_box = driver.find_element(By.XPATH, "//input[@placeholder='Search Facebook']")

    # Clear by simulating backspace key presses
    search_box.send_keys(Keys.COMMAND + "a")  # Select all text (use Keys.CONTROL for Windows)
    search_box.send_keys(Keys.BACKSPACE)
    time.sleep(1)


    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)
    print("navigated to search: " + search_term)

    # Wait for search results to load
    time.sleep(3)

  # Locate using text, if href-based XPATH doesn't work
    try:
        videos_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Videos')]/ancestor::a"))
        )
        driver.execute_script("arguments[0].click();", videos_tab)
    except Exception as e:
        print("Error: Could not locate or click on the Videos tab.", e)


    # Scroll and collect posts
    curr_urls = set()
    scroll_pause_time = 3  # Time to wait after each scroll, modify as needed
    scroll_attempts = 40 # Number of times selenium will scroll, modify as needed

    for i in range(scroll_attempts):
        # Find all anchor tags that link to videos/posts
        posts = driver.find_elements(By.XPATH, "//a[contains(@href, '/watch')]")

        # Collect URLs
        for post in posts:
            full_url = post.get_attribute("href")
            curr_urls.add(full_url)

        # Scroll down to the bottom of the page to load more content
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)

    all_urls.extend(list(curr_urls))

# Save URLs to CSV
url_df = pd.DataFrame(all_urls)
url_df.to_csv('your_output_path', index=False)
print("CSV created")

driver.quit()