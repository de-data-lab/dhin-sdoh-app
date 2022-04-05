# Delaware Health Information Network (DHIN) and Social Determinants of Health (SDOH) Data API
## DHIN-SDOH REST API
### Quickstart

`curl dhin-cwi.ddil.ai/data`

### Overview

This REST API exposes 35 census tract level features (detailed in the documentation below) for all 3 counties in Delaware between 2018 and 2019 that broadly represent Social Determinants of Health (SDOH) indicators. It is important to note, that not all variables are unique in context. For example, each age category is represented as its own column, all variables of age, just different categories for it. 

In addition to this, we summarize insurance claims from the Delaware Health Information Network's (DHIN) Health Care Claims Database (HCCD) of select chronic diseases (N=27) defined by the Centers for Medicare & Medicaid Services (CMS). We broadly derived data sources from the [Healthy Places Index](https://healthyplacesindex.org/wp-content/uploads/2021/04/HPI2Documentation2018-02-20-FINALrev2021-04-22.pdf) framework, adapting it to the avialable resources in the state of Delaware. Each entry for a specific chronic disease represents the census tract normalized rate of disease for that region. 

This data is intended to facilitate the 1) analysis of social determinants of health at the census tract levl and 2) provide a case-use of how to incorporate data on social determinants of health to your own domain of interest, in this case, health claims. 


### Usage
The DHIN–SDOH API is currently hosted at https://dhin-cwi.ddil.ai.

#### Endpoints
##### Get DHIN-SDOH data 
`GET /data` 
parameters:
-- year ([2018, 2019], optional)

#### Sample Request

`curl https://dhin-cwi.ddil.ai/data?year=2018`

#### Sample Response
```json
[
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
}
]
```

### Data Dictionary
All descriptions are relative to the census tract geographic area indicated by `GEOID`.

<ul>
<li>GEOID - Census Tract Code</li>
<li>All - Proportion of insured population that filed a claim related to one of the DHIN major disease categories within the census tract</li>
<li>acqhypo - Proportion of all claims related to acquired hypothyroidism </li>
<li>alzdisease - Proportion of all claims related to alzhiemer disease </li>
<li>alzdisorders - Proportion of all claims related to alzhiemer related disorders, or senile dementia </li>
<li>ami - Proportion of all claims related to acute myocardial infarction </li>
<li>anemia - Proportion of all claims related to anemia </li>
<li>arthritis - Proportion of all claims related to rheumatoid arthritis/osteoarthritis </li>
<li>asthma - Proportion of all claims related to asthma </li>
<li>atrialfib - Proportion of all claims related to atrial fibrillation </li>
<li>breastcancer - Proportion of all claims related to breast cancer </li>
<li>cataract - Proportion of all claims related to cataract </li>
<li>ckd - Proportion of all claims related to chronic kidney disease </li>
<li>colorectalcancer - Proportion of all claims related to colorectal cancer </li>
<li>copd - Proportion of all claims related to chronic obstructive pulmonary disease </li>
<li>depression - Proportion of all claims related to depression </li>
<li>diabetes - Proportion of all claims related to diabetes </li>
<li>endometrial - Proportion of all claims related to endometrial cancer</li>
<li>glaucoma - Proportion of all claims related glaucoma </li>
<li>heartfailure - Proportion of all claims related to heart failure </li>
<li>hipfracture - Proportion of all claims related to hip fracture </li>
<li>hyperlipidemia - Proportion of all claims related to hyperlipidemia </li>
<li>hyperplasia - Proportion of all claims related to benign prostatic hyperplasia </li>
<li>hypertension - Proportion of all claims related to hypertension </li>
<li>ihd - Proportion of all claims related to ischemic heart disease </li>
<li>lungcancer - Proportion of all claims related to lung cancer </li>
<li>osteoporosis - Proportion of all claims related to osteoporosis </li>
<li>prostatecancer - Proportion of all claims related to prostate cancer </li>
<li>stroke - Proportion of all claims related to stroke / transient ischemic attack </li>
<li>year - Calendar year period of data collection </li>
<li>population_count - Total census tract population </li>
<li>median_household_income - Census tract median household income (USD) </li>
<li>supermarket_access_pct - Percentage of the urban and small town population residing less than 1/2 mile from a
supermarket/large grocery store, and the percent of the rural population living less than 1 mile
from a supermarket/large grocery store</li>
<li>tree_canopy_pct - Population-weighted percentage of the census tract area with tree canopy </li>
<li>race_white_pct - Percentage of population self-identifying as White </li>
<li>race_black_pct - Percentage of population self-identifying as Black </li>
<li>race_asian_pct - Percentage of population self-identifying as Asian </li>
<li>race_american_indian_alaskan_native_alone_pct - Percentage of population identifying as American Indian and/or Alaskan Native </li>
<li>race_native_hawaiian_pacific_islander_alone_pct - Percentage of population identifying as Native Hawaiian and/or Pacific Islander </li>
<li>race_other_alone_pct - Percentage of population identifying as Other </li>
<li>race_two_or_more_pct - Percentage of population identifying as two or more races</li>
<li>gender_total_male_pct - Percentage of population identifying as male</li>
<li>gender_total_female_pct - Percentage of population identifying as male </li>
<li>age_under_19_pct - Percentage of population under the age of 19 </li>
<li>age_20_29_pct - Percentage of population between the ages of 20 - 29</li>
<li>age_30_39_pct - Percentage of population between the ages of 30 - 39</li>
<li>age_40_49_pct - Percentage of population between the ages of 40 - 49</li>
<li>age_50_59_pct - Percentage of population between the ages of 50 - 59</li>
<li>age_60_69_pct - Percentage of population between the ages of 60 - 69</li>
<li>age_70_over_pct - Percentage of population over the age of 70 </li>
<li>above_poverty_pct - Percentage of population living above the poverty line</li>
<li>employed_pct - Percentage of population that is employed</li>
<li>bachelors_plus_pct - Percentage of population that holds a bachelor degree or higher </li>
<li>high_school_enrollment_pct - Percentage of high school aged population (15 - 17) that is enrolled in high school</li>
<li>pre_school_enrollment_pct - Percentage of preschool aged population (3 - 4) that is enrolled in preschool school< </li>
<li>health_insurance_pct - Percentage of population with health insurance </li>
<li>medicare_pct - Percentage of population with Medicare </li>
<li>medicaid_pct - Percentage of population with Medicaid </li>
<li>owners_pct -  Percentage of housing units occupied by the owner(s)</li>
<li>habitable_pct - Average percentage of housing units with a complete kitchen and/or plumbing </li>
<li>uncrowded_pct - Percentage of housing units with an occupant per room ratio equal to or less than 1  </li>
<li>severe_cost_burden_owner_pct - Percentage of owner occupied housing units with below median MFI </li>
<li>severe_cost_burden_renter_pct - Percentage of renter occupied housing units with below median MFI </li>
<li>two_parent_pct - Percentage of housing units with children living with two parents </li>
<li>vehicle_access_pct - Percentage of housing units with an automotive vehicle available to household members</li>
<li>commute_pct - Percentage of census tract total worker population over the age of 16 that commutes to work by biking, walking, or transit (excludes worker population that works from home) </li>
<li>voter_pct - Percentage of census tract population </li>
<li>diesel_pm_rank - Census tract diesel particular matter percentile (mixture of particles that is part of diesel exhaust)</li>
<li>pm_rank - Census tract particulate matter 2.5 percentile (PM 2.5 - tiny particles or droplets in the air that are two and one half microns or less in width)</li>
<li>safe_drinking_water_rank - Census tract safe drinking water percentile (drinking water contaminant index for selected contaminants)</li>
<li>ozone_rank -  Census tract ozone percentile (Mean of summer months (May-October) of the daily maximum 8-hour ozone concentration (ppm))</li>
<li>park_access_ppa - Percentage of the population living within 1/2 mile of a park, beach, or open space greater than
1 acre </li>
</ul>

Select variables are suffixed with  `_total`, `_z`, or `_rank`, corresponding to total count, standardized, or percentile values respectively.


### Acknowledgements

The  API was developed by the [Data Innovation Lab, Tech Impact](https://techimpact.org). This effort was made possible by our partnerships with Kate DuPont Phillips of Healthy Communities Delaware, Renata Kowalczyk of Wilmington Alliance, Mia Papas of ChristianaCare, and Rita Landgraf of University of Delaware and our work the the Delaware Health Information Network. We would like to extend our deepest thanks for the support and guidance that enabled the success of this initiative.

### Data Sources

Data accesible at the census tract level originate from the following sources:

- ACS, American Community Survey
- CHAS, Comprehensive Housing Assessment System
- CalEPA; California Environmental Protection Agency
- NLCD, National Land Cover Database
- USDA FARA, U.S. Department of Agriculture Food Access Research Atlas
- USEPA, U.S. Environmental Protection Agency
- UC Berkeley, University of California, Berkeley
- GreenInfo


## Running the app locally

1. Clone the repository 
2. Set up a virtual environemnt (optional)

`virtualenv venv`

`source venv/bin/activate`

3. Install dependenices

`pip -r requirements.txt`

4. Start the app

`python app.py`

5. The API will be available at http://localhost:8000/data
