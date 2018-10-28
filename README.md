# mining-rig-monitor
Monitors your Ethereum mining rig. Due to costs and personal needs, this is only used to monitor one rig only. 

Restrictions:
1. Can only monitor 1 mining rig, although that would be easy to add as a feature.
2. Monitors for Nanopool, as it is using Nanopool API.

What You Need:
1. Mining rig
2. Ethereum mining address on Nanopool
3. Twilio account and phone number
4. Windows Task Schedular
5. Python

How To Use:
1. Sign up to Twilio with a trial account https://www.twilio.com/try-twilio
2. In Twilio Console under "Phone numbers", get a phone number.
3. In "rigmonitor.py", replace your auth_token and account_sid in your Twilio console. Replace "rig_address" with your mining rig Ethereum address.
4. Open Windows Task Schedular -> Task Scheduler Library -> Create Task
5. In Triggers Tab, set the scheduled times you want to check your current hash rate (I have it as hourly, indefinitely, daily)
6. In Actions Tab, set Action to "Start a program", Program/script to your python.exe (run python -c "import sys; print(sys.executable)" to get your python.exe path)
7. Still under the same Actions tab, in "Add Arguments", enter "app.py", and in "Start in" set it to the address of your app.py file (ex. C:\Users\jerry\Desktop\rigmonitor)
