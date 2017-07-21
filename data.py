# coding: utf-8
def chapters_train():
# elements from [0] to [69] in text are from "fear and loathing in las vegas by HST"
# elements from [70] to [139] in text are from Azimov's "The Foundation" trilogy	

	text = [
		"""We were somewhere around Barstow on the edge of the desert when the drugs began to
take hold. I remember saying something like “I feel a bit lightheaded; maybe you should drive…”
And suddenly there was a terrible roar all around us and the sky was full of what looked like
huge bats, all swooping and screeching and diving around the car, which was going about a
hundred miles an hour with the top down to Las Vegas. And a voice was screaming: “Holy Jesus!
What are these goddamn animals?” Then it was quiet again. My attorney had taken his shirt off
and was pouring beer on his chest, to facilitate the tanning process. “What the hell are you
yelling about?” he muttered, staring up at the sun with his eyes closed and covered with wraparound
Spanish sunglasses. “Never mind,” I said. “It’s your turn to drive.” I hit the brakes and
aimed the Great Red Shark toward the shoulder of the highway. No point mentioning those bats,
I thought. The poor bastard will see them soon enough.""",
		"""It was almost noon, and we still had more than a hundred miles to go. They would be
tough miles. Very soon, I knew, we would both be completely twisted. But there was no going
back, and no time to rest. We would have to ride it out. Press-registration for the fabulous Mint
400 was already underway, and we had to get there by four to claim our sound-proof suite. A
fashionable sporting-magazine in New York had taken care of the reservations, along with this
huge red Chevy convertible we’d just rented off a lot on the Sunset Strip… and I was, after all, a
professional journalist; so I had an obligation to cover the story, for good or ill.""",
		"""The sporting editors had also given me $300 in cash, most of which was already spent on
extremely dangerous drugs. The trunk of the car looked like a mobile police narcotics lab. We
had two bags of grass, seventy-five pellets of mescaline, five sheets of high-powered blotter acid,
a salt shaker half full of cocaine, and a whole galaxy of multi-colored uppers, downers,
screamers, laughers and also a quart of tequila, a quart of rum, a case of Budweiser, a pint of raw
ether and two dozen amyls. All this had been rounded up the night before, in a frenzy of highspeed
driving all over Los Angeles County – from Topanga to Watts, we picked up everything we
could get our hands on. Not that we needed all that for the trip, but once you get locked into a
serious drug-collection, the tendency is to push it as far as you can. """,
		"""The only thing that really worried me was the ether. There is nothing in the world more
helpless and irresponsible and depraved than a man in the depths of an ether binge. And I knew
we’d get into that rotten stuff pretty soon. Probably at the next gas station. We had sampled
almost everything else, and now – yes, it was time for a long snort of ether. And then do the next
hundred miles in a horrible, slobbering sort of spastic stupor. The only way to keep alert on ether
is to do up a lot of amyls – not all at once, but steadily, just enough to maintain the focus at
ninety miles an hour through Barstow.""",
		"""The Dwark approached our table cautiously, as I recall, and when he handed me the pink
telephone I said nothing, merely listened. And then I hung up, turning to face my attorney. “That
was headquarters,” I said. “They want me to go to Las Vegas at once, and make contact with a
Portuguese photographer named Lacerda. He’ll have the details. All I have to do is check into my
suite and he’ll seek me out.” My attorney said nothing for a moment, then he suddenly came
alive in his chair. “God hell!” he exclaimed. “I think I see the pattern. This one sounds like real
trouble!” He tucked his khaki undershirt into his white rayon bellbottoms and called for more
drink. “You’re going to need plenty of legal advice before this thing is over,” he said. “And my
first advice is that you should rent a very fast car with no top and get the hell out of L.A. for at
least forty-eight hours.” He shook his head sadly. “This blows my weekend, because naturally I’ll
have to go with you – and we’ll have to arn ourselves.” """,
		"""The New York office was not familiar with the Vincent Black Shadow: they referred me to
the Los Angeles bureau – which is actually in Beverly Hills just a few long blocks from the Polo
Lounge – but when I got there, the money-woman refused to give me more than $300 in cash.
She had no idea who I was, she said, and by that time I was pouring sweat. My blood is too thick
for California: I have never been able to properly explain myself in this climate. Not with the
soaking sweats… wild red eyeballs and trembling hands.""",
		"""“Don’t take any guff from these swine,” I said as he slammed the phone down. “Now we
need a sound store with the finest equipment. Nothing dinky. We want one of those new Belgian
Heliowatts with a voice-activated shotgun mike, for picking up conversations in oncoming cars.”
We made several more calls and finally located our equipment in a store about five miles away.
It was closed, but the salesman said he would wait, if we hurried. But we were delayed en route
when a Stingray in front of us killed a pedestrian on Sunset Boulevard. The store was closed by
the time we got there. There were people inside, but they refused to come to the double-glass
door until we gave it a few belts and made ourselves clear. """,
		"""“You’re right,” I said. “And for Christ’s sake don’t smoke that pipe at stoplights. Keep in
mind that we’re exposed.” He nodded. “We need a big hookah. Keep it down here on the seat,
out of sight. If anybody sees us, they’ll think we’re using oxygen.” We spent the rest of that night
rounding up materials and packing the car. Then we ate the mescaline and went swimming in
the ocean. Somewhere around dawn we had breakfast in a Malibu coffee shop, then drove very
carefully across town and plunged onto the smog-shrouded Pasadena Freeway, heading East. """,
		"""I am still vaguely haunted by our hitchhiker’s remark about how he’d “never rode in a
convertible before.” Here’s this poor geek living in a world of convertibles zipping past him on
the highways all the time, and he’s never even ridden in one. It made me feel like King Farouk. I
was tempted to have my attorney pull into the next airport and arrange some kind of simple,
common-law contract whereby we could just give the car to this unfortunate bastard. Just say:
“Here, sign this and the car’s yours.” Give him the keys and then use the credit card to zap off on
a jet to some place like Miami and rent another huge fireapple-red convertible for a drug-addled,
top-speed run across the water all the way out to the last stop in Key West… and then trade the
car off for a boat. Keep moving. """,
		"""Thirty minutes. It was going to be very close. The objective was the big tower of the Mint
Hotel, downtown – and if we didn’t get there before we lost all control, there was also the
Nevada State prison upstate in Carson City. I had been there once, but only for a talk with the
prisoners – and I didn’t want to go back, for any reason at all. So there was really no choice: We
would have to run the gauntlet, and acid be damned. Go through all the official gibberish, get
the car into the hotel garage, work out on the desk clerk, deal with the bellboy, sign in for the
press passes – all of it bogus, totally illegal, a fraud on its face, but of course it would have to be
done. """,
		"""We finally got into the suite around dusk, and my attorney was immediately on the phone
to room service-ordering four club sandwiches, four shrimp cocktails, a quart of rum and nine
fresh grapefruits. “Vitamin C,” he explained. “We’ll need all we can get.” I agreed. By this time
the drink was beginning to cut the acid and my hallucinations were down to a tolerable level.
The room service waiter had a vaguely reptilian cast to his features, but I was no longer seeing
huge pterodactyls lumbering around the corridors in pools of fresh blood. The only problem now
was a gigantic neon sign outside the window, blocking our view of the mountains – millions of
colored balls running around a very complicated track, strange symbols & filigree, giving off a
loud hum. """,
		"""He shook his head. “As your attorney, I advise you not to about me.” The TV news was
about the Laos Invasion – a series of horrifying disasters: explosions and twisted wreckage, men
fleeing in terror, Pentagon generals babbling insane lies. “Turn that shit off!” screamed my
attorney “Let’s get out of here!” A wise move. Moments after we picked up the car my attorney
went into a drug coma and ran a red light on Main Street before I could bring us under control. I
propped him up in the passenger seat and took the wheel myself… feeling fine, extremely sharp.
All around me in traffic I could see people talking and I wanted to hear what they were saying.
All of them. But the shotgun mike was in the trunk and I decided to leave it there. Las Vegas is
not the kind of town where you want to drive down Main Street aiming a black bazooka-looking
instrument at people. Turn up the radio. Turn up the tape machine. Look into the sunset up
ahead. Roll the windows down for a better taste of the cool desert wind. Ah yes. This is what it’s
all about. Total control now. Tooling along the main drag on a Saturday night in Las Vegas, two
good old boys in a fireapple-red convertible… stoned, ripped, twisted… Good People. """,
		"""I turned away. It was too horrible. We were, after all, the absolute cream of the national
sporting press. And we were gathered here in Las Vegas for a very special assignment: to cover
the Fourth Annual “Mint 400”… and when it comes to things like this, you don’t fool around. """,
		"""Well, that’s that,” somebody said. “They’ll be back around in an hour or so. Let’s go back
to the bar.” But not yet. No. There were something like a hundred and ninety more bikes waiting
to start. They went off ten at a time, every two minutes. At first it was possible to watch them out
to a distance of some two hundred yards from the starting line. But this visibility didn’t last long.
The third brace of ten disappeared into the dust about a hundred yards from where we stood…
and by the time they’d sent off the first hundred (with still another hundred to go), our visibility
was down to something like fifty feet. We could see as far as the hay-bales at the end of the
pits""",
		"""So I was not entirely at ease drifting around the casinos on this Saturday night with a car
full of marijuana and head full of acid. We had several narrow escapes: at one point I tried to
drive the Great Red Shark into the laundry room of the Landmark Hotel – but the door was too
narrow, and the people inside seemed dangerously excited. """,
		"""This madness goes on and on, but nobody seems to notice. The gambling action runs
twenty-four hours a day on the main floor, and the circus never ends. Meanwhile, on all the
upstairs balconies, the customers are being hustled by every conceivable kind of bizarre shuck.
All kinds of funhouse – type Shoot the pasties off the nipples of a ten-foot bulle and win a cottoncandy
goat. Stand in front of this fantastic machine, my friend, and for just 99$ your likeness will
appear, two hundred feet tall, on a screen above downtown Las Vegas. Ninety-nine cents more
for a voice message. “Say whatever you want, fella. They’ll hear you, don’t worry about that.
Remember you’ll be two hundred feet tall.” Jesus Christ. I could see myself lying in bed in the
Mint Hotel, half-asleep and staring idly out the window, when suddenly a vicious nazi drunkard
appears two hundred feet tall in the midnight sky, screaming gibberish at the world: “Woodstock
Über Alles!” We will close the drapes tonight. A thing like that could send a drug person
careening around the room like a pingpong ball. Hallucinations are bad enough. But after a
while you learn to cope with things like seeing your dead grandmother crawling up your leg with
a knife in her teeth. Most acid fanciers can handle this sort of thing. But nobody can handle that
other trip – the possibility that any freak with $1.98 can walk into the Circus-Circus and
suddenly appear in the sky over downtown Las Vegas twelve times the size of God, howling
anything that comes into his head. No, this is not a good town for psychedelic drugs. Reality
itself is too twisted. """,
		"""I stepped on the merry-go-round and hurried around the bar, approaching my attorney on
his blind side – and when we came to the right spot I pushed him off. He staggered into the aisle
and uttered a hellish scream as he lost his balance and went down, thrashing into the crowd…
rolling like a log, then up again in a flash, fists clenched, looking for somebody to hit. """,
"""When we got to the Mint I parked on the street in front of the casino, around a corner
from the parking lot. No point risking a scene in the lobby, I thought. Neither one of us could
pass for drunk. We were both hyper-tense. Extremely menacing vibrations all around us. We
hurried through the casino and up the rear escalator. """,
"""“Take a shower,” I said. “I’ll be back in twenty minutes.” I left quickly, locking the door
behind me and taking the key to Lacerda’s room – the one my attorney had stolen earlier. That
poor geek, I thought, as I hurried down the escalator. They sent him out here on this perfectly
reasonable assignment – just a few photos of motorcycles and dune buggies racing around the
desert – and now he was plunged, without realizing it, into the maw of some world beyond his
ken. There was no way he could possibly understand what was happening. """,
"""Now off the escalator and into the casino, big crowds still tight around the crap tables.
Who are these people? These faces! Where do they come from? They look like caricatures of
used-car dealers from Dallas. But they’re real. And, sweet Jesus, there are a hell of a lot of them –
still screaming around these desert-city crap tables at four-thirty on a Sunday morning. Still
humping the American Dream, that vision of the Big Winner somehow emerging from the lastminute
pre-dawn chaos of a stale Vegas casino. """,
"""My attorney was in the bathtub when I returned. Submerged in green water – the oily
product of some Japanese bath salts he’d picked up in the hotel gift shop, along with a new
AM/FM radio plugged into the electric razor socket. Top volume. Some gibberish by a thing
called “Three Dog Night”, about a frog named Jeremiah who wanted “Joy to the World.” First
Lennon, now this, I thought. Next we’ll have Glenn Campbell screaming “Where Have All the
Flowers Gone?” Where indeed? No flowers in this town. Only carnivorous plants. I turned the
volume down and noticed a hunk of chewed-up white paper beside the radio. My attorney
seemed not to notice the sound-change. He was lost in a fog of green steam; only half his head
was visible above the water line. """,
"""I grabbed it away from his hand. “You fool!” I said. “Get in that tub! Get away from that
goddamn radio!” I shoved it back from his hand. The volume was so far up that it was hard to
know what was playing unless you knew Surrealistic Pillow almost note for note… which I did,
at the time, so I knew that “White Rabbit” had finished; the peak and had come and gone. """,
"""But my attorney, it seemed, had not made it. He wanted more. “Back the tape up!” he
yelled. “I need it again!” His eyes were full of craziness now, unable to focus. He seemed on the
verge of some awful psychic orgasm. “Let it roll!” he screamed. “Just as high as the fucker can
go! And when it comes to that fantastic note where the rabbit bites its own head off, I want you
to throw that fuckin radio into the tub with me.” I stared at him, keeping a firm grip on the
radio. “Not me,” I said finally. “I’d be happy to ram a goddamn 440-volt cattle prod into that tub
with you right now, but not this radio. It would blast you right through the wall-stone – dead in
ten seconds.” I laughed. “Shit, they’d make me explain it – drag me down to some rotten
coroner’s inquest and grill me about… yes… the exact details. I don’t need that.” """,
"""“Don’t worry,” I said. “Are you ready?” I hit the “play” button and “White Rabbit” started
building again. Almost immediately he began to howl and moan… another fast run up that
mountain, and thinking, this time, that he would finally get over the top. His eyes were gripped
shut and only his head and both kneecaps poked up through the oily green water. """,
"""How would Horatio Alger handle this situation? One toke over the line, sweet Jesus... one
toke over the line. Panic. It crept up my spine like the first rising vibes of an acid frenzy. All these
horrible realities began to dawn on me: Here I was all alone in Las Vegas with this goddamn
incredibly expensive car, completely twisted on drugs, no attorney, no cash, no story for the
magazine – and on top of everything else I had a gigantic goddamn hotel bill to deal with. We
had ordered everything into that room that human hands could carry – including about six
hundred bars of translucent Neutrogena soap. """,
"""So he had left it with me, for delivery – if I made it back to L.A. Otherwise… well, I could
almost hear myself talking to the California Highway Patrol: What? This weapon? This loaded,
unregistered, concealed and maybe hot 357 Magnum? What am I doing with it? Well, you see,
officer, I pulled off the road near Mescal Springs – on the advice of my attorney, who
subsequently disappeared – and all of a sudden while I was just sort of walking around that
deserted waterhole by myself for no reason at all when this little fella with a beard came up to
me, out of nowhere, and he had horrible linoleum knife in one hand and this huge black pistol in
the other hand... and he offered to carve a big X on my forehead, in memory of Lieutenant
Calley… but when I told him I was a doctor of journalism his whole attitude changed. Yes, you
probably won’t believe this, officer, but he suddenly hurled that knife into the brackish mescal
waters near our feet, and then he gave me this revolver. Right, he just shoved it into my hands,
butt-first, and then he ran off into the darkness. """,
"""Now it was only a matter of slipping the noose: Yes, extremely casual behavior, wild eyes
hidden behind these Saigon-mirror sun glasses… waiting for the Shark to roll up. Where is it? I
gave that evil pimp of a carboy $5, a prime investment right now. """,
"""Why not? They asked. They wanted their stories told. And it was hard to explain; in those
circles, that everything they told me went into the wastebasket or at least the dead-end file
because the lead paragraphs I wrote for that article didn’t satisfy some editor three thousand
miles away – some nervous drone behind a grey formica desk in the bowels of a journalistic
bureaucracy that no con in Nevada will ever understand – and that the article finally died on the
vine, as it were, because I refused to rewrite the lead. For reasons of my own. None of which
would make much sense in The Yard. But what the hell? Why worry about details? I turned to
face my accuser, a small young clerk with a big smile on his face and a yellow envelope in his
hand. “I’ve been calling your room,” he said. “Then I saw you standing outside.” I nodded, too
tired to resist. By now the Shark was beside me, but I saw no point in even tossing my bag into
it. The game was up. They had me. """,
"""My attorney was doing the Big Spit again, in the bathroom. I walked out on the balcony
and stared at the pool, this kidney-shaped bag of bright water that shimmered outside our suite.
I felt like Othello. Here I’d only been in town a few hours, and we’d already laid the groundwork
for a classic tragedy. The hero was doomed; he had already sown the seed of his own downfall. """,
"""“I know,” he replied. “But the guy didn’t have any cash. He’s one of these Satanism freaks.
He offered me human blood – said it would make me higher than I’d ever been in my life,” he
laughed. “I thought he was kidding, so I told him I’d just as soon have an ounce or so of pure
adrenochrome – or maybe just a fresh adrenalin gland to chew on.” I could already feel the stuff
working on me. The first wave felt like a combination of mescaline and methedrmne. Maybe I
should take a swim, I thought. """,
"""“You’re lying!” shouted my attorney. “You were after the evidence! Who put youup to this
– the manager?”
 “I work for the hotel,” she said. “All I do is clean up the rooms.” I turned to my attorney.
“This means they know what we have,” I said. “So they sent this poor old woman up here to steal
it.”
 “No!” she yelled. “I don’t know what you’re talking about!”
 “Bullshit!” said my attorney. “You’re just as much a part of it as they are.”
 “Part of what?”
 “The dope ring,” I said. “You must know what’s going on in this hotel. Why do you think
we’re here?” She stared at us, trying to speak but only blubbering. “I know you’re cops,” she said
finally. “But I thought you were just here for that convention. I swear! All I wanted to do was
clean up your room. I don’t know anything about dope!” My attorsey laughed. “Come on, baby.
Don’t try to tell us you never heard of the Grange Gorman.”
 “No!” she yelled. “No! I swear to Jesus I never heard of that stuff!” My attorney seemed to
think for a moment, then he leaned to help the old lady to her feet. “Maybe she’s telling the he
said to me. “Maybe she’s not part of it.”
 “No! I swear I’m not!” she howled.
 “Well…” I said. “In that case, m""",
"""“No,” said my attorney. “They sent us down from Carson City. You’ll be contacted by
Inspector Rock. Arthur Rock. He’ll be posing as a politician, but you won’t have any trouble
recognizing him.” She seemed to be shuffling nervously.
 “What’s wrong?” I said. “Is there something you haven’t told us?”
 “Oh no!” she said quickly. “I was just wondering – who’s going to pay me?”
 “Inspector Rock will take care of that,” I said. “It’ll all be in cash: a thousand dollars on the
ninth of every month.”
 “Oh Lord!” she exclaimed. “I’d do just about anything for that!”
 “You and a lot of other people,” said my attorney. “You’d be surprised who we have on the
payroll – right here in this same hotel.” She looked stricken. “Would I know them?”
 “Probably,” I said. “But they’re all undercover. The only way you’ll ever know is if
something really serious happens and one of them has to contact you in public, with the pass
word.”""",
"""“‘One Hand Washes the Other,“‘ I said. “The minute you hear that, you say: ‘I fear
nothing.’ That way, they’ll know you.” She nodded. repeating the code several times, while we
listened tomake sure she had it right. “OK,” said my attorney. “That’s it for now. We probably
won;t be seeing you again until the hammer comes down. You’ll be better off ignoring us until
we leave. Don’t bother to make up the room. Just elave a pile of towels and soap outside the
door, exactly at modnight.” He smiled. “That way, we won;t have to risk another one of these
little incidents, will we?” She moved towards the door. “Whatever you say gentlemen. I can;t tell
you how sorry I am about what happened… but it was only because I didn’t realize.” My attorney
ushered her out. “We understand,” he said “But it’s all over now. Thank God for the decent
people.” She smiled as she closed the door behind her. """,
""" Return to the Circus-Circus… Looking for the Ape… to Hell with the
American Dream """,
"""Almost seventy-two hours had passed since that strange encounter, and no maid had set
foot in the room. I wondered what Alice had told them. We had seen her once, trundling a
laundry cart across the parking area as we rolled up in the Whale but we offered no sign of
recognition and she seemed understand. """,
"""But it couldn’t last much longer. The room was full of used towels; they were hanging
everywhere. The bathroom floor was about six inches deep with soap bars, vomit, and grape fruit
rinds, mixed with broken glass. I had to put my boots on every I went in there to piss. The nap of
the mottled grey rug was so thick with marijuana seeds that it appeared to be turning green""",
"""The general back-alley ambience of the suite was so rotten, so incredibly foul, that I
figured I could probably get away with claiming it was some kind of “Life-slice exhibit” that we’d
brought down from Haight Street, to show cops from other parts of the country how deep into
filth and degeneracy the drug people will sink, if left to their own devices. """,
"""But what kind of addict would need all these coconut husks and crushed honeydew rinds?
Would the presence of junkies account for all these uneaten french fries? These puddles of
glazed catsup on the bureau?
 Maybe so. But then why all this booze? and these crude pornographic photos, ripped out
of pulp magazines like Whores of Sweden and Orgies in the Casbah, that were plastered on the
broken mirror with smears of mustard that had dried to a hard yellow crust… and all these signs
of violence, these strange red and blue bulbs and shards of broken glass embedded in the wall
plaster…""",
"""No, these were not the hoofprints of your normal, godfearing junkie. It was far too
aggressive. There was evidence, in this room, of excessive consumption of almost every type of
drug known to civilized man since 1544 A.D. It could only be explained as a montage, a sort of
exaggerated medical exhibit, put together very carefully to show what might happen if twentytwo
serious drug felons – each with a different addiction – were penned up together in the same
room for five days and nights, without relief.
 Indeed. But of course that would never happen in Real Life, gentlemen. We just put this
thing together for demonstration purposes...
 Suddenly the phone was ringing, jerking me out of my fantasy stupor. I looked at it.
Riiiinnnnnggggggg… Jesus, what now? Is this it? I could almost hear the shrill voice of the
Manager, Mr. Heem, saying the police were on their way up to my room and would I please not
shoot through the door when they began kicking it down. 

67
 Riinnnngggg… No, they wouldn’t call first. Once they decided to take me, they would
probably set an ambush in the elevator: first Mace, then a gang-swarm. It would come with no
warning.
 So I picked up the phone. It was my friend Bruce Innes, calling from the Circus-Circus. He
had located the man who wanted to sell the ape I’d been inquiring about. The price was $750.
 “What kind of a greedhead are we dealing with here?” I said. “Last night it was four
hundred.”
 “He claims he just found out it was housebroken,” said Bruce. “He let it sleep in the trailer
last noght, and the thing actually shiot in the shower stall.”
 “That doesn’t mean anything,” I said. “Apes are attracted to water. Next time it’ll shit in
the sink.""",
"""d… the bartender had to call an ambulance, then the cops came and took the ape away.”
 “Goddamnit,” I said. “What’s the bail? I want that ape.”
 “Get a grip on yourself,” he said. “You better stay clear of that jail. That’s all they need to
put the cuffs on you. Forget that ape. You don’t need him.” I gave it some thought, then decided
he was probably right. There was no sense blowing everything just for the sake of some violent
ape I’d never met. For all I knew, hed take a bite out of my head if I tried to bail him out. It
would take him a while to calm down, after the shock of being put behind bars, and I couldnt
afford to wait around. “When are you taking off?” Bruce asked.
 “As soon as possible,” I said. No point hanging around this town any lobger. IU have all I
need. Anything else would only confuse me.” He seemed suprised. “You found the American
Dream?” he said. “In this town?” I nodded. “We’re sitting on the main nerve rightnow,” I said.
“You remember that story the manager told us about the owner of this place? How he always
wanted to run away and join the circus when he was a kid?” Bruce ordered two more beers. He
looked over the casino for a moment, then shrugged. “Yeah, I see what you mean,” he said. “Now
the bastard has his own circus, and a license to steal, too.” He nodded. “You’re right – he’s the
model.”""",
"""Several months later, in Aspen, Bruce sang the same songs in a club jammed with tourists
and a former Astronaut* and when the last set was over, —— came over to our table and began
yelling all kinds of drunken, super-patriot gibber ish, hitting on Bruce about “What kind of nerve
does a god damn Canadian have to come down here and insult this country?”
 “Say man,” I said. “I’m an Amei-ican. I live here, and I agree with every fucking word he
says.” At this point the hash-bouncers appeared, grinning inscrutably and saying: “Good evening
to you gentlemen. The I Ching says it’s time to be quiet, right? And nobody hassles the musicians
in this place, is that clear?” The Astronaut left, muttering darkly about using his in fluence to
“get something done, damn quick,” about the Im""",
"""The Astronaut’s party was speechless. Eight or ten people – wives, managers and favored
senior engineers, showing a good time in fabulous Aspen. Now they looked like somebody had
just sprayed their table with shit-mist. Nobody a word. They ate quickly, and left without tipping.
 So much for Aspen and astronauts. —— would never have kind of trouble in Las Vegas.
 A little bit of this town goes a very long way. After five in Vegas you feel like you’ve been
here for five years. Some people say they like it – but then some people like Nixon, too. He
would have made a perfect Mayor for this town; with John Mitchell as Sheriff and Agnew as
Master of Sewers. """,
"""Fuck you, Efrem, that wisdom cuts both ways.
 As far as you and the Mint people know, I am still up there l850 – legally and spiritually if
not in the actual flesh – a “Do Not Disturb” sign hung out to ward off disturb – The maids won’t
come near that room as long as that sign is on the doorknob. My attorney saw to that – along
with 600 bars of Neutrogena soap that I still have to deliver to Malibu. What will the FBI make of
that? This Great Red Shark full of Neutrogena soap bars? All completely legal. The maids gave us
that soap. They’ll swear to it… Or will they? """,
"""Jesus Creeping God! Is there a priest in this tavern? I want to confess! I’m a fucking
sinner! Venal, mortal, carnal, major, minor – however you want to call it, Lord… I’m guilty.
 But do me this one last favor: just give me five more high-speed hours before you bring
the hammer down; just let me get rid of this goddamn car and off of this horrible desert.
 Which is not really a hell of a lot to ask, Lord, because the incredible truth is that I am not
guilty. All I did was take your gibberish seriously… and you see where it got me? My primitive
Christian instincts have made me a criminal. Creeping through the casino at six in the morning
with a suitcase full of grapefruit and “Mint 400” T-shirts, I remember telling myself, over and
over again, “You are not guilty.” This is merely a necessary expedient, to avoid a nasty scene.
After all, I made no binding agreements; this is an institutional debt – nothing personal. This
whole goddamn nightmare is the fault of that stinking,""",
"""Tuesday, 12:30 P.M… Baker, California… Into the Ballantine Ale now, zombie drunk and
nervous. I recognize this feeling: three or four days of booze, drugs, sun, no sleep and burned
out adrenalin reserves – a giddy, quavering sort of high that means the crash is coming. But
when? How much longer? This tension is part of the high. The possibility of physical and mental
collapse is very real now… but collapse is out of the question; as a solution or even a cheap
alternative, it is unacceptable. Indeed. This is the moment of truth, that fine and fateful line
between control and disaster – which is also the difference between staying loose and weird on
the streets, or spending the next five years of summer mornings playing basketball in the yard at
Carson City. """,
"""Few people understand the psychology of dealing with a highway traffic cop. Your normal
speeder will panic and immediately pull over to the side when he sees the big red light behind
him… and then we will start apologizing, begging for mercy. """,
"""This is to let him know you’re looking for a proper place to pull off and talk… keep
signaling and hope for an off-ramp, one of those uphill side-loops with a sign saying “Max Speed
25”… and the trick, at this point, is to suddenly leave the freeway and take him into the chute at
no less than a hundred miles an hour. """,
"""He will lock his brakes about the same time you lock yours, but it will take him a moment
to realize that he’s about to make a 180-degree turn at this speed… but you will be ready for it,
braced for the Gs and the fast heel-toe work, and with any luck at all you will have come to a
complete stop off the road at the top of the turn and be standing beside your automobile by the
time he catches up. """,
"""He will not be reasonable at first… but no matter. Let him calm down. He will want the
first word. Let him have it. His brain will be in a turmoil: he may begin jabbering, or even pull
his gun. Let him unwind; keep smiling. The idea is to show him that you were always in total
control of yourself and your vehicle – while he lost control of everything. """,
"""It helps to have a police/press badge in your wallet when he calms down enough to ask
for your license. I had one of these – but I also had a can of Budweiser in my hand. Until that
moment, I was unaware that I was holding it. I had felt totally on top of the situation… but when
I looked down and saw that little red/silver evidence-bomb in my hand, I knew I was fucked. """,
"""how grateful I am for this break you want to give me.
 But no… here I was insisting that if he turned me loose I would boom straight ahead for
L.A. which was true, but why say it? Why push him? This is not the right time for a show-down.
This is Death Valley… get a grip on yourself. """,
"""“OK,” he said. “Here’s how it is. What goes into my book, as of noon, is that I apprehended
you… for driving too fast conditions, and advised you… with this written warning – he handed it
to me – ”to proceed no further than the next rest area… your stated destination, right? Where
you an to take a long nap…” He hung his ticket-pad back on his belt. “Do I make myself clear?”
he asked as he turned away. """,
"""I got back on the freeway and drove past the rest area to the intersection where I had to
turn right into Baker. As I am proached the turn I saw… Great Jesus, it’s him, the hitchhiker, the
same kid we’d picked up and terrified on the way out to Vegas. Our eyes met as I slowed down
to make the corner. I was tempted to wave, but when I saw him drop his thumb I thought, no,
this is not the time... """,
"""Suddenly I had two personal enemies in this godforsaken town. The CHP cop would bust
me for sure if I tried to go on through to L.A., and this goddamn rotten kid/hitchhiker would
have me hunted down like a beast if I stayed. (Holy Jesus, Sam! There he is! That guy the kid
told us about! He’s back!) Either way, it was horrible – and if these righteous outback predators
ever got their stories together… and they would; it was inevitable in a town this small… that
would cash my check all around. I’d be lucky to leave town alive. A ball of tar and feathers
dragged onto the prison bus by angry natives. """,
"""“You brainless scumbag!” he shouted. “I sent you a telegram! You’re supposed to be
covering the National District Attorneys’ Conference! I made all the reservations… rented a white
Cadillac convertible… the whole thing is arranged! What the hell are you doing out there in the
middle the fucking desert?” Suddenly I remembered. Yes. The telegram. It was all very clear. My
mind became calm. I saw the whole thing in a flash. “Never mind,” I said. “It’s all a big joke. I’m
actually sitting beside the pool at the Flamingo. I’m talking from a portable phone. Some dwarf
brought it out from the casino. I have total credit! Can you grasp that?” I was breathing heavily,
feeling crazy, sweating into the phone. """,
"""About 20 miles east of Baker I stopped to check the drug bag. The sun was hot and I felt
like killing something. Anything. Even a big lizard. Drill the fucker. I got my attorney’s .357
Magnum out of the trunk and spun the cylinder. It was loaded all the way around: Long, nasty
little slugs – 158 grains with a fine flat trajectory and painted aztec gold on the tips. I blew the
horn a few times, hoping to call up an iguana. Get the buggers moving. They were out there, I""",
"""Luckily, nobody bothered me while I ran a quick inventory on the kit-bag. The stash was a
hopeless mess, all churned together and half-crushed. Some of the mescaline pellets had
disintegrated into a reddish-brown powder, but I counted about thirty-five or forty still intact. My
attorney had eaten all the reds, but there was quite a bit of speed left… no more grass, the coke
bottle was empty, one acid blotter, a nice brown lump of opium hash and six loose amyls… Not
enough for anything serious, but a careful rationing of the mescaline would probably get us
through the four-day Drug Conference. """,
"""On the outskirts of Vegas I stopped at a neighborhood pharmacy and bought two quarts of
Gold tequila, two fifths of Chivas Regal and a pint of ether. I was tempted to ask for some amyls.
My angina pectoris was starting to act up. But druggist had the eyes of a mean Baptist hysteric. I
told I needed the ether to get the tape off my legs, but by that time he’d already rung the stuff up
and bagged it. He didn’t give a fuck about ether. """,
"""succeed in restoring the eyesight of a young man who pulled out his eyes while suffering the
effects of a drug overdose in a jail cell. Charles Innes, Jr., 25, underwent surgery late Thursday at
Maryland General Hospital but doctors said it be weeks before they could determine the
outcome. Statement issued by the hospital reported that Innes no light perception in either eye
prior to surgery and the possibility he will ever have light perception is extremely poor. Innes,
son of a prominent Massachusetts Republican, was found in a jail cell Thursday by a turnkey
who said Innes had pulled out his eyeballs. """,
"""The first order of business was to get rid of the Red Shark. It was too obvious. Too many
people might recognize it, especially the Vegas police; although as far as they knew, the thing
was already back home in L.A. It was last seen running at top speed across Death Valley on
Interstate 15. Stopped and warned in Baker by the CHP… then suddenly disappeared...
 The last place they would look for it, I felt, was in a rental-car lot at the airport. """,
"""“On behalf of the prosecuting attorneys of this county, I welcome you.” We sat in the rear
fringe of a crowd of about 1500 in the main ballroom of the Dunes Hotel. Far up in front of the
room, barely visible from the rear, the executive director of the National District Attorneys’
Association – a middle-aged, well-groomed, successful GOP businessman type named Patrick
Healy – was opening their Third National Institute on Narcotics and Dangerous Drugs. His
remarks reached us by way of a big, low-fidelity speaker mounted on a steel pole in our corner.
Perhaps a dozen others were spotted around the room, all facing the rear and looming over the
crowd… so has no matter where you sat or even tried to hide, you were ways looking down the
muzzle of a big speaker. """,
"""But the best technicians available to the National DAs’ convention in Vegas apparently
couldn’t handle it. Their sound system looked like something Ulysses S. Grant might have
triggered up to address his troops during the Siege of Vicksburg. The voices from up front
crackled with a fuzzy, high-pitched urgency, and the delay was just enough to keep the words
disconcertingly out of phase with the speaker’s gestures. """,
"""“What the fuck are these people talking about?” my attorney whispered. “You’d have to be
crazy on acid to think a joint looked like a goddamn cockroach!” I shrugged. It was clear that
we’d stumbled into a prehistoric gathering. The voice of a “drug expert” named Bloomquist
crackled out of the nearby speakers: “…about these flashbacks, the patient never knows; he
thinks it’s all over and he gets himself straightened out for six months… and then, damn it, the
whole trip comes back on him.” Gosh darn that fiendish LSD! Dr. E. R. Bloomquist, MD, was the
keynote speaker, one of the big stars of the conference. He is the author of a paperback book
titled Marijuana, which – according to the cover – “tells it like it is.” (He is also the inventor of
the roach/cockroach theory...) According to the book jacket, he is an “Associate Clinical Professor
of Surgery (Anesthesiology) at the University of Southern California School of Medicine”… and
also “a well-known authority on the abuse of dangerous drugs. Dr. Bloomquist “has also
appeared on national network television panels, has served as a consultant for government
agencies, was a member of the Committee on Narcotics Addiction and Alcoholism of the Council
on Mental Health of the American Medical Association.” His wisdom is massively reprinted and
distributed, says the publisher. He is clearly one of the heavies on that circuit of second-rate
academic hustlers who get paid anywhere from $500 to $1000 a hit for lecturing to cop crowds.
Dr. Bloomquist’s book is a compendium of state bullshit. On page 49 he explains, the “four states
of being” in the cannabis society: “Cool, Groovy, Hip & Square” – in that descending order. “The
square is seldom if ever cool,” says Bloomquist. “He is ‘not with it’, hat is, he doesn’t know ‘what’s
happening.’ But if he manages to figure it out, he moves up a notch to ‘hip.’ And if he can bring
himself to approve of what’s happening, he becomes ‘groovy.’ And after that, with much luck and
perseverence, he can rise to the rank of ‘cool.’” Bloomquist writes like somebody who once
bearded Tim Leary in a campus cocktail lounge and paid for all the drinks. And it was probably
somebody like Leary who told him, with a straight face, that sunglasses are known in the drug
culture as “tea shades.” This is the kind of dangerous gibberish that used to be posted, in the
form of mimeographed bulletins, in Police Department locker rooms. """,
"""Indeed: KNOW YOUR DOPE FIEND. YOUR LIFE MAY DEPEND ON IT! You will not be
able to see his eyes because of Tea-Shades, but his knuckles will be white from inner tension and
his pants will be crusted with semen from constantly jacking off when he can’t find a rape victim.
He will stagger and babble when questioned. He will not respect your badge. The Dope Fiend
fears nothing. He will attack, for no reason, with every weapon at his command – including
yours. BEWARE. Any officer apprehending a suspected marijuana addict should use all necessary
force immediately. One stitch in time (on him) will usually save nine on you. Good luck. """,
"""Just because you’re a cop, these days, doesn’t mean you can’t be With It. And this
conference attracted some real peacocks. But my own costume – $40 FBI wingtips and a Pat
Boone madras sportcoat – was just about right for the mass median; because for every urbanhipster,
there were about twenty crude-looking rednecks who could have passed for assistant
football coaches at Mississippi State""",
"""The first session – the opening remarks – lasted most of the afternoon. We sat patiently
through the first two hours, although it was clear from the start that we weren’t going to Learn
anything and it was equally clear that we’d be crazy to try any Teaching. It was easy enough to
sit there with a head full of mescaline and listen to hour after hour of irrelevant gibberish…
There was certainly no risk involved. These poor bastards didn’t know mescaline from macaroni. """,
"""Here were more than a thousand top-level cops telling each other “we must come to terms
with the drug culture,” but they had no idea where to start. They couldn’t even find the goddamn
thing. There were rumors in the hallways that maybe the Mafia was behind it. Or perhaps the
Beatles. At one point somebody in the audience asked Bloomquist if he thought Margaret Mead’s
“strange behavior,” of late, might possibly be explained by a private marijuana addiction. """,
"""He paused, looking around – then he seemed to think better of it, and kept moving. By the
time he got to the exit the whole rear of the room was in turmoil. Even Bloomquist, far up front
on the stage, seemed aware of a distant trouble. He stopped talking and peered nervously in the
direction of the noise. Probably he thought a brawl had erupted – maybe a racial conflict of some
kind, something that couldn’t be helped. """,
"""“Hurry up with those drinks,” said my attorney. “We’re thirsty.” He laughed and rolled his
eyes as the bartender glanced back at him. “Only two rums,” he said. “Make mine a Bloody
Mary.” The bartender seemed to stiffen, but our Georgia friend didn’t notice. His mind was
somewhere else. “Hell, I really hate to hear this,” he said quietly. “Because everything that
happens in California seems to get down our way, sooner or later. Mostly Atlanta, but I guess
that was back when the goddamn bastards were peaceful. It used to be that all we had to do was
keep ‘em under surveillance. They didn’t roam around much…” He shrugged. “But now, Jesus,
nobody’s safe. They could turn up anywhere.” """,
"""Most of the crew got away; just ran off across the sand dimes, like big lizards… and every
one of them stark naked, except for the weapons. “They’ll turn up everywhere, pretty soon.” OI
said. “And let’s hope we’ll be ready for them.” The Georgia man whacked his fist on the bar. “But
we can’t just lock ourselves in the house and be prisoners!” he exclaimed. “We don’t even know
who these people are! How do you recognize them?”""",





"""TERMINUS–... Its location (see map) was an odd one for the role it was called upon to play in
Galactic history, and yet as many writers have never tired of pointing out, an inevitable one.
Located on the very fringe of the Galactic spiral, an only planet of an isolated sun, poor in
resources and negligible in economic value, it was never settled in the five centuries after its
discovery, until the landing of the Encyclopedists....""",
"""Pirenne stirred uneasily, as the muted buzzer upon his desk muttered peevishly. He had almost
forgotten the appointment. He shoved the door release and out of an abstracted comer of one
eye saw the door open and the broad figure of Salvor Hardin enter. Pirenne did not look up.
Hardin smiled to himself. He was in a hurry, but he knew better than to take offense at
Pirenne's cavalier treatment of anything or anyone that disturbed him at his work. He buried
himself in the chair on the other side of the desk and waited.""",
"""Anselm haut Rodric – "haut" itself signifying noble blood -Sub-prefect of Pluema and Envoy
Extraordinary of his Highness of Anacreon-plus half a dozen other titleswas met by Salvor
Hardin at the spaceport with all the imposing ritual of a state occasion.
With a tight smile and a low bow, the sub-prefect had flipped his blaster from its holster and
presented it to Hardin butt first. Hardin returned the compliment with, a blaster specifically
borrowed for the occasion. Friendship and good will were thus established, and if Hardin noted
the barest bulge at Haut Rodric's shoulder, he prudently said nothing.""",
"""If Hardin found himself bored by the afternoon and evening that followed, he had at least the
satisfaction of realizing that Pirenne and Haut Rodric – having met with loud and mutual
protestations of esteem and regard – were detesting each other's company a good deal more.
Haut Rodric had attended with glazed eye to Pirenne's lecture during the "inspection tour" of
the Encyclopedia Building. With polite and vacant smile, he had listened to the latter's rapid
patter as they passed through the vast storehouses of reference films and the numerous
projection rooms.""",
"""The dinner that evening was much the mirror image of the events of that afternoon, for Haut
Rodric monopolized the conversation by describing – in minute technical detail and with
incredible zest – his own exploits as battalion head during the recent war between Anacreon
and the neighboring newly proclaimed Kingdom of Smyrno.
The details of the sub-prefect's account were not completed until dinner was over and one by
one the minor officials had drifted away. The last bit of triumphant description of mangled
spaceships came when he had accompanied Pirenne and Hardin onto the balcony and relaxed
in the warm air of the summer evening.""",
"""The sub-prefect seemed unimpressed. He blew smoke rings. That's a nice theory, Dr. Pirenne.
I imagine you've got charters with the Imperial Seal upon it – but what's the actual situation?
How do you stand with respect to Smyrno? You're not fifty parsecs from Smyrno's capital. you
know. And what about Konom and Daribow?""",
"""Haut Rodric calmed down and said: "Well, now, Dr. Pirenne, you respect the Emperor's
property and so does Anacreon, but Smyrno might not. Remember, we've just signed a treaty
with the Emperor – I'll present a copy to that Board of yours tomorrow – which places upon us
the responsibility of maintaining order within the borders of the old Prefect of Anacreon on
behalf of the Emperor. Our duty is clear, then, isn't it?""",
""""For instance, if he foresaw the Anacreonian mess, why not have placed us on some other
planet nearer the Galactic centers? It's well known that Seldon maneuvered the Commissioners
on Trantor into ordering the Foundation established on Terminus. But why should he have done
so? Why put us out here at all if he could see in advance the break in communication lines, our
isolation from the Galaxy, the threat of our neighbors – and our helplessness because of the
lack of metals on Terminus? That above all! Or if he foresaw all this, why not have warned the
original settlers in advance that they might have had time to prepare, rather than wait, as he is
doing, until one foot is over the cliff, before doing so?""",
"""He went on: "And you men and half of Terminus as well are just as bad. We sit here,
considering the Encyclopedia the all-in-all. We consider the greatest end of science. is the
classification of past data. It is important, but is there no further work to be done? We're
receding and forgetting, don't you see? Here in the Periphery they've lost nuclear power. In
Gamma Andromeda, a power plant has undergone meltdown because of poor repairs, and the
Chancellor of the Empire complains that nuclear technicians are scarce. And the solution? To
train new ones? Never! Instead they're to restrict nuclear power.""",
"""I think so!" Hardin jumped up and pushed his chair away. His eyes were cold and hard. "If
there's one thing that's definite, it is that there's something smelly about the whole situation;
something that is bigger than anything we've talked about yet. Just ask yourself this question:
Why was it that among the original population of the Foundation not one first-class psychologist
was included, except Bor Alurin? And he carefully refrained from training his pupils in more
than the fundamentals.""",
"""Hari Seldon was, of course, undisturbed. He went on: "It is a fraud in the sense that neither I
nor my colleagues care at all whether a single volume of the Encyclopedia is ever published. It
has served its purpose, since by it we extracted an imperial charter from the Emperor, by it we
attracted the hundred thousand humans necessary for our scheme, and by it we managed to
keep them preoccupied while events shaped themselves, until it was too late for any of them to
draw back.""",
"""This, by the way, is a rather straightforward crisis, much simpler than many of those that are
ahead. To reduce it to its fundamentals, it is this: You are a planet suddenly cut off from the
still-civilized centers of the Galaxy, and threatened by your stronger neighbors. You are a small
world of scientists surrounded by vast and rapidly expanding reaches of barbarism. You are an
island of nuclear power in a growing ocean of more primitive energy; but are helpless despite
that, because of your lack of metals""",
"""THE FOUR KINGDOMS – The name given to those portions of the Province of Anacreon which
broke away from the First Empire in the early years of the Foundational Era to form
independent and short-lived kingdoms. The largest and most powerful of these was Anacreon
itself which in area...""",
"""He eyed Sermak closely and continued in measured tones, "When Hari Seldon established the
Foundation here, it was for the ostensible purpose of producing a great Encyclopedia, and for
fifty years we followed that will-of-the-wisp, before discovering what he was really after. By that
time, it was almost too late. When communications with the central regions of the old Empire
broke down, we found ourselves a world of scientists concentrated in a single city, possessing
no industries, and surrounded by newly created kingdoms, hostile and largely barbarous. We
were a tiny island of nuclear power in this ocean of barbarism, and an infinitely valuable prize.""",
""""I? Oh, yes, again my policy of appeasement. You still seem to lack grasp of the fundamental
necessities of our position. Our problem wasn't over with the departure of the Anacreonians.
They had just begun. The Four Kingdoms were more our enemies than ever, for each wanted
nuclear power-and each was kept off our throats only for fear of the other three. We are
balanced on the point of a very sharp sword, and the slightest sway in any direction – If, for
instance, one kingdom becomes too strong; or if two form a coalition – You understand?""",
"""On the whole, it was an uncomfortable job, and his first trip to the Foundation in three years,
despite the disturbing incident that had made it necessary, was something in the nature of a
holiday.
And since it was not the first time he had had to travel in absolute secrecy, he again made use
of Hardin's epigram on the uses of the obvious.
He changed into his civilian clothes – a holiday in itself – and boarded a passenger liner to the
Foundation, second class. Once at Terminus, he threaded his way through the crowd at the
spaceport and called up City Hall at a public visiphone.""",
"""Without my crimson robe? Besides, he was a Smyrnian. It was an interesting experience,
though. It is remarkable, Hardin, how the religion of science has grabbed hold. I've written an
essay on the subject – entirely for my own amusement; it wouldn't do to have it published.
Treating the problem sociologically, it would seem that when the old Empire began to rot at the
fringes, it could be considered that science, as science, had failed the outer worlds. To be
reaccepted it would have to present itself in another guise and it has done just that. It works out
beautifully.""",
""""He won't – except with guns, or so he thinks. You see, he came to me on the day I left
Anacreon and requested that the Foundation put this battle cruiser into fighting order and turn it
over to the Anacreonian navy. He had the infernal gall to say that your note of last week
indicated a plan of the Foundation's to attack Anacreon. He said that refusal to repair the battle
cruiser would confirm his suspicions; and indicated that measures for the self-defense of
Anacreon would be forced upon him. Those are his words. Forced upon him! And that's why I'm
here.""",
"""Superficial, Verisof, superficial. You and I both know that the armament he now has could
defeat Terminus handily, long before we could repair the cruiser for our own use. What does it
matter, then, if we give him the cruiser as well? You know it won't ever come to actual war.""",
"""In the ancient days when the Galactic Empire had embraced the Galaxy, and Anacreon had
been the richest of the prefects of the Periphery, more than one emperor had visited the
Viceregal Palace in state. And not one had left without at least one effort to pit his skill with air
speedster and needle gun against the feathered flying fortress they call the Nyakbird.""",
"""Lepold appreciated his uncle's sour-grapes attitude and it was not without malice that he began
enthusiastically, "But you should have been with us today, uncle. We flushed one in the wilds of
Sarnia that was a monster. And game as they come. We had it out for two hours over at least
seventy square miles of ground. And then I got to Sunwards – he was motioning graphically, as
though he were once more in his speedster –"and dived torque-wise. Caught him on the rise
just under the left wing at quarters. It maddened him and he canted athwart. I took his dare and
veered a-left, waiting for the plummet. Sure enough, down he came. He was within wing-beat
before I moved and then""",
"""His dark eyes blazed from beneath his grizzled brows and the young king sat down slowly. For
a moment, there was sardonic satisfaction in the regent's face, but it faded quickly. His thick
lips parted in a smile and one hand fell upon the king's shoulder.""",
"""Anacreon with his devil's smile and devil's brain – and the power of the other three kingdoms
behind him, combined in cowardly union against the greatness of Anacreon."
Lepold flushed and the sparkle in his eyes blazed. "By Seldon, if I had been my grandfather, I
would have fought even so."
"No, Lepold. We decided to wait – to wipe out the insult at a fitter time. It had been your father's
hope, before his untimely death, that he might be the one to – Well, well!" Wienis turned away
for a moment. Then, as if stifling emotion, "He was my brother. And yet, if his son were–"
"Yes, uncle, I'll not fail him. I have decided. It seems only proper that Anacreon wipe out this
nest of troublemakers, and that immediately."
"No, not immediately. First, we must wait for the repairs of the battle cruiser to be completed.
The mere fact that they are willing to undertake these repairs proves that they fear us. The
fools attempt to placate us, but we are not to be turned from our path, are we?"
And Lepold's fist slammed against his cupped palm.
"Not while I am king in Anacreon."
Wienis' lip twitched sardonically. "Besides which we must wait for Salvor Hardin to arrive."
"Salvor Hardin!" The king grew suddenly round-eyed, and the youthful contour of his beardless
face lost the almost hard lines into which they had been compressed.
"Yes, Lepold, the leader of the Foundation himself is coming to Anacreon on your birthday –
probably to soothe us with buttered words. But it won't help him."
"Salvor Hardin!" It was the merest murmur.""",
"""There was a short, rebellious silence, and then Lepold said, "Everyone believes it just the
same. I mean all this talk about the Prophet Hari Seldon and how he appointed the Foundation
to carry on his commandments that there might some day be a return of the Galactic Paradise:
and how anyone who disobeys his commandments will be destroyed for eternity. They believe
it. I've presided at festivals, and I'm sure they do.""",
""""Here it is." Bort was a trifle disconcerted, but didn't show it. "The religion – which the
Foundation has fostered and encouraged, mind you – is built on on strictly authoritarian lines.
The priesthood has sole control of the instruments of science we have given Anacreon, but
they've learned to handle these tools only empirically. They believe in this religion entirely, and
in the ... uh ... spiritual value of the power they handle. For instance, two months ago some fool
tampered with the power plant in the Thessalekian Temple – one of the large ones. He
contaminated the city, of course. It was considered divine vengeance by everyone, including
the priests.""",
""""That gives us time, my foot," ground out Bort, impatiently. "The king's a god, I tell you. Do you
suppose he has to carry on a campaign of propaganda to get his people into fighting spirit? Do
you suppose he has to accuse us of aggression and pull out all stops on cheap emotionalism?
When the time comes to strike, Lepold gives the order and the people fight. Just like that.
That’s the damnedness of the system. You don’t question a god. He may give the order
tomorrow for all I know; and you can wrap tobacco round that and smoke it.""",
"""The snow had ceased, but it caked the ground deeply now and the sleek ground car advanced
through the deserted streets with lumbering effort. The murky gray light of incipient dawn was
cold not only in the poetical sense but also in a very literal way – and even in the then turbulent
state of the Foundation's politics, no one, whether Actionist or pro-Hardin found his spirits
sufficiently ardent to begin street activity that early.""",
""""Maybe. I don't know. However, this is the point. At today's session of the Council, just after you
announce that I have left for Anacreon, you will further announce, officially, that on March 14th
next, there will be another Hari Seldon recording, containing a message of the utmost
importance regarding the recent successfully concluded crisis. That's very important, Lee. Don't
add anything more no matter how many questions are asked.""",
"""Salvor Hardin did not travel to the planet Anacreon – from which planet the kingdom derived its
name – immediately. It was only on the day before the coronation that he arrived, after having
made flying visits to eight of the larger stellar systems of the kingdom, stopping only long,
enough to confer with the local representatives of the Foundation.""",
"""He had been introduced to Lepold as one of a long line of introducees, and from a safe
distance, for the king stood apart in lonely and impressive grandeur, surrounded by his deadly
blaze of radioactive aura. And in less than an hour this same king would take his seat upon the
massive throne of rhodium-iridium alloy with jewel-set gold chasings, and then, throne and all
would rise maestically into the air, skim the ground slowly to hover before the great window
from which the great crowds of common folk could see their king and shout themselves into
near apoplexy. The throne would not have been so massive, of course, if it had not had a
shielded nuclear motor built into it.""",
"""Nor was there any mention of what I had for breakfast that day, or the name of my current
mistress, or any other irrelevant detail." Mallow's smile was fading into a sneer. "I was sent – to
quote yourself – to keep my eyes open. They were never. shut. You wanted to find out what
happened to the captured Foundation merchant ships. I never saw or heard of them. You
wanted to find out if Korell had nuclear power. My report tells of nuclear blasters in the
possession of the Commdor's private bodyguard. I saw no other signs. And the blasters I did
see are relics of the old Empire, and may be show-pieces that do not work, for all my
knowledge.""",
"""This goes beyond money, or markets. We have the science of the great Hari Seldon to prove
that upon us depends the future empire of the Galaxy, and from the course that leads to that
Imperium we cannot turn. The religion we have is our all-important instrument towards that end.
With it we have brought the Four Kingdoms under our control, even at the moment when they
would have crushed us. It is the most potent device known with which to control men and
worlds.""",
"""And time enough, too," said Mallow, indifferently, "for a policy outdated, dangerous and
impossible. However well your religion has succeeded in the Four Kingdoms, scarcely another
world in the Periphery has accepted it. At the time we seized control of the Kingdoms, there
were a sufficient number of exiles, Galaxy knows, to spread the story of how Salvor Hardin
used the priesthood and the superstition of the people to overthrow the independence and
power of the secular monarchs. And if that wasn't enough, the case of Askone two decades
back made it plain enough. There isn't a ruler in the Periphery now that wouldn't sooner cut his
own throat than let a priest of the Foundation enter the territory.""",
"""The secretary to the mayor leaned forward, "Mallow, I'm not bluffing. The preliminaries are
over. I have only to sign one final paper and the case of the Foundation versus Hober Mallow,
Master Trader, is begun. You abandoned a subject of the Foundation to torture and death at
the hands of an alien mob, Mallow, and you have only five seconds to prevent the punishment
due you. For myself, I'd rather you decided to bluff it out. You'd be safer as a destroyed enemy,
than as a doubtfully-converted friend.""",
""""Now any dogma primarily based on faith and emotionalism, is a dangerous weapon to use on
others, since it is almost impossible to guarantee that the weapon will never be turned on the
user. For a hundred years now, we've supported a ritual and mythology that is becoming more
and more venerable, traditional – and immovable. In some ways, it isn't under our control any
more.""",
"""And Jael shook his head again, "No, Mallow, you've missed it. I told you he played dirty. He's
not out to convict you; he knows he can't do that. But he is out to ruin your standing with the
people. You heard what he said. Custom is higher than law, at times. You could walk out of the
trial scot-free, but if the people think you threw a priest to the dogs, your popularity is gone.""",
""""They'll admit you did the legal thing, even the sensible thing. But just the same you'll have
been, in their eyes, a cowardly dog, an unfeeling brute, a hard-hearted monster. And you would
never get elected to the council. You might even lose your rating as Master Trader by having
your citizenship voted away from you. You're not native born, you know. What more do you
think Sutt can want?" Mallow frowned stubbornly, "So!" "My boy," said Jael. "I'll stand by you,
but I can't help. You're on the spot, –dead center.""",
"""They were suspicious thoughts, for the events of that day were queer. Consider. Two people,
neither of whom I knew more than casually, make unnatural and somewhat unbelievable
propositions to me. One, the secretary to the mayor, asks me to play the part of intelligence
agent to the government in a highly confidential matter, the nature and importance of which has
already been explained to you. The other, self-styled leader of a political party, asks me to run
for a council seat.""",
""""There was one thing I could do. I got rid of Twer for five minutes by sending him after my
officers. In his absence, I set up a Visual Record receiver, so that whatever happened might be
preserved for future study. This was in the hope, the wild but earnest hope, that what confused
me at the time might become plain upon review.""",
"""The chamber dimmed, and the empty air filled again with frozen figures in ghostly, waxen
illusion. The officers of the Far Star struck their stiff, impossible attitudes. A gun pointed from
Mallow's rigid hand. At his left, the Revered Jord Parma, caught in mid-shriek, stretched his
claws upward, while the failing sleeves hung halfway.""",
""""What do you think? Those three merchant ships we lost in their space sector weren't knocked
over with compressed-air pistols. Jael, they're getting ships from the Empire itself. Don't open
your mouth like a fool. I said the Empire! It's still there, you know. It many be gone here in the
Periphery but in the Galactic center it's still very much alive. And one false move means that it,
itself, may be on our neck. That's why I must be mayor and high priest. I'm the only man who
knows how to fight the crisis.""",
""""Well, you'll have your own way, as always." The Commdor shrugged and turned away. "And
as for your father's displeasure: I much fear me it extends to a niggardly refusal to supply more
ships."
"More ships!" She blazed away, hotly, "And haven't you five? Don't deny it. I know you have
five; and a sixth is promised.""",
""""Well!" The Commdora's figure expanded and her eyes sparkled, "You learned wisdom at last,
though in your dotage. And now when you are master of this hinterland, you may be sufficiently
respectable to be of some weight and importance in the Empire. For one thing, we might leave
this barbarous world and attend the viceroy's court. Indeed we might.""",
"""Hober Mallow shuffled his feet wearily as he leafed through the reports. Two years of the
mayoralty had made him a bit more housebroken, a bit softer, a bit more patient, –but it had not
made him learn to like government reports and the mind-breaking officialese in which they were
written""",
""""No," said Jael, violently, "not the way you did it. You claim to have foreseen everything, and
don't explain why you traded with Korell to their exclusive benefit for three years. Your only plan
of battle is to retire without a battle. You abandon all trade with the sectors of space near Korell.
You openly proclaim a stalemate. You promise no offensive, even in the future. Galaxy, Mallow,
what am I supposed to do with such a mess?""",
""""A strong offensive is indicated. The stalemate you seem to be satisfied with is fatal. It would be
a confession of weakness to all the worlds of the Periphery, where the appearance of strength
is all-important, and there's not one vulture among them that wouldn't join the assault for its
share of the corpse. You ought to understand that. You're from Smyrno, aren't you?""",
""""When I first landed on Korell," he began, A bribed the Commdor with the trinkets and gadgets
that form the trader's usual stock. At the start, that. was meant only to get us entrance into a
steel foundry. I had no plan further than that, but in that I succeeded. I got what I wanted. But it
was only after my visit to the Empire that I first realized exactly what a weapon I could build that
trade into.""",
""""But we, –we, our little Foundation, our single world almost without metallic resources, –have
had to work with brute economy. Our generators have had to be the size of our thumb, because
it was all the metal we could afford. We had to develop new techniques and new methods,
–techniques and methods the Empire can't follow because they have degenerated past the
stage where they can make any really vital scientific advance.""",
"""Sutt was at the window, his back to Mallow and Jael. It was early evening now, and the few
stars that struggled feebly here at the very rim of the Galaxy sparked against the background of
the misty, wispy Lens that included the remnants of that Empire, still vast, that fought against
them.""",
"""Suppose you were a traitor. Suppose your visit to the Empire had brought you a subsidy and a
promise of power. Your actions would be precisely what they are now. You would bring about a
war after having strengthened the enemy. You would force the Foundation into inactivity. And
you would advance a plausible explanation of everything, one so plausible it would convince
everyone""",
"""Mallow lifted his gloomy face, and exclaimed fiercely, "What business of mine is the future? No
doubt Seldon has foreseen it and prepared against it. There will be other crises in the time to
come when money power has become as dead a force as religion is now. Let my successors
solve those new problems, as I have solved the one of today.""",
"""KORELL–...And so after three years of a war which was certainly the most unfought war on
record, the Republic of Korell surrendered unconditionally, and Hober Mallow took his place
next to Hari Seldon and Salvor Hardin in the hearts of the people of the Foundation.""",
"""As the Empire rotted, the outer regions fell into the hands of independent "kings." The
Foundation was threatened by them. However, by playing one petty ruler against another,
under the leadership of their first mayor, Salvor Hardin, they maintained a precarious
independence. As sole possessors, of nuclear power among worlds which were losing their
sciences and falling back on coal and oil, they even established an ascendancy. The
Foundation became the "religious" center of the neighboring kingdoms.""",
"""It had been falling for centuries before one man became really aware of that fall. That man was
Hari Seldon, the man who represented the one spark of creative effort left among the gathering
decay. He developed and brought to its highest pitch the science of psychohistory.
Psychohistory dealt not with man, but with man-masses. It was the science of mobs; """,
"""BEL RIOSE .... In his relatively short career, Riose earned the title of "The Last of the Imperials"
and earned it well. A study of his campaigns reveals him to be the equal of Peurifoy in strategic
ability and his superior perhaps in his ability to handle men. That he was born in the days of the
decline of Empire made it all but impossible for him to equal Peurifoy's record as a conqueror.
Yet he had his chance when, the first of the Empire's generals to do so, he faced the
Foundation squarely....""",
"""Barr smiled thinly. "Not elsewhere, I believe. I keep this in repair myself as well as I can. I must
apologize for your wait at the door. The automatic device registers the presence of a visitor but
will no longer open the door.""",
"""The old man replied with difficulty, "I shall be as indelicate a host as you a guest. I shall remind
you that once a viceroy thought as you did of the spiritless Siwennians. By the orders of that
viceroy my father became a fugitive pauper, my brothers martyrs, and my sister a suicide. Yet
that viceroy died a death sufficiently horrible at the hands of these same slavish Siwennians.""",
"""Riose held the empty cup as he spoke. "Patrician, listen to me. These are days when the most
successful soldiers are those whose function is to lead the dress parades that wind through the
imperial palace grounds on feast days and to escort the sparkling pleasure ships that carry His
Imperial Splendor to the summer planets. I ... I am a failure. I am a failure at thirty-four, and I
shall stay a failure. Because, you see, I like to fight.""",
"""Riose nibbled casually at a cakelet. "Because for three years I have traced every rumor, every
myth, every breath concerning the magicians – and of all the library of information I have
gathered, only two isolated facts are unanimously agreed upon, and are hence certainly true.
The first is that the magicians come from the edge of the Galaxy opposite Siwenna; the second
is that your father once met a magician, alive and actual, and spoke with him.""",
"""Ducem Barr began, "My own knowledge is the result of two accidents; the accidents of being
born the son of my father, and of being born the native of my country. It begins over forty years
ago, shortly after the great Massacre, when my father was a fugitive in the forests of the South,
while I was a gunner in the viceroy's personal fleet. This same viceroy, by the way, who had
ordered the Massacre, and who died such a cruel death thereafter.""",
"""Bel Riose reached for the belt of linked metal that clung to the curved wall. It came away with a
little sucking noise as the tiny adhesion-field broke at the touch of his hand. The ellipsoid at the
apex of the belt held his attention. It was the size of a walnut.""",
"""Riose laughed suddenly. "He foresaw that? Then he foresaw wrong, my good scientist. I
suppose you call yourself that. Why, the Empire is more powerful now than it has been in a
millennium. Your old eyes are blinded by the cold bleakness of the border. Come to the inner
worlds some day; come to the warmth and the wealth of the center.""",
"""of the best, and the youngest, and the strongest, there to breed, grow, and develop. The worlds
on which they were placed were chosen carefully; as were the times and the surroundings. All
was arranged in such a way that the future as foreseen by the unalterable mathematics of
psychohistory would involve their early isolation from the main body of Imperial civilization and
their gradual growth into the germs of the Second Galactic Empire – cutting an inevitable
barbarian interregnum from thirty thousand years to scarcely a single thousand.""",
"""FOUNDATION ... With forty years of expansion behind them, the Foundation faced the menace
of Riose. The epic days of Hardin and Mallow had gone and with them were gone a certain
hard daring and resolution....""",
"""The fourth man blinked his little eyes stealthily. Words crept out from between thin lips. "It is
nothing to sleep over in fat triumph, this grasping of little ships. Most likely, it will but anger that
young man further.""",
""""Then let's forget what we should have done earlier," interrupted Forell impatiently, "and
continue with what we should do now. In any case, what if we had imprisoned him, or killed
him, what then? We are not certain of his intentions even yet, and at the worst, we could not
destroy an Empire by snipping short one man's life. There might be navies upon navies waiting
just the other side of his nonreturn.""",
""""To draw our own conclusions, obviously." Forell's fingers were tapping quietly again. "The
young man is a military leader of the Empire, yet he played the pretense of being a minor
princeling of some scattered stars in an odd comer of the Periphery. That alone would assure
us that his real motives are such as it would not benefit him to have us know. Combine the
nature of his profession with the fact that the Empire has already subsidized one attack upon us
in my father's time, and the possibilities become ominous. That first attack failed. I doubt that
the Empire owes us love for that""",
""""Patriotism be damned," said Forell quietly. "Do you think I give two puffs of nuclear emanation
for the future Second Empire? Do you think I'd risk a single Trade mission to smooth its path?
But – do you suppose Imperial conquest will help my business or yours? If the Empire wins,
there will be a sufficient number of yearning carrion crows to crave the rewards of battle.""",
"""Bel Riose interrupted his annoyed stridings to look up hopefully when his aide entered. "Any
word of the Starlet?"
"None. The scouting party has quartered space, but the instruments have detected nothing.
Commander Yume has reported that the Fleet is ready for an immediate attack in retaliation."
The general shook his head. "No, not for a patrol ship. Not yet. Tell him to double – Wait! I'll
write out the message. Have it coded and transmitted by tight beam."
He wrote as he talked and thrust the paper at the waiting officer. "Has the Siwennian arrived
yet?"
"Not yet."
"Well, see to it that he is brought in here as soon as he does arrive."
The aide saluted crisply and left. Riose resumed his caged stride.
When the door opened a second time, it was Ducem Barr that stood on the threshold. Slowly,
in the footsteps of the ushering aide, he stepped into the garish room whose ceiling was an
ornamented holographic model of the Galaxy, and in the center of which Bel Riose stood in
field uniform.""",
""""Find them? That I did," cried Riose. His lips were stiff as he spoke. It seemed to require effort
to refrain from grinding molars. "Patrician, they are not magicians; they are devils. It is as far
from belief as the outer galaxies from here. Conceive it! It is a world the size of a handkerchief,
of a fingernail; with resources so petty, power so minute, a population so microscopic as would
never suffice the most backward worlds of the dusty prefects of the Dark Stars. Yet with that, a
people so proud and ambitious as to dream quietly and methodically of Galactic rule."""
]
	return  text
















def chapters_test():
# elements from [0] to [19] in text are from "fear and loathing in las vegas by HST"
# elements from [20] to [39] in text are from Azimov's "The Foundation" trilogy		
	text = [
		"""The first order of business was to get rid of the Red Shark. It was too obvious. Too many
people might recognize it, especially the Vegas police; although as far as they knew, the thing
was already back home in L.A. It was last seen running at top speed across Death Valley on
Interstate 15. Stopped and warned in Baker by the CHP… then suddenly disappeared... """,
		"""By the time I got to the terminal I was pouring sweat. But nothing abnormal. I tend to
sweat heavily in warm climates. Clothes are soaking wet from dawn to dusk. This worried at
first, but when I went to a doctor and described my normal daily intake of booze, drugs and
poison he told me to come back when the sweating stopped. That would be the danger point, he
said – a sign that my body’s desperately overworked flushing mechanism had broken down
completely. “I have great faith in the natural processes,” he said. “But in your case… well… I find
no precedent. We’ll just have to wait and see, then work with what’s left.” I spent about two
hours in the bar, drinking Bloody Marys for the V-8 nutritional content and watching the flights
from L.A. I’d eaten nothing but grapefruit for about twenty hours and my head was adrift from
its moorings. """,
		"""Do I look like a goddamn Nazi?” I said. “I’ll have a natural American car, or nothing at
all!” They called up the white Coupe de Ville at once. Everything was automatic. I could sit in the
red-leather driver’s seat and make every inch of the car jump, by touching the proper buttons. It
was a wonderful machine: Ten grand worth of gimmicks and high-priced Special Effects. The
rear-windows leaped up with a touch, like frogs in a dynamite pond. The white canvas top ran
up and down like a roller-coaster. The dashboard was full of esoteric lights & dials & meters that
I would never understand – but there was no doubt in my mind that I was into a superior
machine. """,
		"""I had a terrible vision of Lucy crashing into Barbra Streisand’s dressing room at the
Americana and laying this brutal story on her. That would finish us. They would track us down
and probably castrate us both, prior to booking. I explained this to my attorney, who was now in
tears at the idea of sending Lucy away. She was still powerfully twisted, and I felt the only
solution was to get her as far as possible from the Flamingo before she got straight enough to
remember where she’d been and what happened to her. """,
		"""Then we drove her out to the airport, saying we were going to trade the White Whale in
for a Mercedes 600, and my attorney took her into the lobby with all her gear. She was still
unhinged and babbling when he led her away. I drove around a corner and waited for him. """,
		"""My attorney was doing the Big Spit again, in the bathroom. I walked out on the balcony
and stared at the pool, this kidney-shaped bag of bright water that shimmered outside our suite.
I felt like Othello. Here I’d only been in town a few hours, and we’d already laid the groundwork
for a classic tragedy. The hero was doomed; he had already sown the seed of his own downfall. """,
		"""“Shit!” I snapped. “How many people has that junkie bastard shot since we’ve known him?
Six? Eight? That evil little tuck is so guilty that I should probably kill him myself, on general
principles. He shot that narc just as sure as he killed that girl at the Holiday Inn… and that guy
in Ventura!” He eyed me coldly. “You better be careful, man. You’re into some heavy slander.” I
laughed, tossing my luggage together in a lump at the foot of the bed while I sat down to finish
my drink. I actually intended to leave. I didn’t really want to, but I figured that nothing I could
possibly do with this gig was worth the risk of tangled up with Lucy… No doubt she was a
beautiful person, if she ever got straight… very sensative, with a secret reserve karma
undernenth her Pit Bull act; a great talent with fine instincts… Just a heavy little gal who
unfortunately went stone crazy somewhere prior to her eighteenth birthday. """,
		"""Jesus, I thought. What a terrible thing to lay on somebody a head full of acid.
 “But here’s the problem,” he was saying. “I have to leave here right away. That bastard
cashed a bad check downstairs and gave you as a reference, so they’ll be looking for both of
you… yeah, I know, but you can’t judge a book by it’s cover, Lucy; some people are just basically
rotten… anyway, the pie as a reference, so they’ll be looking for both of us. The last thing in the
world you want to do is call this hotel again; they’ll trace the call and put you straight behind
bars… no, I’m moving to the Tropicana right away; I’ll call you from there when I know my room
number… yeah, probably two hours; I have to act casual, or they’ll capture me too… I think I’ll
probably use a different name, but I’ll let you know what it is… sure, just as soon as I check in…
what? of course; we’ll go to the Circus-Circus and catch the polar bear act; it’ll freak you right
out…” """,
		"""My attorney had gone back to watching television. The news was on again. Nixon’s face
filled the screen, but his speech was hopelessly garbled. The only word I could make out was
“sacrifice.” Over and over again: “Sacrifice… sacrifice… sacrifice” I could hear myself breathing
heavily. My attorney seemed to notice. “Just stay relaxed,” he said over his shoulder, with out
looking at me. “Don’t try to fight it, or you’ll start getting brain bubbles… strokes, aneurisms…
you’ll just wither up and die.” His hand snaked out to change channels. """,
		"""What the fuck are these people talking about?” my attorney whispered. “You’d have to be
crazy on acid to think a joint looked like a goddamn cockroach!” I shrugged. It was clear that
we’d stumbled into a prehistoric gathering. The voice of a “drug expert” named Bloomquist
crackled out of the nearby speakers: “…about these flashbacks, the patient never knows; he
thinks it’s all over and he gets himself straightened out for six months… and then, damn it, the
whole trip comes back on him.” Gosh darn that fiendish LSD! Dr. E. R. Bloomquist, MD, was the
keynote speaker, one of the big stars of the conference. He is the author of a paperback book
titled Marijuana, which – according to the cover – “tells it like it is.” (He is also the inventor of
the roach/cockroach theory...) According to the book jacket, he is an “Associate Clinical Professor
of Surgery (Anesthesiology) at the University of Southern California School of Medicine”… and
also “a well-known authority on the abuse of dangerous drugs. Dr. Bloomquist “has also
appeared on national network television panels, has served as a consultant for government
agencies, was a member of the Committee on Narcotics Addiction and Alcoholism of the Council
on Mental Health of the American Medical Association.” His wisdom is massively reprinted and
distributed, says the publisher. He is clearly one of the heavies on that circuit of second-rate
academic hustlers who get paid anywhere from $500 to $1000 a hit for lecturing to cop crowds.
Dr. Bloomquist’s book is a compendium of state bullshit. On page 49 he explains, the “four states
of being” in the cannabis society: “Cool, Groovy, Hip & Square” – in that descending order. “The
square is seldom if ever cool,” says Bloomquist. “He is ‘not with it’, hat is, he doesn’t know ‘what’s
happening.’ But if he manages to figure it out, he moves up a notch to ‘hip.’ And if he can bring
himself to approve of what’s happening, he becomes ‘groovy.’ And after that, with much luck and
perseverence, he can rise to the rank of ‘cool.’” Bloomquist writes like somebody who once
bearded Tim Leary in a campus cocktail lounge and paid for all the drinks. And it was probably
somebody like Leary who told him, with a straight face, that sunglasses are known in the drug
culture as “tea shades.” This is the kind of dangerous gibberish that used to be posted, in the
form of mimeographed bulletins, in Police Department locker rooms. """,
		"""Indeed: KNOW YOUR DOPE FIEND. YOUR LIFE MAY DEPEND ON IT! You will not be
able to see his eyes because of Tea-Shades, but his knuckles will be white from inner tension and
his pants will be crusted with semen from constantly jacking off when he can’t find a rape victim.
He will stagger and babble when questioned. He will not respect your badge. The Dope Fiend
fears nothing. He will attack, for no reason, with every weapon at his command – including
yours. BEWARE. Any officer apprehending a suspected marijuana addict should use all necessary
force immediately. One stitch in time (on him) will usually save nine on you. Good luck. """,
		"""“Hurry up with those drinks,” said my attorney. “We’re thirsty.” He laughed and rolled his
eyes as the bartender glanced back at him. “Only two rums,” he said. “Make mine a Bloody
Mary.” The bartender seemed to stiffen, but our Georgia friend didn’t notice. His mind was
somewhere else. “Hell, I really hate to hear this,” he said quietly. “Because everything that
happens in California seems to get down our way, sooner or later. Mostly Atlanta, but I guess
that was back when the goddamn bastards were peaceful. It used to be that all we had to do was
keep ‘em under surveillance. They didn’t roam around much…” He shrugged. “But now, Jesus,
nobody’s safe. They could turn up anywhere.""",
		"""My attorney was laughing as we careened in low gear, with the light sout, through a dusty
tangle of backstreets behind the Desert Inn. “Jesus Christ,” he said. “Those Okies were getting
excited. That guy in the back seat was trying to bite me! Shit, he was frothing at the mouth.” He
nodded solemnly. “I should have maced the fucker… a criminal psychotic, total breakdown…
you never know when they’re likely to explode.” I swung the Whale into a turn that seemed to
lead out of the maze – but instead of skidding, the bastard almost rolled. """,
		"""We’ll see,” I said, moving around to the rear with the air-hose. In truth, I was nervous.
The two front ones were tighter than snare drums; they felt like teak wood when I tapped on
them with the rod. But what the hell? I thought. If they explode, so what? It’s not often that a
man gets a chance to run terminal experiments on a virgin Cadillac and four brand-new $80
tires. For all I knew, the thing might start cornering like a Lotus Elan. If not, all I had to do was
call the VIP agency and have another one delivered… maybe threaten them with a lawsuit
because all four tires had exploded on me, while driving in heavy traffic. Demand an Eldorado,
next time, with four Michelin Xs. And put it all on the card… charge it to the St. Louis Browns. """,
		"""About thirty minutes after our brush with the Okies we pulled into an all-night diner on
the Tonopah highway, on the kirts of a mean/scag ghetto called “North Las Vegas.” Which is
actually outside the city limits of Vegas proper. North Vegas is where you go when you’ve fucked
up once too often on the Strip, and when you’re not even welcome in the cut-rate downtown
places around Casino Center. """,
		"""But there was nothing in the atmosphere of the North Star to put me on my guard. The
waitress was passively hostile, but I was accustomed to that. She was a big woman. Not fat, but
large in every way, long sinewy arms and a brawler’s jawbone. A burned-out caricature of Jane
Russell: big head of dark hair, face slashed with lipstick and a 48 Double-E chest that was
probably spectacular about twenty years ago when she might have been a Mama for the Hell’s
Angels chapter in Berdoo… but now she was strapped up in a giant pink elastic brassiere that
showed like a bandage through the sweaty white rayon of her uniform. """,
		"""My attorney left at dawn. We almost missed the first flight to L.A. because I couldn’t find
the airport. It was less than thirty minutes from the hotel. I was sure of that. So we left the
Flamingo at exactly seven-thirty… but for some reason we failed to make the turnoff at the
stoplight in front of the Tropicana. We kept going straight ahead on the freeway, that parallels
the main airport runway, but on the opposite from the terminal… and there is no way to get
across legally. """,
		"""I saw the cops waiting for me, so I slowed down like maybe I’d changed my mind… but
when I saw them relax, I did a quick change of pace and tried to run right over the bastards.” I
laughed. “Jesus, it was like running full bore into a closet full of gila monsters. The fuckers
almost killed me. All I remember is seeing five or six billyclubs coming down on me at the same
time, and a lot of voices screaming: ‘No! No! It’s suicide! Stop the crazy gringo!’ “I woke up about
two hours later in a bar in downtown Lima. They’d stretched me out in one of those half-moon
leather booths. My luggage was all stacked beside me. No body had opened it… so I went back
to sleep and caught the first flight out, the next morning.” My attorney was only half listening.
“Look,” he said, “I’d really like to hear more about your adventures in Peru, but not now. Right
now all I care about is getting across that god damn runway.” We were flashing along at good
speed. I was looking for an opening, some kind of access road, some lane across the run way to
the terminal. We were five miles past the last stop light and there wasn’t enough time to turn
around and go back to it.""",
		"""“Rediculous,” I said. “Just say you were hitchhiking to the airport and I picked you up.
You never saw me before. Shit, thos town is full of white Cadillac convertibles… and I plan to go
through there so fast that nobody will even glimpse the goddamn license plate.” We were
approaching the plane. I could see passengers but so far nobody had noticed us… approaching
from this unlikely direction. “Are you ready?” I said. """,
		"""I took a fast right on Russell, then a left onto Maryland Parkway… and suddenly I was
cruising in warm anonym ity past the campus of the University of Las Vegas… no tension on
these faces; I stopped at a red light and got lost, for a moment, in a sunburst of flesh in the crosswalk:
fine sinewy thighs, pink mini-skirts, ripe young nipples, sleeveless blouses, long sweeps of
blonde hair, pink lips and blue eyes- all the hallmarks of a dangerously innocent culture. """,
		"""By the time I got to the terminal I was pouring sweat. But nothing abnormal. I tend to
sweat heavily in warm climates. Clothes are soaking wet from dawn to dusk. This worried at
first, but when I went to a doctor and described my normal daily intake of booze, drugs and
poison he told me to come back when the sweating stopped. That would be the danger point, he
said – a sign that my body’s desperately overworked flushing mechanism had broken down
completely. “I have great faith in the natural processes,” he said. “But in your case… well… I find
no precedent. We’ll just have to wait and see, then work with what’s left.” I spent about two
hours in the bar, drinking Bloody Marys for the V-8 nutritional content and watching the flights
from L.A. I’d eaten nothing but grapefruit for about twenty hours and my head was adrift from
its moorings. """,
		"""Raoul Duke, leftfielder & batting champion of the St. Louis Browns. Five days at $25 per,
plus twenty-five cents a mile. His card was valid, so of course we had no choice… This is true.
The car rental agency had no legal reason to hassle me, since my card was technically valid.
During the next four days I drove that car all over Las Vegas – even the VIP agency’s main office
on Paradise Boulevard several times – and at no time was I bothered by any show of rudeness.
 This is one of the hallmarks of Vegas hospitality. The only bedrock rule is Don’t Burn the
Locals. Beyond that, nobody cares. They would rather not know. If Charlie Manson checked into
the Sahara tomorrow morning, nobody would hassle him as long as he tipped big. """,
		""" drove straight to the hotel after renting the car. There was still no sign of my attorney, so
I decided to check in on my own – if only to get off the street and avoid a public breakdown. I
left the Whale in a VIP parking slot and shambled self-consciously into the lobby with one small
leather bag – a hand-crafted, custom-built satchel that had just been made for me by a
leathersmith friend in Boulder. """,
		"""After ten minutes of standing in line behind this noisy little asshole and his friends, I felt
the bile rising. Where did this cop – of all people – get the nerve to argue with anybody in terms
of Right & Reason? I had been there with these fuzzy shitheads – and so, I sensed, had the desk
clerk. He had air of a man who’d been fucked around, in his time, by a good cross-section of
mean-tempered rule – crazy now he was just giving their argument back to them: It didn’t matter
who’s right or wrong, man… or who’s paid & who hasn’t… what matters right now is that for at
time in my life I can work out on a pig: “Fuck you, I’m in charge here, and I’m telling you we
don’t have for you.” I was enjoying this whipsong, but after a while I felt dizzy, nervous, and my
impatience got the better of my amusement. So I stepped around the Pig and spoke directly to
the desk clerk – “Say,” I said, “I hate to interrupt, but I have a reservation and I wonder if maybe
I could just sort of slide through and get out of your way.” I smiled, letting him know I’d been
digging his snake-bully act on the cop party that was now standing there, psychologically offbalance
and staring at me like I was some kind of water-rat crawling up to the desk. """,
		"""Our room was in one of the farthest wings of the Flamingo. The place is far more than a
hotel: It is a sort of huge underfinanced Playboy Club in the middle of the desert. Something like
nine separate wings, with interconnecting causeways and pools – a vast complex, sliced up by a
maze of car-ramps and driveways. It took me about twenty minutes to wander from the desk to
the distant wing we’d been assigned to. """,
		"""He shook his head, struggling to focus on the question. “Shit,” he said finally. “I met her
on the plane and I had all that acid.” He shrugged. “You know, those little blue barrels. Jesus,
she’s a religious freak. She’s running away from home for something like the fifth time in six
months. It’s terrible. I gave her that cap before I realized… shit, she’s never even had a drink!”
“Well,” I said, “it’ll probably work out. We can keep her loaded and peddle her ass at the drug
convention.” He stared at me. """,
		"""After much difficulty, we got back to the room and tried to have a serious talk with Lucy. I
felt like a Nazi, but it had to be done. She was not right for us – not in this fragile situation. It
was bad enough if she were only what she appeared to be – a strange young girl in the throes of
a bad psychotic episode – but what worried me far more than that was the likelyhood that she
would probably be just sane enough, in a few hours, to work herself into a towering Jesus-based
rage at the hazy recollection of being picked up and seduced in the Los Angeles International
Airport by some kind of cruel Samoan who fed her liquor and LSD, then dragged her to a Vegas
hotel room and savagely penetrated every orifice in her body with his throbbing, uncircumcised
member. """,
		"""“Never mind,” I said. “Just picture yourself telling a jury that you tried to help this poor
girl by giving her LSD and then taking her out to Vegas for one of your special stark-naked back
rubs.” He shook his head sadly. “You’re right. They’d probably burn me at the goddamn stake…
set me on fire right there in the dock. Shit, it doesn’t pay to try to help somebody these days…” """,
		"""I thought about this… but the only alternative was to take her out to the desert and feed
her remains to the lizards. I wasn’t ready for this; it seemed a bit heavy for the thing we were
trying to protect: My attorney. It came down to that. So the problem was to work out a balance,
to aim Lucy in a direction that wouldn’t snap her mind and provoke a disastrous backlash. """,
		"""Then we drove her out to the airport, saying we were going to trade the White Whale in
for a Mercedes 600, and my attorney took her into the lobby with all her gear. She was still
unhinged and babbling when he led her away. I drove around a corner and waited for him. """,
		"""My attorney was doing the Big Spit again, in the bathroom. I walked out on the balcony
and stared at the pool, this kidney-shaped bag of bright water that shimmered outside our suite.
I felt like Othello. Here I’d only been in town a few hours, and we’d already laid the groundwork
for a classic tragedy. The hero was doomed; he had already sown the seed of his own downfall. """,
		"""“Yeah. She really flipped over you. The only way I could get rid of her, out there in the
airport, was by saying you were taking me out to the desert for a showdown – that you wanted
me out of the way so you could have her all to yourself.” He shrugged. “Shit, I had to tell her
something. I said she should go to the Americana and wait to see which one of us came back.”
He laughed again. “I guess she figures you won. That phone message wasn’t for me, was it?” I
nodded. It made no sense at all, but I knew it was true. Drug reasoning. The rhythms were
brutally clear – and, to him, they made excellent sense. """,
		"""ney sagged. “He was my cousin. The jury found him innocent.”
 “Shit!” I snapped. “How many people has that junkie bastard shot since we’ve known him?
Six? Eight? That evil little tuck is so guilty that I should probably kill him myself, on general
principles. He shot that narc just as sure as he killed that girl at the Holiday Inn… and that guy
in Ventura!” He eyed me coldly. “You better be careful, man. You’re into some heavy slander.” I
laughed, tossing my luggage together in a lump at the foot of the bed while I sat down to finish
my drink. I actually intended to leave. I didn’t really want to, but I figured that nothing I could
possibly do with this gig was worth the risk of tangled up with Lucy… No doubt she was a
beautiful person, if she ever got straight… very sensative, with a secret reserve karma
undernenth her Pit Bull act; a great talent with fine instincts… Just a heavy little gal who
unfortunately went stone crazy somewhere prior to her eighteenth birthday. """,
		"""“I don’t know for sure what they done to me, but I remember it was horrible. One guy
picked me up in the Los Angeles airport; he’s the one who gave me the pill… and the other one
met us at the hotel; he was sweating real bad and he talked so fast that I couldn’t understand
what he wanted… No sir, I don’t recall exactly what they did to me at that point, because I was
still under the influence of that drug… yessir, the LSD they gave me… and I think I was naked
for a long time, maybe the whole time they had me there. I think it was evening, because I
remember they had the news on. Yessir, Walter Cronkite, I remember his face all through it...”
No, I was not ready for this. No jury would doubt her testimony, especially when it came
stuttering out through a fog of tears and obscene acid flashbacks. And the fact that she couldn’t
recall precisely what we had done to her would make it impossible to deny. The jury would
know what we’d done. They would have read about people like us in the $2.95 paperbacks: Up
To The Hilt and Only Skin Deep, and seen your type in the $5 fuck-flicks. """,
		""" A Terrible Experience with Extremely Dangerous Drugs. """,
		"""He was nervously shifting the phone from ear to ear while he talked: “No… listen, I have
to get off; they probably have the phone tapped… yeah, I know, it was horrible, but it’s all over
now... O MY GOD! THEY’RE KICKING THE DOOR DOWN!” He hurled the phone down and
began shouting: “No! Get away from me! I’m innocent! It was Duke! I swear to God!” He kicked
the phone against the wall, then leaned down to it and began yelling again: “No, I don’t know
where she is! I think she went back to Montana. You’ll never catch Lucy! She’s gone!” He kicked
the receiver again, then picked it up and held it about a foot away from his mouth as he uttered
a long, quavering groan. “No! No! Don’t put that thing on me!” he screamed. Then he slammed
the phone down. """,
		"""“I know,” he replied. “But the guy didn’t have any cash. He’s one of these Satanism freaks.
He offered me human blood – said it would make me higher than I’d ever been in my life,” he
laughed. “I thought he was kidding, so I told him I’d just as soon have an ounce or so of pure
adrenochrome – or maybe just a fresh adrenalin gland to chew on.” I could already feel the stuff
working on me. The first wave felt like a combination of mescaline and methedrmne. Maybe I
should take a swim, I thought. """,
		"""“Finish the fucking story!” I snarled. “What happened? What about the glands?” He
backed away, keeping an eye on me as he edged across the room. “Maybe you need another
drink,” he said nervously. “Jesus, that stuff got right on top of you, didn’t it?” I tried to smile.
“Well… nothing worse… no, this is worse…” It was hard to move my jaws; my tongue felt like
burning magnesium. “No… nothing to worry about,” I hissed. “Maybe if you could just… shove
me into the pool, or something…”""",
		"""It was after midnight when I finally was able to talk and move around… but I was still not
free of the drug; the voltage had merely been cranked down from 220 to 110. I was a babbling
nervous wreck, flapping around the room like a wild animal, pouring sweat and unable to
concentrate on any one thought for more than two or three seconds at a time. """,
		"""“Forget it,” he said. “That’s Army territory. Bomb tests, nerve gas – we’d never make it.”
We wound up at a place called The Big Flip about halfway downtown. I had a “New York steak”
for $1.88. My attorney ordered the “Coyote Bush Basket” for $2.09… and after that we drank off
a pot of watery “Golden West” coffee and watched four boozed-up cowboy types kick a faggot
half to death between the pinball machines. """,
"""Sometime around midnight my attorney wanted coffee. He bad been vomiting fairly
regularly as we drove around the Strip, and the right flank of the Whale was badly streaked. We
were idling at a stoplight in front of the Silver Slipper beside a big blue Ford with Oklahoma
plates… two hoggish-looking couples in the car, probably cops from Muskogee using the Drug
Conference to give their wives a look at Vegas. They looked like they’d just beaten Caesar’s
Palace for about $38 at the blackjack tables, and now they were headed for the Circus-Circus to
whoop it up… but suddenly, they found themselves next to a white Cadillac convertible all
covered with vomit and a 300-pound Samoan in a yellow fishnet T-shirt yelling at them: “Hey
there! You folks want to buy some heroin?” No reply. No sign of recognition. They’d been
warned about this kind of crap: Just ignore it... """,
"""We made another turn and almost rolled again. The Coupe de Ville is not your ideal
machine for high speed cornering in residential neighborhoods. The handling is very mushy…
unlike the Red Shark, which had responded very nicely to situations requiring the quick fourwheel
drift. But the Whale Bad of cutting loose at the critical moment – had a tendency to dig in,
which accounted for that sickening ‘here we go’ sensation. """,
"""“We’ll see,” I said, moving around to the rear with the air-hose. In truth, I was nervous.
The two front ones were tighter than snare drums; they felt like teak wood when I tapped on
them with the rod. But what the hell? I thought. If they explode, so what? It’s not often that a
man gets a chance to run terminal experiments on a virgin Cadillac and four brand-new $80
tires. For all I knew, the thing might start cornering like a Lotus Elan. If not, all I had to do was
call the VIP agency and have another one delivered… maybe threaten them with a lawsuit
because all four tires had exploded on me, while driving in heavy traffic. Demand an Eldorado,
next time, with four Michelin Xs. And put it all on the card… charge it to the St. Louis Browns. """,
"""About thirty minutes after our brush with the Okies we pulled into an all-night diner on
the Tonopah highway, on the kirts of a mean/scag ghetto called “North Las Vegas.” Which is
actually outside the city limits of Vegas proper. North Vegas is where you go when you’ve fucked
up once too often on the Strip, and when you’re not even welcome in the cut-rate downtown
places around Casino Center. """,
"""The big hotels and casinos pay a lot of muscle to make sure high rollers don’t have even
momentary hassles with “undesirables.” Security in a place like Caesar’s Palace is super tense and
strict. Probably a third of the people on the floor at given time are either shills or watchdogs.
Public drunks known pickpockets are dealt with instantly-hustled out parking lot by Secret
Service type thugs and given a impersonal lecture about the cost of dental work and of trying to
make a living with two broken erms. """,


















		"""Ever since I came, huh? Well, it seems the old bird who's boss here has his weak points. He
leans toward pious speeches, so I took a chance that worked. I'm here in the capacity of your
spiritual adviser. There's something about a pious man such as he. He will cheerfully cut your
throat if it suits him, but he will hesitate to endanger the welfare of your immaterial and
problematical soul. It's just a piece of empirical psychology. A trader has to know a little of
everything.""",
		""""All right. I'll grant that. I don't scoot about space to save the Foundation or anything like that.
But I'm out to make money, and this is my chance. If it helps the Foundation at the same time,
all the better. And I've risked my life on slimmer chances."
Ponyets rose, and Gorov rose with him, "What are you going to do?"
The trader smiled, "Gorov, I don't know – not yet. But if the crux of the matter is to make a sale,
then I'm your man. I'm not a boaster as a general thing, but there's one thing I'll always back
up. I've never ended up below quota yet."
The door to the cell opened almost instantly when he knocked, and two guards fell in on either
side.""",
		"""Ponyets said rapidly, "Gentlemen, this is pure gold. Gold through and through. You may subject
it to every known physical and chemical test, if you wish to prove the point. It cannot be
identified from naturally-occurring gold in any way. Any iron can be so treated. Rust will not
interfere, not will a moderate amount of alloying metals– """,
		"""And Ponyets countered, "A rose can grow from the mud, your Veneration. In your dealings with
your neighbors, you buy material of all imaginable variety, without inquiring as to where they
get it, whether from an orthodox machine blessed by your benign ancestors or from some
space-spawned outrage. Come, I don't offer the machine. I offer the gold.""",
		""""In that secrecy is the essence of its use; that same secrecy you described as the only safety
with regard to nucleics. You may bury the transmuter in the deepest dungeon of the strongest
fortress on your furthest estate, and it will still bring you instant wealth. It is the gold you buy,
not the machine, and that gold bears no trace of its manufacture, for it cannot be told from the
natural creation.""",
		""""I didn't," Ponyets answer was patient. "I juiced it up out of a food irradiation chamber. It isn't
any good, really. The power consumption is prohibitive on any large scale or the Foundation
would use transmutation instead of chasing all over the Galaxy for heavy metals. It's one of the
standard tricks every trader uses, except that I never saw an iron-to-gold one before. But it's
impressive, and it works – very temporarily.""",
		""""What's there to explain? It's obvious, Gorov. Look, the clever dog thought he had me in a
foolproof trap, because his word was worth more than mine to the Grand Master. He took the
transmuter. That was a capital crime in Askone. But at any time he could say that he had lured
me on into a trap with the purest of patriotic motives, and denounce me as a seller of forbidden
things.""",
		"""TRADERS-... With psychohistoric inevitability. economic control of the Foundation grew. The
traders grew rich; and with riches came power....
It is sometimes forgotten that Hober Mallow began life as an ordinary trader. It is never
forgotten that he ended it as the first of the Merchant Princes....""",
		"""The trader nodded, "I've been there. Stinking rathole! I suppose you can call it a republic but it's
always someone out of the Argo family that gets elected Commdor each time. And if you ever
don't like it – things happen to you." He twisted his lip and repeated, "I've been there.""",
		"""Jorane Sutt did not waste his time in the luxury of annoyance. As secretary to the mayor, he
had held off opposition councilmen, jobseekers, reformers, and crackpots who claimed to have
solved in its entirety the course of future history as worked out by Hari Seldon. With training like
that, it took a good deal to disturb him.""",
		"""The secretary said calmly, "There's nothing miraculous about the possibility. Since the Four
Kingdoms accepted the Foundation Convention, we have had to deal with considerable groups
of dissident populations in each nation. Each former kingdom has its pretenders and its former
noblemen, who can't very well pretend to love the Foundation. Some of them are becoming
active, perhaps""",
		""""Hold on!" Mallow's hand fell on the other's balled fist. "Don't go into a blaze. If it's a trick, I'll be
back some day for the reckoning. if it isn't, your snake, Sutt, is playing into our hands. Listen,
there's a Seldon crisis coming up.""",
		""""But it could mean, on the other hand, that they haven't nuclear power after all. Or maybe they
have and are keeping undercover, for fear we know something. It's one thing, after all, to
piratize blundering, light-armed merchant ships. It's another to fool around with an accredited
envoy of the Foundation when the mere fact of his presence may mean the Foundation is
growing suspicious.""",
		"""And there was suddenly a gun in his hand. He added, "I don't know what insubordination is. I
have never had any experience with it. But if there's anyone here who thinks he can teach me,
I'd like to teach him my antidote in return.""",
		"""Mallow stared him down, sardonically. "Twer," he said, "I'm disappointed. Your three years in
politics seem to have gotten you out of trader habits. Remember, I may be a democrat back at
the Foundation, but there's nothing short of tyranny that can run my ship the way I want it run. I
never had to pull a blaster on my men before, and I wouldn't have had to now, if you hadn't
gone out of line.""",
		""""Free Trade, then. You must see that it would be of benefit to both of us. There are things you
have that we want, and things we have that you want. It asks only an exchange to bring
increased prosperity. An enlightened ruler such as yourself, a friend of the people – I might say,
a member of the people – needs no elaboration on that theme. I won't insult your intelligence by
offering any.""",
		""""So it has always been in effect. Surely you remember the case of Askone twenty years ago.
First they were sold some of your goods and then your people asked for complete freedom of
missionary effort in order that the goods might be run properly; that Temples of Health be set
up. There was then the establishment of religious schools; autonomous rights for all officers of
the religion and with what result? Askone is now an integral member of the Foundation's
system and the Grand Master cannot call his underwear his own. Oh, no! Oh, no! The dignity of
an independent people could never suffer it.""",
		"""The Commdor referred to his dwelling place as a house. The populace undoubtedly would call
it a palace. To Mallow's straightforward eyes, it looked uncommonly like a fortress. it was built
on an eminence that overlooked the capital. Its walls were thick and reinforced. Its approaches
were guarded, and its architecture was shaped for defense. Just the type of dwelling, Mallow
thought sourly, for Asper, the Well-Beloved.""",
		"""Mallow said, "We can explain the workings of dummy corporations, if you would like. –Then,
working further at random, take our complete line of household gadgets. We have collapsible
stoves that will roast the toughest meats to the desired tenderness in two minutes. We've got
knives that won't require sharpening. We've got the equivalent of a complete laundry that can
be packed in a small closet and will work entirely automatically. Ditto dish-washers. Ditto-ditto
floor-scrubbers, furniture polishers, dust-precipitators, lighting fixtures – oh, anything you like.
Think of your increased popularity, if you make them available to the public. Think of your
increased quantity of, uh, worldly goods, if they're available as a government monopoly at nine
hundred percent profit. It will be worth many times the money to them, and they needn't know
what you pay for it. And, mind you, none of it will require priestly supervision. Everybody will be
happy.""",
		"""There is no need for dramatics, Licia, my dear," said the Commdor, mildly. "The young man
will attend at dinner tonight, and you can speak with him all you wish and even amuse yourself
by listening to all I say. Room will have to be arranged for his men somewhere about the place.
The stars grant that they be few in numbers""",
"""The Commdor's own bodyguard, in the confusion, had struggled to the front line, and Mallow,
for the first time, was near enough to see their unfamiliar hand-weapons in detail.
They were nuclear! There was no mistaking it; an explosive projectile weapon with a barrel like
that was impossible. But that wasn't the big point. That wasn't the point at all.
The butts of those weapons had, deeply etched upon them, in worn gold plating, the
Spaceship-and-Sun!
The same Spaceship-and-Sun that was stamped on every. one of the great volumes of the
original Encyclopedia that the Foundation had begun and not yet finished. The same
Spaceship-and-Sun that had blazoned the banner of the Galactic Empire through millennia.
Mallow talked through and around his thoughts, "Test that pipe! It's one piece. Not perfect;
naturally, the joining shouldn't be done by hand.""",
"""The Far Star was two days out in space, when Hober Mallow, in his private quarters with Senior
Lieutenant Drawt, handed him an envelope, a roll of microfilm, and a silvery spheroid.
"As of an hour from now, Lieutenant, you're Acting Captain of the Far Star, until I return, –or
forever."
Drawt made a motion of standing but Mallow waved him down imperiously.
"Quiet, and listen. The envelope contains the exact location of the planet to which you're to
proceed. There you will wait for me for two months. If, before the two months are up, the
Foundation locates you, the microfilm is my report of the trip.
"If, however," and his voice was somber, "I do not return at the end of two months, and
Foundation vessels do not locate you, proceed to the planet, Terminus, and hand in the Time
Capsule as the report. Do you understand that?"
"Yes, sir."
"At no time are you, or any of the men, to amp""",
"""Onum Barr was an old man, too old to be afraid. Since the last disturbances, he had lived alone
on the fringes of the land with what books he had saved from the ruins. He had nothing he
feared losing, least of all the worn remnant of his life, and so he faced the intruder without
cringing.""",
"""The stranger said, "My name is Hober Mallow. I come from a far province."
Barr nodded and smiled, "Your tongue convicted you of that long ago. I am Onum Barr of
Siwenna – and once Patrician of the Empire."
"Then this is Siwenna. I had only old maps to guide me."
"They would have to be old, indeed, for star-positions to be misplaced."
Barr sat quite still, while the other's eyes drifted away into a reverie. He noticed that the nuclear
force-shield had vanished from about the man and admitted dryly to himself that his person no
longer seemed formidable to strangers – or even, for good or for evil, to his enemies.""",
""""That is easily enough done, and poor though I am, deprives me of nothing. Do you mean the
capital of the planet, or of the Imperial Sector?"
The younger man's eyes narrowed, "Aren't the two identical? Isn't this Siwenna?"
The old patrician nodded slowly, "Siwenna, yes. But Siwenna is no longer capital of the
Normannic Sector. Your old map has misled you after all. The stars may not change even in
centuries, but political boundaries are all too fluid."
"That's too bad. In fact, that's very bad. Is the new capital far off?"
"It's on Orsha II. Twenty parsecs off. Your map will direct you. How old is it?"
"A hundred and fifty years."
"That old?" The old man sighed. "History has been crowded since. Do you know any of it?"
Mallow shook his bead slowly.""",
"""a long time to use up. Compared to the wealth of the last century, though, we have gone a long
way downhill – and there is no sign of turning, not yet. Why are you so interested in all this,
young man? You are all alive and your eyes shine!""",
"""Mallow jerked his head, "There isn't much law out there where I come from. Fighting and scars
are part of a trader's overhead. But fighting is only useful when there's money at the end, and if
I can get it without, so much the sweeter. Now will I find enough money here to make it worth
the fighting? I take it I can find the fighting easily enough.""",
"""Barr's face darkened. "Civil wars are chronic in these degenerate days, but Siwenna had kept
apart. Under Stannell VI, it had almost achieved its ancient prosperity. But weak emperors
followed, and weak emperors mean strong viceroys, and our last viceroy – the same Wiscard,
whose remnants still prey on the commerce among the Red Stars – aimed at the Imperial
Purple. He wasn't the first to aim. And if he had succeeded, he wouldn't have been the first to
succeed.""",
""""Thank you," said Barr, wearily. "It's kind of you to humor an old man. They rebelled; or I should
say, we rebelled, for I was one of the minor leaders. Wiscard left Siwenna, barely ahead of us,
and the planet, and with it the province, were thrown open to the admiral with every gesture of
loyalty to the Emperor. Why we did this, –I'm not sure. Maybe we felt loyal to the symbol, if not
the person, of the Emperor, –a cruel and vicious child. Maybe we feared the horrors of a siege.""",
""""On the pretext that they had rebelled against their viceroy, the Emperor's anointed. And the
admiral became the new viceroy, by virtue of one month of massacre, pillage and complete
horror. I had six sons. Five died – variously. I had a daughter. I hope she died, eventually. I
escaped because I was old. I came here, too old to cause even our viceroy worry." He bent his
gray head, "They left me nothing, because I had helped drive out a rebellious governor and
deprived an admiral of his glory.""",
""""Eh?" Barr smiled acidly. "He is safe, for he has joined the admiral as a common soldier under
an assumed name. He is a gunner in the viceroy's personal fleet. Oh, no, I see your eyes. He is
not an unnatural son. He visits me when he can and gives me what he can. He keeps me alive.
And some day, our great and glorious viceroy will grovel to his death, and it will be my son who
will be his executioner.""",
""""Destroy them? Oh, no. Half a planet would be wiped out before the smallest power station
would be touched. They are irreplaceable and the suppliers of the strength of the fleet." Almost
proudly, "We have the largest and best on this side of Trantor itself.""",
""""Wait!" Barr held out his thin hands. "Where do you rush? You come here, but I ask no
questions. In the city, where the inhabitants are still called rebels, you would be challenged by
the first soldier or guard who heard your accent and saw your clothes.""",
"""He returned but once, for a moment, to the old patrician's house, before leaving it entirely,
however. And when Onum Barr stepped into his little garden early the next morning, he found a
box at his feet. It contained provisions, concentrated provisions such as one would find aboard
ship, and alien in taste and preparation""",
"""The trader glanced humorously at the two flabby hands that had been named as his possible
executioners then and there, and said, "Your Wisdom, you are wrong on three counts. First, I
am not a creature of the viceroy come to test your loyalty. Second, my gift is something the
Emperor himself in all his splendor does not and will never possess. Third, what I wish in return
is very little; a nothing; a mere breath.""",
"""The tech-man looked up, and his face was congested with blood, "Sir, I am a tech-man, senior
grade. I have twenty years behind me as supervisor and I studied under the great Bier at the
University of Trantor. If you have the infernal charlatanry to tell me that a small container the
size of a – of a walnut, blast it, holds a nuclear generator, I'll have you before the Protector in
three seconds.""",
"""The tech-man's flush faded slowly as he bound the chain about his waist, and, following
Mallow's gesture, pushed the knob. The radiance that surrounded him shone into dim relief. His
blaster lifted, then hesitated. Slowly, he adjusted it to an almost burnless minimum.""",
"""The tech-man's home was a small two-story affair on the Outskirts of the huge, cubiform,
windowless affair that dominated the center of the city. Mallow passed from one to the other
through an underground passage, and found himself in the silent, ozone-tinged atmosphere of
the powerhouse.""",
"""Mallow relaxed for almost the first time in six months. He was on his back in the sunroom of his
new house, stripped to the skin. His great, brown arms were thrown up and out, and the
muscles tautened into a stretch, then faded into repose.""",
"""Yes," Sutt rubbed his forehead thoughtfully with one finger, "but since then your activities have
been significant. We know a good deal of what you're doing, Mallow. We know, exactly, how
many factories you're putting up; in what a hurry you're doing it; and how much it's costing you.
And there's this palace you have," he gazed about him with a cold lack of appreciation, "which
set you back considerably more than my annual salary; and a swathe you've been cutting – a
very considerable and expensive swathe – through the upper layers of Foundation society.""",
"""Riose said pleadingly, "You don't understand, patrician, and I doubt my ability to make you. I
can't argue on your ground. You're the scholar, not I. But this I can tell you. Whatever you think
of the Empire, you will admit its great services. Its armed forces have committed isolated
crimes, but in the main they have been a force for peace and civilization. It was the Imperial
navy that created the Pax Imperium that ruled over all the Galaxy for thousands of years.
Contrast the millennia of peace under the Sun-and-Spaceship of the Empire with the millennia
of interstellar anarchy that preceded it. Consider the wars and devastations of those old days""",
""""Then you realize that it must be stopped in embryo or perhaps not at all. You have known of
this Foundation before anyone had heard of it. You know more about it than anyone else in the
Empire. You probably know how it might best be attacked; and you can probably forewarn me
of its countermeasures. Come, let us be friends.""",
""""Why not?" Bel Riose's eyes glistened fiercely. "No, stay where you are. I'll tell you when you
may leave. Why not? If you think I underestimate this enemy I have discovered, you are wrong.
Patrician," he spoke reluctantly, "I lost a ship on my return. I have no proof that it fell into the
hands of the Foundation; but it has not been located since and were it merely an accident, its
dead hulk should, certainly have been found along the route we took. It is not an important loss
– less than the tenth part of a fleabite, but it may mean that the Foundation has already opened
hostilities. Such eagerness and such disregard for consequences might mean secret forces of
which I know nothing. Can you help me then by answering a specific question? What is their
military power?""",
"""reached mathematical maturity with one man, Hari Seldon, and died with him, for no man since
has been capable of manipulating its intricacies. But in that short period, it proved itself the
most powerful instrument ever invented for the study of humanity. Without pretending to predict
the actions of individual humans, it formulated definite laws capable of mathematical analysis
and extrapolation to govern and predict the mass action of human groups.""",
"""CLEON II commonly called "The Great." The last strong Emperor of the First Empire, he is
important for the political and artistic renaissance that took place during his long reign. He is
best known to romance, however, for his connection with Bel Riose, and to the common man,
he is simply "Riose's Emperor." It is important not to allow events of the last year of his reign to
overshadow forty years of...
ENCYCLOPEDIA GALACTICA""",
	]
	return text
index_train = []
index_test = []
def set_train_index():
	for x in range(0, 70):
		index_train.append(0)
	for x in range(70, 140):
		index_train.append(1)	
	return index_train
def set_test_index():
	for x in range(0, 45):
		index_test.append(0)
	for x in range(45, 90):
		index_test.append(1)
	return index_test
