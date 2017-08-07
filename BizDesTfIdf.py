# https://github.com/RaRe-Technologies/gensim/blob/develop/docs/notebooks/gensim%20Quick%20Start.ipynb
import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s : %(message)s', level = logging.INFO)
# corpus
raw_corpus = [
    "withdrawal limit value for each account",
    "Variable for iACH Top Casual EMEA Strategy",
    "ACH EMEA Top Casual RADD for our new strategy",
    "Create issuer decline for ACH EMEA Top and Casual population",
    "To define High Risk ACH population",
    "Levergae Yodlee information to decline high risk population and at the same time enable lower risky population",
    "CC excessive rejection",
    "Cust_id and Address zip pairs from last 3 months good history txns",
    "Accounts with good PPDG purchasing history",
    "This RADD is used in Automated Loss Prevention System (ALPS) project and aimed to mitigate flash fraud consumer loss automatically. This RADD will store segments and their solutions.",
    "Publish one off conn_type",
    "APAC RTN aggregation based on 1 year's historical data",
    "Generate list contains all account which entering SMB segment within 180 days",
    "This RADD will calculate the exposure for all APAC LM/SMB merchants which will be used on casescoring CP for leads scoring.",
    "IDI Account level RADD for ARM2017 model.",
    "Bank Account Level variables used in ARM17. The keys are bank account number hmac, routing number, bank country",
    "Calculate seller's average and standard deviation transactions amount for all CS segment, based on previous 3 month activity. exclude sellers who didn't participate in any transaction or their standard deviation is 0",
    "A RADD containing all senders who have had between 400 and 1000 txns in the last year.",
    "This RADD contains senders and their counterparties, who have frequent and safe transactions with each other in history(past 6 months).",
    "Creates daily table of candidate accounts who may receive automated mitigating actions.",
    "The RADD is used for flash fraud automation project and the owner is Customized Fraud Solution team.",
    "To create phone black list containing all leaky phones identified by CRM bad phone logics",
    "A list of bad zip codes in the casual and top segments.",
    "A list of bad zip codes used for block action (WAX PrOX)",
    "A Radd to lookup primary bank information using account as key",
    "RADD contains list of merchants whose binding txns were of 2500 local currency This should provide a coverage of ~60% of all bindings !",
    "a list of BINS for 3DS initiation",
    "This radd shows the count of distinct sender accounts for each browser hash at trasaction",
    "buyer abuse linking account",
    "CAM2013_RR is a process that is generated in PayPal SAS machine.The SAS process result is inserted into tables in  pp_tables_risk. This Fast-R process creates the RADD.",
    "This the request to load case id level shipment data",
    "We're generating a string that explains why a transaction does not involve a Stolen Financial or an Account Take Over. This information will be used to dispute Unauthorized chargebacks.",
    "The uploaded code needs to be run daily and the final table CB_OPT_COMPASS_RADD will serve as input for the RADD file.Primary keys for the RADD are ATKC_CASE_ID and PAYMENT_TRANSID",
    "Consumer Consistency on High ASP solution average model score online RADD",
    "Save offline calculated Trust Address list for online usage",
    "Create a new radd to upload some offline generated rollups and airline merchants information",
    "this is to create crowdfunding RADD",
    "RADD file to store bank account number hmac of active + confirmed + no return within last 30 days",
    "consumer attributes v2 RADD with new components",
    "Detect CC Bin attack and build surgical solution accordingly.",
    "RADD for casual seller BSM strategy",
    "max TPV in the last 1.2 year is a time frame of 10 days, for all CS accounts",
    "Radd that is used for the new CS ebay strategy and contains data about claims, sub_segmentation and previous TPV.",
    "RADD for the casual seller OOH strategy",
    "thresholds RADD for the casual seller OOH strategy",
    "P value for Casual Sellers QP engine.",
    "Segmentation for Casual Sellers QP.",
    "The daily batch looks for binding events between PayPal accounts and 3rd party apps using PayPal to process payments using 'future payments' flow.  the table  pp_scratch_ars.ea_binding_events_2014_15 contains historic binding events and should be used once to prepopulate the RADD before the daily batch starts the incremental update process.",
    "Create one radd for SME and LM queueing solutions",
    "daily exchange rate to be used as part of eBay listing RISK components",
    "list of attacked BINs for DCC txns",
    "Querying tracking data with minimal latency, looking for suspicious indicators. For pending transactions we will keep a daily check until they are shipped and show only the latest results.",
    "The RADD contains  assets that were used in fraudulent activity, and need to be black listed to prevent further abuse of the flow",
    "A calculation of eBay risk score per leaf as applies to EMEA SMEs only.",
    "ASP, ATTACK and ALID data ratios, amounts and counts.",
    "eBay variables that has spike pattern for listing, transaction, feedback etc.",
    "6 RADD Variables are calculated for EG Growth Criteria. They are from the definitions for EG given by various SRM teams",
    "Final eBay RADD variables for ebay MM model 2016 daily build  which joins listing, txns, fdbk variables.",
    "All cases where eBay already adjudicated. Making sure that seller wont get debited twice.",
    "This radd is used to generate the eBay NA LM and SMB merchant bad history.",
    "Aggregation of ecommerce platforms and other partners",
    "Creating Growth Rate variables w.r.t TPV, ASP and Txn count recently and past 24 months for eBay Sellers",
    "Creating Sender Country - Receiver Country Pair Risk Ratings variables",
    "Creating Vertical Change(VC) features for eBay EG Model Vertical Change Features tries to capture a shift in selling domain by an eBay Seller The eBay Leaf category is the most granular domain of the listing selected by the seller.",
    "Capture patterns of withdrawal by ebay sellers",
    "Dummy RADD, will be changed later on with the complete final logic. This  RADD contains aggregated seller side data used to determine EG activity.",
    "Holds the last max 12 months nTPV and average 3 months nTPV which is used by the EMEA SMB & LM Onboarding Team to                 decide on whether to increase a buisness account's Release Amount increase automatically at ExitLimit checkpoint on                  Pluto.",
    "EMEA SRM's Daily RADD holding data for Queue Prioritization (QP) and other solutions.",
    "EMEA SMB & LM subsegmentation RADD, would be used to enable good merchants and place heavier actions on bad subsegments.",
    "Stores population of UK/DE merchants who had an increase in TPV and ASP, will be caught by rule when exiting to gambling",
    "This RADD will be used in a package of attributes which aim to detect EG behavior in order to reduce seller loss.",
    "This process focus on searching the PayPal accounts who has multiple  debit cards opened on the same address.",
    "Core/CCC Consumer Credit attribute - PP financial status pack",
    "This is the source of tran site which is not available anywhere in LIVE",
    "Store SF QP solution P part value.",
    "A RADD to hold the binning of RDP detection attributes",
    "Growing Exposure attribute for PAD and iACH EMEA population",
    "RADD for ars attribute incons_high_cnt",
    "This RADD contains a list of all Fraudnet resolutions that were observed in the account's historic good transactions",
    "this radd will collect data regarding fraudnet timezone user's good history. collecting all its used timezones, how many times it used each and when was the last time.",
    "this radd holds the historic data of flags combinations used in each pp transaction",
    "Statistic data of the USD amount sent successfully by an account for the last year. The key is PP account, and the values are: tx_cnt, avg_usd, median_usd, std_usd, max_usd and min_usd.",
    "Map between rcvr rcvr_cntry to the average fess taken from his transactions in the last 50 days.",
    "Map between sndr sndr_cntry to the average currency exchange fess taken from his transactions in the last 180 days.",
    "A RADD contatining data from ebay. The key is the ebay username, and the values are: creation time stamp (in unix), registered email and full name.",
    "This RADD will be used as part of RESET V2 project, its purpose is to identify fraudlent transactions within the trusted segment",
    "This RADD holds all the last 4 month's supercookies with at least one bad transaction",
    "This RADD shows the bad rates of each FraudNet resolution for the nearest 30 days. The bad rates include ATO bad rates, SF bad rate and any bad rate (both count and dollar for each). In addition each row in the RADD (resolution) will hold the general bad rates for convenience and comparison purposes.",
    "See this: https://grs-core.fsc.local/grs-core-portal-home/analytical-platform/ip_geo/",
    "generate mobile ip of the last 300 days from ULDS and Dyson table to support Peeking 3.0 logic",
    "Map between rcvr to the average fess taken from his transactions in the last 50 days.",
    "Map between seller to his mcc_code and and txn_categ_code",
    "Map between sndr to the average currency exchange fess taken from his transactions in the past.",
    "This RADD computes the ATO bad rate for every combination of transaction flags and types,",
    "filling a radd with merchant id's that rules in the high asp project use.",
    "HIgh ASP whitelisting RADD for Tokenization.",
    "This RADD will contain bank account level aggregation data for all recent iACH users.",
    "This RADD will contain user level aggregation data for all recent iACH users.",
    "Ranking RTNs used by Casual and Top consumers by size and \"riskiness\" (customers' NSF BPS).",
    "SQL to get the customers who have been tagged under the bad bank segment.",
    "a radd to identify all merchants who are IPR hold enabled",
    "create a RADD for setting alf of kickstarter_mam_alf, for the special risk treatment",
    "Identifies kickstarter MAM accounts so that they can be whitelisted from risk models and rules.",
    "This one is to calculate the last 10 days on ebay tpv for NA SMB and LM accounts",
    "This RADD record all the Large Enterprise accounts' IDs, which will be used in ATO queue management, including enqueue, case scoring and case evaluation.",
    "Collect offline bank data to be used in live attributes",
    "mapping between MCC codes and True Industry categories with their fraud risk scores",
    "LM Dynamic Solution with auto variable selection RADD",
    "This is a part of a migration process of GRS DM, that its target is to move all running processes (RADDs) from SDOT environment to DT. All SDOT RADDs can be found in https://confluence.paypal.com/display/GRSDM/SDOT+Batch+Mapping",
    "idi_misc_10_radd is a misc RADD that ran on SDOT env.",
    "Owner of this RADD is Luna Lu. This RADD was migrated from SDOT env",
    "RADD will contain information about all EMEA sellers maximum 30 days TPV.This information will be used in Pluto for the iEG solution.",
    "Seller-level variables for the Marketplaces component",
    "marketplace level variables",
    "This is to find those NA SMB/LM accounts which are being queued by MRO in the last 7 days",
    "to set importent flags such as am_flag and ts_flag and so on",
    "Use network V3 bad network seed_id as an indicator to detect potential bad transactions made by buyers belonging to the bad network.",
    "This process is used to create a RADD which identifies ASP limits for a merchant category code.",
    "This is to calculate the off_ebay tpv for SMB/LM accounts in NA for the last 1 year",
    "This is to calculate the on_ebay tpv for SMB/LM accounts in NA for the last 1 year",
    "Create daily RADD variables for PayPal Credit Payment Hold Model.",
    "Seller-level variables for the Platforms component",
    "List of all DE existing accounts to evaluate eligibility for PP+ at onboarding through Falcon flow.",
    "list of PP+ LATAM merchants that cannot handle AFRs",
    "this RADD contains  variables that are based on PP data, and were found valuable in the onboarding model and young account model.",
    "A daily updated RADD for big merchants, and contains their profiles like money received/ withdrawal/claim and so on.",
    "This process creates a RADD file to include first transaction date for each PayPal account. This file will be used at RPDS to manage fraud risk of PPC reuse transactions.",
    "The PayPal Working Capital (PPWC) Risk Model 2 (PRM2.0) model is built to - Predict the probability of a PayPal Seller going 180D+ delinquent at the end of 12 months. - Improve the credit risk assessment on PPWC loans or advances1. - The model score will be used in strategy for loan/advance underwriting and loan/advance assignment. - The model development started in May 2016, and is scheduled for implementation in early October 2016.",
    "This script will check what is the longest unpaid transaction per pui user and will also tag \"true subsequent\" users (for when the EDGE container is emptied)",
    "a centralized radd to hold everything pui related",
    "FATCA Information Reporting",
    "Calculate the daily CBE value of sellers",
    "evaluate how risky a cust is from previous enQ behavior",
    "evaluate how risky a src_type_id is from PIT perspective",
    "WH solution that leverege DB card history to enable ACH tranasctions",
    "This RADD contains amount denial information for LM and SME accounts of NA",
    "This process creates a PP sender account RADD file based on PPC transactions/account history and fraud performance.  this file will be used at RPDS to manage fraud risk of PPC reuse transactions.",
    "Chargeback Representment Strategy RADD file",
    "Run through release amount scorecard to calculate new release amount limit and make appeal decision",
    "create table to prevent repeat fraudster who use known bad assets like vid",
    "Used for ACH EMEA Strategy. Identify merchants  that has high NSF and sells gambling products",
    "a radd containing a pattern of risky memo words.",
    "RADD to bring additional information to optimize chargebacks",
    "RADD file to store risky bank routing numbers for accounts with ACH return codes",
    "This process is dedicated to establish and refresh cust - bank pairs that have caused no buyer-related gross loss in past 1 year.",
    "Add PPWC eligible population to the driver, provide reason code for all eligible population, update ntpv_3mth",
    "A daily updated model to give big sellers a risk assessment about whether they will turn bad, generate loss or create Bad Buyer Experience.",
    "upload DNB credit bureau data on live so can be used in live solution",
    "create a RADD for identifying bad consumers based on super cookie info.",
    "creation of a new RADD file to store credit card BINs issued by sanctioned banks.These BINs will be called by Risk rules (Pluto) in order to disallow their use for transactions and withdrawals, as well as block them from being added to accounts.",
    "contains all the information that NA SRM team uses for eBay loss analysis",
    "Large Merchant Variable Selection Dynamic Solution for segment SF RADD",
    "This is the final logic of the RADD which relies on a new production table. It replaces the dummy RADD. It was done under Sapna's authorization.   RADD keys are 'leaf_id' and 'seg'.",
    "Seller TPV seasonality detection RADD variable",
    "Buyer_Confirm is a hold release method . DI and DE and DA checkpoints need this variable to counter collusion",
    "Calculate the daily EG variables for the SME/LM segment",
    "Merge smm17 score from all  seller segments",
    "SMM17 SME production codes",
    "SFM13 variables used in SMM17 model",
    "This RADD will be used to whitelist transactions between a specific external test account sending to a specific merchant account. Normally this is during integration phase when large merchants need to test their website using PP. Currently using PP_OAP_CRME2E_T.CRM_OWNED_GENERIC_RADD  WHERE K01 = 'WH_Sndr_Rcvr' to test this functionality for the last 6 months.",
    "This RADD will include historical information on the variety of products EMEA SMB and LM merchants have sold in the previous 6 months",
    "RADD to store TA model variables",
    "A list of Top Consumers who have a high ratio of purchasing from credit-risky verticals.",
    "Finds accounts with unrecovered bank net loss in the entity",
    "Based on txn level classification to Tangible and Intangible, this process provides seller level aggregations and classification.",
    "This is a per txn classification to Tangible (TG), Intangible (IG) or unknown. Also supplied is detection of ticket txns and the type of the ticket (Travel or Other).",
    "phone enrichment process for NB collection",
    "this will create the RADD for best matching agent for a tls fingerprint",
    "this will create the RADD for matching agents for a tls fingerprint",
    "this will create the RADD for tls fingerprints for best matching osfamily for a tls fingerprint",
    "this will create the RADD for matching the probability of an agent to the tls fingerprints",
    "this will create the RADD for tls fingerprints, having the best match for a tls fingerprint",
    "this will create the RADD for tls fingerprints matching OSs",
    "This RADD includes very valuable information for the models in POS checkpoint such as the frequency of shopping, and the speed",
    "These are the RADD attributes with the key of sndr_id to be used in TOK17_SF model",
    "All of these attributes has been used in TOK17-NSF model. These attributes contain very reach information on ALID, Lynx, Verticals, and ...",
    "Identifying customers with at least 1 high amount trvael TX",
    "Trusted Phone RADD for Tokenization.",
    "Create the paypal data for uk customer",
    "This process creates a PP sender account RADD file based PPC acquisition flow. This RADD file will be used in RPDS to manage UK PPC fraud risk.",
    "This RADD file has information about when the customer used a particular APP_GUID for the first time. this also can be used to find APP_GUID TOF. Has only last 30 APP_GUId's due to space constarint",
    "The RADD file will contain the aggregated VT payment information for new or suspicous Pro/VT merchants",
    "Receivers list with an average take rate of more than 3.5% in WAX transactions of the last month",
    "Accounts used for sf collusion trend",
    "The corresponding default settings of daily/monthly/lifetime withdraw limit of each exit channel and country.",
    "This RADD will hold account level aggregation of hitorical maximum withdrawal amount in a given sliding window for withdrawal hold solution optimization.",
    "This table should expose PayPal agregated data based on email address",
    "Email pattern RADD",
    "Logic of calculation Monthly Quotas of a sender. STEP1: calculate stats of the last three months and then get the average. STEP2: calculate the stats of current month. STEP3: calculate the stats left.",
    "R - Recency F - Frequency M - Monetary C - Consistency",
    "Young Consumer Routing RADD",
    "YC routing radd based on historical data",
    "RADD file to store bank account number hmac and bank routing number of confirmed banks the Yodlee returns a strong name mismatch",
    "This RADD identifies new high risk accounts entering the SMB segment.",
    "This is a daily RADD for YS PreTxn, asset and account rating.",
    "a radd with \"young seller\" sub segmentation",
    # "GRCM case and acct level aggregate information",
    # "this process is to calculated exposure for LM/SMB account, which would be used in later queue framework",
    # "for dynamical QP radd 1",
    # "for dynamical_qp radd 2, the score would be calculated by the combination of radd 1 and radd 2",
    # "SRO main RADD",
    # "This RADD contains information about RDA Machine ID. through this we can get the pairing of customer and the device he used.",
    # "This process creates a PP sender account RADD file based PPC acquisition flow. This RADD file will be used in RPDS to manage UK PPC fraud risk. New version use a different data source for more accurate repayment info, PPC days on file also added to this RADD.",
    # "Generate RADD to profile risky buyer/seller and pass that recommendation to teammates",
    # "Process to generate precomputed data for Data Share with Synchrony",
    # "venmo email domain fraudscore",
    "This is a component of CRM All Purpose Radd to detect safe senders.",
    "This RADD is to white list existing/old billing agreement based subsequent txns from all ATO checks.  table 1: get all active billing agreements (excluding ebay accounts) table 2 & 3: get BA created date  table 4: Get Auth Flow pass info at binding   table 5: get BA's active in last 12 months and #txns made by them  table 6: club them all table 5: to reduce size of RADD, make relevant exclusion like ba_created should be atleast 2 months old and should have done more than 2 txns OR AF pass at binding. This is to provide relief to habitual users (from ATO).",
    "Need a RADD file to maintain 6 month history of bad and good devices leveraging STC data shared by Google",
    "Static RADD for Venmo RR for Email Domain",
    "IP3 Risk rating RADD",
    "Month of Year risk rating RADD",
    "Venmo phone area code risk rating",
    "Bank RTN Risk Rating RADD",
    "Venmo Week of the month static RADD",
    "RADD based on PRIMEs trust platform which collects all trusted emails and phones for each customer from 4 different levels - trusted activity,signup,confirmed,aged",
    "RADD based on PRIMEs trust abilities, enriched with a customer that added the email as part of trusted activity and is the most indicative customer for additional risk assesments",
    "venmo cc bin",
    "venmo email pattern",
    "This is a RADD developed with the graph theory",
    "venmo rtn numbers",
    "Upload BINDB to live for BUFS component",
    "Casual seller data mart",
    "This process will create number of ebay accounts linked to PP-id and also variables related to age for ebay accounts linked to PP-id.",
    "We observed that PP accounts are linked to several ebay accounts and want to compute ato and cc bad-rates (unit and dollar-wise) for ebay accounts linked to paypal account in the past 1 month.",
    "We observed that PP accounts are linked to several ebay accounts and want to compute ato and cc bad-rates (unit and dollar-wise) for ebay accounts linked to paypal account in the past 2 months.",
    "No reliable online ebay auction type tagging. Use offline listing auction type tagging.",
    "Rollup on email pmt amt/cnt/asp/pct, and ratio describing behavior changing",
    "RADD for keystroke based ARS attribute",
    "Counts the number of accounts that have used this bank account; bank sharing.",
    "Variables describing seller voluntary refund behavior, rollup and ratios of the last 7/30/90 days",
    "As part of the Send & Request (email payments) loss mitigation effort, this table will contain several components or variables indicating risky flow history and changes.",
    "The radd summarize the information from invoice of S&R (email payment) flow, including the transaction, listing, memo and shipping information"
]

# Create a set of frequent words and add stopwords
stoplist = set('for a an of the and to in test from this that'.split(' '))
# Lowercase each document, split it by white space and filter resource stopwords
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in raw_corpus]

# Count word frequencies
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

# Only keep words that appear more than once
processed_corpus = [[token for token in text if frequency[token] > 1] for text in texts]
# print(processed_corpus)

from gensim import corpora

dictionary = corpora.Dictionary(processed_corpus)
# print(dictionary)

# vector
# print(dictionary.token2id)

new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
# print(new_vec)

bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
# print(bow_corpus)

from gensim import models
# train the model
tfidf = models.TfidfModel(bow_corpus)
# transform the "system minors" string
testset = [
    "idi_cfas_seller_radd",
    "idi_cfas_seller_ti_radd",
    "IDI_MISC_09",
    "ONUS DATA PROCESSING",
    "test test test",
    "how to score this test set for each tpv amount",
    "looking forward to see you",
    "GRCM case and acct level aggregate information",
    "this process is to calculated exposure for LM/SMB account, which would be used in later queue framework",
    "for dynamical QP radd 1",
    "for dynamical_qp radd 2, the score would be calculated by the combination of radd 1 and radd 2",
    "SRO main RADD",
    "This RADD contains information about RDA Machine ID. through this we can get the pairing of customer and the device he used.",
    "This process creates a PP sender account RADD file based PPC acquisition flow. This RADD file will be used in RPDS to manage UK PPC fraud risk. New version use a different data source for more accurate repayment info, PPC days on file also added to this RADD.",
    "Generate RADD to profile risky buyer/seller and pass that recommendation to teammates",
    "Process to generate precomputed data for Data Share with Synchrony",
    "venmo email domain fraudscore",
    "cfas seller ti"
]
for str in testset:
    t = tfidf[dictionary.doc2bow(str.lower().split())]
    if (t == []):
        print("Input : %s" %str)
        print("Score : %d" %0)
    else:
        print("Input : %s" % str)
        print("t : ", t)
        count = 0
        sum = 0
        for item in t:
            count += 1
            sum += item[1]
        res = sum/count
        print("Score : %f" % res)