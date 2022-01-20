import streamlit as st
import pandas as pd
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl



def email(sender_email, receiver_email,password,html_file,subject):
    # Create secure connection with server and send email
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        st.write('**********************************************************')
        print('**********************************************************')
        server.login(sender_email, password)
        st.write('Successfully logged in')
        print('Successfully logged in')


        # Send email here
        for i , receiver_email in enumerate(receiver_email):
                message = MIMEMultipart("alternative")
                message["Subject"] = subject
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Bcc"] = receiver_email  # Recommended for mass emails
                message["Cc"] = sender_email  # Recommended for mass emails
                message["Reply-to"] = sender_email
                message['mail_type'] = 'html'
                message['mailed_by'] = 'https://pradeepodela.github.io/'
                message['mailed_by_name'] = 'Pradeep OdeLa'
                message['Signature'] = 'https://pradeepodela.github.io/'
                message['security'] = 'https://pradeepodela.github.io/'

                # file = codecs.open(html_file, "r", "utf-8")
                # html = file.read()
                # file.close()

                part2 = MIMEText(html_file, "html")
                message.attach(part2)
                try:
                    server.sendmail(sender_email, receiver_email, message.as_string())
                    st.write(f'{i}. Email sent to: ', receiver_email)
                    print(f'{i}. Email sent to: ', receiver_email)
                except:
                    st.write('**********************************************************')
                    print('**********************************************************')
                    st.write(f'{i}. There is a problem sending Email to : ', receiver_email)
                    st.write('**********************************************************')
                    print(f'{i}. There is a problem sending Email to : ', receiver_email)
                    print('**********************************************************')
        st.write('Succefully sent all emails')
        st.write('**********************************************************')
        print('**********************************************************')



st.title('Dashboard ')


st.markdown(
	'''
	<style>
	[data-testid='sidebar'][aria-expanded='true'] > div:firstchild{width:400px}
	[data-testid='sidebar'][aria-expanded='false'] > div:firstchild{width:400px , margin-left: -400px}
	</style>
	''',
	unsafe_allow_html=True
)

st.markdown('---')

st.title('login to your email')

sender_email = st.text_input('email')
password = st.text_input('password', type='password')

st.markdown('---')
subject = st.text_input('subject')

data_file = st.file_uploader("Upload Emails CSV",type=["csv"])
		
if data_file is not None:
    df = pd.read_csv(data_file)
    st.dataframe(df)
    email_colum = st.selectbox('select email column',df.columns)
    st.dataframe(df[email_colum])
    receiver_email = df[email_colum].tolist()
st.markdown('---')
html_file = st.text_area("Message/HTML", height=500)

send = st.button('send Emails')
if send:
    email(sender_email, receiver_email,password,html_file,subject)


