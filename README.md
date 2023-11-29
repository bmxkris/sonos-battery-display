## Collection of scripts to display the battery charge percentage on an e-ink display

* This project consists of:
    * A Python script that should be run by cron, which looks for a Sonos Roam, and then queries it for its battery data. This is then saved to a file
    * A Microphython scirpt that is run on a Raspberry Pi Pico W, which fetches the battery data and displays it on an e-ink display

N.B. Something on the network has to serve the file containing the battery data

Why didn't I have the Pico W directly discover the speaker and ask for the battery details? I couldn't get the SoCo Python module to fit on the Pico