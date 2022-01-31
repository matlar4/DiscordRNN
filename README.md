# DiscordRNN
Application which gets all discord messages and a RNN tries to repliacte it's users\
\
[First file](GetAllDiscordMessages.py) uses a discord bot and a gitignored csv with information about channels, token and users to get all messages from a server, reformat them and save into a txt (said txt is not in this repo to protect the privacy of the users). 
\
RNN.py uses Andrej Karpathy's Minimal character-level Vanilla RNN model: [LINK](https://gist.github.com/karpathy/d4dee566867f8291f086) It is only slightly modified for this project. Initially, messages were only saved if loss was under a certain level but this was later removed. 
