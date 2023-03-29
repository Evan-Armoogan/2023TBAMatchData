import csv

def get_dict():
    f = open("scout_data.csv", "r")
    data = list(csv.DictReader(f, delimiter=","))
    f.close()
    return data

def get_scouts_list(data):
    scouts = []
    for row in data:
        if not (row['Scout'] in scouts):
            scouts.append(row["Scout"])
    return scouts

def get_scout_accuracy(data, scouts):
    scout_dict = {}
    for scout in scouts:
        sum = 0
        occurrences = 0
        for row in data:
            if row["Scout"] == scout:
                match_accuracy = ((float(row["Mobility Accuracy"]) + float(row["Auto Bridge Accuracy"]) + float(row["Endgame Bridge Accuracy"]))/3)*0.3 + ((float(row["Alliance Auto Accuracy"]) + float(row["Alliance Tele Accuracy"]))/2)*0.7
                sum += match_accuracy
                occurrences += 1
        scout_accuracy = sum/occurrences
        scout_dict[scout] = scout_accuracy
    return scout_dict

def write_file(scout_list, scout_dict):
    f = open("scout_accuracy.csv", "w")
    line = "Scout,Accuracy\n"
    f.write(line)
    for scout in scout_list:
        line = f"{scout},{scout_dict[scout]}\n"
        f.write(line)
    f.close()
    

def main():
    data = get_dict()
    scouts = get_scouts_list(data)
    scout_dict = get_scout_accuracy(data, scouts)
    write_file(scouts, scout_dict)
    print("Complete")

if __name__ == "__main__":
    main()


    


