# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# 세션생성, 로그인
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('test.seungeun@gmail.com', 'hakaituvzatfwnwl')

# 제목, 본문 작성
msg = MIMEMultipart()
msg['Subject'] = '제목이다'
msg.attach(MIMEText('안뇽 파이썬공부하면서 보내는 이메일이다! 승은아 파이어족 화이팅 ㅎㅎ', 'plain'))

# 파일첨부 (파일 미첨부시 생략가능)
# attachment = open('파일명', 'rb')
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= " + filename)
# msg.attach(part)

# 메일 전송
s.sendmail("test.seungeun@gmail.com", "dev.seungeun@gmail.com", msg.as_string())
s.quit()
