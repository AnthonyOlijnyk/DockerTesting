Initial Creation

This is a test script that takes an image, recolors it, and then shows the three recolors on one figure.

To use this file normally, just download the folder, cd into it in terminal and write python imageprocessing.py or hdftest.py

You should also see four lines printed to the terminal if you did imageprocessing.py and you should see a couple of matricies if you did hdftest.py. This was done to show the difference between how these scripts run inside a container vs outside a container.

Update 1

Now when running the script in docker, use docker-compose up when the image has been pulled. This will run both applications in separate containers.
