import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Definition lists
    city_choise = ['chicago', 'new york city', 'washington']
    filter_choice = ['month','day','none']
    month_list = ['january', 'february', 'march', 'april', 'may', 'june']
    day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'saturday', 'sunday']

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = str(input("Would you like to see data for Chicago, New York City, or Washington? Please choose one of the 3 cities.\n")).lower()
        if city not in city_choise:
            print("This city is not in the list! Please note the correct spelling.")
            continue
        else:
            city == city
            break

        # inputdata for filter (month, day or not all all)
    while True:
        filter = str(input('Would you like to filter the data by month, day, or not at all? Type "none" if you don´t want any filter.\n')).lower()
        if filter not in filter_choice:
            print("This filter is not in the list! Please note the correct spelling.")
            continue
        else:
            filter == filter
            break

    # solution filter choise "none"
    if filter == "none":
        month = "all"
        day = "all"

    # solution "month"
    # get user input for month (january, february, ... , june)

    elif filter == "month":
        while True:
            month = str(input('Which month - January, February, March, April, May, or June? \n')).lower()
            if month not in month_list:
                print("This month is not in the list! Please note the correct spelling.")
                continue
            else:
                month == month
                day = "all"
                break

    # solution day
    # get user input for day of week (monday, tuesday, ... sunday)

    else:
        while True:
            day = str(input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? \n')).lower()
            if day not in day_list:
                print("This day is not in the list!")
                continue
            else:
                day == day
                month = "all"
                break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == "all":
        common_month = df['month'].mode()
        common_month = int(common_month)
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        print('Most common month: ', months[common_month - 1].title())


    # display the most common day of week
    if day == "all":
        common_day = df['day_of_week'].mode()[0]
        print('Most common day of week: ', common_day)


    # display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most popular hour
    popular_hour = df['hour'].mode()[0]

    print('Most Popular Start Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    while True:
        try:
            gender = df['Gender'].value_counts()
        except KeyError:
            print('Ther is no gender column in dataset!')
            break
        print(gender)
        break

    # Display earliest, most recent, and most common year of birth
    while True:
        try:
            earliest = int(df['Birth Year'].min())
        except KeyError:
            print('No birth year column in dataset!')
            break
        earliest = int(df['Birth Year'].min())
        print('Earliest year of birth: ', earliest)
        most_recent = int(df['Birth Year'].max())
        print('Most recent year of birth: ', most_recent)
        most_common = int(df['Birth Year'].value_counts().index[0])
        print('Most common year of birth: ', most_common)
        break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    start = df['Start Time']
    end = df['End Time']
    total = end - start
    print('Display total travel time: ', total.sum())


    # display mean travel time
    print('Display mean travel time: ', total.mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_ss = df['Start Station'].value_counts().index[0]
    print('Most common start station: ', most_common_ss)

    # display most commonly used end station
    most_common_es = df['End Station'].value_counts().index[0]
    print('Most common end station: ', most_common_es)

    # display most frequent combination of start station and end station trip
    most_common_se = (df['Start Station'] + df['End Station']).value_counts().index[0]
    print('Most common combination of start station and end station trip: ', most_common_se)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays the row data"""
    solution_trip = ["yes", "no"]
    x = 0
    y = 5
    while True:
        trip_data = str(input("Would you like to view individual trip data? Type 'yes' or 'no'\n")).lower()
        if trip_data not in solution_trip:
            print("This option is not in the list!")
            continue
        elif trip_data == "yes":
            print(df.iloc[x:y])
            x += 5
            y += 5
            continue
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
