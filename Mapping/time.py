import schedule
import time
from plyer import notification

def job():
    if __name__ == '__main__':
        notification.notify(
        title='Hi there',
        message='Son 12:52 en 10 minutos se ejecutará el script',
        timeout=10
        )
    return

schedule.every().day.at("12:53").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) # wait one minute