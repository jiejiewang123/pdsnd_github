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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = ''
    while city not in cities:
        city = input("Please input the city name, chicago, new york city or washington: ").lower()
    print(city)
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june', 'august', 'september', 'october', 'november', 'december']
    month = ''
    while month not in months:
        month = input("Please input the month you want to explore of the city: ").lower()
    print(month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in days:
        day = input("Please input the day of a week you want to explore of the city: ").lower()
    print(day)

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
    #load data
    df = pd.read_csv(CITY_DATA[city])
    #Convert the start time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #filter by month using index in months if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
    # filer by month to create new dataframe
        df = df[df['month'] == month]

    #filer by day if applicable
    if day != 'all':
    #filter by day to create new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['hour'] = df['Start Time'].dt.hour
    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]

    print('The most common month is: ', most_common_month)


    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', most_common_day)

    # TO DO: display the most common start hour

    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(start_station))
    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination_station= df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('The most frequent combination start and end station trip is \n {}'.format(combination_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time is {}'.format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].min()
    print('The mean travel time is {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts_user_type = df['User Type'].value_counts()
    print('The counts of user types is: ', counts_user_type)


    # TO DO: Display counts of gender
    counts_gender = df['Gender'].value_counts()
    print('counts of gender is: ', counts_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    earlist = df['Birth Year'].min()
    print('The earliset birth year is: ', earlist)
    most_recent = df['Birth Year'].max()
    print('The most recent birth year is: ', most_recent)
    most_common_year = df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('Do you like to display 5 records of the raw data? Enter yes or no.\n')

        if raw_data.lower() == 'yes':
            i = 0
            while True:
                print(df.iloc[i:i+5])
                i += 5
                more_data = input('Do you like to display more data? Enter yes or no. \n')
                if more_data.lower() != 'yes':
                    break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
