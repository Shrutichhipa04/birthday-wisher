# 🎂 Automated Birthday Wisher

This is a Python script that sends personalized birthday emails automatically using a list of people stored in a CSV file. The message is generated using a template with the recipient's name and is sent using SMTP.

---

## 📸 Screenshots
![Screenshot 2025-07-03 111845](https://github.com/user-attachments/assets/344758b9-ed88-40b9-bbcc-06f6e83ec9d3)

### 📁 Folder Structure
```
birthday-wisher/
├── main.py
├── birthdays.csv
└── letter_templates/
    ├── letter_1.txt
    └── letter_2.txt
```

### 📨 Sample Letter Template (letter_1.txt)
```
Dear [NAME],

Wishing you a fantastic birthday filled with joy and surprises!

Cheers,
Shruti
```

### ✅ Sample CSV Format (birthdays.csv)
| name   | email              | year | month | day |
|--------|--------------------|------|-------|-----|
| Shruti | shruti@email.com   | 2003 | 6     | 20  |

---

## 🛠 Technologies Used

- **Python**
- `pandas` – to read CSV file
- `datetime` – to check today’s date
- `random` – to pick a template
- `smtplib` – to send emails

---

## 🚀 How It Works

1. Reads all birthdays from `birthdays.csv`.
2. If today’s date matches someone’s birthday, it:
   - Picks a random `.txt` template
   - Replaces `[NAME]` with actual name
   - Sends an email using Gmail SMTP server

---

## ⚠️ Setup Instructions

1. Clone the repo:  
```bash
git clone https://github.com/yourusername/birthday-wisher.git
cd birthday-wisher
```

2. Install dependencies (only `pandas` needed):  
```bash
pip install pandas
```

3. Add your email and password to the script securely.

4. Run the script:  
```bash
python main.py
```

> 💡 Make sure to enable **"less secure app access"** or use an **App Password** if you're using Gmail.

---

## ✨ Author

Made with 💖 by **Shruti Chhipa**
