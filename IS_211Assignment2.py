import urllib2, datetime, logging, argparse

LOG_FILENAME = 'errors.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.ERROR)

def downloadData(url):
    response = urllib2.urlopen(url)
    return response.read()


def processData(csvData):
    personData = {}
    data = csvData.split('\n')

    for i in data[1:-1]:
        x = i.split(',')
        id = int(x[0])
        try:
            dateLst = map(int, x[2].split('/'))
            dateObj = datetime.date(dateLst[2], dateLst[1], dateLst[0])
            personData[id] = (x[1], dateObj)
        except:
            log.error("Error processing line %d for ID %d" % (id+1, id))

    return personData


def displayPerson(id, personData):
    try:
        pd = personData[id]
        print("Person #%d is %s with a birthday of %s" % (id, pd[0], pd[1]))
    except KeyError:
        print("No user found with that id")
    
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="URL for downloading birthday data")
args = parser.parse_args()
try:
    if args.url:
        csvData = downloadData(args.url)
    else:
        raise NameError("URL not specified.")
    log = logging.getLogger('assignment2')
    personData = processData(csvData)
    
    while True:
        id = int(str(raw_input("Enter an ID")))
        if id<=0:
            break
        displayPerson(id, personData)
    
except Exception as e:
    print(e)
