import re
import requests
# return consist of university name, link, requirement, course, TOEFL iBT score, IELTS score, DET score
def getUnivData(link):
    # get the text
    x = requests.get(link, verify=False)


    # write text to file

    # get text inside <a>  with the class elementor-toggle-title using regex
    # <a href="" class="elementor-toggle-title">World Cinema</a>
    univCourse = re.findall(r'<a href="" class="elementor-toggle-title">(.*?)</a>', x.text)
    # <div id="elementor-tab-content-4502" class="elementor-tab-content elementor-clearfix" data-tab="2" role="tabpanel" aria-labelledby="elementor-tab-title-4502" tabindex="0" hidden="hidden">
    univRequirement = re.findall(r'<div id="elementor-tab-content-4502" class="elementor-tab-content elementor-clearfix" data-tab="2" role="tabpanel" aria-labelledby="elementor-tab-title-4502" tabindex="0" hidden="hidden">(.*?)</div>', x.text)

# <title>S06. Yale University &#8211; IISMA</title>
    univName = re.findall(r'<title>(.*?) &#8211; IISMA</title>', x.text)

    # if univRequirement is empty, then it means that the university doesn't have any requirement
    if not univRequirement:
        univRequirement = ['No requirement']
    # if univCourse is empty, then it means that the university doesn't have any course
    if not univCourse:
        univCourse = ['No course']

    # remove html tag <p> and </p> if exist
    univRequirement[0] = re.sub(r'<p>|</p>', '', univRequirement[0])
    # remove html tag <span ...> and </span> if exist
    univRequirement[0] = re.sub(r'<span.*?>|</span>', '', univRequirement[0])
    # remove html tag <br/> and <br /> <br> if exist
    univRequirement[0] = re.sub(r'<br/>|<br />|<br>', '', univRequirement[0])
    # remove &#8211; if exist
    univRequirement[0] = re.sub(r'&#8211;', '', univRequirement[0])
    # remove &nbsp; if exist
    univRequirement[0] = re.sub(r'&nbsp;', '', univRequirement[0])

# add space behind to handle regex error
    univRequirement[0] = univRequirement[0] + ' '

    # get the number after TOEFL iBT: . number only
    toefl = re.findall(r'TOEFL iBT: (.*?) ', univRequirement[0])
    # get the first, array. if it's empty, then it means that the university doesn't have TOEFL iBT requirement
    if not toefl:
        toefl = ['No TOEFL iBT requirement']    

    # get the number after IELTS: . number only
    ielts = re.findall(r'IELTS: (.*?) ', univRequirement[0])
    # get the first, array. if it's empty, then it means that the university doesn't have IELTS requirement
    if not ielts:
        ielts = ['No IELTS requirement']
    # get the number after Duolingo English Test: . number only. can be with space around the number or not. example: 95 or  95
    det = re.findall(r'Duolingo English Test: (.*?) ', univRequirement[0])
    # get the first, array. if it's empty, then it means that the university doesn't have DET requirement
    if not det:
        det = ['No DET requirement']

    # if div with id elementor-tab-content-4504 and class lementor-tab-content elementor-clearfix exist, then it means that the university has awardee detais.
    # get the line
    awardee = re.findall(r'<div id="elementor-tab-content-4504" class="elementor-tab-content elementor-clearfix" data-tab="4" role="tabpanel" aria-labelledby="elementor-tab-title-4504" tabindex="0" hidden="hidden">(.*?)</div>', x.text)
    # if awardee is not empty, then it means that the university has awardee details
    if not awardee:
        awardee = ['No awardee details']
    else:
        # <p><strong>Applicants</strong><br />Applicants : 145 students <br />GPA : 3.03-4.00<br />TOEFL iBT Score : 88-96<br />IELTS Score : 6.5-8.5<br />Duolingo English Test Score : 70-155</p><p><strong>Awardees</strong><br />Awardees : 15 students<br />GPA : 3.11-3.96<br />TOEFL iBT Score : &#8211;<br />IELTS Score : 8<br />Duolingo English Test Score : 140-155</p>
        # remove html tag <p> and </p> if exist
        awardee[0] = re.sub(r'<p>|</p>', '', awardee[0])
        # remove html tag <strong> and </strong> if exist
        awardee[0] = re.sub(r'<strong>|</strong>', '', awardee[0])
        # remove html tag <br/> and <br /> <br> if exist
        awardee[0] = re.sub(r'<br/>|<br />|<br>', '', awardee[0])
        # remove &#8211; if exist
        awardee[0] = re.sub(r'&#8211;', '', awardee[0])
        # remove &nbsp; if exist
        awardee[0] = re.sub(r'&nbsp;', '', awardee[0])
        
    



    # return the result
    return [univName[0], link, univRequirement[0], univCourse, toefl[0], ielts[0], det[0], awardee[0]]