This .js file has been created in the buffer with anotoer .js file, which I deleted with the :bdelete file2.js command. 
Now, to save this file I need to write this buffer from the memory it is residing now
to the HDD :wq.

New concept:
The hardest thing for me when learning about buffers was visualizing how they worked because my mind was used to windows from when using a mainstream text editor. A good analogy is a deck of playing cards. If I have 2 buffers, I have a stack of 2 cards. The card on top is the only card I see, but I know there are cards below it. If I see file1.js buffer displayed then the file1.js card is on the top of the deck. I can't see the other card, file2.js here, but it's there. If I switch buffers to file2.js, that file2.js card is now on the top of the deck and file1.js card is below it.

