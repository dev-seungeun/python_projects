# -*- coding: utf-8 -*-
import os
import smtplib

from email.utils import formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from_addr = formataddr(('Google Test_Seungeun', 'test.seungeun@gmail.com'))
to_addr = formataddr(('Google Dev_Seungeun', 'dev.seungeun@gmail.com'))

session = None
try:
    # SMTP 세션 생성, 로그인
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.set_debuglevel(True)  # 상세 로그 출력

    # SMTP 계정 인증 설정
    session.ehlo()
    session .starttls()
    session .login('test.seungeun@gmail.com', 'hakaituvzatfwnwl')

    # 메일 컨텐츠 설정
    message = MIMEMultipart("alternative")

    # 메일 송/수신 옵션 설정
    title = '제목이다'
    message.set_charset('utf-')
    message['From'] = from_addr
    message['To'] = to_addr
    message['Subject'] = title

    # 메일 컨텐츠 - 내용
    body = '''
    <h2>안녕?</h2>
    <h4>난 승은이얌</h4>
    <h4>파이썬을 공부하고 있찌!</h4>
    '''
    bodyPart = MIMEText(body, 'html', 'utf-8')
    message.attach(bodyPart)

    # 메일 컨텐츠 - 첨부파일
    attachments = [
        os.path.join(os.getcwd(), 'storage', 'example.txt')
    ]

    for attachment in attachments:
        attach_binary = MIMEBase('application', 'octect-stream')
        try:
            binary = open(attachment, 'rb').read()  # read file to bytes

            attach_binary.set_payload(binary)
            encoders.encode_base64(attach_binary)  # Content-Transfer-Encoding: base64

            filename = os.path.basename(attachment)
            attach_binary.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', filename))

            message.attach(attach_binary)
        except Exception as e:
            print(e)

    # 메일 발송
    session.sendmail(from_addr, to_addr, message.as_string())

    print('Successfully sent the mail!!!')

except Exception as e:
    print(e)

finally:
    if session is not None:
        session.quit()


# 파일첨부 (파일 미첨부시 생략가능)
# attachment = open('파일명', 'rb')
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= " + filename)
# msg.attach(part)

