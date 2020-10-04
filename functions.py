import bs4
import smtplib
import ssl
from selenium import webdriver


def get_events_page(url, credentials, driver):
    # Initializing the webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path=driver, options=options)
    driver.get(url)

    # Iniciamos sesion en JOBO
    mail = driver.find_element_by_id("login")
    mail.send_keys(credentials['mail'])

    passwd = driver.find_element_by_id("password")
    passwd.send_keys(credentials['password'])

    acceder = driver.find_element_by_id("continue_button")
    acceder.click()

    # Entramos en la lista de espectaculos
    comprar = driver.find_element_by_class_name("tickets_menu_add_products")
    comprar.click()

    return driver.page_source


def get_events(page):
    events_page = bs4.BeautifulSoup(page, 'html.parser')
    events = events_page.find_all(attrs={'data-product-type': "EVENT"})

    return events


def get_view_events(conection_BBDD):

    conection_BBDD.execute("SELECT Titulo FROM ESPECTACULOS;")

    view = conection_BBDD.fetchall()
    view = [item for t in view for item in t]

    return view


def available_events(events, view_events, conection_BBDD):

    mail_text = ""

    none_type = type(None)

    for event in events:

        if isinstance(event.find(attrs={'class': "buy_unavailable"}), none_type):

            title = event.find(attrs={'class': "title"}).text
            title = title.replace('\n', ' ').replace('\r', '').replace('\t', '').replace(' ', '')

            if title not in view_events:

                text = new_event(event, title, conection_BBDD)

                mail_text = mail_text + text

    return mail_text


def new_event(event, title, conection_BBDD):

    dia = event.find(attrs={'class': "day"}).text
    dia = dia.replace('\n', ' ').replace('\r', '').replace('\t', '')

    hora = event.find(attrs={'class': "time"}).text
    hora = hora.replace('\n', ' ').replace('\r', '').replace('\t', '')

    sitio = event.find(attrs={'class': "location"}).text
    sitio = sitio.replace('\n', ' ').replace('\r', '').replace('\t', '')

    # Agregamos el espectaculo a la BBDD de espectaculos enviados
    conection_BBDD.execute('insert into ESPECTACULOS values (?,?,?,?)', [title, dia, hora, sitio])

    text = 'TITULO: {}\n DIA: {}\n HORA: {}\n SITIO: {}\n\n\n\n'.format(title, dia, hora, sitio)

    return text


def send_mail(mail_text, credentials_gmail, send_to):

    mail_gmail = credentials_gmail['mail']
    pass_gmail = credentials_gmail['password']

    # Enviamos un mail con los eventos disponibles
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(mail_gmail, pass_gmail)

        subject = "NOVEDADES JOBO"

        message = 'Subject: {}\n\n{}'.format(subject, mail_text)

        server.sendmail(mail_gmail, send_to, message.encode('utf-8'))

    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()
