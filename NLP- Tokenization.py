# Natural Language Processing

# importing the libraries

import nltk

mycorspe = """I have three visions for India.
In 3000 years of our history, people from all over the world have come and invaded us,
captured our lands, conquered our minds.
From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British, the French, the Dutch, all of then came and looted us, took over what was ours.
Yet we have not done this to any other nation, We have not conquered anyone. We have not grabbed their land, their culture,
their history and tried to enforce our way of life on them.
Why? Because we respect the freedom of others.
That is why my first vision is that of freedom.
I believe that India got its first vision of this in 1857,
when we started the war of Independence.
It is this freedom that we must protect and nurture and build on. If we are not free, no one will respect us. 
My second vision for India's development. For fifty years we have been a developing nation. 2t is time we see ourselves as a developed nation.
Us are among the top 5 nations of the world In terms of GDP, we have a 10 percent growth rate in most areas. Our poverty levels are falling.
Our achievements are being globally recognised today. Yet we lack the self-confidence to see ourselves as a developed nation, self-reliant and self-assured,
Isn't this incorrect? I have a third vision. India must stand up to the world. Because I believe that unless India stands up to the world, no one will respect us.
Only strength respects strength. We must be strong not only as a military power but also as an economic power. Beth must go hand-in-hand.
My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of space, Professor Satish Dhawan,
who succeeded him and Dr. Brahm Prakash, father of muclear materi
I was lucky to have worked with all three of them closely and consider this the great opportunity
I see four milestones in my career"""

mycorspe

# Tokenizing the corpse into sentences

mysentences = nltk.sent_tokenize(mycorspe)

# Tokenizing the corpse into words

mywords = nltk.word_tokenize(mycorspe)


