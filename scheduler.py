import schedule
from datetime import datetime, timedelta, time
from main import send_reminder

def schedule_single_reminder(hours, chat_id):
    try:
        reminder_time = datetime.now() + timedelta(hours=3)
        schedule.every().at(reminder_time.strftime("%H:%M")).do(send_reminder, chat_id).tag(f"reminder_{chat_id}")
        schedule.clear(f"reminder_{chat_id}")
    except Exception as e:
        print(f"An error occurred while scheduling single reminder: {str(e)}")

# Run the scheduler in a separate thread
def run_scheduler():
    while True:
        try:
            schedule.run_pending()
        except Exception as e:
            print(f"An error occurred in the scheduler: {str(e)}")