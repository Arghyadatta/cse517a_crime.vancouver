from common import *

def analysis():
    df = pd.read_csv("raw_data/crime.csv")
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

# Distribution of crimes per day

def crimes_per_YEAR():
    year = 2010
    mon = 12
    print "--------------------------------------------------------------------"
    print "Crimes from: ", year, " and Month: ", mon
    df = pd.read_csv("raw_data/crime.csv")
    df = df[df.YEAR == year]
    df = df[df.MONTH == mon]
    print df['TYPE'].value_counts().sort_index()
    
if __name__ == "__main__":
    analysis()   
    crimes_per_YEAR()

