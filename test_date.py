from datetime import datetime, timedelta
import calendar


def calculate_month_end_date(gte_date, week_start_day,ref_interval):
    # Convert the 'gte' date to a datetime object
    week_structure = {
        "0": "monday",
        "1": "tuesday",
        "2": "wednesday",
        "3": "thursday",
        "4": "friday",
        "5": "saturday",
        "6": "sunday"
    }

    def get_matching_day(given_day):
        weekdays_list = [("monday", "Sunday"), ("tuesday", "monday"), ("wednesday", "tuesday"),
                         ("thrusday", "wednesday"), ("friday", "thursday"), ("saturday", "sunday"),
                         ("sunday", "saturday")]
        for pair in weekdays_list:
            if pair[0].lower() == given_day.lower():
                return pair[1]
        return None

    def get_next_weekday_date(date_str, target_weekday):
        date_obj = datetime.strptime(date_str, "%d/%m/%Y")
        current_weekday = date_obj.weekday()
        target_weekday_index = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].index(
            target_weekday)

        if current_weekday == target_weekday_index:
            return date_obj.strftime("%d/%m/%Y")

        days_until_target = (target_weekday_index - current_weekday + 7) % 7
        new_date_obj = date_obj + timedelta(days=days_until_target)
        return new_date_obj.strftime("%d/%m/%Y")

    if ref_interval == "month":
        gte_datetime = datetime.strptime(gte_date, "%d/%m/%Y")
        year = gte_datetime.year
        month = gte_datetime.month
        days_in_month = calendar.monthrange(year, month)[1]
        month_end_date = datetime(year, month, days_in_month).strftime("%d/%m/%Y")
        week_end_day = get_matching_day(week_start_day)
        new_date = get_next_weekday_date(month_end_date,week_end_day)
        return new_date
    elif ref_interval == "quarter":
        gte_datetime = datetime.strptime(gte_date, "%d/%m/%Y")
        year = gte_datetime.year
        month = gte_datetime.month
        quarter = (month - 1) // 3 + 1
        quarter_last_month = quarter * 3
        days_in_quarter = calendar.monthrange(year, quarter_last_month)[1]
        quarter_end_date = datetime(year, quarter_last_month, days_in_quarter).strftime("%d/%m/%Y")
        week_end_day = get_matching_day(week_start_day)
        new_date = get_next_weekday_date(quarter_end_date, week_end_day)
        return new_date
    elif ref_interval == "year":
        gte_datetime = datetime.strptime(gte_date, "%d/%m/%Y")
        year = gte_datetime.year
        month = gte_datetime.month
        year_end_date = datetime(year, 12, 31).strftime("%d/%m/%Y")
        week_end_day = get_matching_day(week_start_day)
        new_date = get_next_weekday_date(year_end_date, week_end_day)
        return new_date

print(calculate_month_end_date("03/01/2022", "monday","year"))
