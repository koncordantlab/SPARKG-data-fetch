import json
import requests

def get_chemical_details_pubchem(chem_name):
    response = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+chem_name+'/json')
    if response.status_code == 200:
        # print(f"Getting data from PubChem for {chem_name}")
        data = json.loads(response.text)
        output = {}
        props = data["PC_Compounds"][0]["props"]
        output['PubChemCID'] = data["PC_Compounds"][0]["id"]["id"]["cid"]

        for prop in props:
            # print(prop)
            label = prop["urn"]["label"]
            value_dict = prop["value"]
            if prop["urn"].get("name"):
                label = f"{label} ({prop['urn']['name']})"
            output[label] = value_dict.get("ival", value_dict.get("fval", value_dict.get("sval", value_dict.get("binary"))))
            
    else:
        # print(f"Error fetching data for {chem_name}:\n {response.status_code} - {response.text}")
        # return {'name': chem_name}
        return None
    return output

def save_file(data, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(data, indent=8))

def get_element_list(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines() if line.strip()]

if __name__ == "__main__":

    # element_list = get_element_list('./data/from_email/chemical_list_email.txt')
    # data = {}
    # not_found = []
    # for element in element_list:
    #     if get_chemical_details_pubchem(element):
    #         data[element] = get_chemical_details_pubchem(element)
    #         print(f"Data fetched for {element}")
    #     else:
    #         not_found.append(element)
    #         print(f"Data not found for {element}")
    #         continue
    # save_file(not_found, './data/from_email/not_found_chemical_list_email.json')
    # save_file(data, './data/from_email/chemical_list_email.json')



    # Define categories
    opioids = [
        "Codeine", "Morphine", "Oxymorphone", "Hydrocodone", "Hydromorphone", "Oxycodone", "Methadone", "Fentanyl",
        "Carfentanil", "Meperidine", "Tramadol", "Buprenorphine", "Norbuprenorphine", "Pentazocine", "Naloxone", "Naltrexone",
        "Norcarfentanil", "Noroxycodone", "6-acetylmorphine", "EDDP", "O-desmethyltramadol", "Metonitazene", "N-desethylmetonitazene",
        "U-47700", "Etonitazene", "AH-7921", "MT-45", "Isotonitazene", "N-PyrrolidinoEtonitazene", "Thebacon", "Acetylfentanyl",
        "Butyrfentanyl", "Furanylfentanyl", "Remifentanil", "Sufentanil", "Alfentanil", "Thiafentanil", "N-Allylnorcodeine",
        "N-Allylnormorphine", "N-Methylmorphine", "Nicomorphine", "Hydromorphinol", "Dihydrocodeine", "Dihydroetorphine",
        "Desomorphine", "Etorphine", "Drotebanol", "Levacetylmethadol", "Norlevorphanol", "Phenadoxone", "3-Methylfentanyl",
        "Acetyldihydrocodeine", "Allylprodine", "Benzylmorphine", "Beta-Hydroxyfentanyl", "Meptazinol", "Diprenorphine",
        "Difenoxin", "Dihydromorphine", "Phenoperidine", "Tebaine", "Myrophine", "Piritramide"
    ]

    # Stimulants
    stimulants = [
        "Methamphetamine", "Amphetamine", "Dextroamphetamine", "Methylphenidate", "Benzoylecgonine", "Cocaine", "MDMA", "MDA",
        "Modafinil", "Armodafinil", "Phenylpropanolamine", "Methcathinone", "Mephedrone", "Pyrovalerone", "Ethylphenidate",
        "Desoxypipradrol", "Fenethylline", "4-Methylamphetamine", "Hexedrone", "Alpha-PVP", "Flakka", "Alpha-ethylphenidate",
        "4-Fluoromethcathinone", "N-Ethylpentylone", "N-Methylpentylone", "Pentylone", "N,N-dimethylpentylone", "Cathine",
        "Cathinone", "Ephedrine", "Pseudoephedrine", "Phenmetrazine", "Methylone", "Ethylone", "Butylone", "Pentedrone",
        "3-MMC", "4-MEC", "5-MAPB", "6-APB", "5-APB", "3,4-Methylenedioxyphenyl-2-butanone", "PMMA", "PMEA", "MDAI", "DIPT",
        "4-HO-MIPT", "4-HO-DPT", "4-HO-DiPT", "2C-B-Fly", "25H-NBOMe", "25D-NBOMe", "Fencamfamine", "Naphyrone", "Dimethylamphetamine",
        "Ethcathinone", "Bupropion", "Propylhexedrine", "Methylbenzodioxolylbutanamine", "4-Methylaminorex", "2-DPMP", "PMA", 
        "TFMPP", "Methylphenidate hydrochloride", "Dexmethylphenidate", "Mephedrone hydrochloride", "Methcathinone hydrochloride"
    ]

    # Sedatives
    sedatives = [
        "Zopiclone", "Eszopiclone", "Zolpidem", "Temazepam", "Flunitrazepam", "Alprazolam", "Diazepam", "Clonazepam",
        "Lorazepam", "Nordiazepam", "Oxazepam", "Midazolam", "Bromazepam", "Phenazepam", "Flubromazepam", "Flualprazolam",
        "Etizolam", "Bromazolam", "Diclazepam", "Adinazolam", "Pyrazolam", "Clobazam", "Clonazolam", "Flunitrazolam",
        "Thionylbromazepam", "Carisoprodol", "Meprobamate", "Phenobarbital", "Secobarbital", "Gabapentin", "Pregabalin",
        "Zaleplon", "Brotizolam", "Cinolazepam", "Loprazolam", "Nitrazepam", "Clotiazepam", "Quazepam", "Flurazepam",
        "Medazepam", "Oxazolam", "Prazepam", "Tofisopam", "Triazolam", "Chlordiazepoxide", "Ethinamate", "Methyprylon",
        "Methylpentynol", "Paraldehyde", "Flunitrazolam", "Nimetazepam", "Bromisovalum", "Secbutabarbital"
    ]

    hallucinogens = [
        "LSD", "Psilocin", "Psilocybin", "4-HIAA", "DMT", "5-MeO-DMT", "4-AcO-DMT", "5-MeO-MiPT", "5-MeO-DiPT", "Ibogaine",
        "Harmaline", "Salvinorin A", "Mescaline", "2C-B", "2C-I", "2C-T-7", "DOC", "DOB", "DOI", "2C-C", "2C-E", "2C-T-4",
        "2C-P", "2C-D", "N-Ethyl-2C-B", "N-Ethyl-2C-I", "N-Methyl-2C-B", "N-Methyl-2C-I", "25B-NBOMe", "25C-NBOMe", "25I-NBOMe",
        "2C-T-21", "4-HO-DET", "4-HO-DPT", "4-HO-DBT", "4-HO-EMPT", "4-HO-McPT", "4-HO-TMT", "4-AcO-MiPT", "4-AcO-DPT",
        "6-APDB", "5-APDB", "6-MAPB", "5-MAPB", "2C-V", "2C-G", "2C-N", "2C-Y", "2C-G-NBOMe", "2C-B-NBOMe", "2C-C-NBOMe"
    ]

    dissociatives = [
        "Ketamine", "Phencyclidine", "Eticyclidine", "Deschloroketamine", "Norketamine", "3-MeO-PCP", "2-fluoro-2-oxo PCE",
        "2-Oxo-3-hydroxy-LSD", "3-Methoxyphencyclidine", "Tiletamine", "Dextrorphan", "Levomethorphan", "Dizocilpine", "Dextrallorphan", 
        "Memantine", "Rolicyclidine", "Tenocyclidine", "Ephenidine", "Methoxphenidine", "Fluorexetamine", "Methoxetamine", "Diperodon"
    ]

    synthetic_cannabinoids = [
        "JWH-018", "JWH-073", "JWH-250", "AM-2201", "AB-FUBINACA", "ADB-FUBINACA", "MDMB-4en-PINACA butanoic acid",
        "AMB-FUBINACA", "ADB-CHMINACA", "APP-FUBINACA", "AB-CHMINACA", "THJ-018", "THJ-2201", "CUMYL-PINACA", "PX-2",
        "PX-3", "FUB-PB-22", "5F-PB-22", "5F-ADB", "XLR-11", "AKB48", "CP-55940", "SR-144528", "UR-144", "AB-001",
        "AB-005", "ADB-PINACA", "HU-210", "CP-47497", "WIN-55212", "HU-308", "CBDV", "CBG", "THCV", "CBC", "CBD-A", "SR-144528", 
        "AM-694", "XLR-12", "JWH-398", "JWH-081", "JWH-122", "JWH-210", "JWH-133", "JWH-307"
    ]

    inhalants = [
        "Toluene", "Chloroform", "Butane", "Ether", "Nitrous Oxide", "Amyl Nitrite", "Isobutyl Nitrite", "Cyclohexyl Nitrite",
        "Acetone", "Gasoline", "Propane", "Diethyl Ether", "Chlorodifluoromethane", "Ethyl chloride", "Tetrafluoroethane", "Benzene", 
        "Dichloromethane", "Methyl ethyl ketone", "Trichloroethylene", "Hexane", "Heptane", "Ethyl acetate", "Methyl isobutyl ketone", 
        "Dimethyl ether", "Toluene diisocyanate"
    ]

    other_substances = [
        "CBD", "THC", "Delta-8-THC", "Delta-10-THC", "THC-O-Acetate", "THC-P", "Nabilone", "Dronabinol", "Levonantradol",
        "7-hydroxymitragynine", "Mitragynine", "Speciociliatine", "Xylazine", "7-aminoclonazepam", "Norbuprenorphine",
        "alpha-hydroxyalprazolam", "alpha-hydroxybromazolam", "R-HHC-COOH", "S-HHC-COOH", "8R-OH-R-HHC", "8S-OH-R-HHC",
        "7-OH-CBD glucuronide", "HHC", "Hexahydrocannabinol", "8-Hydroxy-THC", "11-Hydroxy-THC", "Olivetol", "Cannabigerol", "Cannabichromene",
        "Cannabidiolic Acid", "Delta-6a10a-THC", "Cannabicyclol", "Cannabinol", "CBN-A", "THC-A", "Cannabitriol"
    ]

    list_of_lists = [opioids, 
                     stimulants, 
                     sedatives, 
                     hallucinogens, 
                     dissociatives, 
                     synthetic_cannabinoids, 
                     inhalants, 
                     other_substances]

    # Get data for each category
    for category in list_of_lists:
        data = {}
        for element in category:
            data[element] = get_chemical_details_pubchem(element)
            print(f"Data fetched for {element}")
        save_file(data, f'./data/from_llm/{[k for k, v in locals().items() if v is category][0]}_details.json')




