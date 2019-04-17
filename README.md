# monitor-and-report
Monitor a log file, when getting what you want,  report to a email

### Usage

1. Show help message and exit

   `python monitor.py -h  `

   ```
   Usage: monitor.py [options]
   Options:
     -h, --help            show this help message and exit
     --log_file=LOG_FILE   log file path
     --smtp_adress=SMTP_ADRESS   smtp adress
     --port=PORT           smtp port
     --user=USER           username
     --pwd=PWD             password
     --recipient=RECIPIENT  recipient
     --target_text=TARGET_TEXT   target text
     --subject=SUBJECT     subject
     --body=BODY           body
     --sleep_time=SLEEP_TIME  sleeping time after getting the target(sec)
     --max_time=MAX_TIME   max sending successfully times
   ```

2. Run in the back

   nohup python monitor.py --smtp_adress "smtp.xx.com" --user "xxx@xx.xx" --pwd "password" --recipient "xxx@xx.xx" --target_text "target_text" --log_file "log file path" >/dev/null 2>&1 &

### Notice

**1. Please setup your SMTP service of your email account first.**

**2. Sender email and recipient email can be the same or different. **



