import scrapy
from bs4 import BeautifulSoup
from weihongbo_England.items import UcasItem
from weihongbo_England import items
from w3lib.html import remove_tags
import re
import time
class BaiduSpider(scrapy.Spider):
    name = 'Birkbeck_University_of_London_P'
    allowed_domains = []
    base_url= '%s'
    start_urls = []
    C = ['http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSACFMN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSACTEC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSABIOS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDABIOS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCHANL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDCHANL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAALCOM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSTAPP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCSTAPP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSASFMO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSARCHP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAARCHP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDAPLMN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAAPLMN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCAPLMN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBIOBS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBOWSB_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRBOWSB_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCBUSIN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBIEBI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBIEIM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBIITM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCOACG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRCHMST_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCHIYD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACLARC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACLCVL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACLSSC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCLICH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCCLICH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDCLICH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCCLOUD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCCLODD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCCOACH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACOGCO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCOGCO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCOGNP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACOGNP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMALITCS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRLITCS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRCOSCI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCOSCI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCOMFS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLCPLTH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLCPLTI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHI_PO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACOLIT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGVETH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCGVETH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCGVETJ_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCORSS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACCRIT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCRIND_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCCRIMN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACWRIT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMFCWRIT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMJCMLGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSCRIGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACUCRS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDDIASP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCDIASP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMADIASP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSDATSC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMADEVSC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSDEVSC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMADIGMC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMADIGMD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMADIGMM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCDIMMN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHIERL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCEMNTC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGECNMC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSECNMC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSEDPSC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDEDPSC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCEDPSC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAEDNRO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSEDNRO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDENSUS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSENSUS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGGLEVI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHIEUR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSEUPOP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAFMSCR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAFSMEU_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAFPCUR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAFMCUP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSFINAN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSFINAD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSECFIN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSRISKM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGFRNCS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRFNEUR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAGNSCU_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDGNSSO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCGNSSO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGNSSO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDGGINS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCGGINS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGGINS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGEOGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCGEOGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDGEOGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGGLOGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGGERMS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGCRMG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGEVPP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGLGEP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAGHESC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRGLIDS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRPOGLB_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPOGLB_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSGOPPO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMMHACPS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCEDUHE_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSHISTO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHISTO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGHISTO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRHISTO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAAARCH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDAARCH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCAARCH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAAHIST_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCAHIST_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDAHIST_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGHAART_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHIOID_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHMMBC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHISPH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDHISPH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCHISPH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHIBRI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSHRMCC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSHRMNG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLAHRTI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLAHMRT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSIYMNG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSITECH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDICOMM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCICOMM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMACMNIB_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBUINL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBUIND_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDIDEVP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCIDEVP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSIDEVP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDIDAGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSIDAGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLINELI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLIELJD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGIFPPG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSINTMN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSIMKTG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSICGBG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAINVGR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSINVST_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAJOURN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCJOURN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDJOURN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMALNGTC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLGENLL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGLINGS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRMNGMT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNGMT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCMNGMT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCMNGMJ_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDMANGT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMCORG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMPRAC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNBSI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNBSE_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNCOR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNCRI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNHRM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNIBD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNIBS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNIMK_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMNSPO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMAKTG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMKCOM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMBADMIN/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMATFI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGMTHMT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGMTHMT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMATHS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMATFM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMEDIP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAHIMVL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAMLTCU_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBIMCR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBIMCD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSMEGPI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMALIMDR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAMUMEM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRMUMEM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCMUMEM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDMUMEM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSNLECN_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSORPSF_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSORPSY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAPLPHY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRPLPHY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCPLPHY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDPLPHY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGPLASC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRPOLTC_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPOPME_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPOPHE_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGPRABS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCPRSTR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCCRPRO_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAPSANY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPDCPA_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPSYDP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGPSYPR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDPDHDV_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPDHDV_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPSRMT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRPSYCH_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPSYGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDPSYGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GCGPSYSL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAPSYSL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAPUBHI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRPPMNG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSPPMNG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMLLAWSS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMARNSST_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMASCRWR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCSCRWR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMASOCGY_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSLPOT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSOCRS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCSOCRS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPDSOCRS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRSOCAL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRSOCCM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRSOCGR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRSOCLW_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRSOCPA_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGSPLAS_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCSPORG_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCSPRGJ_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSPORM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCSPORM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCSPRMJ_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSMMRK_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSMBUF_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSPOGP_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSSPRMK_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDCSTATI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/GDGSTATI_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMRBISCL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBISC3_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSBISCL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMATESOL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCBIMOL_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMATEXPR_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMFTTDCT_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMAVCSTD_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TMSWARHM_C/',
'http://www.bbk.ac.uk/study/2019/postgraduate/programmes/TPCWEDDV_C/',]

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
            print(location)
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
            ielts_desc = response.xpath('//*[@id="content"]/div[8]/div/div[2]').extract()[0]
            ielts_desc = remove_tags(ielts_desc)
            #ielts_desc = re.findall('INTERNATIONAL ENTRY REQUIREMENTS(.*)Visa requirements',ielts_desc)[0]
           # print(ielts_desc)
        except:
            ielts_desc = 'N/A'
            #print(ielts_desc)
        try:
            ielts = re.findall('(\d\.\d)',ielts_desc)[0]

            #i#elts = remove_tags(ielts)
            print(ielts)
        except:
            ielts = '6.5'

        try:
            ielts_l = re.findall('(\d\.\d)',ielts_desc)[1]
            print(ielts_l)
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
            duration =  '1'
            #duration = remove_tags(duration)
            #duration = re.findall('(\d) Years',duration)[0]
            #print(duration)
        except:
            duration = ''
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
            alevel = response.xpath('//*[@id="tab-Entry_Requirements"]/div/div[1]/div/table[1]').extract()[0]
            alevel = remove_tags(alevel)
            alevel = re.findall("(\w\w\w) at A Level",alevel)[0]
            #print(alevel)
        except:
            alevel = 'CC'
            #print(alevel)
        try:
            ucascode = response.xpath('/html/body/div[3]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[2]').extract()[0]
            ucascode = remove_tags(ucascode)

            #print(ucascode)
        except:
            ucascode = ''
            #print(ucascode)

        try:
            tuition_fee = '12500'
            # tuition_fee = remove_tags(tuition_fee)
            # tuition_fee = tuition_fee.replace('  ','')
            # tuition_fee = tuition_fee.replace('\n','')
            # tuition_fee = re.findall('Full-time international students: £(.*) paStudents',tuition_fee)[0]
            # tuition_fee = int(tuition_fee)
            #print(tuition_fee)
        except:
            tuition_fee = 0

        try:
            teach_time = response.xpath('//*[@id="content"]/div[3]').extract()[0]
            teach_time = remove_tags(teach_time)
            if 'full-time' in teach_time:
                teach_time = 'fulltime'
            else:
                teach_time = 'parttime'
            #print(teach_time)
        except:
            teach_time = 'N/A'
            #print(teach_time)

        teach_type = 'taught'

        assessment_en = ''
        require_chinese_en = '<div>UG A recognised International Foundation Year from a UK institution or a Chinese institution when following a validated UK syllabus. OR Successfully completed first year of a Chinese University degree OR 2 or 3 year Diploma (Zhuanke or Da Zhuan) with a minimum final grade of 70% or equivalent PG Completion of a Bachelor degree from an accredited Chinese university with 75% or higher (GPA 2.9 or above) If you find that your qualifications do not meet our entry requirements, relevant experience and completion of one of BGU’s online pre-arrival courses can also be taken into account to meet the entry criteria.</div>'
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
        item["career_en"] = ''
        item["application_open_date"] = 'all year'
        item["deadline"] = ''
        item["apply_pre"] = '£'
        item["apply_fee"] = apply_fee
        #item["rntry_requirements_en"] = rntry_requirements_en
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
        item["batch_number"] = 3
        item["finishing"] = 0
        stime = time.time()
        create_time = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(float(stime)))
        #print(create_time)
        item["create_time"] = create_time
        item["import_status"] = 0
        item["duration"] = duration
        item["tuition_fee"] = tuition_fee
        item["update_time"] = create_time
        #item["alevel"] = alevel
        #item["ib"] = ib
        #item["ucascode"] = ucascode
        item["rntry_requirements"] = rntry_requirements_en
        item["require_chinese_en"] = require_chinese_en
        item["teach_time"] = teach_time
        item["teach_type"] = teach_type
        item["assessment_en"] = assessment_en
        #item["apply_pre"] = ''
        yield item


