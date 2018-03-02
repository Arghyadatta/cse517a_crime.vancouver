from common import *

def analysis(df):
    print "The different columns in the dataset are: ", df.columns.tolist()
    print
    print 'Types of Criminal Activities Reported: ', len(set(df.TYPE.tolist()))
    print
    print 'Various Types of Criminal Activities Reported: '
    for i in set(df.TYPE.tolist()): print i
    print
    print "Types of Neighbourhood :", len(set(df.NEIGHBOURHOOD.tolist()))
    print
    print "Various Types of Neighbourhood :"
    for i in set(df.NEIGHBOURHOOD.tolist()): print i
    print
    print "Per Type count values:"
    print df['TYPE'].value_counts().sort_index()

def crimes_per_YEAR(df):
    year = Input("Enter Year for analysis: ")
    month = Input("Enter Month for analysis")
    print "--------------------------------------------------------------------"
    print "Crimes from: ", year, " and Month: ", mon
    df = df[df.YEAR == year]
    df = df[df.MONTH == month]
    print df['TYPE'].value_counts().sort_index()

def crimes_per_day(df):
    df.index = pd.DatetimeIndex(df['DATE'])
    plt.figure(figsize=(15,6))
    plt.title('Distribution of Crimes per day', fontsize=16)
    plt.tick_params(labelsize=14)
    sns.distplot(df.resample('D').size(), bins=60);

def time_series_crimes_per_day(df):
    df.index = pd.DatetimeIndex(df['DATE'])
    # we need to create a range of possible values
    data_daily = pd.DataFrame(df[df.DATE != "2011-06-15"].resample('D').size())
    data_daily['MEAN'] = df[df.DATE != '2011-06-15'].resample('D').size().mean()
    data_daily['STD'] = df[df.DATE != '2011-06-15'].resample('D').size().std()
    upper_limit = data_daily['MEAN'] + 2 * data_daily['STD']
    lower_limit = data_daily['MEAN'] - 2 * data_daily['STD']

    plt.figure(figsize=(15,6))
    df.resample('D').size().plot(label='Crimes per day')
    upper_limit.plot(color='red', ls='--', linewidth=1.5, label='UCL')
    lower_limit.plot(color='red', ls='--', linewidth=1.5, label='LCL')
    data_daily['MEAN'].plot(color='red', linewidth=2, label='Average')
    plt.title('Total crimes per day', fontsize=16)
    plt.xlabel('Day')
    plt.ylabel('Number of crimes')
    plt.tick_params(labelsize=14)
    plt.legend(prop={'size':16});

def data_per_day(df):
    df.index = pd.DatetimeIndex(df['DATE'])
    date = Input("Please type a date in the format yyyy-mm-dd")
    print ("Number of crimes on " + date + " as per records:  ", len(df[date]))
    print ("Types of crimes on "+date)
    print df[date]['TYPE'].value_counts()
    print "--------------------------------------------------------------------"
    print "Neighbourhood of crimes on "+date
    print df[date]['NEIGHBORHOOD'].value_counts()
    print "Hours of crime on "+date
    print df[date]['HOUR'].value_counts()

   
if __name__ == "__main__":
    df = pd.read_csv("raw_data/crime.csv")
    df['DATE'] = df.YEAR.astype('str').map(str) + '/' + df.MONTH.astype('str') + '/' +df.DAY.astype('str')
    df.DATE = df.DATE.apply(pd.to_datetime).dt.date
    df['TIME'] = df.HOUR.astype('int64').astype('str') + ':' + df.MINUTE.astype('int64').astype('str')
    
    analysis(df)   
    crimes_per_YEAR(df)

