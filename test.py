import sys
import time
import xpc

def monitor():
    with xpc.XPlaneConnect() as client:
        while True:
            posi = client.getPOSI();
            ctrl = client.getCTRL();
            tail_num = client.getDREF("sim/aircraft/view/acf_descrip")
            text = ''.join(chr(int(i)) for i in tail_num)

            hours = client.getDREF("sim/cockpit2/clock_timer/local_time_hours")
            minutes = client.getDREF("sim/cockpit2/clock_timer/local_time_minutes")
            seconds = client.getDREF("sim/cockpit2/clock_timer/local_time_seconds")

            print(text)
            print("Time: %i:%i:%i" % (hours[0], minutes[0], seconds[0]))
            print("Lat:%4f Long:%4f Alt:%4f" % (posi[0], posi[1], posi[2]))
            print("Aileron:%2f Elevator:%2f Rudder:%2f Throttle:%2f" % (ctrl[1], ctrl[0], ctrl[2], ctrl[3]))
            print()

            time.sleep(0.2)


if __name__ == "__main__":
    monitor()
