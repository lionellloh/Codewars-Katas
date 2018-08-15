# https://www.codewars.com/kata/52996b5c99fdcb5f20000004/train/python


def runoff(voters):
    record = dict()
    # Tallying


    num_voters = len(voters)

    base_case = [ [] for voter in voters]
    print("base case: {}".format(base_case))

    for votes in voters:
        if votes != []:
            if record.get(votes[0], None):
                record[votes[0]] += 1

            else:
                record[votes[0]] = 1

    print(record)

    for k,v in record.items():
        # Check first condition
        print("v is {}, k is {}, num_voters/2 is {}".format(v, k, num_voters/2))
        if v > num_voters/2:
            print("can")
            # break
            return k

            print("really")
        else:
            print("cannot")
        # Remove the last
    to_be_removed = []
    smallest = len(voters)
    for k, v in record.items():
        if v < smallest:
            smallest = v
            to_be_removed = []
            to_be_removed.append(k)

        elif v == smallest:
            to_be_removed.append(k)

        print("TO BE REMOVED", to_be_removed)

        for votes in voters:
            for r in to_be_removed:
                print(r)
                print("VOTES", votes)
                votes.remove(r)




        print(voters)

        to_be_removed = []

    print("voters: {}".format(voters))
    if voters == base_case:
        print("LOL")
        return None

    else:
        runoff(voters)




voters = [['dem', 'ind', 'rep'], ['rep', 'ind', 'dem'], ['ind', 'dem', 'rep'], ['ind', 'rep', 'dem']]

print(runoff(voters))