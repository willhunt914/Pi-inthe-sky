# Pi-inthe-sky

## Table of Contents

* [Planning](#Planning)
* [Safety & Risk Mitigation](#Safety/Risk_Mitigation)
* [Schedule](#Schedule)
* [Weekly Progress](#Weekly_progress)
* [Final Reflection](#Final_Reflection)
  

## Planning 

The goal of this assignment is to have a projectile launch and land without breaking. The Projectile also has to document the data from the launch. 


- Our first idea for the project was to do a slingshot because it would be relatively easy to make and could launch a far distance.
- To make this happen, we need to ensure that we can remotely save accelerometer data on the pico, and develop the CAD design in a way such that the pico will not break.
- A success for this project would be for the payload to launch at least 20 feet without breaking and for it to collect our data.
- If we have extra time, we will improve the slingshot and/or projectile to make it launch further and faster.
- For this project, we still need to learn how to make a slingshot that will launch the projectile far enough. We also have to learn how to make the projectile strong enough so  that it won't break.

#### Safety/Risk_Mitigation

- The biggest safety concerns for this project are the projectile hitting someone or the slingshot breaking
- For safe launches, we will wear safety glasses, and make sure that nobody is downrange
- We will also test the slingshot at lower power and work our way up so that we can identify potential failures and be confident that it won't break

[Materials List](https://docs.google.com/document/d/1O94NrEtbGrpvcdbZZRessnzT4ntu9cPLEgHKotI4B5Y/edit)

![WIN_20231206_09_42_07_Pro](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/8e2b437d-e054-4eb0-9128-844bc5761be3)

_Our first sketch idea for the slingshot and projectile_

![image](https://github.com/willhunt914/Pi-inthe-sky/assets/113116262/390b0333-f159-4d26-827f-21391df52989)

_Block diagram for code_

### Schedule

Week 1 (Jan 2 - 5): Finalize CAD and code plans

Week 2 (Jan 8 - 12): Begin CAD and code prototypes

Week 3 (Jan 15 - 19): Work on CAD and code

Week 4 (Jan 22 - 26): Work on CAD and code/wiring

Week 5 (Jan 29 - Feb 2): Try to get functional code product

Week 6 (Feb 5 - 9): Work on CAD, troubleshoot code

Week 7 (Feb 12 - 16): Troubleshoot code/wiring

Week 8 (Feb 19 - 23): Finish code and wiring

Week 9 (Feb 26 - Mar 1): Finish prototype

Week 10 (Mar 4 - 8): Finalize CAD and circuit board

Week 11 (Mar 11 - 15): Fabricate CAD design and circuit board

Week 12 (Mar 18 - 22): Build the final product

Week 13 (Mar 25 - 28): Final preparations for the first launch

### Weekly_progress

Week 1: This week was mainly focused on planning. We decided that the slingshot was our first and only design. We also began working on our code and got the basic shape of the projectile. 

Week 2: This  week we added holes to screw the two projectile halves together. We began working on the code using the "Data Saver 1" assignment and building off of it. We started planning for the creation of the slingshot as well. 

![Screenshot 2024-01-24 093237](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/fa171d8a-c4e1-4a0b-bd60-e93c20f0c469)

Week 3: This week we completed the sling for the slingshot. We continued to work on the code as well.

![slingshot](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/c03777e6-7903-40f0-9b7a-92ef31277af5)

Week 4: This week we continued to troubleshoot the code and get it to work as well as fixing an issue with the screw holes being too small in the onshape document. 

Week 5: This week we mainly focused on the Onshape. Shown below, we added structure to the legs to screw the pico in. 

![support screenshot](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/10be424d-c8e9-4674-b05e-cc038eb6e1bc)

We also thickened the walls of the sphere to make it more sturdy and used the section view to make sure that nothing was intersecting.

Week 6: This week we printed the sphere and made sure all of the holes for the screws, switch, and LED were the right size. 

![unnamed](https://github.com/willhunt914/Pi-inthe-sky/assets/113116262/150bdcec-7e1f-410f-895b-b98814293792)
[DataCode](https://github.com/willhunt914/Pi-inthe-sky/blob/main/pi%20in%20the%20sky/datasaver1.py)

[FinalCode](https://github.com/willhunt914/Pi-inthe-sky/blob/main/pi%20in%20the%20sky/finalproject.py)

Week 7: This week we put all our eggs in the code basket. Early in the week, we focused on getting the original Data Saver 1 assignment to work and later we added code to get an altimeter to work as well. This code was all relatively simple and the only thing we struggled with was getting the pins to match on the Pico and in the code.  

[DataCode](https://github.com/willhunt914/Pi-inthe-sky/blob/main/pi%20in%20the%20sky/datasaver1.py)

[FinalCode](https://github.com/willhunt914/Pi-inthe-sky/blob/main/pi%20in%20the%20sky/finalproject.py)

Week 8: This was kind of a rest week for us. Sometimes in a project, it takes one step back to go two steps forward and we needed this step back to stay on track.

Week 9: This week we made updated wiring diagrams, including one on the circuit board. With this figured out, we should be ready to solder the circuit board next week.

![piinthe skywiring](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/0c917ec4-f363-4596-afea-f286fa11b91b)\

![cowbell](https://github.com/willhunt914/Pi-inthe-sky/assets/113116262/5d358a55-ca3d-4559-9f80-79e875e3470c)

Week 10: This week we worked on soldering the circuit board. We got mostly done but found some things that needed to be changed and had to spend a lot of time trying to desolder. 

Week 11: This week was mainly focused on desoldering. The switch and battery were both soldered incorrectly so we had to move those parts which was a very tedious process.

Week 12: This week we fixed the issues with the circuit board by repositioning and resoldering a few components. After some more troubleshooting, we successfully recorded and saved data on the pico using the circuit board. 

![unnamed](https://github.com/willhunt914/Pi-inthe-sky/assets/113116262/c5d71d35-b219-48d4-9a49-1b5821c7fc3d)

Week 13: This week we found an issue with the bottom half of our sphere. the holes (shown below) were not accurate and did not allow the pico to screw in.

![Capture](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/5c0e9c0f-1fcd-487f-b121-520f58c8460d)

To fix this we printed with the sphere facing the other way so that the outside of the sphere looked worse but the inside was accurate and allowed the pico to screw in. We also thickened the collums to make the pico more secured when we launch it.
![unnamed](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/db0cc9b9-622a-44d3-b6ba-d35fb62ac654)
Improved sphere is shown here

Week 14: This week was our first official launch and we learned a lot. 

https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/e0a7af9b-5579-4325-a1ba-615e4b85e25b
First Launch 

https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/b8908008-caed-4c41-9e5b-d67659929b9b
Second Launch

![image](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/2a466842-b951-43f0-8740-12b4606c91d7)
Data from frist launch

The main issue that we had was the Pico and the cowbell became seperated before the first launch. The most likely reason for that was that we dropped it on accident before we shot it and it came appart. The battery also became loose during the launch. To fix this we plan to add some foam inside of ther sphere  to give it more support and hold the pico together.  


### Final_Reflection

Will:
We put all of our chips into this project. We knew that the closer it came to the end of the year the less motivation we would have. Because of this, we jumped into the project early. We completed the prototype CAD for the projectile within the first two weeks without running into any problems. It took some time to think about how to create the slingshot but after finding exercise bands in my house the idea came together. Although we had the backbone for the code from the "Data Saver 1" assignment we still ran into some struggles. The Pico would occasionally delete our code.py and boot.py files as well as all of the libraries which delayed the process. The main struggle that I had was doing the soldering. Although I had messed with a soldering iron in the past I did not know how to wire any of it together. Some of my peers with more knowledge in this department helped a lot with this. Something that wasted a lot of our time was soldering the battery in the wrong holes and without a header. This caused me to have to remove all of the solder from those pins which was a long multi-day process. Through the trials and tribulations I became a better engineer and a bettere 

Jack
