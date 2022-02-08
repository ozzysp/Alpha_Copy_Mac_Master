# A Python app to make backup with Qt Designer. 


This little backup program was made with PyQt5 library in Qt Designer 
software and looks and feel simple to easy handle in hush situations
when you need a fast backup. 

Designed to fit in a 3.5" inches screen of a Raspberry Pi, the 
interface is quite simple and can be operated with a single touch
in screen.

This is my first full stack project and I will make more in future.

How to install:

At first, clone the project through by clicking in "Code" button then 
select "Download ZIP" button. 

Choose your work directory and save ZIP file in there. Next, double click
at ZIP file and uncompressed the app on that directory.

Now, with terminal you may navigate with ls and cd statement
until you reach the Alpha_Copy_Mac folder, when you choose this folder you must
activate venv to use it.

To activate venv tap in terminal ->
>> source venv/bin/activate

When venv has activate, navigate to src folder and run app ->
>>python3 main.py

Mode of use:

When you start the application, a splash screen appears showing
loading Volumes attached on device.

The second screen shows your original files HD and destination
files HD, choose by clicking in dropdown button set your device and
click in "Confirm" button.

Next window will be show second confirmation options to ensure your
chosen devices. In this window will start a backup process when
you click in "Make Copy" button a new folder will be created with
date and time stamp at this moment.

Next a progress bar will be show, when finish a next window will
appear. 

This window can be a "Successful Copy" message with "Done" button
or can be "Errors Found" message invalidating your copy and with
another "Done" button. In this case you can repeat the process or
try in another device.

The next window will be an "Eject Devices" button to unmount all 
HD's to secure disconnect USB. 

After all, a new window it will show up with "Ejected Devices"
message and a "Make New Copy" button to restart a new backup 
process.

I hope it can be useful for everyone. 


ADVICE.

THIS APP HAS BEEN MADE FOR EDUCATIONAL PURPOSES ONLY, I AM NOT 
RESPONSIBLE FOR LOSS OR DAMAGE TO THE MATERIALS INVOLVED IN ITS 
USE. ITS USE IS AT THE USER'S OWN RISK AND DISCLAIMS ANY 
RESPONSIBILITIES REGARDING SUCH MATERIALS.

Thanks for everyone who helped me and made this possible.
