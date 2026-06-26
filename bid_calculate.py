import csv
import datetime

COMM_DATA_TYPES = {"elec_cons_cumul": 2, "elec_cons_inst_rate": 3, "tot_energy_stor": 4, "pres_energy_stor": 6}
comm_data = {}
HAS_ADV_LOAD_UP = False 

if HAS_ADV_LOAD_UP:
    COMM_DATA_TYPES["alu_tot_energy_stor"] = 8
    COMM_DATA_TYPES["alu_pres_energy_stor"] = 10

#note, this will create a new log and then error if log.csv doesn't already exist
#so only run after log.csv is created
with open("log.csv", "r") as f:
    log_data = csv.reader(f)
    latest_data = comm_data[-1]

    #check if it matches the current time
    log_datetime = latest_data[0]
    curr_datetime = datetime.datetime.now()
    #basic - 5 min checking
    if (int(datetime.datetime.now().minute) - int(log_datetime.split()[3].split(":")[0])) >= 5:
        print("something wrong with log :(")

    for comm_type in COMM_DATA_TYPES.keys():
        comm_data[comm_type] = latest_data[COMM_DATA_TYPES[comm_type]]

#do some calculations here with comm_data