import pandas as pd
import time

CITY_DATA = { 'chicago': '/Users/wiktoriatwarog/Documents/Project_2_Python/chicago.csv',
              'new york city': '/Users/wiktoriatwarog/Documents/Project_2_Python/new_york_city.csv',
              'washington': '/Users/wiktoriatwarog/Documents/Project_2_Python/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
    while (city != 'chicago') and (city != 'new york city') and (city != 'washington'):
        print('Please use one of those names: Chicago, New York City, Washington.')
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()

    all = input('Would you like to filter the data by month, day? (Yes / No)\n').lower()

    while True:
        if all == 'yes':

            # get user input for month (all, january, february, ... , june)
            month = input('(If you choose month) Which month - January, February, March, April, May, or June?\n').lower()

            while (month != 'january') and (month != 'february') and (month != 'march') and (month != 'april') \
                and (month != 'may') and (month != 'june') and (month != 'all'):
                print('Please use one of those names: All, January, February, March, April, May, or June.')
                month = input('(If you choose month) Which month - January, February, March, April, May, or June?\n').lower()

                # get user input for day of week (all, monday, tuesday, ... sunday)
            day = input('(If you choose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()

            while (day != 'monday') and (day != 'tuesday') and (day != 'wednesday') and (day != 'thursday') and (day != 'friday') \
                and (day != 'saturday') and (day != 'sunday') and (day != 'all'):
                print('Please use one of those names: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.')
                day = input('(If you choose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
            break

        if all == 'no':
            month = 'all'
            day = 'all'
            break

        else:
            all = input('Would you like to filter the data by month, day? (Yes / No)\n').lower()

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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_l = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month_l]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most popular month: ', months[df['month'].value_counts().idxmax() - 1], ' Count: ', df['month'].value_counts().max())

    # TO DO: display the most common day of week
    print('Most popular day of week: ', df['day_of_week'].value_counts().idxmax(), ' Count: ', df['day_of_week'].value_counts().max())

    # TO DO: display the most common start hour
    print('Most popular hour: ', df['hour'].value_counts().idxmax(), ' Count: ', df['hour'].value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most popular start station: ', df['Start Station'].value_counts().idxmax(), ' Count: ', df['Start Station'].value_counts().max())

    # TO DO: display most commonly used end station
    print('Most popular end station: ', df['End Station'].value_counts().idxmax(), ' Count: ', df['End Station'].value_counts().max())

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end_station'] = df['Start Station'] + ' to ' + df['End Station']
    print('Most popular trip (start station and end station): ', df['start_end_station'].value_counts().idxmax(), ' Count: ', df['start_end_station'].value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['total_travel_time'] = df['End Time'] - df['Start Time']
    print('Total travel time for chosen period: ', df['total_travel_time'].sum())

    # TO DO: display mean travel time
    print('Mean travel time for chosen period: ', df['total_travel_time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if (city == 'chicago') or (city == 'new_york_city'):
        print('Counts of gender:')
        print(df['Gender'].value_counts())
    else:
        print('Counts of gender are not available for Washington.')

    # TO DO: Display earliest, most recent, and most common year of birth (not available for Washington)
    if (city == 'chicago') or (city == 'new_york_city'):
        print('Earliest year of birth: ', int(df['Birth Year'].min()))
        print('Most recent year of birth: ', int(df['Birth Year'].max()))
        print('Most common year of birth: ', int(df['Birth Year'].value_counts().idxmax()))
    else:
        print('Year of birth data not available for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays raw data. Number of rows is selected by the user.
    Then, asks the user if 5 more row should be displayed."""

    user_input = input('Would you like to see raw data? Yes / No \n').lower()
    should_finish = False

    while should_finish != True:
        if user_input == 'yes':
            n = int(input('How many rows? eg. 5, 10\n'))
            for number in range(n):
                row_df = df.iloc[number]
                print(row_df)
                print('-'*40)
            continuation = input('Would you like to see 5 more rows? Yes / No \n').lower()
            n_cont = n
            while should_finish != True:
                if continuation == 'yes':
                    for number in range(n_cont, n_cont + 5):
                        row_df = df.iloc[number]
                        print(row_df)
                        print('-'*40)
                    n_cont = n_cont + 5
                    continuation = input('Would you like to see 5 more rows? Yes / No \n').lower()
                if continuation == 'no':
                    print('Finishing program.')
                    should_finish = True

        if user_input == 'no':
                print('Finishing program.')
                should_finish = True

        if (user_input != 'no') and (user_input != 'yes'):
            user_input = input('Would you like to see raw data? Yes / No').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
