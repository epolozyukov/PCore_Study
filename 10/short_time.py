#You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was made:

#Weekday Month Day, time e.g., Friday May 2, 7pm

#You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.

#Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.

#Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".

def shorten_to_date(long_date):
    date =' '.join([x for x in long_date.split()][:-1]).replace(',', '')
    return date

def shorten_to_date2(long_date):
    num = long_date.find(',')
    return long_date[0:num]

date= "Monday February 2, 8pm"
print(shorten_to_date(date))
print(shorten_to_date2(date))