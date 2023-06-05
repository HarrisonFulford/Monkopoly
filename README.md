# Monkopoly
This repository contains a finished ICS (intro to computer science) group project which was completed by my friend cadechanyi and I, I worked on back end, he worked on front end. It's a parody of the game monopoly (comprised entirely of inside jokes) that is playable on LAN. Download and extract the zip file to play.
General Information:
The project name is Monkopoly. It is a spinoff from the popular game Monopoly. Most of the elements of the game are consistent with Monopoly, but it features a custom board and a few small custom changes to add to the theme of the monkeys, Mentor College, and the ICS classroom. It is an online python game featuring 4 player’s made with the tkinter module for graphics and the socket module for an online connection. The level of effort put it was 9.5 out of 10. Both Harrison and I spent several hours learning and dealing with bugs up to the very end of the project. Our four files used for the final game had a combines total of over 1400 lines of code, and there were plenty more in on the other files we did not use for the final including the 700 lines in the single player file, and the near 100 images made and photoshopped for the graphics of the game. The participants involved in the creation of the game were Cade Chanyi and Harrison Fulford. Key dates of the project included February 9th, the date it was assigned. The first culture meeting report on February 13th. February 18th, the first project deliverable date and the 20 project days that followed to complete a deliverable and update the time log, all up until May 2nd the last day for the last deliverable, final time log, and paper trail. May 4th and May 8th, the two days of our presentation.
Project Summary:
The project first started on Tuesday February 9th. We were deliberating on whether our project should be a small custom 1 player game called coke game involving the school ourselves and the specialties of the ICS class and classroom, or a monopoly game with a custom theme. In the end we decided on doing the monopoly game because we would be able to do it with tools we were already familiar with and it involved less complex graphics and graphic movement unlike the custom game which we would have to learn from scratch. Upon choosing the topic, Our client decided that the game would need to be multiplayer and playable from 4 separate computers. Now we had to split up the work among Harrison and I. Harrison decided to be more back end as he was less familiar with graphics in tkinter which is the python module we used for the graphics of our game. And I decided I would be front end and would be responsible for making the general looks of the game and the logic for graphics. 

Our client also requested we make a custom theme for the game, as to be more different from the actual board game and being front end I went to work with ideas. I decided to bring a lot of elements from our classroom to the game while keeping the logic mostly the same. The game would be called Monkopoly as the creators of the game were deemed the king of the monkeys and the third monkey overall. The currency of the game would be cokes and the client loves coke. The railways were buses because we were in school. The chance cards were healthcare hazard, and the community chest were baboon bins. The two companies were the coke company and the Pepsi company, as they are rival companies and the client loves coke which is why here a small logic change from the actual game took place; in Monkopoly players who owned the Pepsi company would get the amount the person payment rent rolled multiplied by five, and the person who owner the coke company would receive the amount they rolled multiplied by 10. And if a player owned both they would receive the roll multiplied by 15. As well as with the buses, three were yellow while one was red. The red bus was Smith’s bus, and the owner of Smith's bus would receive one level higher of bus rent depending on the number they own. So if one owned a smith bus and that was the only one they owned they would receive 50$ instead of 25$. If they owned all the buses, they would receive $400 instead of $200 because continuing the pattern the level of 4 is $200 and we would double that to get the next level of bus rent. In addition, all the properties had different custom names. Some of the property names involved stuff from the school such as primary campus or mentor office. Others were from countries or just stuff from people in the school. The taxes were also changed to be mentor school fees, relating to the school and field trip cost. The coke was changed to smith class as passing you would receive cokes from smith. The Jail was Brampton because it is far worse, and free parking was changed to lunch break. 

The first part of the project was for each of us to separately develop files for the two major aspects of the game. In photoshop, I made the digital board with all the custom changes. I made the pieces which were animated monkeys in different colours. Then I developed the method of moving them randomly by replacing the label on the identified coordinates of that board place. Harrison’s first task was to make a working multiplayer python file that established a connection and allowed clients to communicate amongst each other. He did this by using python socket module. We finished these tasks by February 22nd. We then began to merge the files into one, with the gui piece movement being seen by all clients connected. By making each player their own client files, and the server a separate file void of any options, we made it so that any changes made by a client went to the server then the server sent it back to each client, once received each client applied the changes to their board. The rest of the project was done by me establishing the gui functions: movement and board changes and pop ups, adding them to the multiplayer file, then Harrison making it so the changes will be sent to server and then sent out to all clients, and then me making it so that the board is redraw from the new data received. Once all of the aspects had been added into the multiplayer game and established, we polished them off and tested each one then made a list of custom rolls in the game so we could show the client all the features.

Top Areas of Praise
1.	The digital board. Making the digital board with custom places and Monkopoly themed took a lot of time of effort. The first iterations of the board were highly blurred and unfocused. It took not only a lot of photoshop work, but also some changes in tkinter with the way the image was imported and processes into the window. The board also took a lot of creative elements and making them funny without crossing a line and remembering it is a respectful project was more difficult than I care to admit. But in the end, it was clear and careful board that was similar to monopoly, but had lots of unique changes and small details, such as the monkey sitting on the ‘MONKOPOLY’ board text, and the Chanyi and Fulford in the corner of the board.
2.	Manage property gui. Managing the property could have been done in a lot of different ways and there was a few iterations of what it could have been, but in the end, I decided to make it as easy and pleasing as possible. I remade the property cards to be smaller and made a separate tkinter window for managing which. The player selected the set that they wanted to manage and then selected how they wanted to manage the properties in that set. This making it very easy and simple with lots of options. In addition, it was an easy to use gui, that did not take long to work.
3.	The trade function. Making the trade function was one of the most difficult areas of the project. Harrison spent some time trying work a way around the server sending a trade to only one client, but then came up the clever of method of sending the trade to all players and each player checking if they were the one being traded with. 
4.	The next was adding houses gui, probably my favorite part of the project as it took a lot of time, using the manage gui I made for managing property if they decided to add houses it would send to server then send back to all clients. From their client file had a check for new houses and kept tracked and added the house images or hotel images on that property.
5.	The last area of praise were the digital chance cards. It was challenging making a realistic card that would execute a function when it was read. It wanted to make it so that when The action would occur after the player acknowledge the card, and by making it a button so that when clicked Harrison could execute the send code worked perfectly.

Areas of Improvement
1.	First area of improvement would be more complicated graphics. While I am very proud of the graphics especially using a limited python module, the next level would be to make pieces slide smoothly on the screen and chance card pop up. Maybe a little cop lights blue and red to add to the effects of being in jail.
2.	Next area of improvement would be to allow for another number of players. The game was designed for a specific number of players which was 4. So without 4 total players the game would not run. The next step in improving this would be to allow 2-4 players.
3.	Another area to improve on would be piece customization. When a player joined, they had to be the piece that corresponded with the order they joined, for improvement purposes this could be changed so a players chooses what piece they want to be and when a new player tries to join their options of pieces are limited to those which have yet to be chosen.
4.	Making an easier to connect and better module or another software for multiplayer games that can handle more traffic between clients and server as well as a possible connect back to game method.

Lessons Learned
1.	Spend more time at the start coming up with methods to do things. Don’t get half through the project and realize how difficult it will be to do something, such as when we did not account for trade and spent some time trying to think of a way, we could do communication directly to a client.
2.	Do not be afraid to learn something new. Being afraid to learn something new and trying to do the project using an old method is inferior to learning an easier new method. I insisted on using tkinter because I already knew it and I figured that it would be easier and take less time to use tkinter than to learn a new method from scratch. I was very wrong. There were many methods in the game that took a lot more time and effort in tkinter than it would have in a software designed around digital game making. 
3.	Instead of saying you will do something in your deliverable make sure you can actually do it. Come up with a solid plan and avoid planning after the project has been started.
Appendix A: Extra Praises
1.	Socket established communication.
2.	Monkopoly updating property views after trade.
3.	Updating property list after trade.
4.	Changing owner of property in trade
5.	Accepting a trade
6.	Hotels png and houses png
7.	Monkopoly houses establishment
8.	Monkopoly monkey colours
9.	Monkopoly money changes and money view

Appendix B: Extra Improvements
1.	Adding more colour to the game in buttons and controls. 
2.	Adding additional methods to complete tasks
3.	Allow players to think of moves to make in options and controls and save then send when it is there turn, such as thinking of a trade saving it, then when it is there turn send out the trade.
4.	Save player’s trade and manage changes so once they exit the trade or manage and come back in it is saved for later.
![image](https://github.com/HarrisonFulford/Monkopoly/assets/126714741/57d9da05-8e99-4cd3-8276-72bb0ddcfeb7)
