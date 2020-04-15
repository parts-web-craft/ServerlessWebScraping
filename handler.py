import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def scraping(event, context):
    try:
        request_error = {
            "statusCode": 400,
            "body": json.dumps({"message": "リクエストが不正です。"})
        }

        if event['body'] is None:
            return request_error

        params = json.loads(event['body'])
        if "url" not in params or not params['url']:
            return request_error

        options = Options()
        options.binary_location = "./driver/headless-chromium"
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--single-process")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome("./driver/chromedriver", chrome_options=options)
        driver.get(params['url'])
        source = driver.page_source
        driver.close()
        driver.quit()

        return {
            "statusCode": 200,
            "body": json.dumps({"response": source})
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "internal server error"})
        }
