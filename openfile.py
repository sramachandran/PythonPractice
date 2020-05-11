def count_of_records(fname):
    count = 0
    with open(fname,'r') as f:
        for line in f:
            count +=1
    print("count of records:", count)


count_of_records("HR Metrics to BI.txt")