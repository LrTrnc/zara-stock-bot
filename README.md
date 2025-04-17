# Zara Stock Alert Bot

A Python bot that monitors Zara product availability (XS/S sizes) and sends an email alert when the item is back in stock.

## Features
- Tracks stock for selected Zara sizes (XS, S)
- Sends email notifications via Gmail
- Avoids duplicate notifications
- Checks availability every 5 minute

## ⚠️ Important: Gmail App Password Required

**Do NOT use your Gmail login password.**  
This bot uses Gmail SMTP to send alerts, which requires an **App Password** for secure access.

To generate an App Password:

1. Enable **2-Step Verification** on your Gmail account  
2. Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a new app password (choose "Mail" and "Other")
4. Copy the 16-character password
5. Use it as the value for `APP_PASSWORD` in your `.env` file

> 📌 Using your normal Gmail password will **not work** and is a security risk.


## Setup

1. Clone this repo
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` file and add:

  EMAIL=your_email@gmail.com
  APP_PASSWORD=your_app_password 
  RECEIVER=your_email@gmail.com

4. Run the script: `python main.py`


# Zara Stok Takip Botu

XS ve S bedenler için Zara ürün stoklarını takip eden ve ürün yeniden stoğa girdiğinde e-posta ile bildirim gönderen bir Python botudur.

## Özellikler
- Belirli Zara bedenlerini (XS, S) takip eder
- Gmail aracılığıyla e-posta bildirimi gönderir
- Aynı beden için tekrar tekrar bildirim göndermez
- Her 5 dakikada bir stok kontrolü yapar

## ⚠️ Önemli: Gmail Uygulama Şifresi Gerekli

**Gmail giriş şifrenizi kullanmayın.**  
Bu bot, Gmail SMTP sunucusunu kullanarak e-posta gönderir ve bunun için güvenli bir **uygulama şifresi** gereklidir.

Uygulama şifresi oluşturmak için:

1. Gmail hesabınızda **iki adımlı doğrulamayı** (2FA) etkinleştirin  
2. [Google Uygulama Şifreleri](https://myaccount.google.com/apppasswords) sayfasına gidin  
3. Yeni bir uygulama şifresi oluşturun (Hizmet olarak "Mail", cihaz olarak "Other" seçin)  
4. Oluşan 16 haneli şifreyi kopyalayın  
5. Bu şifreyi `.env` dosyanızdaki `APP_PASSWORD` alanına yazın

> 📌 Gmail giriş şifrenizi kullanmak **çalışmaz** ve güvenlik riski oluşturur.

## Kurulum

1. Bu repoyu klonlayın  
2. Gereken kütüphaneleri yükleyin: `pip install -r requirements.txt`
3. `.env` belgesi oluştur ve içine şunları ekle:

  EMAIL=your_email@gmail.com
  APP_PASSWORD=your_app_password 
  RECEIVER=your_email@gmail.com

4. Script'i çalıştır: `python main.py`

   



