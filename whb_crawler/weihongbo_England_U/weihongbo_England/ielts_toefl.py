import re

class ielts_toefl:

    def __init__(self,ucas_ielts):
        #self.ucas_ielts = re.findall('IELTS: (\d)',ucas_ielts)
        self.ucas_ielts = re.findall('(\d+)', ucas_ielts)


ucas_ielts = 'Applicants should possess a Master\'s degree from a UK university or hold an equivalent qualification; an overall merit or equivalent, with merit in the dissertation is normally required; applicants should submit a research proposal on a relevant subject; non-native speakers of English are normally also required to satisfy minimum English language requirements such as: IELTS: 7 (with a minimum of 6.5 in each section) or equivalent; TOEFL iBT: 93 (minimum 26 in writing, 22 in speaking, 19 in listening, 18 in reading); Pearson Academic: 63 (minimum 63 in writing and speaking, and 57 in reading and listening); Cambridge Certificate of Proficiency in English (CPE): Grade B; Cambridge Certificate in Advanced English (CAE): Grade A.'
a = ielts_toefl(ucas_ielts)

print(a.ucas_ielts)