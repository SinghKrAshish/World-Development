from flask import Flask, render_template, request
import pickle

regressor = pickle.load(open('modelforcpi.sav', 'rb'))
countries = ['Afghanistan',
 'Albania',
 'Algeria',
 'Angola',
 'Argentina',
 'Armenia',
 'Australia',
 'Austria',
 'Azerbaijan',
 'Bahamas, The',
 'Bahrain',
 'Bangladesh',
 'Barbados',
 'Belarus',
 'Belgium',
 'Belize',
 'Benin',
 'Bhutan',
 'Bolivia',
 'Bosnia and Herzegovina',
 'Botswana',
 'Brazil',
 'Brunei Darussalam',
 'Bulgaria',
 'Burkina Faso',
 'Burundi',
 'Cabo Verde',
 'Cambodia',
 'Cameroon',
 'Canada',
 'Central African Republic',
 'Chad',
 'Chile',
 'China',
 'Colombia',
 'Comoros',
 'Congo, Dem. Rep.',
 'Congo, Rep.',
 'Costa Rica',
 "Cote d'Ivoire",
 'Croatia',
 'Cuba',
 'Cyprus',
 'Czechia',
 'Denmark',
 'Djibouti',
 'Dominica',
 'Dominican Republic',
 'Ecuador',
 'Egypt',
 'El Salvador',
 'Equatorial Guinea',
 'Eritrea',
 'Estonia',
 'Eswatini',
 'Ethiopia',
 'Fiji',
 'Finland',
 'France',
 'French Polynesia',
 'Gabon',
 'Gambia',
 'Georgia',
 'Germany',
 'Ghana',
 'Greece',
 'Grenada',
 'Guam',
 'Guatemala',
 'Guinea',
 'Guinea-Bissau',
 'Guyana',
 'Haiti',
 'Honduras',
 'Hong Kong',
 'Hungary',
 'Iceland',
 'India',
 'Indonesia',
 'Iran',
 'Iraq',
 'Ireland',
 'Israel',
 'Italy',
 'Jamaica',
 'Japan',
 'Jordan',
 'Kazakhstan',
 'Kenya',
 "Korea, Dem. People's Rep.",
 'Korea, Rep.',
 'Kosovo',
 'Kuwait',
 'Kyrgyzstan',
 'Lao PDR',
 'Latvia',
 'Lebanon',
 'Lesotho',
 'Liberia',
 'Libya',
 'Lithuania',
 'Luxembourg',
 'Madagascar',
 'Malawi',
 'Malaysia',
 'Maldives',
 'Mali',
 'Malta',
 'Mauritania',
 'Mauritius',
 'Mexico',
 'Moldova',
 'Mongolia',
 'Montenegro',
 'Morocco',
 'Mozambique',
 'Myanmar',
 'Namibia',
 'Nepal',
 'Netherlands',
 'New Zealand',
 'Nicaragua',
 'Niger',
 'Nigeria',
 'North Macedonia',
 'Norway',
 'Oman',
 'Pakistan',
 'Panama',
 'Papua New Guinea',
 'Paraguay',
 'Peru',
 'Philippines',
 'Poland',
 'Portugal',
 'Puerto Rico',
 'Qatar',
 'Romania',
 'Russia',
 'Rwanda',
 'Samoa',
 'São Tomé and Príncipe',
 'Saudi Arabia',
 'Senegal',
 'Serbia',
 'Seychelles',
 'Sierra Leone',
 'Singapore',
 'Slovak Republic',
 'Slovenia',
 'Solomon Islands',
 'Somalia',
 'South Africa',
 'South Sudan',
 'Spain',
 'Sri Lanka',
 'St. Lucia',
 'St. Vincent and the Grenadines',
 'Sudan',
 'Suriname',
 'Sweden',
 'Switzerland',
 'Syria',
 'Tajikistan',
 'Tanzania',
 'Thailand',
 'Timor-Leste',
 'Togo',
 'Tonga',
 'Trinidad and Tobago',
 'Tunisia',
 'Turkey',
 'Turkmenistan',
 'Uganda',
 'Ukraine',
 'United Arab Emirates',
 'United Kingdom',
 'United States',
 'Uruguay',
 'Uzbekistan',
 'Vanuatu',
 'Venezuela',
 'Vietnam',
 'Yemen',
 'Zambia',
 'Zimbabwe']
iclasses = ['High income', 'Low income', 'Lower middle income', 'Upper middle income', ]
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        country = str(request.form.get('country'))
        incomeclass = str(request.form.get('incomeclass'))
        electricity_access = float(request.form.get('electricity_access'))
        gdp = float(request.form.get('gdp'))
        gdp_capita = float(request.form.get('gdp_capita'))
        labor_rate = float(request.form.get('labor_rate'))
        labor_force = float(request.form.get('labor_force'))
        land_area = float(request.form.get('land_area'))
        life_expectancy = float(request.form.get('life_expectancy'))
        adult_literacy = float(request.form.get('adult_literacy'))
        water_access = float(request.form.get('water_access'))
        air_pollution = float(request.form.get('air_pollution'))
        population_density = float(request.form.get('population_density'))
        population = float(request.form.get('population'))
        alcohol_consumption = float(request.form.get('alcohol_consumption'))
        unemployment_rate = float(request.form.get('unemployment_rate'))
        social_support = float(request.form.get('social_support'))
        freedom = float(request.form.get('freedom'))
        generosity = float(request.form.get('generosity'))

        country = [0]*countries.index(country) + [1] + [0]*(186-countries.index(country)-1)
        incomeclass = [0]*iclasses.index(incomeclass) + [1] + [0]*(4-iclasses.index(incomeclass)-1)

        y_test = [
            electricity_access,
            gdp,
            gdp_capita,
            labor_rate,
            labor_force,
            land_area,
            life_expectancy,
            adult_literacy,
            water_access,
            air_pollution,
            population_density,
            population,
            alcohol_consumption,
            unemployment_rate,
            social_support,
            freedom,
            generosity
        ] + country + incomeclass
        print(y_test)

        # y_test = transformer.transform(data)

        result = float(regressor.predict([y_test])[0])
        result1="The forecasted value of the CPI as per analysis is: " + str(result)
        return render_template('index.html', pred=result1)
    return render_template('index.html', pred='\n')


if __name__ == '__main__':
    app.run(debug=True)
