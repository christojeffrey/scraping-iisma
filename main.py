import re
import requests

from getUnivData import getUnivData


x = requests.get('https://iisma.kemdikbud.go.id/info/host-universities-list/', verify=False)

# get data-elementor-lightbox-title, then find the href in the same line. put it in a list
y = re.findall(r'data-elementor-lightbox-title=".*?" href="(.*?)"', x.text)

univList = []
# split by , push to list
for i in y:
    univList.append(i.split(','))



# flatten
univList = [item for sublist in univList for item in sublist]

# remove duplicate
univList = list(dict.fromkeys(univList))

# print
# result consist of university name, link, requirement, course, TOEFL iBT score, IELTS score, DET score
result = []
for i in range(len(univList)):
    print(i, univList[i])
    result.append(getUnivData(univList[i]))

# write as csv with header
import csv
with open('univData.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['univName', 'link', 'univRequirementDetail', 'univCourse', 'toefl', 'ielts', 'det', 'awardee'])
    writer.writerows(result)


