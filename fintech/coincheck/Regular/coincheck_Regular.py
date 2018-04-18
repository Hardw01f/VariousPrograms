import tool
import sys

rate = tool.get_parameter()
rate = str(rate)
print(rate)
print(rate.split(","))

split_rate = rate.split(",")
print(split_rate)

now_rate = split_rate[0]
split_rate = now_rate.split(":")
now_rate = split_rate[1]
print(now_rate)

tool.send_slack(now_rate)

