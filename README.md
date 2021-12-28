# Delaware Health Information Network and Community Wellness Index Data API
## DHIN-CWI REST API
### Quickstart

`curl dhin-cwi.ddil.ai/data`

### Overview
The REST API exposes census tract level data summarizing insurance claims of select chronic diseases per the Delaware Health Information Network (DHIN) database, 
as well as socioeconomic indicators of community wellness across economic, education, healthcare, housing, social, and transportation categories. 
This data is intended to facilitate the analysis of social determinants of health.

### Usage
The API is currently hosted at https://dhin-cwi.ddil.ai.

#### Endpoints
##### Get DHIN-CWI data 
`GET /data` 
parameters:
-- year ([2018, 2019], optional)

#### Sample Request

`curl https://dhin-cwi.ddil.ai/data?year=2018`

#### Sample Response
`[
{
"GEOID": 10001040100,
"All": 0.2038777908,
"acqhypo": 0.0114571093,
"alzdisease": 0.0007344301,
"alzdisorders": 0.0026439483,
"ami": 0.0026439483,
"anemia": 0.0070505288,
"arthritis": 0.0384841363,
"asthma": 0.0233548766,
"atrialfib": 0.0070505288,
"breastcancer": 0.0052878966,
"cataract": 0.0148354877,
"ckd": 0.0248237368,
"colorectalcancer": 0.0011750881,
"copd": 0.0239424207,
"depression": 0.035840188,
"diabetes": 0.0389247944,
"endometrial": 0.000440658,
"glaucoma": 0.0145417156,
"heartfailure": 0.0049941246,
"hipfracture": 0.000440658,
"hyperlipidemia": 0.026439483,
"hyperplasia": 0.008960047,
"hypertension": 0.0703584019,
"ihd": 0.0148354877,
"lungcancer": 0.0020564042,
"osteoporosis": 0.0041128085,
"prostatecancer": 0.0033783784,
"stroke": 0.009106933,
"year": 2018,
"population_count": 6808,
"median_household_income": 63826,
"supermarket_access_pct": 0,
"tree_canopy_pct": 0.2775,
"race_white_pct": 0.8733842538,
"race_black_pct": 0.0779964747,
"race_asian_pct": 0.0126321974,
"race_american_indian_alaskan_native_alone_pct": 0.0058754407,
"race_native_hawaiian_pacific_islander_alone_pct": 0.000293772,
"race_other_alone_pct": 0.000293772,
"race_two_or_more_pct": 0.0295240893,
"gender_total_male_pct": 0.4615158637,
"gender_total_female_pct": 0.5384841363,
"age_under_19_pct": 0.2652761457,
"age_20_29_pct": 0.0850470035,
"age_30_39_pct": 0.1495299647,
"age_40_49_pct": 0.1277908343,
"age_50_59_pct": 0.1417450059,
"age_60_69_pct": 0.134106933,
"age_70_over_pct": 0.0965041128,
"above_poverty_pct": 0.7230157561,
"employed_pct": 0.926056338,
"bachelors_plus_pct": 0.1365384615,
"high_school_enrollment_pct": 0.99375,
"pre_school_enrollment_pct": 0.6875,
"health_insurance_pct": 0.8969804618,
"medicare_pct": 0.0558233951,
"medicaid_pct": 0.1398122304,
"owners_pct": 0.850116189,
"habitable_pct": 1,
"uncrowded_pct": 0.9914794733,
"severe_cost_burden_owner_pct": 0.0624708625,
"severe_cost_burden_renter_pct": 0.1447368421,
"two_parent_pct": 0.6870748299,
"vehicle_access_pct": 0.9546862897,
"commute_pct": 0.0193462308,
"voter_pct": 0.96,
"diesel_pm_rank": 83.9622641509,
"pm_rank": 59.2417061611,
"safe_drinking_water_rank": 100,
"ozone_rank": 95.2830188679,
"park_access_ppa": 1,
"employment_density": 0.0141312567,
"race_white_total": 5946,
"race_black_total": 531,
"race_asian_total": 86,
"race_american_indian_alaskan_native_alone_total": 40,
"race_native_hawaiian_pacific_islander_alone_total": 2,
"race_other_alone_total": 2,
"race_two_or_more_total": 201,
"age_under_19_total": 1806,
"age_20_29_total": 579,
"age_30_39_total": 1018,
"age_40_49_total": 870,
"age_50_59_total": 965,
"age_60_69_total": 913,
"age_70_over_total": 657,
"median_household_income_z": -0.0872472937,
"supermarket_access_z": -1.4026176362,
"tree_canopy_z": 0.926579113,
"above_poverty_z": 0.0590509321,
"employed_z": -0.3905004225,
"bachelors_plus_z": -1.0398403191,
"high_school_enrollment_z": 0.4040906126,
"pre_school_enrollment_z": 0.569182783,
"health_insurance_z": -0.3493406109,
"owners_z": 0.7991707218,
"habitable_z": 0.5039842141,
"uncrowded_z": 0.4381365723,
"severe_cost_burden_owner_z": 0.6973534587,
"severe_cost_burden_renter_z": 0.5067345194,
"two_parent_z": 0.4917542695,
"vehicle_access_z": 0.3042587929,
"commute_z": -0.5289930776,
"voter_z": 1.5722972906,
"diesel_pm_z": -1.1819604267,
"pm_z": -0.3679950778,
"safe_drinking_water_z": -1.6867702161,
"ozone_z": -2.3121349216,
"park_access_ppa_z": -1.0200845788,
"employment_density_z": -0.4158042316,
"economic_unweighted": -0.1395655947,
"education_unweighted": -0.0221889745,
"healthcare_unweighted": -0.3493406109,
"housing_unweighted": 0.5890758973,
"neighborhood_unweighted": -0.4779818334,
"environment_unweighted": -1.3872151605,
"social_unweighted": 1.03202578,
"transportation_unweighted": -0.1123671423,
"cwi_score": -0.0592656006,
"cwi_score_rank": 49.0291262136,
"economic_unweighted_rank": 41.7475728155,
"education_unweighted_rank": 44.6601941748,
"healthcare_unweighted_rank": 28.640776699,
"housing_unweighted_rank": 87.8640776699,
"neighborhood_unweighted_rank": 13.5922330097,
"environment_unweighted_rank": 4.854368932,
"social_unweighted_rank": 89.3203883495,
"transportation_unweighted_rank": 33.4951456311,
"supermarket_access_pct_rank": 0,
"tree_canopy_pct_rank": 79.6116504854,
"above_poverty_pct_rank": 49.5145631068,
"employed_pct_rank": 28.1553398058,
"bachelors_plus_pct_rank": 12.1359223301,
"high_school_enrollment_pct_rank": 96.8253968254,
"pre_school_enrollment_pct_rank": 78.3783783784,
"health_insurance_pct_rank": 28.640776699,
"medicare_pct_rank": 74.2718446602,
"medicaid_pct_rank": 40.2912621359,
"owners_pct_rank": 78.1553398058,
"habitable_pct_rank": 100,
"uncrowded_pct_rank": 75.641025641,
"severe_cost_burden_owner_pct_rank": 26.213592233,
"severe_cost_burden_renter_pct_rank": 33.0097087379,
"two_parent_pct_rank": 65.0485436893,
"vehicle_access_pct_rank": 47.0297029703,
"commute_pct_rank": 26.6990291262,
"voter_pct_rank": 97.5247524752,
"median_household_income_rank": 54.3689320388,
"park_access_ppa_rank": 0,
"employment_density_rank": 2.9126213592
},...`
<!---
### Data Dictionary
<ul>
<li>GEOID - Census Tract Code</li>
<li>All - Proportion of insured population that filed a claim related to one of the DHIN major disease categories within the census tract<li>
<li>acqhypo -
<li>alzdisease - Proportion of all claims related to alzhiemer disease
<li>alzdisorders - Proportion of all claims related to alzhiemer disorder
ami - Proportion of all claims related to AMI
anemia - Proportion of all claims related to anemia
arthritis - Proportion of all claims related to artritis
asthma - Proportion of all claims related to asthma
atrialfib - Proportion of all claims related to atrialfib
breastcancer - Proportion of all claims related to breast cancer 
cataract - Proportion of all claims related to cataract
ckd: Proportion of all claims related to ckd
colorectalcancer - Proportion of all claims related to colorectal cancer
copd - Proportion of all claims related to copd
depression - Proportion of all claims related to depression
diabetes - Proportion of all claims related to diabetes
endometrial - Proportion of all claims related to endometrial
glaucoma - Proportion of all claims related glaucoma
heartfailure - Proportion of all claims related to heart failure
hipfracture - Proportion of all claims related to hip fracture
hyperlipidemia - Proportion of all claims related to hyperlipidemia
hyperplasia - Proportion of all claims related to hyperplasia
hypertension - Proportion of all claims related to hypertension
ihd - Proportion of all claims related to IHD
lungcancer - Proportion of all claims related to lung cancer
osteoporosis - Proportion of all claims related to osteoporosis
prostatecancer - Proportion of all claims related to prostate cancer
stroke - Proportion of all claims related to stroke
year - Calendar year period of data collection
population_count - Total census tract population
median_household_income - Census tract median household income (USD)
"supermarket_access_pct": 0,
"tree_canopy_pct": 0.109,
race_white_pct - Percentage of census tract population identifying racially as White
race_black_pct - Percentage of census tract population  identifying as Black
race_asian_pct - Percentage of census tract population racially identifying as Asian
race_american_indian_alaskan_native_alone_pct - Percentage of census tract population racially identifying as American Indian and/or Alaskan Native
race_native_hawaiian_pacific_islander_alone_pct - Percentage of census tract population identifying as solely Native Hawaiian and/or Pacific Islander
race_other_alone_pct - Percentage of census tract population identifying as "Other
race_two_or_more_pct": 0.0516088592,
"gender_total_male_pct": 0.510865023,
"gender_total_female_pct": 0.489134977,
"age_under_19_pct": 0.2672377768,
"age_20_29_pct": 0.1259924781,
"age_30_39_pct": 0.1671541997,
"age_40_49_pct": 0.1291266193,
"age_50_59_pct": 0.1391558713,
"age_60_69_pct": 0.0942331801,
"age_70_over_pct": 0.0770998746,
"above_poverty_pct": 0.7059072623,
"employed_pct": 0.9323308271,
"bachelors_plus_pct": 0.2238037553,
"high_school_enrollment_pct": 1,
"pre_school_enrollment_pct": 0.6781609195,
"health_insurance_pct": 0.9111334675,
"medicare_pct": 0.0667337357,
"medicaid_pct": 0.1961770624,
"owners_pct": 0.6352941176,
"habitable_pct": 1,
"uncrowded_pct": 0.9877005348,
"severe_cost_burden_owner_pct": 0.1356589147,
"severe_cost_burden_renter_pct": 0.2323943662,
"two_parent_pct": 0.5381818182,
"vehicle_access_pct": 0.9657754011,
"commute_pct": 0.0234052318,
"voter_pct": 0.13,
"diesel_pm_rank": 77.358490566,
"pm_rank": 81.0426540284,
"safe_drinking_water_rank": 100,
"ozone_rank": 81.1320754717,
"park_access_ppa": 5,
"employment_density": 1.4384488735,
"race_white_total": 3456,
"race_black_total": 1004,
"race_asian_total": 24,
"race_american_indian_alaskan_native_alone_total": 17,
"race_native_hawaiian_pacific_islander_alone_total": 0,
"race_other_alone_total": 38,
"race_two_or_more_total": 247,
"age_under_19_total": 1279,
"age_20_29_total": 603,
"age_30_39_total": 800,
"age_40_49_total": 618,
"age_50_59_total": 666,
"age_60_69_total": 451,
"age_70_over_total": 369,
"median_household_income_z": -0.5813788125,
"supermarket_access_z": -1.4026176362,
"tree_canopy_z": -0.7137432898,
"above_poverty_z": -0.055547572,
"employed_z": -0.2003124619,
"bachelors_plus_z": -0.5011067587,
"high_school_enrollment_z": 0.483717755,
"pre_school_enrollment_z": 0.5371756973,
"health_insurance_z": -0.0715844139,
"owners_z": -0.286179733,
"habitable_z": 0.5039842141,
<li>uncrowded_z": 0.2271553349,
<li>severe_cost_burden_owner_z": -0.9568161547,
<li>severe_cost_burden_renter_z": -0.2794991492,
<li>two_parent_z": -0.2813132373,
<li>vehicle_access_z": 0.4290288412,
<li>commute_z": -0.4844479942,
<li>voter_z": -1.3339576583,
<li>diesel_pm_z": -0.9580832165,
<li>pm_z": -1.1009064207,
<li>safe_drinking_water_z": -1.6867702161,
<li>ozone_z": -1.899905647,
<li>park_access_ppa_z": 2.1106871439,
<li>employment_density_z": -0.1736185698,
<li>economic_unweighted": -0.2790796155,
<li>education_unweighted": 0.1732622312,
<li>healthcare_unweighted": -0.0715844139,
<li>housing_unweighted": -0.1582710976,
<li>neighborhood_unweighted": -0.044823088,
<li>environment_unweighted": -1.4114163751,
<li>social_unweighted": -0.8076354478,
<li>transportation_unweighted": -0.0277095765,
<li>cwi_score": -0.2272321714,
<li>cwi_score_rank": 32.5242718447,
<li>economic_unweighted_rank": 35.4368932039,
<li>education_unweighted_rank": 60.1941747573,
<li>healthcare_unweighted_rank": 37.3786407767,
<li>housing_unweighted_rank": 33.4951456311,
<li>neighborhood_unweighted_rank": 48.5436893204,
<li>environment_unweighted_rank": 3.3980582524,
<li>social_unweighted_rank": 14.5631067961,
<li>transportation_unweighted_rank": 46.1165048544,
<li>supermarket_access_pct_rank": 0,
<li>tree_canopy_pct_rank": 26.213592233,
<li>above_poverty_pct_rank": 44.6601941748,
<li>employed_pct_rank": 38.3495145631,
<li>bachelors_plus_pct_rank": 36.8932038835,
<li>high_school_enrollment_pct_rank": 100,
<li>pre_school_enrollment_pct_rank": 77.8378378378,
<li>health_insurance_pct_rank": 37.3786407767,
<li>medicare_pct_rank": 81.5533980583,
<li>"medicaid_pct_rank": 66.5048543689,
<li>"owners_pct_rank": 31.5533980583,
<li>habitable_pct_rank": 100,
<li>uncrowded_pct_rank": 62.1794871795,
<li>"severe_cost_burden_owner_pct_rank": 84.9514563107,
<li>"severe_cost_burden_renter_pct_rank": 64.5631067961,
<li>"two_parent_pct_rank": 34.9514563107,
<li>"vehicle_access_pct_rank": 60.396039604,
<li>"commute_pct_rank": 33.0097087379,
<li>"voter_pct_rank": 9.4059405941,
<li>"median_household_income_rank": 30.5825242718,
<li>"park_access_ppa_rank": 100,
<li>"employment_density_rank": 53.3980582524
</ul>
-->
