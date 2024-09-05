import math

FLAT_RATE = 3999  
INCLUDED_MINUTES = 600
ADDITIONAL_RATE = 40  
TAX_RATE = 5.25 / 100

weekday_minutes = int(input("Weekday minutes: "))
night_minutes = int(input("Night minutes: "))
weekend_minutes = int(input("Weekend minutes: "))

additional_minutes = max(0, weekday_minutes - INCLUDED_MINUTES)
pretax_bill = FLAT_RATE + additional_minutes * ADDITIONAL_RATE

taxes = math.ceil(pretax_bill * TAX_RATE)
total_bill = pretax_bill + taxes
total_minutes = weekday_minutes + night_minutes + weekend_minutes
avg_cost_per_minute = round(pretax_bill / total_minutes) if total_minutes else 0

print(f"Pretax bill: ${pretax_bill / 100:.2f}")
print(f"Average cost per minute (before tax): ${avg_cost_per_minute / 100:.2f}")
print(f"Taxes: ${taxes / 100:.2f}")
print(f"Total bill: ${total_bill / 100:.2f}")