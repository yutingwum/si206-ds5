import re
import unittest

# TODO: read dataset.txt under data folder
# hint: what is the file path?
f = open("", "r")

data = f.read()

# TODO:
# store all url (start with http:// or https://) in all_url variable
# The outcome should be similar to this:
# ["http://abc.com", "http://edf.com"]
regex = r""
all_url = re.findall(regex, data, re.MULTILINE)

# TODO:
# store all url which country is either United States or Japan in a list of
# Tuple and assign it to variable country_url, the outcome should be similar
# to this:
# [("https://abc.com/", "United States"), ("https://edf.co.jp", "Japan")]
regex = r""
country_url = re.findall(regex, data, re.MULTILINE)

# TODO:
# store all email address in all_email as a list
# the result should be similar to this:
# ["abc@coj.fd", "bcd@ee1.ab.jp"]
regex = r""
all_email = re.findall(regex, data, re.MULTILINE)

# TODO:
# store all email with gmail as domain in gmail_email as a list. It should
# include @gmail.com, @gmail.co.jp, @gmail.com.tw and so on.
regex = r""
gmail_email = re.findall(regex, data, re.MULTILINE)

# TODO:
# store all edu email in edu_email as a list. It should include all email ends
# with .edu
regex = r""
edu_email = re.findall(regex, data, re.MULTILINE)

# TODO:
# store all uniqname email in uniqname_list as a list. It should include only
# the username part of the email which the domain is @umich.edu
regex = r""
uniqname_list = re.findall(regex, data, re.MULTILINE)


#### -----------------------------------------------------------------
#### You don't need to modify the code below
#### -----------------------------------------------------------------
class RegTest(unittest.TestCase):
    def test_all_url(self):
        answer = ['http://www.google.com', 'http://www.yelp.com', 
                    'http://www.samsung.co.kr', 'http://www.oracle.com', 
                    'https://www.tencent.com', 'http://cars.mclaren.com', 
                    'http://www.lotuscars.com', 'https://orangeamps.com', 
                    'http://www.korg.com']
        self.assertEqual(all_url, answer)
    def test_country_url(self):
        answer = [('http://www.google.com', 'United States'), 
                    ('http://www.yelp.com', 'United States'), 
                    ('http://www.oracle.com', 'United States'), 
                    ('http://www.korg.com', 'Japan')]
        self.assertEqual(country_url, answer)
    def test_all_email(self):
        answer = ['maurammy@hinet.net', 'bichengx@hinet.net', 
                    'jonssona@gmail.com', 'nagarw@yahoo.com', 
                    'ssreddy@yahoo.co.uk', 'ohworth@gmail.co.jp', 
                    'dustinlh@umich.edu', 'jribolla@yahoo.co.uk', 
                    'edgarn@umich.edu', 'jshank@gmail.co.jp', 
                    'rohtikoo@gmail.com', 'peiyaoh@yahoo.com',
                    'pfigura@icloud.com', 'awpearlm@hinet.net', 
                    'samarthg@mit.edu', 'estwee@gmail.co.jp', 
                    'amykuo@yahoo.com', 'ramkumar@hinet.net', 
                    'peiting@yahoo.co.uk', 'purvak@gmail.com', 
                    'rohilp@gmail.com', 'henqian@gmail.com', 
                    'srshetty@gmail.com.tw', 'hhwong@gmail.com.tw', 
                    'dlouie@icloud.com', 'asheikh@umich.edu', 
                    'chijim@yahoo.com', 'kaveri@gmail.co.jp', 
                    'lingbo@gmail.com.tw', 'ibramo@hinet.net', 
                    'smithale@eecs.mit.edu', 'aravindb@icloud.com', 
                    'gingrasl@mit.edu', 'katieand@gmail.com.tw', 
                    'annasr@gmail.co.jp', 'kesun@icloud.com', 
                    'chhemmin@icloud.com', 'robthomp@eecs.mit.edu', 
                    'morelm@hinet.net', 'cbledsoe@eecs.mit.edu', 
                    'shenwan@gmail.co.jp', 'jillmeye@gmail.com',
                    'aschri@yahoo.com', 'ambail@umich.edu', 
                    'jungar@gmail.co.jp', 'jessabm@hinet.net']
        self.assertEqual(all_email, answer)
    def test_gmail_email(self):
        answer = ['jonssona@gmail.com', 'ohworth@gmail.co.jp', 
                    'jshank@gmail.co.jp', 'rohtikoo@gmail.com', 
                    'estwee@gmail.co.jp', 'purvak@gmail.com', 
                    'rohilp@gmail.com', 'henqian@gmail.com', 
                    'srshetty@gmail.com', 'hhwong@gmail.com', 
                    'kaveri@gmail.co.jp', 'lingbo@gmail.com', 
                    'katieand@gmail.com', 'annasr@gmail.co.jp', 
                    'shenwan@gmail.co.jp', 'jillmeye@gmail.com', 
                    'jungar@gmail.co.jp']
        self.assertEqual(gmail_email, answer)
    def test_edu_email(self):
        answer = ['dustinlh@umich.edu', 'edgarn@umich.edu', 
                    'samarthg@mit.edu', 'asheikh@umich.edu', 
                    'smithale@eecs.mit.edu', 'gingrasl@mit.edu', 
                    'robthomp@eecs.mit.edu', 'cbledsoe@eecs.mit.edu', 
                    'ambail@umich.edu']
        self.assertEqual(edu_email, answer)
    def test_uniqname_list(self):
        answer = ['dustinlh', 'edgarn', 'asheikh', 'ambail']
        self.assertEqual(uniqname_list, answer)

if __name__ == "__main__":
    unittest.main(verbosity=2)