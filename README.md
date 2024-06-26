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
- A success for this project would be for the payload to launch without breaking and for it to collect our data.
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


![launch1](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/364e096b-91cc-47e8-813c-f9493ff0bfce)


### First Launch 

![image](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/2a466842-b951-43f0-8740-12b4606c91d7)

Data from first launch

The main issue that we had was the Pico and the cowbell became separated after the second launch. The most likely reason was that we did not have any cushioning on the inside to protect it. The battery also became loose during the launch. To fix this we plan to add some foam inside of the sphere  to give it more support and hold the pico together.  

### Final Launch


![IMG_8627-ezgif com-crop](https://github.com/willhunt914/Pi-inthe-sky/assets/71402974/e201ab76-8007-4c54-b9da-c26cbbc9e589)

This launch went a lot better, and we successfully got all of the data that we needed. 

![image](https://github.com/willhunt914/Pi-inthe-sky/assets/113116262/85a3a8c5-5f3b-477e-8b68-cff8796ce9d4)

This graph shows X, Y, and Z acceleration. All of the acceleration values were consistent until about t = 249 seconds, when all of the values spike. The X and Y acceleration spikes up as the ball starts travelling quickly, and the Z acceleration spikes down as the ball travels upward against gravity. The actual values for the acceleration seem off, which we're guessing is because our accelerometer is not calibrated very well, but the data still shows the launch very clearly.


![image](https://github.com/willhunt914/Pi-inthe-sky/assets/113116262/6270a083-23c0-41a0-b48e-ef087abb27b0)

The altimeter data is unfortunately not very helpful, as there isn't much change at t = 249 when the launch occured. The altimeter we used was not very precise, and the values regularly fluctuated by up to a meter. Since there was so much error, and our ball didn't travel very high, there isn't a clear change in the data during the launch. 

### Final Code and Wiring

[Final Code](https://github.com/willhunt914/Pi-inthe-sky/blob/main/pi%20in%20the%20sky/finalproject.py)

![image](https://github.com/willhunt914/Pi-inthe-sky/assets/113116262/94aab748-0a67-4023-9d02-8f90b2f98642)

_final wiring on circuitboard_



### Final_Reflection

Will:

We put all of our chips into this project. We knew that the closer it came to the end of the year the less motivation we would have. Because of this, we jumped into the project early. We completed the prototype CAD for the projectile within the first two weeks without running into any problems. It took some time to think about how to create the slingshot but after finding exercise bands in my house the idea came together. Although we had the backbone for the code from the "Data Saver 1" assignment we still ran into some struggles. The Pico would occasionally delete our code.py and boot.py files as well as all of the libraries which delayed the process. The main struggle that I had was doing the soldering. Although I had messed with a soldering iron in the past, I did not know how to wire any of it together. Some of my peers with more knowledge in this department helped a lot with this. Something that wasted a lot of our time was soldering the battery in the wrong holes and without a header. This caused me to have to remove all of the solder from those pins which was a long multi-day process. If I did this project again I would raise the columns that hold the pico so that we could plug the pico into the computer without unscrewing it. I would also have an accessible switch for power on the outside so we could turn it on right before we launched instead of in the classroom. Although these problems caused some issues, I am still very happy with how the project came out. Through the trials and tribulations of this project, I became a better engineer and a better person.  

Jack:

The biggest strugle with this project was getting the code to work and save data. It took a lot of troubleshooting and a pico swap, but we eventually got it to work consistently. Our first launch didn't go very well, as we didn't get any data. We're pretty sure that this was because things came loose when it hit the ground, since the accelerometer didn't have power when we recovered it. To keep this from happening again, we added some foam to keep everything in place. The second launch went a lot better, and we successfully got data. If I had to do this project again, I would try to find a more accurate sensor to record height data. I would also change the external switch to be power instead of data/code to make things more convenient. We also could have recorded how far it launched. Overall, I think that this project was a success, as we were able to launch from our homemade slingshot and collect meaningful data from it.
