import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Birkbeck_University_of_London_U'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSACCG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSACC9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSACCN9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSACCNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSACM9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSACMN9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSACMN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSACMNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSACMF_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSACMGF_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSACFN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSACFIN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAANHA_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAANHAR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSAPABU_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSAPABJ_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAARCH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAARCHY_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAACGE_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAARCGE_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAARHM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAARHUM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAARHUD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFARHM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAARMD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAARMED_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFAARTMM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSBIOM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSBIOMC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSBIOMD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBMMOBI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFBIOM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSBUS9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSBUSN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSBUSN9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSBUSNS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSBUPS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSBUPSY_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFBUSN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBBCHMAN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBACLSD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBACLSDS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBACLSC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBACLSCS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSCVP9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSCVPP9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSCOMPT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSCOMP_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSCOMPG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFCOMP_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUFSCITW_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFSCITWO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFSCOIT9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFSCOITW_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBACOHP_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBACONHP_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBACWRT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBACWRIT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBACWEN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSCRIM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSCRIMG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBBCULM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSDATS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSDATSC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSDGLB_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSDGLOB_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSDIGTS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHEAHIS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSEASCI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSECSL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSECSLL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSECNM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSECNMC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSECBS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSECBUS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFECBS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSECMT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSECMAT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAENGL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAENGLS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSGLEVI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSEVMN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSEVMNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAFMED_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAFMMED_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSFIEC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSFIECO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSFEAC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSFNEAC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAFRCH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAFRNCH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAFRNCD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAFRIX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSGEOG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSGEOGY_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSGLGY_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSGLOGY_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSGLOGD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHGLOGY_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAGERM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAGERMN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAGERMD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAGMIX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAGLPR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAGLPIR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHHEIN9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHHEINT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAHIST_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAHISTO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAHIAR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAHIARC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAHSIR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAHISIR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAAHIS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHIST_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHISD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAAHHI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHWHI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHHID_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAACUR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHCUR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHCUD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAAHFM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHFMD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAAHWFM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAHUGE_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAHUMGE_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFIMNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSIMNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSIYMNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAICMX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAICML_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAINCM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAICOMD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAICOML_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAINTCM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAINTCD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUCHINTG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUCHINTH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUCHINTP_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUCHINTS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAJRME_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAJRMDD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAJRMED_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFSLABSC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGEN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNGEN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGEND_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNIX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNFX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGFM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNGFM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNGFD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNPX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGGP_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGGPO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGGPD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGHI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNGHI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNGHD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNHX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNWX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGLW_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNGLW_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGLWD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNJX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNJR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNJOD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNJOR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNMX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGMN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGMAN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGMND_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALPOX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGPO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGPOL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALGPOD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBLLAWL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBLLAWLL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFLAWL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHLAWLM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHLIFSC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHLIFS2_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHLIFSJ_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALLNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALILNG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALILGD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHLINGC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALGLX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAMNGN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAMNGNT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUFAMNO9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFAMNGMO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFAMNGO9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUFAMNGO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUFAMCO9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFAMNCO9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFAMNACO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUFAMNCO_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSMKTG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSMAKTG_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHMATHS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHMATH2_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSMTHT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSMTHMT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHMTHMT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UDHMTHMT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSMTST_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSMTSTA_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSMWAC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSMTWAC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSMWEC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSMTWEC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSMWMN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSMTWMN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAMDCU_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAMDCUL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAMDCUD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHMIVOC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNMD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBALNMDR_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBALNDX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAPLPH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAPLPHY_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHPHYMA_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHPHYM2_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSPSAS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSPSAST_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHPSAST_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAPOLT_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAPOLTC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAPOPH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAPOPHI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSPRFS9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSPRFST_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHPCSP9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UCHPCSPF_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSPSYC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSPSYCH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAPCHED_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UFSPSYCH_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFPSYC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAPSYS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAPSYSL_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBAPPDC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBAPAPDC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSSOS9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBSSOSC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSSOSC9_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSSOSCI_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBFSOSC_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBASPLX_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBASPLM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBASPLMD_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBASPLAM_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBSSTECN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBATS_D_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBATS_DS_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UUBATSEN_C/',
'http://www.bbk.ac.uk/study/2019/undergraduate/programmes/UBATS_EN_C/',]

    for i in C:
        fullurl = base_url % i
        start_urls.append(fullurl)
    def parse(self, response):
        pass
        # print(response.url)
        item = UcasItem()
        university = 'Birkbeck, University of London'
        try:
            location = 'Central London'
            #location = remove_tags(location)
            #location = remove_tags(location)
            #print(location)
        except:
            location = 'n/a'
            #print(location)
        try:
            department = response.xpath('').extract()
            department = remove_tags(department)
        except:
            department = ''

        try:
            degree_name = response.xpath('//h1').extract()[0]
            degree_name = remove_tags(degree_name)
            degree_name = re.findall('\((.*)\)',degree_name)[0]
            #degree_name = degree_name.replace('\n',degree_name)
            #print(degree_name)
        except:
            degree_name = ''

        try:
            degree_overview_en = ''
            degree_overview_en = remove_tags(degree_overview_en)
            degree_overview_en = "<div><p>" + degree_overview_en + "</p></div>"
            #print(degree_overview_en)
        except:
            degree_overview_en = ''

        try:
            programme_en = response.xpath('//h1').extract()[0]
            programme_en = remove_tags(programme_en)
            programme_en = re.findall("(.*)\(.*\)",programme_en)[0]
            #programme_en = programme_en.replace('\n','')
            #programme_en = programme_en.replace('  ','')
            #print(programme_en)
        except:
            programme_en = ''
            #print(programme_en)

        try:
            overview_en = response.xpath('//*[@id="content"]/div[5]').extract()[0]
            overview_en = remove_tags(overview_en)
            overview_en = '<div>'+overview_en +'</div>'
            overview_en = overview_en.replace('  ','')
            overview_en = overview_en.replace('\n\n','\n')
            overview_en = overview_en.replace('\n\n','\n')
            #overview_en = remove_tags(overview_en)
            #print(overview_en)
        except:
            overview_en = ''

        try:
            start_date = '10'

            #print(start_date)
        except:
            start_date = ''


        try:
            modules_en = response.xpath('//*[@id="courseStructure"]').extract()[0]
            modules_en = remove_tags(modules_en)
            modules_en = modules_en.replace('\n\n','\n')
            modules_en = modules_en.replace('\r\n','')
            modules_en = modules_en.replace('  ','')
            modules_en = "<div><p>" + modules_en + "</p></div>"
            #print(modules_en)
        except:
            modules_en = 'N/A'
            #print(modules_en)

        apply_fee = 0

        try:
            degree_requirements = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[2]/div[2]/div[1]/div[2]').extract()[0]
            degree_requirements = remove_tags(degree_requirements)
            degree_requirements = degree_requirements.replace('  ','')
            #print(degree_requirements)
        except:
            degree_requirements = ''
            #print(degree_requirements)

        try:
            rntry_requirements_en = response.xpath('//*[@id="content"]/div[8]/div/div[2]').extract()[0]
            rntry_requirements_en = remove_tags(rntry_requirements_en)
            rntry_requirements_en = rntry_requirements_en.replace('  ','')
            rntry_requirements_en = rntry_requirements_en.replace('\n','')
            rntry_requirements_en = re.findall('Entry requirements(.*)Visa requirements',rntry_requirements_en)[0]
            #print(rntry_requirements_en)
        except:
            rntry_requirements_en = ''

        try:
            professional_background = response.xpath('').extract()
            professional_background = remove_tags(professional_background)
        except:
            professional_background = ''

        try:
            ielts_desc = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div[1]/table[2]/tbody[2]/tr[1]/td[2]').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
            #print(ielts_desc)
        except:
            ielts_desc = 'If English is not your first language or you have not previously studied in English, our usual requirement is the equivalent of an International English Language Testing System (IELTS Academic Test) score of 6.5, with not less than 6.0 in each of the sub-tests.'

        try:
            ielts = '6.5'
            #i#elts = remove_tags(ielts)
            #print(ielts)
        except:
            ielts = '6.5'

        try:
            ielts_l = re.findall('(\d.\d)',ielts_desc)[1]
            #print(ielts_l)
            #ielts_l = remove_tags(ielts_l)
        except:
            ielts_l = '6.0'

        try:
            ielts_s = ielts_l

        except:
            ielts_l = ''

        try:
            ielts_r = ielts_l
        except:
            ielts_l = ''

        try:
            ielts_w = ielts_l
        except:
            ielts_l = ''

        try:
            toefl_code = response.xpath('').extract()
            toefl_code = remove_tags(toefl_code)
        except:
            toefl_code = ''

        try:
            toefl_desc = response.xpath('').extract()
            toefl_desc = remove_tags(toefl_desc)
        except:
            toefl_desc = ''

        try:
            toefl = response.xpath('').extract()
            toefl = remove_tags(toefl)

        except:
            toefl = ''

        try:
            toefl_l = response.xpath('').extrcat()
            toefl_l = remove_tags(toefl_l)

        except:
            toefl_l = ''

        try:
            toefl_s = response.xpath('').extract()
            toefl_s = remove_tags(toefl_s)

        except:
            toefl_s = ''

        try:
            toefl_r = response.xpath('').extract()
            toefl_r = remove_tags(toefl_r)
        except:
            toefl_r = ''

        try:
            toefl_w = response.xpath('').extract()
            toefl_w = remove_tags(toefl_w)
        except:
            toefl_w = ''

        try:
            work_experience_desc_en = response.xpath('//*[@id="content"]/div[13]/div/a/div/div[1]/p').extract()[0]
            work_experience_desc_en = remove_tags(work_experience_desc_en)
            #print(work_experience_desc_en)
        except:
            work_experience_desc_en = ''

        try:
            interview_desc_en = response.xpath('').extract()
            interview_desc_en = remove_tags(interview_desc_en)
        except:
            interview_desc_en = ''

        try:
            portfolio_desc_en = response.xpath('').extract()
            portfolio_desc_en = remove_tags(portfolio_desc_en)
        except:
            portfolio_desc_en = ''

        try:
            apply_desc_en = 'If English is not your first language or you have not previously studied in English, our usual requirement is the equivalent of an International English Language Testing System (IELTS Academic Test) score of 6.5, with not less than 6.0 in each of the sub-tests.'
            apply_desc_en = remove_tags(apply_desc_en)
            apply_desc_en = "<div>" + apply_desc_en + "</div>"
            #print(apply_desc_en)
        except:
            apply_desc_en = ''

        try:
            apply_documents_en = '<p>birth certificate or passport IELTS English Language certificate degree certificate or transcript additional documentation requested by Registry. Please note: documentation that may be required by the Admissions Tutor in the relevant school and this should be sent directly to the school.</p>'
            apply_documents_en = remove_tags(apply_documents_en)
        except:
            apply_documents_en = ''


        #other = ''
        try:
            apply_proces_en = response.xpath('').extract()
        except:
            apply_proces_en = ''


        try:
            duration =  response.xpath('//h1').extract()[0]
            duration = remove_tags(duration)
            duration = re.findall('(\d)',duration)[0]
            #print(duration)
        except:
            duration = 'N/A'
            #print(duration)



        try:
            other = response.xpath('//*[@id="what-you-will-study"]/div/div[1]/div[1]/div[2]/div/div[2]/div/div/a').extract()[0]
            other = remove_tags(other)
            #print('成功'+ other + response.url)
        except:
            other = ''
           #print('失败' + other)

        try:
            ib = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div[1]/table[1]/tbody/tr[11]/td[2]').extract()[0]
            ib = remove_tags(ib)
            #print(ib)
        except:
            ib = ''
            #print(ib)

        try:
            alevel = response.xpath('//*[@id="content"]/div[8]/div/div[2]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = alevel.replace('\n','')
            alevel = alevel.replace('\r\n','')
            alevel = re.findall("UCAS.*?(\d\d\d)",alevel)[0]
            #print(alevel)
        except:
            alevel = 'N/A'
            #print(alevel)
        try:
            ucascode = response.xpath('//*[@id="content"]/div[2]/div[1]/dl/dd[5]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = response.xpath('//*[@id="content"]/div[8]/div/div[2]').extract()[0]
            tuition_fee = remove_tags(tuition_fee)
            tuition_fee = tuition_fee.replace('  ','')
            tuition_fee = tuition_fee.replace('\n','')
            tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0

        try:
            assessment_en = response.xpath('//body').extract()[0]
            assessment_en = remove_tags(assessment_en)
            assessment_en = assessment_en.replace('\n','')
            assessment_en = assessment_en.replace('\r\n','')
            assessment_en = re.findall('Assessment(.*)Methods of assessment on this course',assessment_en)[0]
            #assessment_en = assessment_en.replace('  ', ' ')
            #assessment_en = assessment_en.replace('\n', '')
            assessment_en = assessment_en.replace('                                                                                                ','')
            #assessment_en = assessment_en.replace('		','')
            assessment_en = "<div>"+assessment_en+'</div>'
            #print(assessment_en)
        except:
            assessment_en = 'N/A'
            #print(assessment_en)

        try:
            career_en = response.xpath('//body').extract()[0]
            career_en = remove_tags(career_en)
            career_en = career_en.replace('\n','')
            career_en = career_en.replace('\r\n','')
            career_en = re.findall('Careers and employability(.*)How to apply',career_en)[0]
            #career_en = career_en.replace('  ', ' ')
            #career_en = career_en.replace('\n', '')
            career_en = career_en.replace('                                                                    ','')
            career_en = career_en.replace('                                                        ','')
            career_en = "<div>"+career_en+'</div>'
            #print(career_en)
        except:
            career_en = 'N/A'
            #print(career_en)


        item["university"] = university
        item["location"] = location
        item["department"] = department
        item["degree_type"] = 1
        item["degree_name"] = degree_name
        #item["degree_overview_en"] = degree_overview_en
        item["programme_en"] = programme_en
        item["overview_en"] = overview_en
        item["teach_time"] = 1
        item["start_date"] = start_date
        item["modules_en"] = modules_en
        item["career_en"] = career_en
        item["application_open_date"] = 'all year'
        item["deadline"] = ''
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_end
        item["degree_requirements"] = degree_requirements
        item["tuition_fee_pre"] = '£'
        #item["major_requirements"] = rntry_requirements_en
        item["professional_background"] = professional_background
        item["ielts_desc"] = ielts_desc
        item["ielts"] = ielts
        item["ielts_l"] = ielts_l
        item["ielts_s"] = ielts_l
        item["ielts_r"] = ielts_l
        item["ielts_w"] = ielts_l
        item["toefl_code"] = toefl_code
        item["toefl_desc"] = toefl_desc
        item["toefl"] = 0
        item["toefl_l"] = 0
        item["toefl_s"] = 0
        item["toefl_r"] = 0
        item["toefl_w"] = 0
        item["work_experience_desc_en"] = work_experience_desc_en
        item["interview_desc_en"] = interview_desc_en
        item["portfolio_desc_en"] = portfolio_desc_en
        item["apply_desc_en"] = apply_desc_en
        item["apply_documents_en"] = apply_documents_en
        item["other"] = other
        item["url"] = response.url
        item["gatherer"] = 'weihongbo'
        item["apply_proces_en"] = apply_proces_en
        item["batch_number"] = 5
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        item["alevel"] = alevel
        item["ib"] = ib
        item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["assessment_en"] = assessment_en
        #item["apply_pre"] = ''
        yield item


