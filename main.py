from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import smtplib
import schedule




options = Options()
options.add_argument("--headless") 
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
 
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

chromedriver_path = "/Users/laraturunc/Documents/zara-bot/chromedriver"


sender_email = "laraturunc2103@gmail.com"
app_password = "qaejnurybzslspyr"
receiver_email = "laraturunc2103@gmail.com"

last_notified_sizes = set()

from email.message import EmailMessage

def send_email():
    subject = "🎉 Zara Stoğa Girdi!"
    body = "XS veya S beden stoğa girdi! Hemen bak: https://www.zara.com/tr/tr/-k-e-m-e-r-l-i----y-e-l-e-k---t-o-p--p02010812.html"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)
        print("✅ E-posta gönderildi!")




def check_stock():
    global last_notified_sizes
    print("🕵️ Stoğu kontrol ediyorum...")
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)

    url = "https://www.zara.com/tr/tr/-k-e-m-e-r-l-i----y-e-l-e-k---t-o-p--p02010812.html?v1=417748060"
    driver.get(url)
    driver.implicitly_wait(10)
    time.sleep(10)



    try:
        add_button = driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Ekle')]")
        driver.execute_script("arguments[0].scrollIntoView();", add_button)
        add_button.click()
        print("✅ EKLE butonuna tıklandı!")
        time.sleep(3)
    except:
        print("🛒 'EKLE' butonu bulunamadı.")
        driver.quit()
        return

    size_buttons = driver.find_elements(By.CSS_SELECTOR, "button.size-selector-sizes-size__button")
    current_stock = set()
    notified_this_round = False

    for button in size_buttons:
        text = button.text.strip().upper()
        data_status = button.get_attribute("data-qa-action")
        print(f"👉 {text} | stock status: {data_status}")

        if text in ["XS", "S", "XL"] and data_status == "size-in-stock":
            current_stock.add(text)
            if text not in last_notified_sizes:
                send_email()
                last_notified_sizes.add(text)
                notified_this_round = True
            else:
                print(f"⚠️ {text} zaten bildirildi, tekrar gönderilmiyor.")

    if not notified_this_round:
        print("❌ XS/S/XL stokta yok.")
        last_notified_sizes = last_notified_sizes.intersection(current_stock)

    driver.quit()



check_stock()


schedule.every(1).minutes.do(check_stock)
print("🔁 Zara stoğu takip ediliyor... (her 1 dakikada bir)")

while True:
    schedule.run_pending()
    time.sleep(1)