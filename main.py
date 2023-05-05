from FlightRadar24.api import FlightRadar24API
fr_api = FlightRadar24API()

airlines = fr_api.get_airlines()

flights_in_air = fr_api.get_flights()

military_icao = ["PLF", "FAG", "ASY", "ASF", "BAF", "BRS", "AFB", "CFC", "CKJ", "FAC", "HRZ", "CEF", "DAF", "FAE", "EGY", "EEF", "FNF", "FAF", "CTM", "GAF", "GHF", "HAF", "HUF", "IFC", "IAM", "RJZ", "LAF", "LBF", "LYF", "RMF", "FAM", "NAF", "KIW", "NGR", "NOW", "MJN", "FPR", "PLF", "AFP", "RCH", "NYB", "MBR", "DNY", "FNY", "GNY", "HNA", "MMI", "ANX", "NRN", "INP", "ROF", "NAT", "715"]

def main():

    for i in range (0, len(military_icao), 1):
        target_af = military_icao[i]
        target_af_details = list(filter(lambda airline: airline['ICAO'] == target_af, airlines))
        target_flight = fr_api.get_flights(airline = military_icao[i])

        if len(target_flight) > 0:
            #print(target_af_details)
            #print()

            if len(target_af_details) == 0:
                details0 = fr_api.get_flight_details(target_flight[0].id)
                target_flight[0].set_flight_details(details0)
                operator = target_flight[0].airline_name
                
            else: 
                operator = target_af_details

            print(operator)
            print()
            
            for j in range (0, len(target_flight), 1):
            
                details = fr_api.get_flight_details(target_flight[j].id)
                target_flight[j].set_flight_details(details)
                
                print((j+1), ".:  ", target_flight[j])

                print("Aircraft: ", target_flight[j].aircraft_model)
                
                print("Latitude: ", target_flight[j].latitude, "Longitude: ", target_flight[j].longitude)

                print("Destination: ", target_flight[j].destination_airport_name)

                print()
            
            print("***")
            print()
    return(0)

#main()

