from dateutil.relativedelta import (MO, TU, WE, TH, FR, SA, SU)
from pandas import (DateOffset, Timestamp, date_range)
from datetime import  timedelta
from pandas.tseries.holiday import (Holiday, nearest_workday, sunday_to_monday,  Easter)
from pandas.tseries.offsets import Day, CustomBusinessDay

from pandas_market_calendars.market_calendar import ( MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)



####################################################
# US New Years Day Jan 1
#####################################################
USNewYearsDay = Holiday(
    'New Years Day',
    month=1,
    day=1,
    start_date = Timestamp('1952-09-29'),
     #observance=sunday_to_monday,
    days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY,)    
)



#########################################################################
# Martin Luther King Jr. 
#    Starting 1998
##########################################################################
USMartinLutherKingJrFrom2022 = Holiday( # Early Close 1:30pm
    'Dr. Martin Luther King Jr. Day',
    month=1,
    day=1,
    start_date=Timestamp('2022-01-01'),
    days_of_week=(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY,),
    offset=DateOffset(weekday=MO(3)),
)

USMartinLutherKingJrPre2022 = Holiday( # Early Close 12:00pm
    'Dr. Martin Luther King Jr. Day',
    month=1,
    day=1,
    start_date=Timestamp('1998-01-01'),
    end_date=Timestamp("2021-12-31"),
    offset=DateOffset(weekday=MO(3)),
)


#########################################################################
# US Presidents Day Feb 
##########################################################################
USPresidentsDayFrom2022 = Holiday('President''s Day',  # 1:30pm Early Close
    start_date=Timestamp('2022-01-01'),
    month=2, day=1,
    offset=DateOffset(weekday=MO(3)))

USPresidentsDayPre2022 = Holiday('President''s Day',  # 12:00pm Early Close
    end_date=Timestamp('2021-12-31'),
    month=2, day=1,
    offset=DateOffset(weekday=MO(3)))
    


############################################################
# Good Friday 
############################################################
GoodFriday = Holiday(
    "Good Friday 1908+", 
    start_date=Timestamp('1908-01-01'), 
    month=1, 
    day=1, 
    offset=[Easter(), Day(-2)]
)

##################################################
# US Memorial Day (Decoration Day) May 30 
##################################################
USMemorialDayFrom2022 = Holiday( # 1:30pm early close
    'Memorial Day',
    month=5,
    day=25,
    start_date=Timestamp('2022-01-01'),
    offset=DateOffset(weekday=MO(1)),
)

USMemorialDayPre2022 = Holiday( # 12:00pm early close
    'Memorial Day', 
    month=5,
    day=25,
    end_date=Timestamp('2021-12-31'),
     offset=DateOffset(weekday=MO(1)),
)

#######################################
# US Juneteenth (June 19th)
#######################################
USJuneteenthFrom2022 = Holiday(
    'Juneteenth Starting at 2022',
    start_date=Timestamp('2022-06-19'),
    month=6, day=19,
    observance=nearest_workday,
)

#######################################
# US Independence Day July 4
#######################################
USIndependenceDayFrom2022 = Holiday(
    'July 4th',
    month=7,
    day=4,
    start_date=Timestamp('2022-01-01'),
    observance=nearest_workday,
)
USIndependenceDayPre2022 = Holiday(
    'July 4th',
    month=7,
    day=4,
    end_date=Timestamp('2021-12-31'),
    observance=nearest_workday,
)


#################################################
# US Labor Day Starting 1887
#################################################
USLaborDay = Holiday(
    "Labor Day", 
    month=9, 
    day=1, 
    start_date=Timestamp("1887-01-01"),
    offset=DateOffset(weekday=MO(1))
)


################################################
# US Thanksgiving Nov 30
################################################
USThanksgivingDayFrom2022 = Holiday(
    'Thanksgiving',
    start_date=Timestamp('2022-01-01'),
    month=11, day=1,
    offset=DateOffset(weekday=TH(4))
)

USThanksgivingDayPre2022 = Holiday(
    'Thanksgiving',
    end_date=Timestamp('2021-12-31'),
    month=11, day=1,
    offset=DateOffset(weekday=TH(4))
)

FridayAfterThanksgiving = Holiday(
    'Friday after Thanksgiving',
    month=11,
    day=1,
    offset=[DateOffset(weekday=TH(4)), Day(1)],
)


################################
# Christmas Dec 25
################################
ChristmasCME = Holiday(
    'Christmas',
    month=12,
    day=25,
    start_date=Timestamp('1999-01-01'),
    observance=nearest_workday, 
)

