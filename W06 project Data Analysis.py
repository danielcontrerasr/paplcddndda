#I added the user input for a country and then it shows the avarage, the max and the min life expectancy of
#that country
highest_lifeE=-1
lowest_lifeE=90000
yearo_Imax=-1
yearo_Imin=900000
countryo_Imax=-1
countryo_Imin=900000
life_expectencies=list()
avarage=0
lowest_country=""
highest_country=""
year_omaxC=""
year_ominc=""
year_of_interest=input("Enter the year of interest:")
avarage2=0

country_of_interest=input("Enter the country of interest:")
with open("life-expectancy.csv") as life_file:
    next(life_file)
    for line in life_file:



      
        clean_line=line.strip()
        parts=clean_line.split(",")
        countries=parts[0]
        code=parts[1]
        year=int(parts[2])
        lifeE=float(parts[3])
        if lifeE<lowest_lifeE:
            lowest_lifeE=lifeE
            lowest_country=countries
            lowest_year=year
        if lifeE>highest_lifeE:
            highest_lifeE=lifeE
            highest_country=countries
            highest_year=year
        if year_of_interest==str(year):
            life_expectencies.append(float(lifeE))
                
            if lifeE>yearo_Imax:
                yearo_Imax=lifeE
                year_omaxC=countries
            if lifeE<yearo_Imin:
                yearo_Imin=lifeE
                year_ominc=countries
        if country_of_interest==str(countries):
            life_expectencies.append(float(lifeE))
           
            if lifeE>countryo_Imax:
                countryo_Imax=lifeE
             
            if lifeE<countryo_Imin:
                countryo_Imin=lifeE
             

            

avarage= sum(life_expectencies)/len(life_expectencies)
avarage2=sum(life_expectencies)/len(life_expectencies)
            
print(f"The overall min life expentacy is: {lowest_lifeE} from {lowest_country} in {lowest_year}")
print(f"The overall max life life expectancy is: {highest_lifeE} from {highest_country} in {highest_year}")
print()
print(f"for the {year_of_interest}:")
print(f"The avarage life expectancy across all countries was: {avarage}")
print(f"The max life expectancy was in {year_omaxC} with {yearo_Imax}")
print(f"The min life expectancy was {year_ominc} with {yearo_Imin}")
print(f"for the {country_of_interest}:")
print(f"The avarage life expectancy across all years was: {avarage2}")
print(f"The max life expectancy is: {countryo_Imax}")
print(f"The min life expectancy is: {countryo_Imin}")