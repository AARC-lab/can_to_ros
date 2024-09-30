#/bin/bash

# if [ $EUID -ne 0 ]; then
#     echo "$0 not running as root. Please call using sudo."
#     exit 2
# fi

python vinParser.py
echo "The current vin details are  " $(cat ./vin_details.json)
echo "The current vin is " $(cat ./vin)
echo "If something is incorrect, run libpanda/scripts/setVin.sh, or run vinParser.py to lookup details"

read -r -p "Does this information look correct? Proceed to generating CANtoROS from this VIN? [Y/N] " response
  case "$response" in
      [yY][eE][sS]|[yY])


	wget https://raw.githubusercontent.com/jmscslgroup/strym/master/strym/dbc/toyota_rav4_hybrid.dbc  -O ~/strym/strym/dbc/toyota_rav4_hybrid.dbc
	wget https://raw.githubusercontent.com/jmscslgroup/strym/master/strym/dbc/honda_pilot_2017.dbc  -O ~/strym/strym/dbc/honda_pilot_2017.dbc
	wget https://raw.githubusercontent.com/jmscslgroup/strym/master/strym/dbc/toyota_rav4_hybrid.dbc  -O ~/strym/strym/dbc/nissan_rogue_2021.dbc
	wget https://raw.githubusercontent.com/jmscslgroup/strym/master/strym/dbc/toyota_rav4_hybrid.dbc  -O ~/strym/strym/dbc/toyota_rav4_2019.dbc
	wget https://raw.githubusercontent.com/jmscslgroup/strym/master/strym/dbc/toyota_rav4_hybrid.dbc  -O ~/strym/strym/dbc/toyota_rav4_2020.dbc
	wget https://raw.githubusercontent.com/jmscslgroup/strym/master/strym/dbc/toyota_rav4_hybrid.dbc  -O ~/strym/strym/dbc/toyota_rav4_2021.dbc
	wget https://raw.githubusercontent.com/jmscslgroup/strym/master/strym/dbc/honda_pilot_2017.dbc -O ~/strym/strym/dbc/honda_pilot_2017.dbc
	python3 ./makeSignalsJSON.py
	python3 ./generateDecode_Subs.py
	./regen_vehicle_interface.sh

    echo "Code generation complete, please perform catkin_make"
esac
