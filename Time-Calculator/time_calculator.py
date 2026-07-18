def add_time(start, duration, day_of_week=None):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0
        
    dur_hour, dur_minute = map(int, duration.split(":"))
    
    total_minutes = start_minute + dur_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60
    
    total_hours = start_hour + dur_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24
    
    if final_hour_24 == 0:
        final_hour = 12
        final_period = "AM"
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = "AM"
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = "PM"
    else:
        final_hour = final_hour_24 - 12
        final_period = "PM"
        
    new_time = f"{final_hour}:{final_minute:02d} {final_period}"
    
    if day_of_week:
        day_index = days.index(day_of_week.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_time += f", {days[new_day_index]}"
        
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
        
    return new_time
