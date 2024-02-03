from internetSpeedTwitterBot import InternetSpeedTwitterBot
import time

USER_SPEED = {"down": 10, "up": 10}

bot = InternetSpeedTwitterBot(USER_SPEED)

current_speed = bot.current_speeds
print(current_speed)
# print(current_speed["down"], USER_SPEED["down"], current_speed["up"], USER_SPEED["up"])

if current_speed["down"] < USER_SPEED["down"] or current_speed["up"] < USER_SPEED["up"]:
    bot.tweet_at_provider()
else:
    print("Don't Worry. Everything is Ok.")

time.sleep(10)
bot.driver.quit()
