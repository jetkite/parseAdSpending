import pandas as pd
import xlsxwriter
df = pd.read_csv('ads-spending.csv')

country_spend = [72]

for x in range(72):
    country_spend.append(0)

countries = df['Country/Territory (Geographic)'].tolist()
spend_data = df['Cost'].tolist()

country_spend[0] = spend_data[countries.index('United States')] if 'United States' in countries else 0
country_spend[1] = spend_data[countries.index('Germany')] if 'Germany' in countries else 0
country_spend[2] = spend_data[countries.index('Austria')] if 'Austria' in countries else 0
country_spend[3] = spend_data[countries.index('Japan')] if 'Japan' in countries else 0
country_spend[4] = spend_data[countries.index('Canada')] if 'Canada' in countries else 0
country_spend[5] = spend_data[countries.index('France')] if 'France' in countries else 0
country_spend[6] = spend_data[countries.index('Switzerland')] if 'Switzerland' in countries else 0
country_spend[7] = spend_data[countries.index('South Korea')] if 'South Korea' in countries else 0
country_spend[8] = spend_data[countries.index('Netherlands')] if 'Netherlands' in countries else 0
country_spend[9] = spend_data[countries.index('United Kingdom')] if 'United Kingdom' in countries else 0
country_spend[10] = spend_data[countries.index('Belgium')] if 'Belgium' in countries else 0
country_spend[11] = spend_data[countries.index('Italy')] if 'Italy' in countries else 0
country_spend[12] = spend_data[countries.index('Brazil')] if 'Brazil' in countries else 0
country_spend[13] = spend_data[countries.index('Taiwan')] if 'Taiwan' in countries else 0
country_spend[14] = spend_data[countries.index('Hong Kong')] if 'Hong Kong' in countries else 0
country_spend[15] = spend_data[countries.index('Denmark')] if 'Denmark' in countries else 0
country_spend[16] = spend_data[countries.index('Sweden')] if 'Sweden' in countries else 0
country_spend[17] = spend_data[countries.index('Finland')] if 'Finland' in countries else 0
country_spend[18] = spend_data[countries.index('Australia')] if 'Australia' in countries else 0
country_spend[19] = spend_data[countries.index('Spain')] if 'Spain' in countries else 0
country_spend[20] = spend_data[countries.index('Poland')] if 'Poland' in countries else 0
country_spend[21] = spend_data[countries.index('Mexico')] if 'Mexico' in countries else 0
country_spend[22] = spend_data[countries.index('Czechia')] if 'Czechia' in countries else 0
country_spend[23] = spend_data[countries.index('Slovakia')] if 'Slovakia' in countries else 0
country_spend[24] = spend_data[countries.index('Thailand')] if 'Thailand' in countries else 0
country_spend[25] = spend_data[countries.index('Hungary')] if 'Hungary' in countries else 0
country_spend[26] = spend_data[countries.index('Ireland')] if 'Ireland' in countries else 0
country_spend[27] = spend_data[countries.index('New Zealand')] if 'New Zealand' in countries else 0
country_spend[28] = spend_data[countries.index('Indonesia')] if 'Indonesia' in countries else 0
country_spend[29] = spend_data[countries.index('Vietnam')] if 'Vietnam' in countries else 0
country_spend[30] = spend_data[countries.index('Norway')] if 'Norway' in countries else 0
country_spend[31] = spend_data[countries.index('Croatia')] if 'Croatia' in countries else 0
country_spend[32] = spend_data[countries.index('Luxembourg')] if 'Luxembourg' in countries else 0
country_spend[33] = spend_data[countries.index('Israel')] if 'Israel' in countries else 0
country_spend[34] = spend_data[countries.index('Greece')] if 'Greece' in countries else 0
country_spend[35] = spend_data[countries.index('South Africa')] if 'South Africa' in countries else 0
country_spend[36] = spend_data[countries.index('Russian Federation')] if 'Russian Federation' in countries else 0
country_spend[37] = spend_data[countries.index('Portugal')] if 'Portugal' in countries else 0
country_spend[38] = spend_data[countries.index('Romania')] if 'Romania' in countries else 0
country_spend[39] = spend_data[countries.index('India')] if 'India' in countries else 0
country_spend[40] = spend_data[countries.index('Latvia')] if 'Latvia' in countries else 0
country_spend[41] = spend_data[countries.index('Estonia')] if 'Estonia' in countries else 0
country_spend[42] = spend_data[countries.index('Lithuania')] if 'Lithuania' in countries else 0
country_spend[43] = spend_data[countries.index('Singapore')] if 'Singapore' in countries else 0
country_spend[44] = spend_data[countries.index('Malaysia')] if 'Malaysia' in countries else 0
country_spend[45] = spend_data[countries.index('Brunei')] if 'Brunei' in countries else 0
country_spend[46] = spend_data[countries.index('Colombia')] if 'Colombia' in countries else 0
country_spend[47] = spend_data[countries.index('Peru')] if 'Peru' in countries else 0
country_spend[48] = spend_data[countries.index('Argentina')] if 'Argentina' in countries else 0
country_spend[49] = spend_data[countries.index('Philippines')] if 'Philippines' in countries else 0
country_spend[50] = spend_data[countries.index('Paraguay')] if 'Paraguay' in countries else 0
country_spend[51] = spend_data[countries.index('Jamaica')] if 'Jamaica' in countries else 0
country_spend[52] = spend_data[countries.index('Haiti')] if 'Haiti' in countries else 0
country_spend[53] = spend_data[countries.index('Guatemala')] if 'Guatemala' in countries else 0
country_spend[54] = spend_data[countries.index('Bolivia')] if 'Bolivia' in countries else 0
country_spend[55] = spend_data[countries.index('Ecuador')] if 'Ecuador' in countries else 0
country_spend[56] = spend_data[countries.index('Chile')] if 'Chile' in countries else 0
country_spend[57] = spend_data[countries.index('Panama')] if 'Panama' in countries else 0
country_spend[58] = spend_data[countries.index('Nicaragua')] if 'Nicaragua' in countries else 0
country_spend[59] = spend_data[countries.index('Puerto Rico')] if 'Puerto Rico' in countries else 0
country_spend[60] = spend_data[countries.index('Costa Rica')] if 'Costa Rica' in countries else 0
country_spend[61] = spend_data[countries.index('Barbados')] if 'Barbados' in countries else 0
country_spend[62] = spend_data[countries.index('Uruguay')] if 'Uruguay' in countries else 0
country_spend[63] = spend_data[countries.index('Dominican Republic')] if 'Dominican Republic' in countries else 0
country_spend[64] = spend_data[countries.index('El Salvador')] if 'El Salvador' in countries else 0
country_spend[65] = spend_data[countries.index('Egypt')] if 'Egypt' in countries else 0
country_spend[66] = spend_data[countries.index('Morocco')] if 'Morocco' in countries else 0
country_spend[67] = spend_data[countries.index('Tunisia')] if 'Tunisia' in countries else 0
country_spend[68] = spend_data[countries.index('Jordan')] if 'Jordan' in countries else 0
country_spend[69] = spend_data[countries.index('Saudi Arabia')] if 'Saudi Arabia' in countries else 0
country_spend[70] = spend_data[countries.index('United Arab Emirates')] if 'United Arab Emirates' in countries else 0
country_spend[71] = spend_data[countries.index('Qatar')] if 'Qatar' in countries else 0
country_spend[72] = spend_data[countries.index('Kuwait')] if 'Kuwait' in countries else 0



countries_main = ["US",
"Germany",
"Austria",
"Japan",
"Canada",
"France",
"Switzerland",
"South Korea",
"Netherlands",
"UK",
"Belgium",
"Italy",
"Brazil",
"Taiwan",
"Hong Kong",
"Denmark",
"Sweden",
"Finland",
"Australia",
"Spain",
"Poland",
"Mexico",
"Czech Republic",
"Slovakia",
"Thailand",
"Hungary",
"Ireland",
"New Zealand",
"Indonesia",
"Viet nam",
"Norway",
"Croatia",
"Luxembourg",
"Israel",
"Greece",
"South Africa",
"Russia",
"Portugal",
"Romania",
"India",
"Latvia",
"Estonia",
"Lithuania",
"Singapore",
"Malaysia",
"Brunei",
"Colombia",
"Peru",
"Argentina",
"Philippinnes",
"Paraguay",
"Jamaica",
"Haiti",
"Guatemala",
"Bolivia",
"Ecuador",
"Chile",
"Panama",
"Nicaragua",
"Puerto Rico",
"Costa Rica",
"Barbados",
"Uruguay",
"Dominican R.",
"El Salvador",
"Egypt",
"Morocco",
"Tunisia",
"Jordan",
"Saudi Arabia",
"UAE",
"Qatar",
"Kuwait"]
df = pd.DataFrame({
    'Countries': countries_main,
    'Ads Spending': country_spend
})

writer = pd.ExcelWriter('ads-spending.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Ads', index=False)
writer.save()