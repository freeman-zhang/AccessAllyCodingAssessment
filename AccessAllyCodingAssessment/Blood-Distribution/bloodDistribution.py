import sys

class Solution(object):
    def bloodDistribution(self, bloodAvailable, bloodNeeded):
        # blood = [O-, O+, A-, A+, B-, B+, AB-, AB+]
        # O receive O
        # A receive A, O
        # B receive B, O
        # AB receive A, B, O, AB
        # RH- receive RH-
        # RH+ recieve RH-, RH+
        #
        #Algorithm:
        #Everyone gets their own blood first 
        #Remaining A, B goes to AB
        #Remaing O goes to A, B, AB
        
        count = 0
        #everyone gets their own blood
        for i in range(len(bloodAvailable)):
            canReceive = min(bloodAvailable[i], bloodNeeded[i])
            count += canReceive
            bloodAvailable[i] -= canReceive
            bloodNeeded[i] -= canReceive

        #every RH+ gets their RH- counterpart
        #O
        canReceive = min(bloodAvailable[0], bloodNeeded[1])
        count += canReceive
        bloodAvailable[0] -= canReceive
        bloodNeeded[1] -= canReceive
        #A
        canReceive = min(bloodAvailable[2], bloodNeeded[3])
        count += canReceive
        bloodAvailable[2] -= canReceive
        bloodNeeded[3] -= canReceive
        #B
        canReceive = min(bloodAvailable[4], bloodNeeded[5])
        count += canReceive
        bloodAvailable[4] -= canReceive
        bloodNeeded[5] -= canReceive
        #AB
        canReceive = min(bloodAvailable[6], bloodNeeded[7])
        count += canReceive
        bloodAvailable[6] -= canReceive
        bloodNeeded[7] -= canReceive

        # A and B blood goes to AB
        abnegAvailable = bloodAvailable[2] + bloodAvailable[4]
        canReceive = min(abnegAvailable, bloodNeeded[6])
        count += canReceive
        bloodNeeded[6] -= canReceive

        abposAvailable = bloodAvailable[2] + bloodAvailable[3] + bloodAvailable[4] + bloodAvailable[5]
        canReceive = min(abposAvailable, bloodNeeded[7])
        count += canReceive
        bloodNeeded[7] -= canReceive

        # O blood goes to everyone remaining
        negativeBloodNeeded = bloodNeeded[0] + bloodNeeded[2] + bloodNeeded[4] + bloodNeeded[6]
        positiveBloodNeeded = bloodNeeded[1] + bloodNeeded[3] + bloodNeeded[5] + bloodNeeded[7]

        canReceive = min(negativeBloodNeeded, bloodAvailable[0])
        count += canReceive
        negativeBloodNeeded -= canReceive
        bloodAvailable[0] -= canReceive

        canReceive = min(positiveBloodNeeded, bloodAvailable[0] + bloodAvailable[1])
        count += canReceive
        positiveBloodNeeded -= canReceive

        return count

if len(sys.argv) < 2:
    print("Enter a file to test, \'all\' to run all tests")
else:
    filename = sys.argv[1]
    if ('/' not in filename):
        filename = 's4/' + filename
    with open(filename) as file:
        blood = file.readlines()
    bloodAvailable = blood[0].split()
    bloodAvailableList = list(map(int, bloodAvailable))
    bloodNeeded = blood[1].split()
    bloodNeededList = list(map(int, bloodNeeded))
    main = Solution()
    print(main.bloodDistribution(bloodAvailableList, bloodNeededList))