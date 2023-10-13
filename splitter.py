import json
import random

# Your input JSON data
data = [
{
    "input": "##USER: Put on some tracks from the Beatles, please",
    "output": "##COMMAND: PLAY ARTIST THE BEATLES ##RESPONSE: Sure thing! Here come the Beatles."
},
{
    "input": "##USER: I'm in the mood for some classic rock, how about Led Zeppelin?",
    "output": "##COMMAND: PLAY ARTIST LED ZEPPELIN ##RESPONSE: Rocking with Led Zeppelin!"
},
{
    "input": "##USER: Play some jazz, like Miles Davis",
    "output": "##COMMAND: PLAY ARTIST MILES DAVIS ##RESPONSE: Let's jazz it up with Miles Davis."
},
{
    "input": "##USER: Could you play something from Taylor Swift's latest album?",
    "output": "##COMMAND: PLAY ARTIST TAYLOR SWIFT ##RESPONSE: Taylor Swift's latest tunes, coming right up!"
},
{
    "input": "##USER: I want to listen to some electronic music, like Daft Punk",
    "output": "##COMMAND: PLAY ARTIST DAFT PUNK ##RESPONSE: Electronic vibes with Daft Punk!"
},
{
    "input": "##USER: How about some country music by Johnny Cash?",
    "output": "##COMMAND: PLAY ARTIST JOHNNY CASH ##RESPONSE: Going country with Johnny Cash!"
},
{
    "input": "##USER: Play songs by Queen, please",
    "output": "##COMMAND: PLAY ARTIST QUEEN ##RESPONSE: Rocking with Queen's hits!"
},
{
    "input": "##USER: I'm feeling nostalgic, play some 90s hip-hop, like Tupac",
    "output": "##COMMAND: PLAY ARTIST TUPAC ##RESPONSE: Nostalgic 90s hip-hop with Tupac!"
},
{
    "input": "##USER: Can you play some indie rock by Arctic Monkeys?",
    "output": "##COMMAND: PLAY ARTIST ARCTIC MONKEYS ##RESPONSE: Indie rock vibes from Arctic Monkeys!"
},
{
    "input": "##USER: Put on some reggae music, like Bob Marley",
    "output": "##COMMAND: PLAY ARTIST BOB MARLEY ##RESPONSE: Reggae vibes with Bob Marley!"
},
{
    "input": "##USER: I need some high-energy music, like the Red Hot Chili Peppers",
    "output": "##COMMAND: PLAY ARTIST RED HOT CHILI PEPPERS ##RESPONSE: Get ready for some high-energy tunes with the Red Hot Chili Peppers!"
},
{
    "input": "##USER: Play some R&B, maybe some Beyonce",
    "output": "##COMMAND: PLAY ARTIST BEYONCE ##RESPONSE: Let's groove to some R&B with Beyonce."
},
{
    "input": "##USER: How about some classical music by Mozart?",
    "output": "##COMMAND: PLAY ARTIST MOZART ##RESPONSE: Time for some classical elegance with Mozart."
},
{
    "input": "##USER: Play me some alternative rock like Radiohead",
    "output": "##COMMAND: PLAY ARTIST RADIOHEAD ##RESPONSE: Enjoying alternative rock with Radiohead!"
},
{
    "input": "##USER: I'm in the mood for some oldies, like Elvis Presley",
    "output": "##COMMAND: PLAY ARTIST ELVIS PRESLEY ##RESPONSE: Traveling back in time with Elvis Presley's classics."
},
{
    "input": "##USER: Play songs from the '80s, like Michael Jackson",
    "output": "##COMMAND: PLAY ARTIST MICHAEL JACKSON ##RESPONSE: Let's dance to '80s hits with Michael Jackson!"
},
{
    "input": "##USER: Can you play some EDM, like Calvin Harris?",
    "output": "##COMMAND: PLAY ARTIST CALVIN HARRIS ##RESPONSE: Getting the party started with EDM from Calvin Harris!"
},
{
    "input": "##USER: Put on some folk music, like Simon & Garfunkel",
    "output": "##COMMAND: PLAY ARTIST SIMON & GARFUNKEL ##RESPONSE: Enjoying the soothing sounds of folk with Simon & Garfunkel."
},
{
    "input": "##USER: Play reggaeton music, like Daddy Yankee",
    "output": "##COMMAND: PLAY ARTIST DADDY YANKEE ##RESPONSE: Dancing to reggaeton beats with Daddy Yankee!"
},
{
    "input": "##USER: How about some pop-rock by Maroon 5?",
    "output": "##COMMAND: PLAY ARTIST MAROON 5 ##RESPONSE: Rocking out with pop-rock from Maroon 5!"
},
{
    "input": "##USER: Play 'Bohemian Rhapsody' by Queen, please",
    "output": "##COMMAND: PLAY SONG BOHEMIAN RHAPSODY - QUEEN ##RESPONSE: Rocking out to 'Bohemian Rhapsody' by Queen."
},
{
    "input": "##USER: Put on 'Shape of You' by Ed Sheeran",
    "output": "##COMMAND: PLAY SONG SHAPE OF YOU - ED SHEERAN ##RESPONSE: Dancing to 'Shape of You' by Ed Sheeran."
},
{
    "input": "##USER: Play 'Billie Jean' by Michael Jackson",
    "output": "##COMMAND: PLAY SONG BILLIE JEAN - MICHAEL JACKSON ##RESPONSE: Getting into the groove with 'Billie Jean' by Michael Jackson."
},
{
    "input": "##USER: I want to hear 'Imagine' by John Lennon",
    "output": "##COMMAND: PLAY SONG IMAGINE - JOHN LENNON ##RESPONSE: Enjoying the classic 'Imagine' by John Lennon."
},
{
    "input": "##USER: Put on 'Rolling in the Deep' by Adele, please",
    "output": "##COMMAND: PLAY SONG ROLLING IN THE DEEP - ADELE ##RESPONSE: Singing along to 'Rolling in the Deep' by Adele."
},
{
    "input": "##USER: Play 'Hotel California' by the Eagles",
    "output": "##COMMAND: PLAY SONG HOTEL CALIFORNIA - THE EAGLES ##RESPONSE: Checking in to 'Hotel California' by The Eagles."
},
{
    "input": "##USER: I'm in the mood for 'Smooth Criminal' by Michael Jackson",
    "output": "##COMMAND: PLAY SONG SMOOTH CRIMINAL - MICHAEL JACKSON ##RESPONSE: Getting ready to groove to 'Smooth Criminal' by Michael Jackson."
},
{
    "input": "##USER: Can you play 'Stairway to Heaven' by Led Zeppelin?",
    "output": "##COMMAND: PLAY SONG STAIRWAY TO HEAVEN - LED ZEPPELIN ##RESPONSE: Ascending 'Stairway to Heaven' with Led Zeppelin."
},
{
    "input": "##USER: Put on 'Purple Haze' by Jimi Hendrix, please",
    "output": "##COMMAND: PLAY SONG PURPLE HAZE - JIMI HENDRIX ##RESPONSE: Rocking out to 'Purple Haze' by Jimi Hendrix."
},
{
    "input": "##USER: I want to hear 'Hey Jude' by the Beatles",
    "output": "##COMMAND: PLAY SONG HEY JUDE - THE BEATLES ##RESPONSE: Singing along to 'Hey Jude' by The Beatles."
},
{
    "input": "##USER: Play 'Purple Rain' by Prince",
    "output": "##COMMAND: PLAY SONG PURPLE RAIN - PRINCE ##RESPONSE: Enjoying 'Purple Rain' by Prince."
},
{
    "input": "##USER: Put on 'Wonderwall' by Oasis, please",
    "output": "##COMMAND: PLAY SONG WONDERWALL - OASIS ##RESPONSE: Listening to 'Wonderwall' by Oasis."
},
{
    "input": "##USER: Play 'Sweet Child o' Mine' by Guns N' Roses",
    "output": "##COMMAND: PLAY SONG SWEET CHILD O' MINE - GUNS N' ROSES ##RESPONSE: Rocking out to 'Sweet Child o' Mine' by Guns N' Roses."
},
{
    "input": "##USER: I'd like to hear 'Imagine Dragons' by Radioactive",
    "output": "##COMMAND: PLAY SONG RADIOACTIVE - IMAGINE DRAGONS ##RESPONSE: Getting fired up with 'Radioactive' by Imagine Dragons."
},
{
    "input": "##USER: Put on 'Shape of My Heart' by Sting",
    "output": "##COMMAND: PLAY SONG SHAPE OF MY HEART - STING ##RESPONSE: Enjoying 'Shape of My Heart' by Sting."
},
{
    "input": "##USER: Play 'Piano Man' by Billy Joel",
    "output": "##COMMAND: PLAY SONG PIANO MAN - BILLY JOEL ##RESPONSE: Singing along to 'Piano Man' by Billy Joel."
},
{
    "input": "##USER: I want to hear 'Time' by Pink Floyd",
    "output": "##COMMAND: PLAY SONG TIME - PINK FLOYD ##RESPONSE: Losing track of time with 'Time' by Pink Floyd."
},
{
    "input": "##USER: Play 'Rolling Stone' by The Weeknd",
    "output": "##COMMAND: PLAY SONG ROLLING STONE - THE WEEKND ##RESPONSE: Listening to 'Rolling Stone' by The Weeknd."
},
{
    "input": "##USER: Put on 'Livin' on a Prayer' by Bon Jovi, please",
    "output": "##COMMAND: PLAY SONG LIVIN' ON A PRAYER - BON JOVI ##RESPONSE: Rocking out to 'Livin' on a Prayer' by Bon Jovi."
},
{
    "input": "##USER: I'd like to hear 'Yellow Submarine' by The Beatles",
    "output": "##COMMAND: PLAY SONG YELLOW SUBMARINE - THE BEATLES ##RESPONSE: Sailing away with 'Yellow Submarine' by The Beatles."
},
{
    "input": "##USER: Play 'Sicko Mode' by Travis Scott",
    "output": "##COMMAND: PLAY SONG SICKO MODE - TRAVIS SCOTT ##RESPONSE: Getting into the groove with 'Sicko Mode' by Travis Scott."
},
{
    "input": "##USER: Put on 'Lose Yourself' by Eminem, please",
    "output": "##COMMAND: PLAY SONG LOSE YOURSELF - EMINEM ##RESPONSE: Listening to 'Lose Yourself' by Eminem."
},
{
    "input": "##USER: Play 'Old Town Road' by Lil Nas X",
    "output": "##COMMAND: PLAY SONG OLD TOWN ROAD - LIL NAS X ##RESPONSE: Riding along with 'Old Town Road' by Lil Nas X."
},
{
    "input": "##USER: I want to hear 'HUMBLE.' by Kendrick Lamar",
    "output": "##COMMAND: PLAY SONG HUMBLE. - KENDRICK LAMAR ##RESPONSE: Getting 'HUMBLE.' with Kendrick Lamar."
},
{
    "input": "##USER: Put on 'God's Plan' by Drake",
    "output": "##COMMAND: PLAY SONG GOD'S PLAN - DRAKE ##RESPONSE: Listening to 'God's Plan' by Drake."
},
{
    "input": "##USER: Play 'Hotline Bling' by Drake",
    "output": "##COMMAND: PLAY SONG HOTLINE BLING - DRAKE ##RESPONSE: Dancing to 'Hotline Bling' by Drake."
},
{
    "input": "##USER: Can you play 'Black Beatles' by Rae Sremmurd?",
    "output": "##COMMAND: PLAY SONG BLACK BEATLES - RAE SREMMURD ##RESPONSE: Rocking out to 'Black Beatles' by Rae Sremmurd."
},
{
    "input": "##USER: Put on 'Uptown Funk' by Mark Ronson ft. Bruno Mars, please",
    "output": "##COMMAND: PLAY SONG UPTOWN FUNK - MARK RONSON FT. BRUNO MARS ##RESPONSE: Grooving to 'Uptown Funk' by Mark Ronson ft. Bruno Mars."
},
{
    "input": "##USER: I'd like to hear 'Mo Money Mo Problems' by The Notorious B.I.G",
    "output": "##COMMAND: PLAY SONG MO MONEY MO PROBLEMS - THE NOTORIOUS B.I.G ##RESPONSE: Enjoying 'Mo Money Mo Problems' by The Notorious B.I.G."
},
{
    "input": "##USER: Play 'Hot Girl Summer' by Megan Thee Stallion",
    "output": "##COMMAND: PLAY SONG HOT GIRL SUMMER - MEGAN THEE STALLION ##RESPONSE: Heating things up with 'Hot Girl Summer' by Megan Thee Stallion."
},
{
    "input": "##USER: Put on 'Suge' by DaBaby, please",
    "output": "##COMMAND: PLAY SONG SUGE - DABABY ##RESPONSE: Listening to 'Suge' by DaBaby."
},
{
    "input": "##USER: Play 'Money' by Cardi B",
    "output": "##COMMAND: PLAY SONG MONEY - CARDI B ##RESPONSE: Counting 'Money' with Cardi B."
},
{
    "input": "##USER: I want to hear 'Gin and Juice' by Snoop Dogg",
    "output": "##COMMAND: PLAY SONG GIN AND JUICE - SNOOP DOGG ##RESPONSE: Sipping on 'Gin and Juice' with Snoop Dogg."
},
{
    "input": "##USER: Put on 'In Da Club' by 50 Cent, please",
    "output": "##COMMAND: PLAY SONG IN DA CLUB - 50 CENT ##RESPONSE: Partying 'In Da Club' with 50 Cent."
},
{
    "input": "##USER: Play 'Sick Boy' by The Chainsmokers",
    "output": "##COMMAND: PLAY SONG SICK BOY - THE CHAINSMOKERS ##RESPONSE: Listening to 'Sick Boy' by The Chainsmokers."
},
{
    "input": "##USER: Can you play 'No Role Modelz' by J. Cole?",
    "output": "##COMMAND: PLAY SONG NO ROLE MODELZ - J. COLE ##RESPONSE: Getting introspective with 'No Role Modelz' by J. Cole."
},
{
    "input": "##USER: Put on 'Bad and Boujee' by Migos",
    "output": "##COMMAND: PLAY SONG BAD AND BOUJEE - MIGOS ##RESPONSE: Feeling 'Bad and Boujee' with Migos."
},
{
    "input": "##USER: I'd like to hear 'Fancy' by Iggy Azalea",
    "output": "##COMMAND: PLAY SONG FANCY - IGGY AZALEA ##RESPONSE: Getting fancy with Iggy Azalea."
},
{
    "input": "##USER: Play 'Hotline Bling' by Drake",
    "output": "##COMMAND: PLAY SONG HOTLINE BLING - DRAKE ##RESPONSE: Dancing to 'Hotline Bling' by Drake."
},
{
    "input": "##USER: Put on 'Old Town Road' by Lil Nas X",
    "output": "##COMMAND: PLAY SONG OLD TOWN ROAD - LIL NAS X ##RESPONSE: Riding along with 'Old Town Road' by Lil Nas X."
},
{
    "input": "##USER: Put on 'Wonderful Tonight,' please",
    "output": "##COMMAND: PLAY SONG WONDERFUL TONIGHT ##RESPONSE: Enjoying 'Wonderful Tonight.'"
},
{
    "input": "##USER: Play 'Don't Stop Believin'",
    "output": "##COMMAND: PLAY SONG DON'T STOP BELIEVIN' ##RESPONSE: Belting out 'Don't Stop Believin'."
},
{
    "input": "##USER: I'd like to hear 'Radioactive.'",
    "output": "##COMMAND: PLAY SONG RADIOACTIVE ##RESPONSE: Getting fired up with 'Radioactive.'"
},
{
    "input": "##USER: Play 'Sweet Child o' Mine.'",
    "output": "##COMMAND: PLAY SONG SWEET CHILD O' MINE ##RESPONSE: Rocking out to 'Sweet Child o' Mine.'"
},
{
    "input": "##USER: Put on 'Hotel California,' please",
    "output": "##COMMAND: PLAY SONG HOTEL CALIFORNIA ##RESPONSE: Checking in to 'Hotel California.'"
},
{
    "input": "##USER: I want to hear 'Bohemian Rhapsody.'",
    "output": "##COMMAND: PLAY SONG BOHEMIAN RHAPSODY ##RESPONSE: Rocking out to 'Bohemian Rhapsody.'"
},
{
    "input": "##USER: Play 'Billie Jean.'",
    "output": "##COMMAND: PLAY SONG BILLIE JEAN ##RESPONSE: Getting into the groove with 'Billie Jean.'"
},
{
    "input": "##USER: Put on 'Rolling in the Deep,' please",
    "output": "##COMMAND: PLAY SONG ROLLING IN THE DEEP ##RESPONSE: Singing along to 'Rolling in the Deep.'"
},
{
    "input": "##USER: I'd like to hear 'Imagine.'",
    "output": "##COMMAND: PLAY SONG IMAGINE ##RESPONSE: Enjoying the classic 'Imagine.'"
},
{
    "input": "##USER: Play 'Smells Like Teen Spirit.'",
    "output": "##COMMAND: PLAY SONG SMELLS LIKE TEEN SPIRIT ##RESPONSE: Rocking out to 'Smells Like Teen Spirit.'"
},
{
    "input": "##USER: Put on 'Wonderwall,' please",
    "output": "##COMMAND: PLAY SONG WONDERWALL ##RESPONSE: Listening to 'Wonderwall.'"
},
{
    "input": "##USER: I want to hear 'Smooth Criminal.'",
    "output": "##COMMAND: PLAY SONG SMOOTH CRIMINAL ##RESPONSE: Getting ready to groove to 'Smooth Criminal.'"
},
{
    "input": "##USER: Play 'Piano Man.'",
    "output": "##COMMAND: PLAY SONG PIANO MAN ##RESPONSE: Singing along to 'Piano Man.'"
},
{
    "input": "##USER: Put on 'Shape of My Heart,' please",
    "output": "##COMMAND: PLAY SONG SHAPE OF MY HEART ##RESPONSE: Enjoying 'Shape of My Heart.'"
},
{
    "input": "##USER: I'd like to hear 'Time.'",
    "output": "##COMMAND: PLAY SONG TIME ##RESPONSE: Losing track of time with 'Time.'"
},
{
    "input": "##USER: Play 'Rolling Stone.'",
    "output": "##COMMAND: PLAY SONG ROLLING STONE ##RESPONSE: Listening to 'Rolling Stone.'"
},
{
    "input": "##USER: Put on 'Livin' on a Prayer,' please",
    "output": "##COMMAND: PLAY SONG LIVIN' ON A PRAYER ##RESPONSE: Rocking out to 'Livin' on a Prayer.'"
},
{
    "input": "##USER: I want to hear 'Yellow Submarine.'",
    "output": "##COMMAND: PLAY SONG YELLOW SUBMARINE ##RESPONSE: Sailing away with 'Yellow Submarine.'"
},
{
    "input": "##USER: Play 'Smooth.'",
    "output": "##COMMAND: PLAY SONG SMOOTH ##RESPONSE: Getting into the smooth vibes of 'Smooth.'"
},
{
    "input": "##USER: Put on 'Don't Stop Me Now,' please",
    "output": "##COMMAND: PLAY SONG DON'T STOP ME NOW ##RESPONSE: Getting ready to enjoy 'Don't Stop Me Now.'"
},
{
    "input": "##USER: Could you please turn on the lights Violet in Galley?",
    "output": "##COMMAND: TURN ON LIGHTS Violet Galley ##RESPONSE: Of course! The lights Violet in Galley have been turned on."
},
{
    "input": "##USER: It's a bit dark in Dining Room. Let's turn on the lights Grey.",
    "output": "##COMMAND: TURN ON LIGHTS Grey Dining Room ##RESPONSE: Sure thing! Illuminating Dining Room with Grey lights."
},
{
    "input": "##USER: How about we brighten up Swimming Pool by turning on the Orange lights?",
    "output": "##COMMAND: TURN ON LIGHTS Orange Swimming Pool ##RESPONSE: Certainly! Orange lights are now brightening up Swimming Pool."
},
{
    "input": "##USER: I need some light in Spa. Let's turn on the Grey lights.",
    "output": "##COMMAND: TURN ON LIGHTS Grey Spa ##RESPONSE: Of course! Adding some light to Spa with Grey lights."
},
{
    "input": "##USER: The room is too dim. Let's turn on the lights Lime.",
    "output": "##COMMAND: TURN ON LIGHTS Lime Guest Bedroom 2 ##RESPONSE: Absolutely! Lights Lime are now on in the room."
},
{
    "input": "##USER: Please turn on the Purple lights in Guest Bedroom 2.",
    "output": "##COMMAND: TURN ON LIGHTS Purple Guest Bedroom 2 ##RESPONSE: Certainly! The Purple lights in Guest Bedroom 2 are now turned on."
},
{
    "input": "##USER: It's quite dark in Engine Room. Can we turn on the lights Pink?",
    "output": "##COMMAND: TURN ON LIGHTS Pink Engine Room ##RESPONSE: Of course! Adding some light to Engine Room with Pink lights."
},
{
    "input": "##USER: I'd like to have some light in Salon. Let's turn on the lights Pink.",
    "output": "##COMMAND: TURN ON LIGHTS Pink Salon ##RESPONSE: Sure thing! Lights Pink are now illuminating Salon."
},
{
    "input": "##USER: The lighting in Dining Room is inadequate. Turn on the Orange lights, please.",
    "output": "##COMMAND: TURN ON LIGHTS Green Guest Bedroom 2 ##RESPONSE: Certainly! Turning on the Green lights in Guest Bedroom 2 for better lighting."
},
{
    "input": "##USER: Can you please turn on the Red lights in Lounge?",
    "output": "##COMMAND: TURN ON LIGHTS Red Lounge ##RESPONSE: Of course! The Red lights in Lounge are now on."
},
{
    "input": "##USER: Let's brighten up Cinema with the Berry lights. Turn them on.",
    "output": "##COMMAND: TURN ON LIGHTS Berry Cinema ##RESPONSE: Absolutely! Brightening up Cinema with Berry lights."
},
{
    "input": "##USER: It's too dark in here. Turn on the Straw lights in Dining Room.",
    "output": "##COMMAND: TURN ON LIGHTS Straw Dining Room ##RESPONSE: Sure thing! Turning on the Straw lights in Dining Room for better visibility."
},
{
    "input": "##USER: We need some light in The Bridge. Turn on the lights Turquoise.",
    "output": "##COMMAND: TURN ON LIGHTS Turquoise The Bridge ##RESPONSE: Of course! Adding light to The Bridge with Turquoise lights."
},
{
    "input": "##USER: Please illuminate Bar Lounge with the Yellow lights.",
    "output": "##COMMAND: TURN ON LIGHTS Yellow Bar Lounge ##RESPONSE: Certainly! Yellow lights are now illuminating Bar Lounge."
},
{
    "input": "##USER: I'd like to have the Brown lights turned on in Guest Bedroom 2.",
    "output": "##COMMAND: TURN ON LIGHTS Brown Guest Bedroom 2 ##RESPONSE: The Brown lights in Guest Bedroom 2 are now on."
},
{
    "input": "##USER: Let's improve the lighting in Cabin Suite. Turn on the Coral lights.",
    "output": "##COMMAND: TURN ON LIGHTS Coral Cabin Suite ##RESPONSE: Absolutely! Enhancing the lighting in Cabin Suite with Coral lights."
},
{
    "input": "##USER: The room is too dim for my liking. Can we turn on the Red lights?",
    "output": "##COMMAND: TURN ON LIGHTS Red Swimming Pool ##RESPONSE: Of course! Lights Red are now on to brighten up the room."
},
{
    "input": "##USER: It's a bit gloomy in Guest Bedroom 6. Let's turn on the lights Yellow.",
    "output": "##COMMAND: TURN ON LIGHTS Yellow Guest Bedroom 6 ##RESPONSE: Sure thing! Illuminating Guest Bedroom 6 with Yellow lights."
},
{
    "input": "##USER: How about we add some light to The Bridge by turning on the Navy lights?",
    "output": "##COMMAND: TURN ON LIGHTS Navy The Bridge ##RESPONSE: Certainly! Navy lights are now adding light to The Bridge."
},
{
    "input": "##USER: I need better lighting in Bar Lounge. Turn on the White lights, please.",
    "output": "##COMMAND: TURN ON LIGHTS Turquoise Lounge ##RESPONSE: Absolutely! Turning on the Turquoise lights in Lounge for improved lighting."
},
{
    "input": "##USER: The room feels dark. Let's turn on the Sky lights in Dining Room.",
    "output": "##COMMAND: TURN ON LIGHTS Sky Dining Room ##RESPONSE: Of course! Adding some light to Dining Room with Sky lights."
},
{
    "input": "##USER: I'd like to have the lights Berry in The Bridge turned on, please.",
    "output": "##COMMAND: TURN ON LIGHTS Navy Observation Deck ##RESPONSE: The lights Navy in Observation Deck are now on."
},
{
    "input": "##USER: It's a bit dim in Spa. Can we turn on the Sky lights?",
    "output": "##COMMAND: TURN ON LIGHTS Sky Spa ##RESPONSE: Certainly! Brightening up Spa with Sky lights."
},
{
    "input": "##USER: Please turn on the Yellow lights in Guest Bedroom 2 for me.",
    "output": "##COMMAND: TURN ON LIGHTS Yellow Guest Bedroom 2 ##RESPONSE: Of course! The Yellow lights in Guest Bedroom 2 are now turned on."
},
{
    "input": "##USER: The lighting in Spa is inadequate. Turn on the Navy lights, please.",
    "output": "##COMMAND: TURN ON LIGHTS Coral Library ##RESPONSE: Certainly! Turning on the Coral lights in Library for better lighting."
},
{
    "input": "##USER: Can you please turn on the lights Gold in The Bridge?",
    "output": "##COMMAND: TURN ON LIGHTS Gold The Bridge ##RESPONSE: Certainly! The lights Gold in The Bridge are now on."
},
{
    "input": "##USER: Let's brighten up Salon with the Purple lights. Turn them on.",
    "output": "##COMMAND: TURN ON LIGHTS Purple Salon ##RESPONSE: Absolutely! Brightening up Salon with Purple lights."
},
{
    "input": "##USER: It's too dark in here. Turn on the Straw lights in Lounge, please.",
    "output": "##COMMAND: TURN ON LIGHTS Berry Cinema ##RESPONSE: Sure thing! Turning on the Berry lights in Cinema for better visibility."
},
{
    "input": "##USER: We need some light in Sun Deck. Turn on the Turquoise lights, please.",
    "output": "##COMMAND: TURN ON LIGHTS White Sun Deck ##RESPONSE: Of course! Adding light to Sun Deck with White lights."
},
{
    "input": "##USER: Please illuminate Master Bedroom with the Brown lights.",
    "output": "##COMMAND: TURN ON LIGHTS Brown Master Bedroom ##RESPONSE: Certainly! Brown lights are now illuminating Master Bedroom."
},
{
    "input": "##USER: I'd like to have the Teal lights turned on in Fitness Center.",
    "output": "##COMMAND: TURN ON LIGHTS Teal Fitness Center ##RESPONSE: The Teal lights in Fitness Center are now on."
},
{
    "input": "##USER: Let's improve the lighting in The Bridge. Turn on the Grey lights.",
    "output": "##COMMAND: TURN ON LIGHTS Grey The Bridge ##RESPONSE: Absolutely! Enhancing the lighting in The Bridge with Grey lights."
},
{
    "input": "##USER: The room is too dim for my liking. Can we turn on the Straw lights?",
    "output": "##COMMAND: TURN ON LIGHTS Straw Guest Bedroom 2 ##RESPONSE: Of course! Lights Straw are now on to brighten up the room."
},
{
    "input": "##USER: It's a bit gloomy in Salon. Let's turn on the lights Orange.",
    "output": "##COMMAND: TURN ON LIGHTS Orange Salon ##RESPONSE: Sure thing! Illuminating Salon with Orange lights."
},
{
    "input": "##USER: How about we add some light to Observation Deck by turning on the Teal lights?",
    "output": "##COMMAND: TURN ON LIGHTS Teal Observation Deck ##RESPONSE: Certainly! Teal lights are now adding light to Observation Deck."
},
{
    "input": "##USER: I need better lighting in The Bridge. Turn on the Navy lights, please.",
    "output": "##COMMAND: TURN ON LIGHTS Grey Dining Room ##RESPONSE: Absolutely! Turning on the Grey lights in Dining Room for improved lighting."
},
{
    "input": "##USER: The room feels dark. Let's turn on the Pink lights in Jacuzzi.",
    "output": "##COMMAND: TURN ON LIGHTS Pink Jacuzzi ##RESPONSE: Of course! Adding some light to Jacuzzi with Pink lights."
},
{
    "input": "##USER: I'd like to have the lights Yellow in Dining Room turned on, please.",
    "output": "##COMMAND: TURN ON LIGHTS Lime Salon ##RESPONSE: The lights Lime in Salon are now on."
},
{
    "input": "##USER: It's a bit dim in Library. Can we turn on the Pink lights?",
    "output": "##COMMAND: TURN ON LIGHTS Pink Library ##RESPONSE: Certainly! Brightening up Library with Pink lights."
},
{
    "input": "##USER: I want a cozy atmosphere in Sun Deck.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 204, 153) Sun Deck ##RESPONSE: Creating a warm and cozy ambiance in Sun Deck."
},
{
    "input": "##USER: Let's make Salon feel energizing.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 0, 0) Swimming Pool ##RESPONSE: Energizing Swimming Pool with vibrant lighting."
},
{
    "input": "##USER: I need a calming environment in Sun Deck.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(102, 204, 102) Engine Room ##RESPONSE: Relax and unwind in the soothing atmosphere of Engine Room."
},
{
    "input": "##USER: Make Observation Deck feel invigorating.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(0, 255, 0) Dining Room ##RESPONSE: Energizing Dining Room with refreshing lighting."
},
{
    "input": "##USER: I want Observation Deck to have a tranquil vibe.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(0, 128, 255) Galley ##RESPONSE: Creating a serene and tranquil atmosphere in Galley."
},
{
    "input": "##USER: Let's set a romantic mood in Master Bedroom.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 102, 178) Library ##RESPONSE: Setting a romantic ambiance in Library."
},
{
    "input": "##USER: I need Game Room to feel like a party.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 0, 128) Fitness Center ##RESPONSE: Get ready to dance! Party mode activated in Fitness Center."
},
{
    "input": "##USER: Make Crew Quarters feel like a forest.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(0, 102, 0) Salon ##RESPONSE: Bringing the essence of a forest to Salon."
},
{
    "input": "##USER: I want a futuristic atmosphere in Spa.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(102, 102, 255) Engine Room ##RESPONSE: Welcome to the future! Engine Room is now in a futuristic setting."
},
{
    "input": "##USER: Set a vibrant mood in Guest Bedroom 2.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 128, 0) Dining Room ##RESPONSE: Infusing vibrancy and energy into Dining Room."
},
{
    "input": "##USER: I need Observation Deck to feel like a beach vacation.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 255, 153) Salon ##RESPONSE: Imagine the beach! Salon is now in vacation mode."
},
{
    "input": "##USER: Create a nostalgic ambiance in Library.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(204, 102, 0) The Bridge ##RESPONSE: Taking The Bridge back in time with a nostalgic atmosphere."
},
{
    "input": "##USER: Let's make Sun Deck feel like a sci-fi movie.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(102, 255, 255) Crew Quarters ##RESPONSE: Crew Quarters is now in the world of sci-fi."
},
{
    "input": "##USER: I want a soothing vibe in Library.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(153, 204, 255) Engine Room ##RESPONSE: Creating a gentle and soothing atmosphere in Engine Room."
},
{
    "input": "##USER: Make The Bridge feel like a tropical paradise.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(0, 204, 102) Guest Bedroom 2 ##RESPONSE: Guest Bedroom 2 is now a tropical paradise."
},
{
    "input": "##USER: Set a mysterious mood in Galley.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(128, 0, 128) Spa ##RESPONSE: Spa is now shrouded in mystery."
},
{
    "input": "##USER: I need Galley to feel like a disco.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 0, 255) Cinema ##RESPONSE: Get ready to groove! Cinema is now a disco."
},
{
    "input": "##USER: Create a serene atmosphere in Spa.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(0, 153, 153) Game Room ##RESPONSE: Game Room is now in a state of serene tranquility."
},
{
    "input": "##USER: Let's make Guest Bedroom 2 feel like a space station.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(204, 255, 255) Cinema ##RESPONSE: Cinema is now a space station in a distant galaxy."
},
{
    "input": "##USER: I want Library to feel like a cafe.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(153, 102, 51) Crew Quarters ##RESPONSE: Welcome to the cafe atmosphere in Crew Quarters."
},
{
    "input": "##USER: Create a lively ambiance in Fitness Center.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 153, 51) Dining Room ##RESPONSE: Energizing Dining Room with a lively vibe."
},
{
    "input": "##USER: Make Crew Quarters feel like a rainy day.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(128, 128, 128) Dining Room ##RESPONSE: Dining Room is now immersed in the ambiance of a rainy day."
},
{
    "input": "##USER: Set a modern and minimalist vibe in The Bridge.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(204, 204, 204) Fitness Center ##RESPONSE: Achieving a modern and minimalist aesthetic in Fitness Center."
},
{
    "input": "##USER: I need Sun Deck to feel like a winter wonderland.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(192, 192, 255) Crew Quarters ##RESPONSE: Crew Quarters is now transformed into a winter wonderland."
},
{
    "input": "##USER: Create a magical atmosphere in Game Room.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 204, 255) Swimming Pool ##RESPONSE: Swimming Pool is now enchanted with a magical aura."
},
{
    "input": "##USER: Let's make Sun Deck feel like a library.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(102, 102, 51) Sun Deck ##RESPONSE: Welcome to the library ambiance in Sun Deck."
},
{
    "input": "##USER: I want a retro vibe in Dining Room.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 204, 102) The Bridge ##RESPONSE: Bringing a touch of retro nostalgia to The Bridge."
},
{
    "input": "##USER: Set a futuristic and high-tech mood in Observation Deck.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(51, 51, 255) Game Room ##RESPONSE: Game Room is now immersed in a futuristic and high-tech environment."
},
{
    "input": "##USER: Make Library feel like a summer day.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 255, 51) Jacuzzi ##RESPONSE: Jacuzzi is now basking in the warmth of a summer day."
},
{
    "input": "##USER: Create a romantic and candlelit atmosphere in Jacuzzi.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(255, 153, 153) Bar Lounge ##RESPONSE: Setting a romantic and candlelit mood in Bar Lounge."
},
{
    "input": "##USER: I need Sun Deck to feel like a spaceship.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(51, 255, 51) Game Room ##RESPONSE: Game Room is now the interior of a futuristic spaceship."
},
{
    "input": "##USER: Let's make Lounge feel like a garden.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(102, 204, 102) Engine Room ##RESPONSE: Engine Room is now transformed into a lush garden."
},
{
    "input": "##USER: I want a mystical atmosphere in Fitness Center.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(102, 0, 102) Guest Bedroom 2 ##RESPONSE: Guest Bedroom 2 is now shrouded in mystical vibes."
},
{
    "input": "##USER: Create an industrial and urban ambiance in Guest Bedroom 6.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(102, 102, 102) The Bridge ##RESPONSE: Achieving an industrial and urban aesthetic in The Bridge."
},
{
    "input": "##USER: Make The Bridge feel like a cozy cabin in the woods.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(153, 102, 102) Crew Quarters ##RESPONSE: Crew Quarters is now reminiscent of a cozy cabin in the woods."
},
{
    "input": "##USER: Set a tranquil and lakeside mood in Dining Room.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(51, 153, 204) Engine Room ##RESPONSE: Engine Room is now in a tranquil lakeside setting."
},
{
    "input": "##USER: I need Cinema to feel like a bustling city street.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(204, 51, 51) Library ##RESPONSE: Library now embodies the energy of a bustling city street."
},
{
    "input": "##USER: Create an ethereal and otherworldly atmosphere in Cabin Suite.",
    "output": "##COMMAND: TURN ON LIGHTS rgb(204, 204, 255) Engine Room ##RESPONSE: Engine Room is now bathed in an ethereal and otherworldly glow."
},
{
    "input": "##USER: Can you tell me the weather forecast for 3rd of june in Seychelles?",
    "output": "##COMMAND: GET WEATHER 3rd of june Seychelles"
},
{
    "input": "##USER: Can you tell me the weather forecast for 3rd of june in Seychelles? ##COMMAND: GET WEATHER 3rd of june Seychelles ##SYSTEM: PARTLY CLOUDY 23C CHANCE OF SHOWERS 20%",
    "output": "##RESPONSE: The weather in Seychelles on 3rd of june is expected to be partly cloudy with a high of 23 degrees Celsius. There's a slight chance of showers, with a 20% probability of precipitation."
},
{
    "input": "##USER: What's the weather like in Santorini on 21st of january?",
    "output": "##COMMAND: GET WEATHER 21st of january Santorini"
},
{
    "input": "##USER: What's the weather like in Santorini on 21st of january? ##COMMAND: GET WEATHER 21st of january Santorini ##SYSTEM: CLEAR SKIES 28C UV INDEX HIGH",
    "output": "##RESPONSE: Expect clear skies in Santorini on 21st of january with a high temperature of 28 degrees Celsius. The UV index is high, so make sure to protect your skin from the sun."
},
{
    "input": "##USER: I'm planning an outdoor event on new year's eve. Can you check the weather forecast for Easter Island?",
    "output": "##COMMAND: GET WEATHER new year's eve Easter Island"
},
{
    "input": "##USER: I'm planning an outdoor event on new year's eve. Can you check the weather forecast for Easter Island? ##COMMAND: GET WEATHER new year's eve Easter Island ##SYSTEM: SUNNY 30C NO PRECIPITATION",
    "output": "##RESPONSE: Great news! new year's eve in Easter Island is forecasted to be sunny with a high of 30 degrees Celsius. There's no precipitation expected, so your outdoor event should go smoothly."
},
{
    "input": "##USER: I need to travel on tomorrow. What's the weather forecast for Hawaii?",
    "output": "##COMMAND: GET WEATHER tomorrow Hawaii"
},
{
    "input": "##USER: I need to travel on tomorrow. What's the weather forecast for Hawaii? ##COMMAND: GET WEATHER tomorrow Hawaii ##SYSTEM: OVERCAST 15C RAIN LIKELY 60%",
    "output": "##RESPONSE: On tomorrow, Easter Island is expected to have overcast skies with a high of 15 degrees Celsius. There's a 60% chance of rain, so be prepared for wet conditions during your travel."
},
{
    "input": "##USER: Can you give me the weather information for tonight evening in Easter Island?",
    "output": "##COMMAND: GET WEATHER tonight evening Easter Island"
},
{
    "input": "##USER: Can you give me the weather information for tonight evening in Easter Island? ##COMMAND: GET WEATHER tonight evening Easter Island ##SYSTEM: PARTLY SUNNY 20C WINDS LIGHT",
    "output": "##RESPONSE: Easter Island will experience partly sunny conditions on tonight evening with a high temperature of 20 degrees Celsius. The winds will be light, making it a pleasant day overall."
},
{
    "input": "##USER: I'm curious about the weather in Santorini on 19th of november. Can you provide the forecast?",
    "output": "##COMMAND: GET WEATHER 19th of november Santorini"
},
{
    "input": "##USER: I'm curious about the weather in Santorini on 19th of november. Can you provide the forecast? ##COMMAND: GET WEATHER 19th of november Santorini ##SYSTEM: RAIN SHOWERS 17C THUNDERSTORMS POSSIBLE",
    "output": "##RESPONSE: 19th of november in Santorini is expected to bring rain showers with a high of 17 degrees Celsius. There's a possibility of thunderstorms, so stay safe and dry."
},
{
    "input": "##USER: What's the expected weather for new year's eve in Hawaii?",
    "output": "##COMMAND: GET WEATHER new year's eve Hawaii"
},
{
    "input": "##USER: What's the expected weather for new year's eve in Hawaii? ##COMMAND: GET WEATHER new year's eve Hawaii ##SYSTEM: PARTLY CLOUDY 25C BREEZY CONDITIONS",
    "output": "##RESPONSE: The weather forecast for new year's eve in Hawaii calls for partly cloudy skies and a high temperature of 25 degrees Celsius. Expect breezy conditions throughout the day."
},
{
    "input": "##USER: I'm planning a trip on new year's eve. Can you tell me the weather forecast for Hawaii?",
    "output": "##COMMAND: GET WEATHER new year's eve Hawaii"
},
{
    "input": "##USER: I'm planning a trip on new year's eve. Can you tell me the weather forecast for Hawaii? ##COMMAND: GET WEATHER new year's eve Hawaii ##SYSTEM: MOSTLY CLEAR 22C LOW HUMIDITY",
    "output": "##RESPONSE: Hawaii is expected to have mostly clear skies on new year's eve with a pleasant high of 22 degrees Celsius. The humidity will be low, making it a great day for your trip."
},
{
    "input": "##USER: I need to know the weather in Svalbard on 10th of march. Can you provide the details?",
    "output": "##COMMAND: GET WEATHER 10th of march Svalbard"
},
{
    "input": "##USER: I need to know the weather in Svalbard on 10th of march. Can you provide the details? ##COMMAND: GET WEATHER 10th of march Svalbard ##SYSTEM: FOGGY 12C VISIBILITY LIMITED",
    "output": "##RESPONSE: Expect foggy conditions in Svalbard on 10th of march with a high temperature of 12 degrees Celsius. Visibility will be limited, so exercise caution while traveling."
},
{
    "input": "##USER: What's the weather like in Honolulu on 10th of march? I have outdoor plans.",
    "output": "##COMMAND: GET WEATHER 10th of march Honolulu"
},
{
    "input": "##USER: What's the weather like in Honolulu on 10th of march? I have outdoor plans. ##COMMAND: GET WEATHER 10th of march Honolulu ##SYSTEM: SUNNY 27C UV INDEX VERY HIGH",
    "output": "##RESPONSE: Fantastic! Honolulu is forecasted to have sunny weather on 10th of march with a high temperature of 27 degrees Celsius. The UV index is very high, so remember your sunscreen for your outdoor plans."
},
{
    "input": "##USER: Can you provide the weather forecast for 23rd of july in Machu Picchu?",
    "output": "##COMMAND: GET WEATHER 23rd of july Machu Picchu"
},
{
    "input": "##USER: Can you provide the weather forecast for 23rd of july in Machu Picchu? ##COMMAND: GET WEATHER 23rd of july Machu Picchu ##SYSTEM: PARTLY CLOUDY 19C SLIGHT CHANCE OF RAIN",
    "output": "##RESPONSE: On 23rd of july, Barcelona is expected to have partly cloudy skies with a high of 19 degrees Celsius. There's a slight chance of rain, so be prepared for possible precipitation."
},
{
    "input": "##USER: I'm traveling on 10th of march. Can you check the weather forecast for Bali?",
    "output": "##COMMAND: GET WEATHER 10th of march Bali"
},
{
    "input": "##USER: I'm traveling on 10th of march. Can you check the weather forecast for Bali? ##COMMAND: GET WEATHER 10th of march Bali ##SYSTEM: OVERCAST 14C RAIN SHOWERS LIKELY 70%",
    "output": "##RESPONSE: 10th of march in Bali is anticipated to be overcast with a high temperature of 14 degrees Celsius. There's a 70% likelihood of rain showers, so pack accordingly for your trip."
},
{
    "input": "##USER: What's the weather outlook for 10th of march in Maldives?",
    "output": "##COMMAND: GET WEATHER 10th of march Maldives"
},
{
    "input": "##USER: What's the weather outlook for 10th of march in Maldives? ##COMMAND: GET WEATHER 10th of march Maldives ##SYSTEM: CLEAR SKIES 31C HEAT ADVISORY",
    "output": "##RESPONSE: Prepare for hot weather on 10th of march in Maldives with clear skies and a high of 31 degrees Celsius. A heat advisory is in effect, so stay hydrated and cool."
},
{
    "input": "##USER: I'm curious about the weather in Phuket on new year's eve. Can you provide the forecast?",
    "output": "##COMMAND: GET WEATHER new year's eve Phuket"
},
{
    "input": "##USER: I'm curious about the weather in Phuket on new year's eve. Can you provide the forecast? ##COMMAND: GET WEATHER new year's eve Phuket ##SYSTEM: CLOUDY 21C CHANCE OF SCATTERED SHOWERS 40%",
    "output": "##RESPONSE: Expect cloudy conditions in Phuket on new year's eve with a high of 21 degrees Celsius. There's a 40% chance of scattered showers, so keep an umbrella handy."
},
{
    "input": "##USER: What's the expected weather for christmas day in Barcelona?",
    "output": "##COMMAND: GET WEATHER christmas day Barcelona"
},
{
    "input": "##USER: What's the expected weather for christmas day in Barcelona? ##COMMAND: GET WEATHER christmas day Barcelona ##SYSTEM: PARTLY SUNNY 23C CALM WINDS",
    "output": "##RESPONSE: The weather forecast for christmas day in Barcelona indicates partly sunny skies with a high temperature of 23 degrees Celsius. Winds will be calm, providing a pleasant day."
},
{
    "input": "##USER: I'm planning an outdoor event on 7th of april. Can you check the weather forecast for Cape Town?",
    "output": "##COMMAND: GET WEATHER 7th of april Cape Town"
},
{
    "input": "##USER: I'm planning an outdoor event on 7th of april. Can you check the weather forecast for Cape Town? ##COMMAND: GET WEATHER 7th of april Cape Town ##SYSTEM: PARTLY CLOUDY 26C SLIGHT CHANCE OF SHOWERS 10%",
    "output": "##RESPONSE: Great news! 7th of april in Cape Town is expected to be partly cloudy with a high of 26 degrees Celsius. There's only a slight 10% chance of showers, so your outdoor event should go smoothly."
},
{
    "input": "##USER: Can you give me the weather information for the day after tomorrow in Barcelona?",
    "output": "##COMMAND: GET WEATHER the day after tomorrow Barcelona"
},
{
    "input": "##USER: Can you give me the weather information for the day after tomorrow in Barcelona? ##COMMAND: GET WEATHER the day after tomorrow Barcelona ##SYSTEM: SUNNY 29C UV INDEX VERY HIGH",
    "output": "##RESPONSE: Expect sunny skies in Barcelona on the day after tomorrow with a high temperature of 29 degrees Celsius. The UV index is very high, so make sure to protect your skin from the sun."
},
{
    "input": "##USER: I want Phuket's weather forecast on 12th of february.",
    "output": "##COMMAND: GET WEATHER 12th of february Phuket"
},
{
    "input": "##USER: I want Phuket's weather forecast on 12th of february. ##COMMAND: GET WEATHER 12th of february Phuket ##SYSTEM: CLEAR SKIES 32C NO PRECIPITATION",
    "output": "##RESPONSE: 12th of february in Phuket is expected to have clear skies and a high temperature of 32 degrees Celsius. There's no precipitation expected, making it a beautiful day."
},
{
    "input": "##USER: What's the weather like in Cape Town on the day after tomorrow?",
    "output": "##COMMAND: GET WEATHER the day after tomorrow Cape Town"
},
{
    "input": "##USER: What's the weather like in Cape Town on the day after tomorrow? ##COMMAND: GET WEATHER the day after tomorrow Cape Town ##SYSTEM: OVERCAST 18C RAIN LIKELY 50%",
    "output": "##RESPONSE: On the day after tomorrow, Maui is likely to have overcast skies with a high of 18 degrees Celsius. There's a 50% chance of rain, so be prepared for wet conditions."
},
{
    "input": "##USER: Can you provide the weather forecast for 28th of may in Auckland?",
    "output": "##COMMAND: GET WEATHER 28th of may Auckland"
},
{
    "input": "##USER: Can you provide the weather forecast for 28th of may in Auckland? ##COMMAND: GET WEATHER 28th of may Auckland ##SYSTEM: PARTLY SUNNY 22C BREEZY CONDITIONS",
    "output": "##RESPONSE: The weather forecast for 28th of may in Auckland calls for partly sunny conditions with a high temperature of 22 degrees Celsius. Expect breezy conditions throughout the day."
},
{
    "input": "##USER: I'm planning a trip on tonight evening. Can you tell me the weather forecast for Hong Kong?",
    "output": "##COMMAND: GET WEATHER tonight evening Hong Kong"
},
{
    "input": "##USER: I'm planning a trip on tonight evening. Can you tell me the weather forecast for Hong Kong? ##COMMAND: GET WEATHER tonight evening Hong Kong ##SYSTEM: MOSTLY CLEAR 24C LOW HUMIDITY",
    "output": "##RESPONSE: Hong Kong is expected to have mostly clear skies on tonight evening with a pleasant high of 24 degrees Celsius. The humidity will be low, making it a great day for your trip."
},
{
    "input": "##USER: I need to know the weather in Los Angeles on 17th of october. Can you provide the details?",
    "output": "##COMMAND: GET WEATHER 17th of october Los Angeles"
},
{
    "input": "##USER: I need to know the weather in Los Angeles on 17th of october. Can you provide the details? ##COMMAND: GET WEATHER 17th of october Los Angeles ##SYSTEM: FOGGY 11C VISIBILITY LIMITED",
    "output": "##RESPONSE: Expect foggy conditions in Los Angeles on 17th of october with a high temperature of 11 degrees Celsius. Visibility will be limited, so exercise caution while traveling."
},
{
    "input": "##USER: What's the expected weather for tomorrow in Maui? I have outdoor plans.",
    "output": "##COMMAND: GET WEATHER tomorrow Maui"
},
{
    "input": "##USER: What's the expected weather for tomorrow in Maui? I have outdoor plans. ##COMMAND: GET WEATHER tomorrow Maui ##SYSTEM: SUNNY 26C UV INDEX HIGH",
    "output": "##RESPONSE: Fantastic! Maui is forecasted to have sunny weather on tomorrow with a high temperature of 26 degrees Celsius. The UV index is high, so remember your sunscreen for your outdoor plans."
},
{
    "input": "##USER: Can you provide the weather forecast for 21st of january in Amsterdam?",
    "output": "##COMMAND: GET WEATHER 21st of january Amsterdam"
},
{
    "input": "##USER: Can you provide the weather forecast for 21st of january in Amsterdam? ##COMMAND: GET WEATHER 21st of january Amsterdam ##SYSTEM: PARTLY CLOUDY 20C SLIGHT CHANCE OF RAIN",
    "output": "##RESPONSE: On 21st of january, Easter Island is expected to have partly cloudy skies with a high of 20 degrees Celsius. There's a slight chance of rain, so be prepared for possible precipitation."
},
{
    "input": "##USER: I'm traveling on tonight evening. Can you check the weather forecast for Honolulu?",
    "output": "##COMMAND: GET WEATHER tonight evening Honolulu"
},
{
    "input": "##USER: I'm traveling on tonight evening. Can you check the weather forecast for Honolulu? ##COMMAND: GET WEATHER tonight evening Honolulu ##SYSTEM: OVERCAST 13C RAIN SHOWERS LIKELY 60%",
    "output": "##RESPONSE: tonight evening in Honolulu is anticipated to be overcast with a high temperature of 13 degrees Celsius. There's a 60% likelihood of rain showers, so pack accordingly for your trip."
},
{
    "input": "##USER: What's the weather outlook for 19th of november in Santorini?",
    "output": "##COMMAND: GET WEATHER 19th of november Santorini"
},
{
    "input": "##USER: What's the weather outlook for 19th of november in Santorini? ##COMMAND: GET WEATHER 19th of november Santorini ##SYSTEM: CLEAR SKIES 30C HEAT ADVISORY",
    "output": "##RESPONSE: Prepare for hot weather on 19th of november in Santorini with clear skies and a high of 30 degrees Celsius. A heat advisory is in effect, so stay hydrated and cool."
},
{
    "input": "##USER: I'm curious about the weather in Santorini on 28th of may. Can you provide the forecast?",
    "output": "##COMMAND: GET WEATHER 28th of may Santorini"
},
{
    "input": "##USER: I'm curious about the weather in Santorini on 28th of may. Can you provide the forecast? ##COMMAND: GET WEATHER 28th of may Santorini ##SYSTEM: CLOUDY 19C CHANCE OF SCATTERED SHOWERS 30%",
    "output": "##RESPONSE: Expect cloudy conditions in Santorini on 28th of may with a high of 19 degrees Celsius. There's a 30% chance of scattered showers, so keep an umbrella handy."
},
{
    "input": "##USER: What's the expected weather for tonight evening in Machu Picchu?",
    "output": "##COMMAND: GET WEATHER tonight evening Machu Picchu"
},
{
    "input": "##USER: What's the expected weather for tonight evening in Machu Picchu? ##COMMAND: GET WEATHER tonight evening Machu Picchu ##SYSTEM: PARTLY SUNNY 21C CALM WINDS",
    "output": "##RESPONSE: The weather forecast for tonight evening in Machu Picchu indicates partly sunny skies with a high temperature of 21 degrees Celsius. Winds will be calm, providing a pleasant day."
},
{
    "input": "##USER: I'm planning an outdoor event on 12th of february. Can you check the weather forecast for Barcelona?",
    "output": "##COMMAND: GET WEATHER 12th of february Barcelona"
},
{
    "input": "##USER: I'm planning an outdoor event on 12th of february. Can you check the weather forecast for Barcelona? ##COMMAND: GET WEATHER 12th of february Barcelona ##SYSTEM: PARTLY CLOUDY 25C SLIGHT CHANCE OF SHOWERS 15%",
    "output": "##RESPONSE: Great news! 12th of february in Barcelona is expected to be partly cloudy with a high of 25 degrees Celsius. There's only a slight 15% chance of showers, so your outdoor event should go smoothly."
},
{
    "input": "##USER: Can you give me the weather information for 7th of april in Santorini?",
    "output": "##COMMAND: GET WEATHER 7th of april Santorini"
},
{
    "input": "##USER: Can you give me the weather information for 7th of april in Santorini? ##COMMAND: GET WEATHER 7th of april Santorini ##SYSTEM: SUNNY 28C UV INDEX VERY HIGH",
    "output": "##RESPONSE: Expect sunny skies in Santorini on 7th of april with a high temperature of 28 degrees Celsius. The UV index is very high, so make sure to protect your skin from the sun."
},
{
    "input": "##USER: I want Auckland's weather forecast on 1st of september.",
    "output": "##COMMAND: GET WEATHER 1st of september Auckland"
},
{
    "input": "##USER: I want Auckland's weather forecast on 1st of september. ##COMMAND: GET WEATHER 1st of september Auckland ##SYSTEM: CLEAR SKIES 31C NO PRECIPITATION",
    "output": "##RESPONSE: 1st of september in Auckland is expected to have clear skies and a high temperature of 31 degrees Celsius. There's no precipitation expected, making it a beautiful day."
},
{
    "input": "##USER: What's the weather like in Maldives on new year's eve?",
    "output": "##COMMAND: GET WEATHER new year's eve Maldives"
},
{
    "input": "##USER: What's the weather like in Maldives on new year's eve? ##COMMAND: GET WEATHER new year's eve Maldives ##SYSTEM: OVERCAST 17C RAIN LIKELY 55%",
    "output": "##RESPONSE: On new year's eve, Santorini is likely to have overcast skies with a high of 17 degrees Celsius. There's a 55% chance of rain, so be prepared for wet conditions."
},
{
    "input": "##USER: Can you provide the weather forecast for the day after tomorrow in Prague?",
    "output": "##COMMAND: GET WEATHER the day after tomorrow Prague"
},
{
    "input": "##USER: Can you provide the weather forecast for the day after tomorrow in Prague? ##COMMAND: GET WEATHER the day after tomorrow Prague ##SYSTEM: PARTLY SUNNY 23C BREEZY CONDITIONS",
    "output": "##RESPONSE: The weather forecast for the day after tomorrow in Prague calls for partly sunny conditions with a high temperature of 23 degrees Celsius. Expect breezy conditions throughout the day."
},
{
    "input": "##USER: I'm planning a trip on 10th of march. Can you tell me the weather forecast for Ibiza?",
    "output": "##COMMAND: GET WEATHER 10th of march Ibiza"
},
{
    "input": "##USER: I'm planning a trip on 10th of march. Can you tell me the weather forecast for Ibiza? ##COMMAND: GET WEATHER 10th of march Ibiza ##SYSTEM: MOSTLY CLEAR 22C LOW HUMIDITY",
    "output": "##RESPONSE: Ibiza is expected to have mostly clear skies on 10th of march with a pleasant high of 22 degrees Celsius. The humidity will be low, making it a great day for your trip."
},
{
    "input": "##USER: I need to know the weather in Maui on tomorrow. Can you provide the details?",
    "output": "##COMMAND: GET WEATHER tomorrow Maui"
},
{
    "input": "##USER: I need to know the weather in Maui on tomorrow. Can you provide the details? ##COMMAND: GET WEATHER tomorrow Maui ##SYSTEM: FOGGY 10C VISIBILITY LIMITED",
    "output": "##RESPONSE: Expect foggy conditions in Maui on tomorrow with a high temperature of 10 degrees Celsius. Visibility will be limited, so exercise caution while traveling."
},
{
    "input": "##USER: What's the expected weather for 1st of september in Hawaii? I have outdoor plans.",
    "output": "##COMMAND: GET WEATHER 1st of september Hawaii"
},
{
    "input": "##USER: What's the expected weather for 1st of september in Hawaii? I have outdoor plans. ##COMMAND: GET WEATHER 1st of september Hawaii ##SYSTEM: SUNNY 27C UV INDEX HIGH",
    "output": "##RESPONSE: Fantastic! Hawaii is forecasted to have sunny weather on 1st of september with a high temperature of 27 degrees Celsius. The UV index is high, so remember your sunscreen for your outdoor plans."
},
{
    "input": "##USER: Can you provide the weather forecast for 12th of february in Hong Kong?",
    "output": "##COMMAND: GET WEATHER 12th of february Hong Kong"
},
{
    "input": "##USER: Can you provide the weather forecast for 12th of february in Hong Kong? ##COMMAND: GET WEATHER 12th of february Hong Kong ##SYSTEM: PARTLY CLOUDY 19C SLIGHT CHANCE OF RAIN",
    "output": "##RESPONSE: On 12th of february, Honolulu is expected to have partly cloudy skies with a high of 19 degrees Celsius. There's a slight chance of rain, so be prepared for possible precipitation."
},
{
    "input": "##USER: I'm traveling on christmas day. Can you check the weather forecast for Santorini?",
    "output": "##COMMAND: GET WEATHER christmas day Santorini"
},
{
    "input": "##USER: I'm traveling on christmas day. Can you check the weather forecast for Santorini? ##COMMAND: GET WEATHER christmas day Santorini ##SYSTEM: OVERCAST 12C RAIN SHOWERS LIKELY 65%",
    "output": "##RESPONSE: christmas day in Santorini is anticipated to be overcast with a high temperature of 12 degrees Celsius. There's a 65% likelihood of rain showers, so pack accordingly for your trip."
},
{
    "input": "##USER: What's the weather outlook for christmas day in Seychelles?",
    "output": "##COMMAND: GET WEATHER christmas day Seychelles"
},
{
    "input": "##USER: What's the weather outlook for christmas day in Seychelles? ##COMMAND: GET WEATHER christmas day Seychelles ##SYSTEM: CLEAR SKIES 29C HEAT ADVISORY",
    "output": "##RESPONSE: Prepare for hot weather on christmas day in Seychelles with clear skies and a high of 29 degrees Celsius. A heat advisory is in effect, so stay hydrated and cool."
},
{
    "input": "##USER: I'm curious about the weather in Santorini on new year's eve. Can you provide the forecast?",
    "output": "##COMMAND: GET WEATHER new year's eve Santorini"
},
{
    "input": "##USER: I'm curious about the weather in Santorini on new year's eve. Can you provide the forecast? ##COMMAND: GET WEATHER new year's eve Santorini ##SYSTEM: CLOUDY 20C CHANCE OF SCATTERED SHOWERS 35%",
    "output": "##RESPONSE: Expect cloudy conditions in Santorini on new year's eve with a high of 20 degrees Celsius. There's a 35% chance of scattered showers, so keep an umbrella handy."
},
{
    "input": "##USER: What's the expected weather for 19th of november in Ibiza?",
    "output": "##COMMAND: GET WEATHER 19th of november Ibiza"
},
{
    "input": "##USER: What's the expected weather for 19th of november in Ibiza? ##COMMAND: GET WEATHER 19th of november Ibiza ##SYSTEM: PARTLY SUNNY 24C CALM WINDS",
    "output": "##RESPONSE: The weather forecast for 19th of november in Ibiza indicates partly sunny skies with a high temperature of 24 degrees Celsius. Winds will be calm, providing a pleasant day."
},
{
    "input": "##USER: I'm planning an outdoor event on new year's eve. Can you check the weather forecast for Rome?",
    "output": "##COMMAND: GET WEATHER new year's eve Rome"
},
{
    "input": "##USER: I'm planning an outdoor event on new year's eve. Can you check the weather forecast for Rome? ##COMMAND: GET WEATHER new year's eve Rome ##SYSTEM: PARTLY CLOUDY 24C SLIGHT CHANCE OF SHOWERS 12%",
    "output": "##RESPONSE: Great news! new year's eve in Rome is expected to be partly cloudy with a high of 24 degrees Celsius. There's only a slight 12% chance of showers, so your outdoor event should go smoothly."
},
{
    "input": "##USER: Can you give me the weather information for 23rd of july in Los Angeles?",
    "output": "##COMMAND: GET WEATHER 23rd of july Los Angeles"
},
{
    "input": "##USER: Can you give me the weather information for 23rd of july in Los Angeles? ##COMMAND: GET WEATHER 23rd of july Los Angeles ##SYSTEM: SUNNY 27C UV INDEX VERY HIGH",
    "output": "##RESPONSE: Expect sunny skies in Los Angeles on 23rd of july with a high temperature of 27 degrees Celsius. The UV index is very high, so make sure to protect your skin from the sun."
},
{
    "input": "##USER: I want Easter Island's weather forecast on 17th of october.",
    "output": "##COMMAND: GET WEATHER 17th of october Easter Island"
},
{
    "input": "##USER: I want Easter Island's weather forecast on 17th of october. ##COMMAND: GET WEATHER 17th of october Easter Island ##SYSTEM: CLEAR SKIES 30C NO PRECIPITATION",
    "output": "##RESPONSE: 17th of october in Easter Island is expected to have clear skies and a high temperature of 30 degrees Celsius. There's no precipitation expected, making it a beautiful day."
},
{
    "input": "##USER: What's the weather like in Barcelona on 12th of february?",
    "output": "##COMMAND: GET WEATHER 12th of february Barcelona"
},
{
    "input": "##USER: What's the weather like in Barcelona on 12th of february? ##COMMAND: GET WEATHER 12th of february Barcelona ##SYSTEM: OVERCAST 16C RAIN LIKELY 50%",
    "output": "##RESPONSE: On 12th of february, Svalbard is likely to have overcast skies with a high of 16 degrees Celsius. There's a 50% chance of rain, so be prepared for wet conditions."
},
{
    "input": "##USER: Can you provide the weather forecast for 7th of april in Maldives?",
    "output": "##COMMAND: GET WEATHER 7th of april Maldives"
},
{
    "input": "##USER: Can you provide the weather forecast for 7th of april in Maldives? ##COMMAND: GET WEATHER 7th of april Maldives ##SYSTEM: PARTLY SUNNY 21C BREEZY CONDITIONS",
    "output": "##RESPONSE: The weather forecast for 7th of april in Maldives calls for partly sunny conditions with a high temperature of 21 degrees Celsius. Expect breezy conditions throughout the day."
},
{
    "input": "##USER: I'm planning a trip on 28th of may. Can you tell me the weather forecast for Rome?",
    "output": "##COMMAND: GET WEATHER 28th of may Rome"
},
{
    "input": "##USER: I'm planning a trip on 28th of may. Can you tell me the weather forecast for Rome? ##COMMAND: GET WEATHER 28th of may Rome ##SYSTEM: MOSTLY CLEAR 20C LOW HUMIDITY",
    "output": "##RESPONSE: Rome is expected to have mostly clear skies on 28th of may with a pleasant high of 20 degrees Celsius. The humidity will be low, making it a great day for your trip."
},
{
    "input": "##USER: I need to know the weather in Los Angeles on new year's eve. Can you provide the details?",
    "output": "##COMMAND: GET WEATHER new year's eve Los Angeles"
},
{
    "input": "##USER: I need to know the weather in Los Angeles on new year's eve. Can you provide the details? ##COMMAND: GET WEATHER new year's eve Los Angeles ##SYSTEM: FOGGY 9C VISIBILITY LIMITED",
    "output": "##RESPONSE: Expect foggy conditions in Los Angeles on new year's eve with a high temperature of 9 degrees Celsius. Visibility will be limited, so exercise caution while traveling."
},
{
    "input": "##USER: What's the expected weather for 1st of september in Bora Bora? I have outdoor plans.",
    "output": "##COMMAND: GET WEATHER 1st of september Bora Bora"
},
{
    "input": "##USER: What's the expected weather for 1st of september in Bora Bora? I have outdoor plans. ##COMMAND: GET WEATHER 1st of september Bora Bora ##SYSTEM: SUNNY 26C UV INDEX HIGH",
    "output": "##RESPONSE: Fantastic! Bora Bora is forecasted to have sunny weather on 1st of september with a high temperature of 26 degrees Celsius. The UV index is high, so remember your sunscreen for your outdoor plans."
},
{
    "input": "##USER: Can you provide the weather forecast for 19th of november in Maldives?",
    "output": "##COMMAND: GET WEATHER 19th of november Maldives"
},
{
    "input": "##USER: Can you provide the weather forecast for 19th of november in Maldives? ##COMMAND: GET WEATHER 19th of november Maldives ##SYSTEM: PARTLY CLOUDY 18C SLIGHT CHANCE OF RAIN",
    "output": "##RESPONSE: On 19th of november, Hong Kong is expected to have partly cloudy skies with a high of 18 degrees Celsius. There's a slight chance of rain, so be prepared for possible precipitation."
},
{
    "input": "##USER: I'm traveling on 28th of may. Can you check the weather forecast for Barcelona?",
    "output": "##COMMAND: GET WEATHER 28th of may Barcelona"
},
{
    "input": "##USER: I'm traveling on 28th of may. Can you check the weather forecast for Barcelona? ##COMMAND: GET WEATHER 28th of may Barcelona ##SYSTEM: OVERCAST 11C RAIN SHOWERS LIKELY 60%",
    "output": "##RESPONSE: 28th of may in Barcelona is anticipated to be overcast with a high temperature of 11 degrees Celsius. There's a 60% likelihood of rain showers, so pack accordingly for your trip."
},
{
    "input": "##USER: What's the weather outlook for 7th of april in Maldives?",
    "output": "##COMMAND: GET WEATHER 7th of april Maldives"
},
{
    "input": "##USER: What's the weather outlook for 7th of april in Maldives? ##COMMAND: GET WEATHER 7th of april Maldives ##SYSTEM: CLEAR SKIES 28C HEAT ADVISORY",
    "output": "##RESPONSE: Prepare for hot weather on 7th of april in Maldives with clear skies and a high of 28 degrees Celsius. A heat advisory is in effect, so stay hydrated and cool."
},
{
    "input": "##USER: I'm curious about the weather in Maui on 21st of january. Can you provide the forecast?",
    "output": "##COMMAND: GET WEATHER 21st of january Maui"
},
{
    "input": "##USER: I'm curious about the weather in Maui on 21st of january. Can you provide the forecast? ##COMMAND: GET WEATHER 21st of january Maui ##SYSTEM: CLOUDY 19C CHANCE OF SCATTERED SHOWERS 30%",
    "output": "##RESPONSE: Expect cloudy conditions in Maui on 21st of january with a high of 19 degrees Celsius. There's a 30% chance of scattered showers, so keep an umbrella handy."
},
{
    "input": "##USER: What's the expected weather for 3rd of june in Maui?",
    "output": "##COMMAND: GET WEATHER 3rd of june Maui"
},
{
    "input": "##USER: What's the expected weather for 3rd of june in Maui? ##COMMAND: GET WEATHER 3rd of june Maui ##SYSTEM: PARTLY SUNNY 22C CALM WINDS",
    "output": "##RESPONSE: The weather forecast for 3rd of june in Maui indicates partly sunny skies with a high temperature of 22 degrees Celsius. Winds will be calm, providing a pleasant day."
},
{
    "input": "##USER: Can you give me the weather information for 1st of september?",
    "output": "##COMMAND: GET WEATHER 1st of september $CURRENT_CITY$"
},
{
    "input": "##USER: Can you give me the weather information for 1st of september? ##COMMAND: GET WEATHER 1st of september $CURRENT_CITY$ ##SYSTEM: SUNNY 28C UV INDEX VERY HIGH",
    "output": "##RESPONSE: Expect sunny skies on 1st of september with a high temperature of 28 degrees Celsius. The UV index is very high, so make sure to protect your skin from the sun."
},
{
    "input": "##USER: I want to know the weather forecast for 21st of january.",
    "output": "##COMMAND: GET WEATHER 21st of january $CURRENT_CITY$"
},
{
    "input": "##USER: I want to know the weather forecast for 21st of january. ##COMMAND: GET WEATHER 21st of january $CURRENT_CITY$ ##SYSTEM: CLEAR SKIES 31C NO PRECIPITATION",
    "output": "##RESPONSE: 21st of january is expected to have clear skies with a high temperature of 31 degrees Celsius. There's no precipitation expected, making it a beautiful day."
},
{
    "input": "##USER: What's the weather like on 19th of november?",
    "output": "##COMMAND: GET WEATHER 19th of november $CURRENT_CITY$"
},
{
    "input": "##USER: What's the weather like on 19th of november? ##COMMAND: GET WEATHER 19th of november $CURRENT_CITY$ ##SYSTEM: OVERCAST 17C RAIN LIKELY 50%",
    "output": "##RESPONSE: On 19th of november, the weather is likely to be overcast with a high of 17 degrees Celsius. There's a 50% chance of rain, so be prepared for wet conditions."
},
{
    "input": "##USER: Can you provide the weather forecast for 10th of march?",
    "output": "##COMMAND: GET WEATHER 10th of march $CURRENT_CITY$"
},
{
    "input": "##USER: Can you provide the weather forecast for 10th of march? ##COMMAND: GET WEATHER 10th of march $CURRENT_CITY$ ##SYSTEM: PARTLY SUNNY 21C BREEZY CONDITIONS",
    "output": "##RESPONSE: The weather forecast for 10th of march calls for partly sunny conditions with a high temperature of 21 degrees Celsius. Expect breezy conditions throughout the day."
},
{
    "input": "##USER: I'm planning a trip on 3rd of june. Can you tell me the weather forecast?",
    "output": "##COMMAND: GET WEATHER 3rd of june $CURRENT_CITY$"
},
{
    "input": "##USER: I'm planning a trip on 3rd of june. Can you tell me the weather forecast? ##COMMAND: GET WEATHER 3rd of june $CURRENT_CITY$ ##SYSTEM: MOSTLY CLEAR 20C LOW HUMIDITY",
    "output": "##RESPONSE: 3rd of june is expected to have mostly clear skies with a pleasant high of 20 degrees Celsius. The humidity will be low, making it a great day for your trip."
},
{
    "input": "##USER: I need to know the weather on 7th of april. Can you provide the details?",
    "output": "##COMMAND: GET WEATHER 7th of april $CURRENT_CITY$"
},
{
    "input": "##USER: I need to know the weather on 7th of april. Can you provide the details? ##COMMAND: GET WEATHER 7th of april $CURRENT_CITY$ ##SYSTEM: FOGGY 9C VISIBILITY LIMITED",
    "output": "##RESPONSE: Expect foggy conditions on 7th of april with a high temperature of 9 degrees Celsius. Visibility will be limited, so exercise caution while traveling."
},
{
    "input": "##USER: What's the expected weather for 10th of march? I have outdoor plans.",
    "output": "##COMMAND: GET WEATHER 10th of march $CURRENT_CITY$"
},
{
    "input": "##USER: What's the expected weather for 10th of march? I have outdoor plans. ##COMMAND: GET WEATHER 10th of march $CURRENT_CITY$ ##SYSTEM: SUNNY 26C UV INDEX HIGH",
    "output": "##RESPONSE: Fantastic! 10th of march is forecasted to have sunny weather with a high temperature of 26 degrees Celsius. The UV index is high, so remember your sunscreen for your outdoor plans."
},
{
    "input": "##USER: Can you provide the weather forecast for 21st of january?",
    "output": "##COMMAND: GET WEATHER 21st of january $CURRENT_CITY$"
},
{
    "input": "##USER: Can you provide the weather forecast for 21st of january? ##COMMAND: GET WEATHER 21st of january $CURRENT_CITY$ ##SYSTEM: PARTLY CLOUDY 18C SLIGHT CHANCE OF RAIN",
    "output": "##RESPONSE: On 21st of january, the weather is expected to have partly cloudy skies with a high of 18 degrees Celsius. There's a slight chance of rain, so be prepared for possible precipitation."
},
{
    "input": "##USER: I'm traveling on christmas day. Can you check the weather forecast?",
    "output": "##COMMAND: GET WEATHER christmas day $CURRENT_CITY$"
},
{
    "input": "##USER: I'm traveling on christmas day. Can you check the weather forecast? ##COMMAND: GET WEATHER christmas day $CURRENT_CITY$ ##SYSTEM: OVERCAST 11C RAIN SHOWERS LIKELY 60%",
    "output": "##RESPONSE: christmas day is anticipated to be overcast with a high temperature of 11 degrees Celsius. There's a 60% likelihood of rain showers, so pack accordingly for your trip."
},
{
    "input": "##USER: What's the weather outlook for 19th of november?",
    "output": "##COMMAND: GET WEATHER 19th of november $CURRENT_CITY$"
},
{
    "input": "##USER: What's the weather outlook for 19th of november? ##COMMAND: GET WEATHER 19th of november $CURRENT_CITY$ ##SYSTEM: CLEAR SKIES 28C HEAT ADVISORY",
    "output": "##RESPONSE: Prepare for hot weather on 19th of november with clear skies and a high of 28 degrees Celsius. A heat advisory is in effect, so stay hydrated and cool."
},
{
    "input": "##USER: I'm curious about the weather on the day after tomorrow. Can you provide the forecast?",
    "output": "##COMMAND: GET WEATHER the day after tomorrow $CURRENT_CITY$"
},
{
    "input": "##USER: I'm curious about the weather on the day after tomorrow. Can you provide the forecast? ##COMMAND: GET WEATHER the day after tomorrow $CURRENT_CITY$ ##SYSTEM: CLOUDY 19C CHANCE OF SCATTERED SHOWERS 30%",
    "output": "##RESPONSE: Expect cloudy conditions on the day after tomorrow with a high of 19 degrees Celsius. There's a 30% chance of scattered showers, so keep an umbrella handy."
},
{
    "input": "##USER: What's the expected weather for 21st of january in the cold weather?",
    "output": "##COMMAND: GET WEATHER 21st of january $CURRENT_CITY$"
},
{
    "input": "##USER: What's the expected weather for 21st of january in the cold weather? ##COMMAND: GET WEATHER 21st of january $CURRENT_CITY$ ##SYSTEM: COLD AND OVERCAST -2C CHANCE OF SNOW 40%",
    "output": "##RESPONSE: Prepare for cold and overcast conditions on 21st of january with a high temperature of -2 degrees Celsius. There's a 40% chance of snow, so be cautious while traveling."
},
{
    "input": "##USER: I want to know the cold weather forecast for 12th of february.",
    "output": "##COMMAND: GET WEATHER 12th of february $CURRENT_CITY$"
},
{
    "input": "##USER: I want to know the cold weather forecast for 12th of february. ##COMMAND: GET WEATHER 12th of february $CURRENT_CITY$ ##SYSTEM: FREEZING COLD -5C BLIZZARD CONDITIONS 80% CHANCE OF SNOW",
    "output": "##RESPONSE: 12th of february is expected to be freezing cold with a high temperature of -5 degrees Celsius. Blizzard conditions are likely with an 80% chance of snow, so stay safe and warm."
},
{
    "input": "##USER: What's the cold weather like on 3rd of june?",
    "output": "##COMMAND: GET WEATHER 3rd of june $CURRENT_CITY$"
},
{
    "input": "##USER: What's the cold weather like on 3rd of june? ##COMMAND: GET WEATHER 3rd of june $CURRENT_CITY$ ##SYSTEM: EXTREMELY COLD -10C ICE STORM WARNING 90% CHANCE OF FREEZING RAIN",
    "output": "##RESPONSE: On 3rd of june, the weather will be extremely cold with a high temperature of -10 degrees Celsius. An ice storm warning is in effect with a 90% chance of freezing rain, so take precautions."
},
{
    "input": "##USER: Can you provide the cold weather forecast for 7th of april?",
    "output": "##COMMAND: GET WEATHER 7th of april $CURRENT_CITY$"
},
{
    "input": "##USER: Can you provide the cold weather forecast for 7th of april? ##COMMAND: GET WEATHER 7th of april $CURRENT_CITY$ ##SYSTEM: FRIGID -8C SNOW SHOWERS 60% CHANCE OF BLIZZARD",
    "output": "##RESPONSE: The cold weather forecast for 7th of april calls for frigid conditions with a high temperature of -8 degrees Celsius. Expect snow showers and a 60% chance of a blizzard."
},
{
    "input": "##USER: I'm planning a trip in the cold weather on 28th of may. Can you tell me the weather forecast?",
    "output": "##COMMAND: GET WEATHER 28th of may $CURRENT_CITY$"
},
{
    "input": "##USER: I'm planning a trip in the cold weather on 28th of may. Can you tell me the weather forecast? ##COMMAND: GET WEATHER 28th of may $CURRENT_CITY$ ##SYSTEM: ICY -6C FREEZING FOG ADVISORY 70% CHANCE OF SLEET",
    "output": "##RESPONSE: 28th of may is expected to be icy with a high temperature of -6 degrees Celsius. A freezing fog advisory is in effect with a 70% chance of sleet, so be cautious during your trip."
},
{
    "input": "##USER: I need to know the cold weather on tomorrow. Can you provide the details?",
    "output": "##COMMAND: GET WEATHER tomorrow $CURRENT_CITY$"
},
{
    "input": "##USER: I need to know the cold weather on tomorrow. Can you provide the details? ##COMMAND: GET WEATHER tomorrow $CURRENT_CITY$ ##SYSTEM: SUBZERO -15C SNOWSTORM WARNING 95% CHANCE OF HEAVY SNOW",
    "output": "##RESPONSE: Expect subzero temperatures on tomorrow with a high of -15 degrees Celsius. A snowstorm warning is in effect with a 95% chance of heavy snowfall, so be prepared for challenging conditions."
},
{
    "input": "##USER: What's the expected cold weather for 1st of september? I have outdoor plans.",
    "output": "##COMMAND: GET WEATHER 1st of september $CURRENT_CITY$"
},
{
    "input": "##USER: What's the expected cold weather for 1st of september? I have outdoor plans. ##COMMAND: GET WEATHER 1st of september $CURRENT_CITY$ ##SYSTEM: BITTER COLD -12C WIND CHILL ADVISORY 85% CHANCE OF HAIL",
    "output": "##RESPONSE: 1st of september is forecasted to be bitterly cold with a high temperature of -12 degrees Celsius. A wind chill advisory is in effect with an 85% chance of hail, so dress warmly for your outdoor plans."
},
{
    "input": "##USER: Can you provide the cold weather forecast for 23rd of july?",
    "output": "##COMMAND: GET WEATHER 23rd of july $CURRENT_CITY$"
},
{
    "input": "##USER: Can you provide the cold weather forecast for 23rd of july? ##COMMAND: GET WEATHER 23rd of july $CURRENT_CITY$ ##SYSTEM: FRIGID CONDITIONS -9C LIGHT SNOW 50% CHANCE OF FREEZING DRIZZLE",
    "output": "##RESPONSE: On 23rd of july, expect frigid conditions with a high temperature of -9 degrees Celsius. There's a 50% chance of light snow and freezing drizzle, so take precautions."
},
{
    "input": "##USER: I'm traveling in the cold weather on tonight evening. Can you check the weather forecast?",
    "output": "##COMMAND: GET WEATHER tonight evening $CURRENT_CITY$"
},
{
    "input": "##USER: I'm traveling in the cold weather on tonight evening. Can you check the weather forecast? ##COMMAND: GET WEATHER tonight evening $CURRENT_CITY$ ##SYSTEM: ARCTIC -18C SNOW AND ICE ADVISORY 100% CHANCE OF BLIZZARD",
    "output": "##RESPONSE: tonight evening is anticipated to be arctic with a high temperature of -18 degrees Celsius. A snow and ice advisory is in effect with a 100% chance of a blizzard, so plan your trip carefully."
},
{
    "input": "##USER: What's the cold weather outlook for 28th of may?",
    "output": "##COMMAND: GET WEATHER 28th of may $CURRENT_CITY$"
},
{
    "input": "##USER: What's the cold weather outlook for 28th of may? ##COMMAND: GET WEATHER 28th of may $CURRENT_CITY$ ##SYSTEM: FREEZING TEMPERATURES -7C SLEET SHOWERS 70% CHANCE OF HAILSTORM",
    "output": "##RESPONSE: Prepare for freezing temperatures on 28th of may with a high of -7 degrees Celsius. There's a 70% chance of sleet showers and a hailstorm, so stay safe and warm."
},
{
    "input": "##USER: I'm curious about the cold weather on tonight evening. Can you provide the forecast?",
    "output": "##COMMAND: GET WEATHER tonight evening $CURRENT_CITY$"
},
{
    "input": "##USER: I'm curious about the cold weather on tonight evening. Can you provide the forecast? ##COMMAND: GET WEATHER tonight evening $CURRENT_CITY$ ##SYSTEM: CHILLY -3C SNOW FLURRIES 45% CHANCE OF SNOW SQUALLS",
    "output": "##RESPONSE: Expect chilly conditions on tonight evening with a high temperature of -3 degrees Celsius. There's a 45% chance of snow flurries and snow squalls, so be prepared for wintry weather."
},
{
    "input": "##USER: The night is falling, better turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Understood, I'm turning on the navigation lights for safety."
},
{
    "input": "##USER: It's getting foggy out here. Time to activate the nav lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigational lights activated to guide us through the fog."
},
{
    "input": "##USER: The weather is closing in, let's illuminate those navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigational lights are now on to guide us through adverse conditions."
},
{
    "input": "##USER: I see other vessels approaching. It's time to switch on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigation lights are active to signal our presence to other vessels."
},
{
    "input": "##USER: It's dusk, and the regulations require us to turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: As per regulations, the navigation lights are now on."
},
{
    "input": "##USER: The moon is hidden by clouds. Let's not take any chances, turn on the nav lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Safety first, navigation lights are shining."
},
{
    "input": "##USER: I just heard a foghorn nearby. It's time for the navigation lights to be on.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Responding to the fog signal, navigation lights are now active."
},
{
    "input": "##USER: We're approaching a busy channel. Better turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigation lights are active to signal our position in the busy channel."
},
{
    "input": "##USER: It's a starry night, but we'll still need the navigation lights on for safety.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Even on a starry night, navigation lights are essential for safety."
},
{
    "input": "##USER: The GPS just indicated reduced visibility. Let's switch on the nav lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Reacting to reduced visibility, navigation lights are now on."
},
{
    "input": "##USER: We're entering a congested harbor. Turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigation lights are active for safe harbor entry."
},
{
    "input": "##USER: I can hear the sound of waves crashing. Better activate the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Responding to the sound of waves, navigation lights are illuminated."
},
{
    "input": "##USER: The lighthouse on the shore is visible. It's time to turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Guided by the lighthouse, navigation lights are now active."
},
{
    "input": "##USER: I see a storm approaching. Turn on the navigation lights for added visibility.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Anticipating the storm, navigation lights are switched on."
},
{
    "input": "##USER: There's a lot of traffic in this shipping lane. Turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigation lights are active to navigate safely among other vessels."
},
{
    "input": "##USER: It's getting misty out here. Turn on the navigation lights to be visible.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Responding to reduced visibility, navigation lights are now on."
},
{
    "input": "##USER: The radar is picking up targets. It's time to turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Reacting to radar contacts, navigation lights are illuminated."
},
{
    "input": "##USER: I just heard a distress call on the radio. Turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: In response to the distress call, navigation lights are active for assistance."
},
{
    "input": "##USER: We're nearing the buoy markers. Turn on the navigation lights for safe passage.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigational lights are active for safe passage near buoy markers."
},
{
    "input": "##USER: The wind is picking up, and visibility is decreasing. Turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Responding to reduced visibility, navigation lights are now on."
},
{
    "input": "##USER: It's a moonless night. Turn on the navigation lights to be visible.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: In the absence of moonlight, navigation lights are now shining."
},
{
    "input": "##USER: The rain is pouring, and it's getting dark. Let's activate the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: For enhanced visibility during heavy rain, navigation lights are active."
},
{
    "input": "##USER: The waves are getting rough. Turn on the navigation lights for safety.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: In response to rough sea conditions, navigation lights are illuminated."
},
{
    "input": "##USER: I just spotted a fishing boat ahead. Turn on the navigation lights to avoid a collision.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigational lights are active to prevent a collision with the fishing boat."
},
{
    "input": "##USER: We're approaching a busy port. Time to switch on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigation lights are shining to signal our approach to the busy port."
},
{
    "input": "##USER: The GPS shows us near a rocky coastline. Turn on the navigation lights for safety.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: For safe navigation near the rocky coast, navigation lights are now on."
},
{
    "input": "##USER: We're passing through a narrow channel. Turn on the navigation lights for visibility.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigation lights are active to ensure visibility in the narrow channel."
},
{
    "input": "##USER: The weather forecast predicts heavy fog. It's time to activate the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Preparing for heavy fog, navigation lights are illuminated."
},
{
    "input": "##USER: The marine radio just received a safety message. Turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: In response to the safety message, navigation lights are active for caution."
},
{
    "input": "##USER: We're nearing a busy harbor entrance. Turn on the navigation lights for safe passage.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigational lights are active for a secure entrance to the busy harbor."
},
{
    "input": "##USER: The wind is howling, and visibility is decreasing. It's time to turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Responding to adverse weather, navigation lights are now on."
},
{
    "input": "##USER: I just saw a buoy marker ahead. Turn on the navigation lights to navigate safely.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigational lights are active for safe passage near the buoy marker."
},
{
    "input": "##USER: We're entering a marked shipping lane. Turn on the navigation lights for visibility.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigation lights are shining to navigate safely in the shipping lane."
},
{
    "input": "##USER: The radar shows nearby vessels. It's time to turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Reacting to radar contacts, navigation lights are illuminated."
},
{
    "input": "##USER: I received a marine safety alert. Turn on the navigation lights for caution.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: In response to the safety alert, navigation lights are active for caution."
},
{
    "input": "##USER: We're approaching a critical turning point. Turn on the navigation lights for safety.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Navigational lights are active for safe navigation around the turning point."
},
{
    "input": "##USER: The GPS is indicating reduced visibility. It's time to turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Responding to reduced visibility, navigation lights are now on."
},
{
    "input": "##USER: The wind is gusting, and the sea is rough. Let's activate the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: In response to rough sea conditions, navigation lights are illuminated."
},
{
    "input": "##USER: The lighthouse on the shore is visible. It's time to turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: Guided by the lighthouse, navigation lights are now active."
},
{
    "input": "##USER: The marine radio just received a distress call. Turn on the navigation lights.",
    "output": "##COMMAND: TURN ON NAV LIGHTS ##RESPONSE: In response to the distress call, navigation lights are active for assistance."
},
{
    "input": "##USER: We've safely reached our destination. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off. Thank you for a safe journey."
},
{
    "input": "##USER: The sun is rising, and visibility is good. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With improved visibility, navigation lights are now switched off."
},
{
    "input": "##USER: The moon is shining brightly. Time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With the moonlight guiding us, navigation lights are now off."
},
{
    "input": "##USER: We're entering a well-lit harbor. Turn off the navigation lights for now.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: In a well-lit harbor, navigation lights are now turned off."
},
{
    "input": "##USER: The radar shows no nearby vessels. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With no nearby vessels, navigation lights are now switched off."
},
{
    "input": "##USER: We've exited the busy shipping lane. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off as we leave the shipping lane."
},
{
    "input": "##USER: The weather is clear, and the stars are visible. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With clear skies and starlight, navigation lights are now off."
},
{
    "input": "##USER: The marine radio just received an all-clear signal. Turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: In response to the all-clear signal, navigation lights are now switched off."
},
{
    "input": "##USER: We've passed the rocky coastline safely. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after safely navigating the rocky coastline."
},
{
    "input": "##USER: The GPS shows good visibility. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With good visibility, navigation lights are now switched off."
},
{
    "input": "##USER: We're leaving the congested harbor. Turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off as we exit the congested harbor."
},
{
    "input": "##USER: The wind has calmed, and visibility is excellent. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With calm winds and excellent visibility, navigation lights are now off."
},
{
    "input": "##USER: I see a lighthouse ahead. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Guided by the lighthouse, navigation lights are now switched off."
},
{
    "input": "##USER: We've passed through the narrow channel. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after safely passing through the narrow channel."
},
{
    "input": "##USER: The fog has cleared, and visibility is good. Turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With improved visibility, navigation lights are now switched off."
},
{
    "input": "##USER: The marine radio reports safe conditions. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: In response to the safe conditions, navigation lights are now turned off."
},
{
    "input": "##USER: We've successfully reached the buoy markers. Turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after reaching the buoy markers."
},
{
    "input": "##USER: We've exited the busy port. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now switched off as we leave the busy port."
},
{
    "input": "##USER: The radar shows no contacts. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With no radar contacts, navigation lights are now turned off."
},
{
    "input": "##USER: We've passed the critical turning point safely. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after safely navigating the turning point."
},
{
    "input": "##USER: The sun is high in the sky, and it's a clear day. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With bright sunlight and clear skies, navigation lights are now switched off."
},
{
    "input": "##USER: We're sailing through calm waters. Turn off the navigation lights for now.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: In calm waters, navigation lights are now turned off."
},
{
    "input": "##USER: The moon is setting, and the horizon is visible. Time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: As the moon sets and the horizon is visible, navigation lights are now off."
},
{
    "input": "##USER: We're entering a well-illuminated harbor. Turn off the navigation lights for now.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: In a well-illuminated harbor, navigation lights are now turned off."
},
{
    "input": "##USER: The radar indicates clear waters. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With clear radar readings, navigation lights are now switched off."
},
{
    "input": "##USER: We've exited the busy shipping lane. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off as we leave the shipping lane."
},
{
    "input": "##USER: The weather is stable, and the stars are shining. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With stable weather and starry skies, navigation lights are now off."
},
{
    "input": "##USER: The marine radio reports favorable conditions. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: In response to the favorable conditions, navigation lights are now turned off."
},
{
    "input": "##USER: We've navigated safely past the rocky coastline. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after a safe passage along the rocky coastline."
},
{
    "input": "##USER: The GPS shows excellent visibility. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With excellent GPS visibility, navigation lights are now switched off."
},
{
    "input": "##USER: We're leaving the congested harbor. Turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off as we exit the congested harbor."
},
{
    "input": "##USER: The wind has calmed, and visibility is excellent. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With calm winds and excellent visibility, navigation lights are now off."
},
{
    "input": "##USER: I see a lighthouse ahead. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Guided by the lighthouse, navigation lights are now switched off."
},
{
    "input": "##USER: We've passed through the narrow channel safely. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after safely passing through the narrow channel."
},
{
    "input": "##USER: The fog has cleared, and visibility is good. Turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With improved visibility, navigation lights are now switched off."
},
{
    "input": "##USER: The marine radio reports safe conditions. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: In response to the safe conditions, navigation lights are now turned off."
},
{
    "input": "##USER: We've reached the buoy markers safely. Turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after reaching the buoy markers."
},
{
    "input": "##USER: We've exited the busy port. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now switched off as we leave the busy port."
},
{
    "input": "##USER: The radar shows no contacts. Let's turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: With no radar contacts, navigation lights are now turned off."
},
{
    "input": "##USER: We've passed the critical turning point safely. It's time to turn off the navigation lights.",
    "output": "##COMMAND: TURN OFF NAV LIGHTS ##RESPONSE: Navigation lights are now turned off after a safe passage around the turning point."
},
{
    "input": "##USER: Can you tell me our current speed?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you tell me our current speed? ##COMMAND: GET SPEED ##SYSTEM: 20 KNOTS",
    "output": "##RESPONSE: Our current speed is 20 knots."
},
{
    "input": "##USER: I'd like to know how fast we're moving.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'd like to know how fast we're moving. ##COMMAND: GET SPEED ##SYSTEM: 15 KNOTS",
    "output": "##RESPONSE: We are cruising at a speed of 15 knots."
},
{
    "input": "##USER: What's our speed right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our speed right now? ##COMMAND: GET SPEED ##SYSTEM: 12 KNOTS",
    "output": "##RESPONSE: Our current speed is 12 knots."
},
{
    "input": "##USER: How quickly are we sailing?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quickly are we sailing? ##COMMAND: GET SPEED ##SYSTEM: 18 KNOTS",
    "output": "##RESPONSE: We are sailing at a speed of 18 knots."
},
{
    "input": "##USER: I'm curious about our speed. What is it?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'm curious about our speed. What is it? ##COMMAND: GET SPEED ##SYSTEM: 22 KNOTS",
    "output": "##RESPONSE: Our current speed is 22 knots."
},
{
    "input": "##USER: What's our velocity at the moment?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our velocity at the moment? ##COMMAND: GET SPEED ##SYSTEM: 25 KNOTS",
    "output": "##RESPONSE: Our velocity at the moment is 25 knots."
},
{
    "input": "##USER: I'd like to know our sailing speed.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'd like to know our sailing speed. ##COMMAND: GET SPEED ##SYSTEM: 30 KNOTS",
    "output": "##RESPONSE: We are sailing at a speed of 30 knots."
},
{
    "input": "##USER: How fast are we going on the water?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we going on the water? ##COMMAND: GET SPEED ##SYSTEM: 17 KNOTS",
    "output": "##RESPONSE: We are traveling on the water at a speed of 17 knots."
},
{
    "input": "##USER: What's our current nautical speed?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current nautical speed? ##COMMAND: GET SPEED ##SYSTEM: 19 KNOTS",
    "output": "##RESPONSE: Our current nautical speed is 19 knots."
},
{
    "input": "##USER: How many knots are we sailing at?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How many knots are we sailing at? ##COMMAND: GET SPEED ##SYSTEM: 28 KNOTS",
    "output": "##RESPONSE: We are sailing at a speed of 28 knots."
},
{
    "input": "##USER: Can you tell me our ship's speed?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you tell me our ship's speed? ##COMMAND: GET SPEED ##SYSTEM: 23 KNOTS",
    "output": "##RESPONSE: Our ship's speed is 23 knots."
},
{
    "input": "##USER: What's our velocity in knots?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our velocity in knots? ##COMMAND: GET SPEED ##SYSTEM: 21 KNOTS",
    "output": "##RESPONSE: Our velocity is currently 21 knots."
},
{
    "input": "##USER: I'm interested in our speed. What is it?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'm interested in our speed. What is it? ##COMMAND: GET SPEED ##SYSTEM: 16 KNOTS",
    "output": "##RESPONSE: Our current speed is 16 knots."
},
{
    "input": "##USER: How quick are we sailing on the sea?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quick are we sailing on the sea? ##COMMAND: GET SPEED ##SYSTEM: 24 KNOTS",
    "output": "##RESPONSE: We are sailing at a speed of 24 knots."
},
{
    "input": "##USER: What's our sailing pace?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our sailing pace? ##COMMAND: GET SPEED ##SYSTEM: 26 KNOTS",
    "output": "##RESPONSE: Our current sailing pace is 26 knots."
},
{
    "input": "##USER: Can you inform me of our current knot speed?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you inform me of our current knot speed? ##COMMAND: GET SPEED ##SYSTEM: 14 KNOTS",
    "output": "##RESPONSE: Our current knot speed is 14 knots."
},
{
    "input": "##USER: How many knots are we currently traveling at?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How many knots are we currently traveling at? ##COMMAND: GET SPEED ##SYSTEM: 31 KNOTS",
    "output": "##RESPONSE: We are currently traveling at a speed of 31 knots."
},
{
    "input": "##USER: I'd like to know our nautical speed.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'd like to know our nautical speed. ##COMMAND: GET SPEED ##SYSTEM: 29 KNOTS",
    "output": "##RESPONSE: Our nautical speed is 29 knots."
},
{
    "input": "##USER: What's our speed in nautical terms?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our speed in nautical terms? ##COMMAND: GET SPEED ##SYSTEM: 27 KNOTS",
    "output": "##RESPONSE: Our current speed, in nautical terms, is 27 knots."
},
{
    "input": "##USER: How fast are we moving on the water?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we moving on the water? ##COMMAND: GET SPEED ##SYSTEM: 33 KNOTS",
    "output": "##RESPONSE: We are moving on the water at a speed of 33 knots."
},
{
    "input": "##USER: What's our current velocity?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current velocity? ##COMMAND: GET SPEED ##SYSTEM: 20 KNOTS",
    "output": "##RESPONSE: We are currently cruising at a velocity of 20 knots. Smooth sailing ahead."
},
{
    "input": "##USER: How fast are we moving?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we moving? ##COMMAND: GET SPEED ##SYSTEM: 15 KNOTS",
    "output": "##RESPONSE: We are moving at a speed of 15 knots. A steady pace for a great journey."
},
{
    "input": "##USER: Can you tell me our speed right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you tell me our speed right now? ##COMMAND: GET SPEED ##SYSTEM: 22 KNOTS",
    "output": "##RESPONSE: Our current speed is 22 knots. We're making good progress."
},
{
    "input": "##USER: I'm curious about our speed. What is it?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'm curious about our speed. What is it? ##COMMAND: GET SPEED ##SYSTEM: 18 KNOTS",
    "output": "##RESPONSE: Our speed is currently 18 knots. Enjoy the ride!"
},
{
    "input": "##USER: How quickly are we going?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quickly are we going? ##COMMAND: GET SPEED ##SYSTEM: 25 KNOTS",
    "output": "##RESPONSE: We are moving at a brisk pace of 25 knots. Hold on, it's an exciting ride!"
},
{
    "input": "##USER: What's our velocity right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our velocity right now? ##COMMAND: GET SPEED ##SYSTEM: 30 KNOTS",
    "output": "##RESPONSE: Our current velocity is a swift 30 knots. We're making great time."
},
{
    "input": "##USER: Can you provide our speed?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you provide our speed? ##COMMAND: GET SPEED ##SYSTEM: 17 KNOTS",
    "output": "##RESPONSE: Our speed is currently 17 knots. Enjoy the journey."
},
{
    "input": "##USER: How fast are we traveling?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we traveling? ##COMMAND: GET SPEED ##SYSTEM: 21 KNOTS",
    "output": "##RESPONSE: We are traveling at a speed of 21 knots. Smooth sailing ahead."
},
{
    "input": "##USER: What's our current speed?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current speed? ##COMMAND: GET SPEED ##SYSTEM: 28 KNOTS",
    "output": "##RESPONSE: Our current speed is a swift 28 knots. Hold on, it's a fast ride!"
},
{
    "input": "##USER: Tell me our velocity, please.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Tell me our velocity, please. ##COMMAND: GET SPEED ##SYSTEM: 23 KNOTS",
    "output": "##RESPONSE: Our velocity is currently 23 knots. Enjoy the journey."
},
{
    "input": "##USER: How quick are we moving?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quick are we moving? ##COMMAND: GET SPEED ##SYSTEM: 19 KNOTS",
    "output": "##RESPONSE: We are moving at a speed of 19 knots. A smooth and comfortable journey."
},
{
    "input": "##USER: I'd like to know our speed.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'd like to know our speed. ##COMMAND: GET SPEED ##SYSTEM: 24 KNOTS",
    "output": "##RESPONSE: Our speed is currently 24 knots. We're making good progress."
},
{
    "input": "##USER: How fast are we sailing?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we sailing? ##COMMAND: GET SPEED ##SYSTEM: 16 KNOTS",
    "output": "##RESPONSE: We are sailing at a speed of 16 knots. A steady pace for our voyage."
},
{
    "input": "##USER: What's our current velocity?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current velocity? ##COMMAND: GET SPEED ##SYSTEM: 27 KNOTS",
    "output": "##RESPONSE: Our current velocity is 27 knots. It's a speedy journey!"
},
{
    "input": "##USER: Can you tell me our speed right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you tell me our speed right now? ##COMMAND: GET SPEED ##SYSTEM: 22 KNOTS",
    "output": "##RESPONSE: Our speed is currently 22 knots. Enjoy the ride!"
},
{
    "input": "##USER: I'm curious about our speed. What is it?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'm curious about our speed. What is it? ##COMMAND: GET SPEED ##SYSTEM: 15 KNOTS",
    "output": "##RESPONSE: Our speed is currently 15 knots. Sit back and relax."
},
{
    "input": "##USER: How quickly are we going?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quickly are we going? ##COMMAND: GET SPEED ##SYSTEM: 20 KNOTS",
    "output": "##RESPONSE: We are traveling at a speed of 20 knots. A pleasant journey is ahead."
},
{
    "input": "##USER: What's our velocity right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our velocity right now? ##COMMAND: GET SPEED ##SYSTEM: 26 KNOTS",
    "output": "##RESPONSE: Our current velocity is 26 knots. We're making great time."
},
{
    "input": "##USER: Can you provide our speed?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you provide our speed? ##COMMAND: GET SPEED ##SYSTEM: 18 KNOTS",
    "output": "##RESPONSE: Our speed is currently 18 knots. Enjoy the journey."
},
{
    "input": "##USER: How fast are we traveling?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we traveling? ##COMMAND: GET SPEED ##SYSTEM: 30 KNOTS",
    "output": "##RESPONSE: We are traveling at a speedy 30 knots. Hold on tight, it's an exciting ride!"
},
{
    "input": "##USER: How fast is our vessel moving right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast is our vessel moving right now? ##COMMAND: GET SPEED ##SYSTEM: 25 KNOTS",
    "output": "##RESPONSE: Our vessel is currently moving at a speed of 25 knots. It's a steady pace for our journey."
},
{
    "input": "##USER: I'd like to know our current speed, please.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'd like to know our current speed, please. ##COMMAND: GET SPEED ##SYSTEM: 19 KNOTS",
    "output": "##RESPONSE: Our current speed is 19 knots. Enjoy the voyage!"
},
{
    "input": "##USER: What's our velocity at this moment?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our velocity at this moment? ##COMMAND: GET SPEED ##SYSTEM: 21 KNOTS",
    "output": "##RESPONSE: Our velocity at this moment is 21 knots. Smooth sailing ahead."
},
{
    "input": "##USER: Can you provide our speed right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you provide our speed right now? ##COMMAND: GET SPEED ##SYSTEM: 27 KNOTS",
    "output": "##RESPONSE: Our speed right now is 27 knots. We're making good progress."
},
{
    "input": "##USER: How quickly are we traveling?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quickly are we traveling? ##COMMAND: GET SPEED ##SYSTEM: 16 KNOTS",
    "output": "##RESPONSE: We are traveling at a speed of 16 knots. A comfortable journey awaits."
},
{
    "input": "##USER: What's our current velocity, Captain?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current velocity, Captain? ##COMMAND: GET SPEED ##SYSTEM: 32 KNOTS",
    "output": "##RESPONSE: Our current velocity, Captain, is a brisk 32 knots. We're moving swiftly."
},
{
    "input": "##USER: Tell me our speed, please.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Tell me our speed, please. ##COMMAND: GET SPEED ##SYSTEM: 23 KNOTS",
    "output": "##RESPONSE: Our speed is currently 23 knots. Enjoy the journey."
},
{
    "input": "##USER: How fast are we moving at the moment?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we moving at the moment? ##COMMAND: GET SPEED ##SYSTEM: 18 KNOTS",
    "output": "##RESPONSE: At the moment, we are moving at a speed of 18 knots. Smooth and steady."
},
{
    "input": "##USER: What's our current speed, Captain?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current speed, Captain? ##COMMAND: GET SPEED ##SYSTEM: 14 KNOTS",
    "output": "##RESPONSE: Our current speed, Captain, is 14 knots. A leisurely pace."
},
{
    "input": "##USER: How quick are we going, Captain?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quick are we going, Captain? ##COMMAND: GET SPEED ##SYSTEM: 29 KNOTS",
    "output": "##RESPONSE: We are going at a swift pace of 29 knots, Captain. Hold on tight!"
},
{
    "input": "##USER: How fast is our vessel moving right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast is our vessel moving right now? ##COMMAND: GET SPEED ##SYSTEM: 24 KNOTS",
    "output": "##RESPONSE: Our vessel is currently moving at a speed of 24 knots. Enjoy the ride!"
},
{
    "input": "##USER: I'd like to know our current speed, please.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: I'd like to know our current speed, please. ##COMMAND: GET SPEED ##SYSTEM: 20 KNOTS",
    "output": "##RESPONSE: Our current speed is 20 knots. Sit back and relax."
},
{
    "input": "##USER: What's our velocity at this moment?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our velocity at this moment? ##COMMAND: GET SPEED ##SYSTEM: 28 KNOTS",
    "output": "##RESPONSE: Our velocity at this moment is 28 knots. A fast-paced journey!"
},
{
    "input": "##USER: Can you provide our speed right now?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Can you provide our speed right now? ##COMMAND: GET SPEED ##SYSTEM: 17 KNOTS",
    "output": "##RESPONSE: Our speed right now is 17 knots. A pleasant voyage."
},
{
    "input": "##USER: How quickly are we traveling?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quickly are we traveling? ##COMMAND: GET SPEED ##SYSTEM: 22 KNOTS",
    "output": "##RESPONSE: We are traveling at a speed of 22 knots. A comfortable and swift journey."
},
{
    "input": "##USER: What's our current velocity, Captain?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current velocity, Captain? ##COMMAND: GET SPEED ##SYSTEM: 26 KNOTS",
    "output": "##RESPONSE: Our current velocity, Captain, is 26 knots. Hold on, it's a fast ride!"
},
{
    "input": "##USER: Tell me our speed, please.",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: Tell me our speed, please. ##COMMAND: GET SPEED ##SYSTEM: 15 KNOTS",
    "output": "##RESPONSE: Our speed is currently 15 knots. Enjoy the voyage!"
},
{
    "input": "##USER: How fast are we moving at the moment?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How fast are we moving at the moment? ##COMMAND: GET SPEED ##SYSTEM: 31 KNOTS",
    "output": "##RESPONSE: At the moment, we are moving at a swift 31 knots. It's an exciting journey!"
},
{
    "input": "##USER: What's our current speed, Captain?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: What's our current speed, Captain? ##COMMAND: GET SPEED ##SYSTEM: 19 KNOTS",
    "output": "##RESPONSE: Our current speed, Captain, is 19 knots. A steady and enjoyable pace."
},
{
    "input": "##USER: How quick are we going, Captain?",
    "output": "##COMMAND: GET SPEED"
},
{
    "input": "##USER: How quick are we going, Captain? ##COMMAND: GET SPEED ##SYSTEM: 34 KNOTS",
    "output": "##RESPONSE: We are going at a rapid pace of 34 knots, Captain. It's an adventurous ride!"
},
{
    "input": "##USER: Can you tell me our current course?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you tell me our current course? ##COMMAND: GET COURSE ##SYSTEM: 245 DEGREES",
    "output": "##RESPONSE: Our current course is 245 degrees, taking us in that direction."
},
{
    "input": "##USER: What's our heading right now?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What's our heading right now? ##COMMAND: GET COURSE ##SYSTEM: 315 DEGREES",
    "output": "##RESPONSE: Our current heading is 315 degrees. We're on a clear path."
},
{
    "input": "##USER: What direction are we headed in?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What direction are we headed in? ##COMMAND: GET COURSE ##SYSTEM: 50 DEGREES",
    "output": "##RESPONSE: We are currently headed in the direction of 50 degrees."
},
{
    "input": "##USER: I'm curious about our course. What is it?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: I'm curious about our course. What is it? ##COMMAND: GET COURSE ##SYSTEM: 180 DEGREES",
    "output": "##RESPONSE: Our course is set at 180 degrees, pointing due South."
},
{
    "input": "##USER: How are we currently oriented?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented? ##COMMAND: GET COURSE ##SYSTEM: 270 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 270 degrees, which is due West."
},
{
    "input": "##USER: What's our current course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What's our current course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 60 DEGREES",
    "output": "##RESPONSE: Our current course, Captain, is set at 60 degrees. We're on the right path."
},
{
    "input": "##USER: Can you provide our heading?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you provide our heading? ##COMMAND: GET COURSE ##SYSTEM: 40 DEGREES",
    "output": "##RESPONSE: Our heading is 40 degrees, showing us the way."
},
{
    "input": "##USER: Which way are we pointing?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Which way are we pointing? ##COMMAND: GET COURSE ##SYSTEM: 110 DEGREES",
    "output": "##RESPONSE: We are currently pointing in the direction of 110 degrees."
},
{
    "input": "##USER: How are we currently oriented, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented, Captain? ##COMMAND: GET COURSE ##SYSTEM: 295 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 295 degrees, Captain. It's a steady course."
},
{
    "input": "##USER: What is our course of action, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What is our course of action, Captain? ##COMMAND: GET COURSE ##SYSTEM: 25 DEGREES",
    "output": "##RESPONSE: Our course of action, Captain, is set at 25 degrees. We're navigating smoothly."
},
{
    "input": "##USER: Can you tell me our current course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you tell me our current course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 70 DEGREES",
    "output": "##RESPONSE: Our current course, Captain, is at 70 degrees. We're on the right path."
},
{
    "input": "##USER: How are we currently oriented, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented, Captain? ##COMMAND: GET COURSE ##SYSTEM: 290 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 290 degrees, Captain. Hold steady."
},
{
    "input": "##USER: What's our current heading, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What's our current heading, Captain? ##COMMAND: GET COURSE ##SYSTEM: 90 DEGREES",
    "output": "##RESPONSE: Our current heading, Captain, is 90 degrees. We're headed due East."
},
{
    "input": "##USER: What direction are we headed in, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What direction are we headed in, Captain? ##COMMAND: GET COURSE ##SYSTEM: 180 DEGREES",
    "output": "##RESPONSE: We are currently headed in the direction of 180 degrees, Captain."
},
{
    "input": "##USER: Can you provide our course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you provide our course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 320 DEGREES",
    "output": "##RESPONSE: Our course, Captain, is set at 320 degrees. We're navigating well."
},
{
    "input": "##USER: What is our course of action?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What is our course of action? ##COMMAND: GET COURSE ##SYSTEM: 30 DEGREES",
    "output": "##RESPONSE: Our current course of action is set at 30 degrees. We're on the right track."
},
{
    "input": "##USER: Can you tell me our heading right now?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you tell me our heading right now? ##COMMAND: GET COURSE ##SYSTEM: 220 DEGREES",
    "output": "##RESPONSE: Our heading is 220 degrees, showing us the way."
},
{
    "input": "##USER: How are we currently oriented?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented? ##COMMAND: GET COURSE ##SYSTEM: 275 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 275 degrees. A steady course for our journey."
},
{
    "input": "##USER: What's our current course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What's our current course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 110 DEGREES",
    "output": "##RESPONSE: Our current course, Captain, is set at 110 degrees. We're on the right path."
},
{
    "input": "##USER: Can you provide our heading?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you provide our heading? ##COMMAND: GET COURSE ##SYSTEM: 160 DEGREES",
    "output": "##RESPONSE: Our heading is 160 degrees, showing us the way."
},
{
    "input": "##USER: Which way are we pointing, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Which way are we pointing, Captain? ##COMMAND: GET COURSE ##SYSTEM: 245 DEGREES",
    "output": "##RESPONSE: We are currently pointing in the direction of 245 degrees, Captain."
},
{
    "input": "##USER: How are we currently oriented, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented, Captain? ##COMMAND: GET COURSE ##SYSTEM: 305 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 305 degrees, Captain. Hold steady."
},
{
    "input": "##USER: What is our course of action, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What is our course of action, Captain? ##COMMAND: GET COURSE ##SYSTEM: 45 DEGREES",
    "output": "##RESPONSE: Our course of action, Captain, is set at 45 degrees. We're navigating smoothly."
},
{
    "input": "##USER: Can you tell me our current course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you tell me our current course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 75 DEGREES",
    "output": "##RESPONSE: Our current course, Captain, is at 75 degrees. We're on the right path."
},
{
    "input": "##USER: How are we currently oriented, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented, Captain? ##COMMAND: GET COURSE ##SYSTEM: 310 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 310 degrees, Captain. Hold the course."
},
{
    "input": "##USER: What's our current heading, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What's our current heading, Captain? ##COMMAND: GET COURSE ##SYSTEM: 120 DEGREES",
    "output": "##RESPONSE: Our current heading, Captain, is 120 degrees. We're headed in the right direction."
},
{
    "input": "##USER: What direction are we headed in, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What direction are we headed in, Captain? ##COMMAND: GET COURSE ##SYSTEM: 150 DEGREES",
    "output": "##RESPONSE: We are currently headed in the direction of 150 degrees, Captain."
},
{
    "input": "##USER: Can you provide our course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you provide our course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 65 DEGREES",
    "output": "##RESPONSE: Our course, Captain, is set at 65 degrees. We're navigating well."
},
{
    "input": "##USER: What is our course of action?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What is our course of action? ##COMMAND: GET COURSE ##SYSTEM: 40 DEGREES",
    "output": "##RESPONSE: Our current course of action is set at 40 degrees. We're on the right track."
},
{
    "input": "##USER: Can you tell me our heading right now?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you tell me our heading right now? ##COMMAND: GET COURSE ##SYSTEM: 155 DEGREES",
    "output": "##RESPONSE: Our heading is 155 degrees, showing us the way."
},
{
    "input": "##USER: How are we currently oriented?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented? ##COMMAND: GET COURSE ##SYSTEM: 290 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 290 degrees. A steady course for our journey."
},
{
    "input": "##USER: What's our current course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What's our current course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 100 DEGREES",
    "output": "##RESPONSE: Our current course, Captain, is set at 100 degrees. We're on the right path."
},
{
    "input": "##USER: Can you provide our heading, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you provide our heading, Captain? ##COMMAND: GET COURSE ##SYSTEM: 135 DEGREES",
    "output": "##RESPONSE: Our heading, Captain, is 135 degrees, showing us the way."
},
{
    "input": "##USER: How are we currently oriented, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented, Captain? ##COMMAND: GET COURSE ##SYSTEM: 305 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 305 degrees, Captain. Hold the course."
},
{
    "input": "##USER: What is our course of action, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: What is our course of action, Captain? ##COMMAND: GET COURSE ##SYSTEM: 35 DEGREES",
    "output": "##RESPONSE: Our course of action, Captain, is set at 35 degrees. We're navigating smoothly."
},
{
    "input": "##USER: Can you tell me our current course, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: Can you tell me our current course, Captain? ##COMMAND: GET COURSE ##SYSTEM: 85 DEGREES",
    "output": "##RESPONSE: Our current course, Captain, is at 85 degrees. We're on the right path."
},
{
    "input": "##USER: How are we currently oriented, Captain?",
    "output": "##COMMAND: GET COURSE"
},
{
    "input": "##USER: How are we currently oriented, Captain? ##COMMAND: GET COURSE ##SYSTEM: 310 DEGREES",
    "output": "##RESPONSE: We are currently oriented at 310 degrees, Captain. Hold steady."
},
{
    "input": "##USER: Can you provide an update on our fuel situation?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you provide an update on our fuel situation? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.8 LPNM 800L 1000NM",
    "output": "##RESPONSE: Our fuel consumption is currently around 0.8 liters per nautical mile. We have 800 liters remaining in the tank, which can power us for another 1000 nautical miles."
},
{
    "input": "##USER: What's our current fuel status?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's our current fuel status? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.6 LPNM 950L 1500NM",
    "output": "##RESPONSE: Our current fuel consumption is approximately 0.6 liters per nautical mile. We have a comfortable 950 liters left, which can take us another 1500 nautical miles."
},
{
    "input": "##USER: How are we doing with our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How are we doing with our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 750L 1500NM",
    "output": "##RESPONSE: We are managing our fuel well at a rate of 0.5 liters per nautical mile. There are 750 liters in the tank, giving us a range of 1500 nautical miles."
},
{
    "input": "##USER: Can you update me on our fuel usage?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you update me on our fuel usage? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.9 LPNM 600L 670NM",
    "output": "##RESPONSE: Our current fuel usage is at 0.9 liters per nautical mile. We have 600 liters remaining, allowing us to sail for approximately 670 nautical miles."
},
{
    "input": "##USER: How's our fuel situation, Captain?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How's our fuel situation, Captain? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.7 LPNM 1100L 1600NM",
    "output": "##RESPONSE: Our fuel situation is stable with a consumption rate of 0.7 liters per nautical mile. We have 1100 liters in reserve, which can power us for another 1600 nautical miles."
},
{
    "input": "##USER: What's the status of our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's the status of our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1200L 3000NM",
    "output": "##RESPONSE: Our fuel reserves are excellent, with a consumption rate of 0.4 liters per nautical mile. We have a generous 1200 liters left, providing a range of 3000 nautical miles."
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.6 LPNM 850L 1400NM",
    "output": "##RESPONSE: Our fuel efficiency is good, at 0.6 liters per nautical mile. We have 850 liters remaining, offering a range of 1400 nautical miles."
},
{
    "input": "##USER: Can you give me an update on our fuel consumption?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you give me an update on our fuel consumption? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 1100L 2200NM",
    "output": "##RESPONSE: Our fuel consumption rate is 0.5 liters per nautical mile. We have a substantial 1100 liters left, providing a range of 2200 nautical miles."
},
{
    "input": "##USER: How's our fuel situation, Captain?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How's our fuel situation, Captain? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.8 LPNM 700L 900NM",
    "output": "##RESPONSE: Our fuel situation is a bit tight, with a consumption rate of 0.8 liters per nautical mile. We have 700 liters remaining, offering a range of 900 nautical miles."
},
{
    "input": "##USER: What's the status of our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's the status of our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1300L 3500NM",
    "output": "##RESPONSE: Our fuel reserves are in excellent shape, with a consumption rate of 0.4 liters per nautical mile. We have a generous 1300 liters left, providing a range of 3500 nautical miles."
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.7 LPNM 950L 1350NM",
    "output": "##RESPONSE: Our fuel efficiency is good at 0.7 liters per nautical mile. We have 950 liters remaining, offering a range of 1350 nautical miles."
},
{
    "input": "##USER: Can you give me an update on our fuel consumption?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you give me an update on our fuel consumption? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 1200L 2400NM",
    "output": "##RESPONSE: Our fuel consumption rate is 0.5 liters per nautical mile. We have a substantial 1200 liters left, providing a range of 2400 nautical miles."
},
{
    "input": "##USER: How's our fuel situation, Captain?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How's our fuel situation, Captain? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.9 LPNM 600L 670NM",
    "output": "##RESPONSE: Our fuel situation is a bit challenging, with a consumption rate of 0.9 liters per nautical mile. We have 600 liters remaining, offering a range of approximately 670 nautical miles."
},
{
    "input": "##USER: What's the status of our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's the status of our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1400L 3700NM",
    "output": "##RESPONSE: Our fuel reserves are in great shape, with a consumption rate of 0.4 liters per nautical mile. We have a substantial 1400 liters left, providing a generous range of 3700 nautical miles."
},
{
    "input": "##USER: How are we doing in terms of fuel?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How are we doing in terms of fuel? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.7 LPNM 875L 1250NM",
    "output": "##RESPONSE: We are currently burning roughly 0.7 liters per nautical mile. There is 875 liters left in the tank, allowing us to sail another 1250 nautical miles."
},
{
    "input": "##USER: Can you provide an update on our fuel situation?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you provide an update on our fuel situation? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.8 LPNM 800L 1000NM",
    "output": "##RESPONSE: Our fuel consumption is currently around 0.8 liters per nautical mile. We have 800 liters remaining in the tank, which can power us for another 1000 nautical miles."
},
{
    "input": "##USER: What's our current fuel status?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's our current fuel status? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.6 LPNM 950L 1500NM",
    "output": "##RESPONSE: Our current fuel consumption is approximately 0.6 liters per nautical mile. We have a comfortable 950 liters left, which can take us another 1500 nautical miles."
},
{
    "input": "##USER: How are we doing with our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How are we doing with our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 750L 1500NM",
    "output": "##RESPONSE: We are managing our fuel well at a rate of 0.5 liters per nautical mile. There are 750 liters in the tank, giving us a range of 1500 nautical miles."
},
{
    "input": "##USER: Can you update me on our fuel usage?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you update me on our fuel usage? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.9 LPNM 600L 670NM",
    "output": "##RESPONSE: Our current fuel usage is at 0.9 liters per nautical mile. We have 600 liters remaining, allowing us to sail for approximately 670 nautical miles."
},
{
    "input": "##USER: How's our fuel situation, Captain?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How's our fuel situation, Captain? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.7 LPNM 1100L 1600NM",
    "output": "##RESPONSE: Our fuel situation is stable with a consumption rate of 0.7 liters per nautical mile. We have 1100 liters in reserve, which can power us for another 1600 nautical miles."
},
{
    "input": "##USER: What's the status of our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's the status of our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1200L 3000NM",
    "output": "##RESPONSE: Our fuel reserves are excellent, with a consumption rate of 0.4 liters per nautical mile. We have a generous 1200 liters left, providing a range of 3000 nautical miles."
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.6 LPNM 850L 1400NM",
    "output": "##RESPONSE: Our fuel efficiency is good, at 0.6 liters per nautical mile. We have 850 liters remaining, offering a range of 1400 nautical miles."
},
{
    "input": "##USER: Can you give me an update on our fuel consumption?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you give me an update on our fuel consumption? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 1100L 2200NM",
    "output": "##RESPONSE: Our fuel consumption rate is 0.5 liters per nautical mile. We have a substantial 1100 liters left, providing a range of 2200 nautical miles."
},
{
    "input": "##USER: How's our fuel situation, Captain?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How's our fuel situation, Captain? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.8 LPNM 700L 900NM",
    "output": "##RESPONSE: Our fuel situation is a bit tight, with a consumption rate of 0.8 liters per nautical mile. We have 700 liters remaining, offering a range of 900 nautical miles."
},
{
    "input": "##USER: What's the status of our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's the status of our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1300L 3500NM",
    "output": "##RESPONSE: Our fuel reserves are in excellent shape, with a consumption rate of 0.4 liters per nautical mile. We have a generous 1300 liters left, providing a range of 3500 nautical miles."
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How are we doing in terms of fuel efficiency? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.7 LPNM 950L 1350NM",
    "output": "##RESPONSE: Our fuel efficiency is good at 0.7 liters per nautical mile. We have 950 liters remaining, offering a range of 1350 nautical miles."
},
{
    "input": "##USER: Can you give me an update on our fuel consumption?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Can you give me an update on our fuel consumption? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 1200L 2400NM",
    "output": "##RESPONSE: Our fuel consumption rate is 0.5 liters per nautical mile. We have a substantial 1200 liters left, providing a range of 2400 nautical miles."
},
{
    "input": "##USER: How's our fuel situation, Captain?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: How's our fuel situation, Captain? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.9 LPNM 600L 670NM",
    "output": "##RESPONSE: Our fuel situation is a bit challenging, with a consumption rate of 0.9 liters per nautical mile. We have 600 liters remaining, offering a range of approximately 670 nautical miles."
},
{
    "input": "##USER: What's the status of our fuel reserves?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: What's the status of our fuel reserves? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1400L 3700NM",
    "output": "##RESPONSE: Our fuel reserves are in great shape, with a consumption rate of 0.4 liters per nautical mile. We have a substantial 1400 liters left, providing a generous range of 3700 nautical miles."
},
{
    "input": "##USER: Hey, how's our fuel game, shipmate?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Hey, how's our fuel game, shipmate? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.6 LPNM 950L 1500NM",
    "output": "##RESPONSE: Our fuel game is strong, shipmate! We're cruising at 0.6 liters per nautical mile, and we've got a hearty 950 liters left to power us for another 1500 nautical miles."
},
{
    "input": "##USER: Captain, what's the fuel sitch? Smooth sailing or running low?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Captain, what's the fuel sitch? Smooth sailing or running low? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.8 LPNM 800L 1000NM",
    "output": "##RESPONSE: Captain, our fuel sitch is pretty smooth sailing. We're at 0.8 liters per nautical mile, and we've got a solid 800 liters left to keep us going for another 1000 nautical miles."
},
{
    "input": "##USER: Ahoy there! Tell me, how's our fuel dance looking today?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Ahoy there! Tell me, how's our fuel dance looking today? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.7 LPNM 875L 1250NM",
    "output": "##RESPONSE: Ahoy there! Our fuel dance is on point today. We're grooving at 0.7 liters per nautical mile, and we've got a dance floor-filling 875 liters left, which can take us for another 1250 nautical miles."
},
{
    "input": "##USER: Yo, navigator! What's the word on our fuel vibe, man?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Yo, navigator! What's the word on our fuel vibe, man? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 750L 1500NM",
    "output": "##RESPONSE: Yo, navigator! Our fuel vibe is solid, man. We're flowing at 0.5 liters per nautical mile, and we've got a chill 750 liters left, giving us a mellow 1500 nautical miles ahead."
},
{
    "input": "##USER: Hey, skipper! Fuel check - are we revving high or just coasting?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Hey, skipper! Fuel check - are we revving high or just coasting? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.9 LPNM 600L 670NM",
    "output": "##RESPONSE: Hey, skipper! We're revving a bit high today, but we're coasting fine. Fuel's at 0.9 liters per nautical mile, and we've got 600 liters in the tank, allowing us to coast for around 670 nautical miles."
},
{
    "input": "##USER: Captain, how's our fuel serenade? Smooth jazz or rock 'n' roll?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Captain, how's our fuel serenade? Smooth jazz or rock 'n' roll? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.7 LPNM 1100L 1600NM",
    "output": "##RESPONSE: Captain, our fuel serenade is more like smooth jazz today. We're cruising at 0.7 liters per nautical mile, and we've got a cool 1100 liters left to keep us sailing for another 1600 nautical miles."
},
{
    "input": "##USER: Navigator, what's the rhythm of our fuel groove?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Navigator, what's the rhythm of our fuel groove? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1200L 3000NM",
    "output": "##RESPONSE: Navigator, the rhythm of our fuel groove is steady and strong. We're sipping at 0.4 liters per nautical mile, and we've got a whopping 1200 liters left, allowing us to groove for a cool 3000 nautical miles."
},
{
    "input": "##USER: Smooth sailing or whitecaps, mate? How's our fuel wave today?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Smooth sailing or whitecaps, mate? How's our fuel wave today? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.6 LPNM 850L 1400NM",
    "output": "##RESPONSE: Mate, it's smooth sailing! Our fuel wave is in the groove at 0.6 liters per nautical mile, and we've got a hearty 850 liters left, taking us on a smooth ride for another 1400 nautical miles."
},
{
    "input": "##USER: Captain, give me the lowdown on our fuel jam, is it chill or heating up?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Captain, give me the lowdown on our fuel jam, is it chill or heating up? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.5 LPNM 1100L 2200NM",
    "output": "##RESPONSE: Captain, our fuel jam is chill, no heating up here. We're flowing at 0.5 liters per nautical mile, and we've got a generous 1100 liters left to keep the chill vibes going for another 2200 nautical miles."
},
{
    "input": "##USER: Hey, skipper, are we riding the fuel waves comfortably?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Hey, skipper, are we riding the fuel waves comfortably? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.8 LPNM 700L 900NM",
    "output": "##RESPONSE: Hey, skipper, we're riding the fuel waves comfortably today. We're at 0.8 liters per nautical mile, and we've got 700 liters left, taking us for a smooth 900 nautical miles."
},
{
    "input": "##USER: Captain, how's the fuel symphony sounding today?",
    "output": "##COMMAND: GET FUEL INFO"
},
{
    "input": "##USER: Captain, how's the fuel symphony sounding today? ##COMMAND: GET FUEL INFO ##SYSTEM: 0.4 LPNM 1300L 3500NM",
    "output": "##RESPONSE: Captain, the fuel symphony is sounding incredible today. We're orchestrating it at 0.4 liters per nautical mile, and we've got a grand 1300 liters left to fuel our voyage for a spectacular 3500 nautical miles."
},
{
    "input": "##USER: Hey there, navigator! What's our final stop?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Hey there, navigator! What's our final stop? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Sydney 309 NM left 11h22min 650 range",
    "output": "##RESPONSE: Hey there, navigator! Our final stop is Sydney. We've got 309 nautical miles left, which should take us about 11 hours and 22 minutes at our current speed. Our range is 650 nautical miles, so we're good to go."
},
{
    "input": "##USER: Captain, can you tell me our destination?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, can you tell me our destination? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Bali 173 NM left 6h15min 395 range",
    "output": "##RESPONSE: Captain, our destination is Bali. We have 173 nautical miles left, approximately 6 hours and 15 minutes at our current pace. Our range is 395 nautical miles, so we're well-equipped for the journey."
},
{
    "input": "##USER: Navigator, where's the wind taking us?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, where's the wind taking us? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Miami 112 NM left 4h5min 260 range",
    "output": "##RESPONSE: Navigator, the wind is taking us to Miami. We've got 112 nautical miles to go, which should take around 4 hours and 5 minutes at our current pace. Our range is 260 nautical miles, so we're in good shape."
},
{
    "input": "##USER: Ahoy, matey! Where be our treasure?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Ahoy, matey! Where be our treasure? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Nassau 81 NM left 3h30min 215 range",
    "output": "##RESPONSE: Ahoy, matey! Our treasure awaits in Nassau. There are 81 nautical miles left, approximately 3 hours and 30 minutes at our current pace. Our range is 215 nautical miles, so we'll reach our bounty with ease."
},
{
    "input": "##USER: Captain, where are we headed?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, where are we headed? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Rio de Janeiro 228 NM left 8h10min 480 range",
    "output": "##RESPONSE: Captain, we're headed to Rio de Janeiro. There are 228 nautical miles left, which should take us about 8 hours and 10 minutes at our current speed. Our range is 480 nautical miles, so we're in no danger of running aground."
},
{
    "input": "##USER: Navigator, what's our final destination?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, what's our final destination? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Santorini 62 NM left 2h20min 170 range",
    "output": "##RESPONSE: Navigator, our final destination is Santorini. We've got just 62 nautical miles left, or about 2 hours and 20 minutes at our current pace. Our range is 170 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Hey there, where's our journey taking us?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Hey there, where's our journey taking us? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Cape Town 150 NM left 5h45min 320 range",
    "output": "##RESPONSE: Hey there, our journey is taking us to Cape Town. There are 150 nautical miles left, which should take about 5 hours and 45 minutes at our current pace. Our range is 320 nautical miles, so we're well-prepared."
},
{
    "input": "##USER: Captain, what's our ultimate destination?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, what's our ultimate destination? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Phuket 91 NM left 3h15min 210 range",
    "output": "##RESPONSE: Captain, our ultimate destination is Phuket. There are 91 nautical miles left, approximately 3 hours and 15 minutes at our current speed. Our range is 210 nautical miles, so we're good to go."
},
{
    "input": "##USER: Navigator, where are we setting our course?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, where are we setting our course? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Venice 53 NM left 1h50min 135 range",
    "output": "##RESPONSE: Navigator, we're setting our course for Venice. There are just 53 nautical miles left, or about 1 hour and 50 minutes at our current pace. Our range is 135 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Ahoy, matey! What be our final port of call?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Ahoy, matey! What be our final port of call? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Monaco 69 NM left 2h5min 170 range",
    "output": "##RESPONSE: Ahoy, matey! Our final port of call be Monaco. There be 69 nautical miles left, takin' us 'bout 2 hours and 5 minutes at our current speed. Our range be 170 nautical miles, so we're in fine shape."
},
{
    "input": "##USER: Captain, where's our destination, mate?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, where's our destination, mate? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Mykonos 45 NM left 1h35min 115 range",
    "output": "##RESPONSE: Captain, our destination, mate, be Mykonos. There be 45 nautical miles left, 'bout 1 hour and 35 minutes at our current pace. Our range be 115 nautical miles, so we're sailin' smooth."
},
{
    "input": "##USER: Navigator, what's the word on our final stop?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, what's the word on our final stop? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Key West 78 NM left 2h50min 185 range",
    "output": "##RESPONSE: Navigator, the word on our final stop be Key West. There be 78 nautical miles left, 'bout 2 hours and 50 minutes at our current speed. Our range be 185 nautical miles, so we're in the clear."
},
{
    "input": "##USER: Hey there, navigator! What's our final stop?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Hey there, navigator! What's our final stop? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Santorini 62 NM left 2h20min 170 range",
    "output": "##RESPONSE: Hey there, navigator! Our final stop is Santorini. We've got just 62 nautical miles left, or about 2 hours and 20 minutes at our current pace. Our range is 170 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Captain, what's our ultimate destination?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, what's our ultimate destination? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Phuket 91 NM left 3h15min 210 range",
    "output": "##RESPONSE: Captain, our ultimate destination is Phuket. There are 91 nautical miles left, approximately 3 hours and 15 minutes at our current speed. Our range is 210 nautical miles, so we're good to go."
},
{
    "input": "##USER: Navigator, where are we setting our course?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, where are we setting our course? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Venice 53 NM left 1h50min 135 range",
    "output": "##RESPONSE: Navigator, we're setting our course for Venice. There are just 53 nautical miles left, or about 1 hour and 50 minutes at our current pace. Our range is 135 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Ahoy, matey! What be our final port of call?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Ahoy, matey! What be our final port of call? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Monaco 69 NM left 2h5min 170 range",
    "output": "##RESPONSE: Ahoy, matey! Our final port of call be Monaco. There be 69 nautical miles left, takin' us 'bout 2 hours and 5 minutes at our current speed. Our range be 170 nautical miles, so we're in fine shape."
},
{
    "input": "##USER: Captain, where's our destination, mate?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, where's our destination, mate? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Mykonos 45 NM left 1h35min 115 range",
    "output": "##RESPONSE: Captain, our destination, mate, be Mykonos. There be 45 nautical miles left, 'bout 1 hour and 35 minutes at our current pace. Our range be 115 nautical miles, so we're sailin' smooth."
},
{
    "input": "##USER: Navigator, what's the word on our final stop?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, what's the word on our final stop? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Key West 78 NM left 2h50min 185 range",
    "output": "##RESPONSE: Navigator, the word on our final stop be Key West. There be 78 nautical miles left, 'bout 2 hours and 50 minutes at our current speed. Our range be 185 nautical miles, so we're in the clear."
},
{
    "input": "##USER: Where are we headed?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Where are we headed? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Barcelona 210 NM left 7 hours 430 range",
    "output": "##RESPONSE: We're headed to Barcelona, my friend. There are 210 nautical miles left, which should take us approximately 7 hours at our current speed. Our range is 430 nautical miles, so we're well-prepared for the journey."
},
{
    "input": "##USER: Captain, can you provide information on our destination?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, can you provide information on our destination? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Honolulu 290 NM left 10 hours 600 range",
    "output": "##RESPONSE: Certainly, our destination is Honolulu. There are 290 nautical miles left, which translates to roughly 10 hours at our current pace. Our range is 600 nautical miles, so we have a comfortable margin."
},
{
    "input": "##USER: Navigator, what's the destination for this voyage?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, what's the destination for this voyage? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Auckland 140 NM left 5 hours 300 range",
    "output": "##RESPONSE: The destination for this voyage is Auckland. We have 140 nautical miles left, which should take about 5 hours at our current pace. Our range is 300 nautical miles, so we're in good shape."
},
{
    "input": "##USER: Ahoy, where's our final port of call?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Ahoy, where's our final port of call? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Seychelles 75 NM left 2 hours 180 range",
    "output": "##RESPONSE: Ahoy, our final port of call is Seychelles. There are just 75 nautical miles left, or about 2 hours at our current pace. Our range is 180 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Captain, can you tell me our ultimate destination?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, can you tell me our ultimate destination? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Maldives 60 NM left 1 hour 140 range",
    "output": "##RESPONSE: Certainly, our ultimate destination is the Maldives. We have 60 nautical miles left, which is approximately 1 hour at our current speed. Our range is 140 nautical miles, so we're in good shape."
},
{
    "input": "##USER: Navigator, where are we setting our course?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, where are we setting our course? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Dubrovnik 50 NM left 1 hour 120 range",
    "output": "##RESPONSE: Navigator, we're setting our course for Dubrovnik. There are just 50 nautical miles left, or about 1 hour at our current pace. Our range is 120 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Hey there, where's our journey taking us?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Hey there, where's our journey taking us? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Lisbon 120 NM left 4 hours 260 range",
    "output": "##RESPONSE: Hey there, our journey is taking us to Lisbon. There are 120 nautical miles left, which should take about 4 hours at our current pace. Our range is 260 nautical miles, so we're well-prepared."
},
{
    "input": "##USER: Captain, what's our final stop?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, what's our final stop? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Venice 40 NM left 1 hour 90 range",
    "output": "##RESPONSE: Captain, our final stop is Venice. There are just 40 nautical miles left, which should take about 1 hour at our current pace. Our range is 90 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Navigator, what's the word on our final destination?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, what's the word on our final destination? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Bali 70 NM left 2 hours 160 range",
    "output": "##RESPONSE: Navigator, the word on our final destination is Bali. There are 70 nautical miles left, which should take about 2 hours at our current pace. Our range is 160 nautical miles, so we're in good shape."
},
{
    "input": "##USER: Ahoy, where be our final port of call?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Ahoy, where be our final port of call? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Monaco 85 NM left 3 hours 200 range",
    "output": "##RESPONSE: Ahoy, where be our final port of call? It's Monaco. We've got 85 nautical miles left, which should take about 3 hours at our current pace. Our range is 200 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Captain, what's our destination, mate?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Captain, what's our destination, mate? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Mykonos 45 NM left 1 hour 115 range",
    "output": "##RESPONSE: Captain, our destination, mate, is Mykonos. We've got 45 nautical miles left, which should take about 1 hour at our current pace. Our range is 115 nautical miles, so we're sailing smoothly."
},
{
    "input": "##USER: Navigator, what's the scoop on our final stop?",
    "output": "##COMMAND: GET DESTINATION INFO"
},
{
    "input": "##USER: Navigator, what's the scoop on our final stop? ##COMMAND: GET DESTINATION INFO ##SYSTEM: Key West 75 NM left 2 hours 180 range",
    "output": "##RESPONSE: Navigator, the scoop on our final stop is Key West. There are 75 nautical miles left, which should take about 2 hours at our current pace. Our range is 180 nautical miles, so we're in good shape"
},
{
    "input": "##USER: Hey, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 07:30 9 October Sydney 130 NM left 4h15min 150 NM range; partly cloudy 16C wind SE 20kph; 215 degrees 18 knots",
    "output": "##RESPONSE: Good morning, ready for a great day? It's the 9th of October, and the time is 07:30. We're currently sailing towards Sydney, with 130 nautical miles left, which should take about 4 hours and 15 minutes at our current speed of 18 knots. Our range is 150 nautical miles, so no worries about refueling. The weather is partly cloudy with a high of 16 degrees Celsius, and we have a southeast wind at 20kph. Our current course is 215 degrees, taking us due south."
},
{
    "input": "##USER: Navigator, what's the status today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the status today? ##COMMAND: GOOD MORNING ##SYSTEM: 08:15 2 April Barcelona 90 NM left 2h30min 120 NM range; clear skies 19C wind SW 12kph; 220 degrees 14 knots",
    "output": "##RESPONSE: Good morning, navigator. Rise and shine! It's the 2nd of April, and the time is 08:15. We're on our way to Barcelona, with just 90 nautical miles left, which should take about 2 hours and 30 minutes at our current speed of 14 knots. Our range is 120 nautical miles, so no need to refuel just yet. The weather is beautiful with clear skies and a high of 19 degrees Celsius, and we have a gentle southwest wind at 12kph. Our current course is 220 degrees, steering us due southwest."
},
{
    "input": "##USER: Captain, what's the word for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the word for today? ##COMMAND: GOOD MORNING ##SYSTEM: 09:00 15 July Bali 75 NM left 2h45min 90 NM range; scattered clouds 28C wind NW 25kph; 235 degrees 20 knots",
    "output": "##RESPONSE: Good morning, captain. Ready to sail? It's the 15th of July, and the time is 09:00. We're heading to Bali, and there are 75 nautical miles left, which should take about 2 hours and 45 minutes at our current speed of 20 knots. Our range is 90 nautical miles, so we're good on fuel. The sky has scattered clouds today, and the temperature will reach a warm 28 degrees Celsius. The wind is blowing from the northwest at 25kph, and our current course is 235 degrees, taking us due southwest."
},
{
    "input": "##USER: Ahoy, matey! What's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Ahoy, matey! What's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 10:30 25 November Monaco 45 NM left 1h30min 60 NM range; sunny 22C wind E 15kph; 250 degrees 12 knots",
    "output": "##RESPONSE: Ahoy, matey! Ready for another adventure? It's the 25th of November, and the time is 10:30. Our destination is Monaco, and we've got just 45 nautical miles left, which should take about 1 hour and 30 minutes at our current speed of 12 knots. Our range is 60 nautical miles, so no refueling needed. Today is sunny with a pleasant high of 22 degrees Celsius, and the wind is blowing from the east at 15kph. Our current course is 250 degrees, taking us due west."
},
{
    "input": "##USER: Captain, what's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 11:15 10 August Mykonos 30 NM left 1 hour 35 NM range; clear skies 30C wind SE 10kph; 260 degrees 8 knots",
    "output": "##RESPONSE: Good morning, captain. Ready to set sail? It's the 10th of August, and the time is 11:15. Our ultimate destination is Mykonos, and we've got just 30 nautical miles left, which should take about 1 hour at our current speed of 8 knots. Our range is 35 nautical miles, so no need to refuel just yet. The skies are clear today, and the temperature will soar to 30 degrees Celsius. The wind is blowing gently from the southeast at 10kph. Our current course is 260 degrees, steering us due west."
},
{
    "input": "##USER: Navigator, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 12:00 3 May Key West 40 NM left 1h30min 50 NM range; partly cloudy 27C wind S 18kph; 270 degrees 15 knots",
    "output": "##RESPONSE: Good morning, navigator. Ready to chart our course? It's the 3rd of May, and the time is 12:00. We're making our way to Key West, and we've got 40 nautical miles left, which should take about 1 hour and 30 minutes at our current speed of 15 knots. Our range is 50 nautical miles, so no need to refuel just yet. The skies are partly cloudy today, with a high of 27 degrees Celsius. The wind is blowing from the south at 18kph, and our current course is 270 degrees, taking us due west."
},
{
    "input": "##USER: Hey there, what's the status for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey there, what's the status for today? ##COMMAND: GOOD MORNING ##SYSTEM: 13:30 20 September Santorini 20 NM left 45min 30 NM range; clear skies 25C wind N 14kph; 280 degrees 10 knots",
    "output": "##RESPONSE: Hey there, ready for the day's journey? It's the 20th of September, and the time is 13:30. Our destination is Santorini, and we're down to just 20 nautical miles left, which should take about 45 minutes at our current speed of 10 knots. Our range is 30 nautical miles, so we're good on fuel. The skies are clear today, with a high of 25 degrees Celsius. The wind is blowing from the north at 14kph, and our current course is 280 degrees, taking us due west."
},
{
    "input": "##USER: Captain, what's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 14:15 5 March Cape Town 25 NM left 1 hour 35min 40 NM range; sunny 24C wind W 22kph; 290 degrees 18 knots",
    "output": "##RESPONSE: Good morning, captain. Ready to set sail? It's the 5th of March, and the time is 14:15. Our ultimate destination is Cape Town, and we've got just 25 nautical miles left, which should take about 1 hour at our current speed of 18 knots. Our range is 40 nautical miles, so no need to refuel just yet. The weather is sunny today, with a high of 24 degrees Celsius. The wind is blowing from the west at 22kph, and our current course is 290 degrees, steering us due west."
},
{
    "input": "##USER: Navigator, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 15:00 15 April Fiji 15 NM left 30min 20 NM range; scattered clouds 31C wind NE 12kph; 300 degrees 6 knots",
    "output": "##RESPONSE: Good morning, navigator. Ready to chart our course? It's the 15th of April, and the time is 15:00. We're making our way to Fiji, and we've got just 15 nautical miles left, which should take about 30 minutes at our current speed of 6 knots. Our range is 20 nautical miles, so no need to refuel just yet. The skies have scattered clouds today, with a high of 31 degrees Celsius. The wind is blowing gently from the northeast at 12kph, and our current course is 300 degrees, taking us due west."
},
{
    "input": "##USER: Hey there, what's the status for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey there, what's the status for today? ##COMMAND: GOOD MORNING ##SYSTEM: 16:30 25 June Phuket 10 NM left 15min 15 NM range; clear skies 35C wind S 8kph; 310 degrees 4 knots",
    "output": "##RESPONSE: Hey there, ready for the day's journey? It's the 25th of June, and the time is 16:30. Our destination is Phuket, and we're down to just 10 nautical miles left, which should take about 15 minutes at our current speed of 4 knots. Our range is 15 nautical miles, so we're good on fuel. The skies are clear today, with a high of 35 degrees Celsius. The wind is blowing from the south at 8kph, and our current course is 310 degrees, taking us due west."
},
{
    "input": "##USER: Captain, what's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 17:15 10 August Venice 5 NM left 10min 5 NM range; clear skies 25C wind SE 6kph; 320 degrees 2 knots",
    "output": "##RESPONSE: Good morning, captain. Ready to set sail? It's the 10th of August, and the time is 17:15. Our ultimate destination is Venice, and we've got just 5 nautical miles left, which should take about 10 minutes at our current speed of 2 knots. Our range is 5 nautical miles, so no need to refuel just yet. The weather is sunny today, with a high of 25 degrees Celsius. The wind is blowing gently from the southeast at 6kph, and our current course is 320 degrees, steering us due west."
},
{
    "input": "##USER: Navigator, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 18:00 3 December Seychelles 2 NM left 5min 2 NM range; clear skies 29C wind N 4kph; 330 degrees 1 knot",
    "output": "##RESPONSE: Good morning, navigator. Ready to chart our course? It's the 3rd of December, and the time is 18:00. We're making our way to Seychelles, and we've got just 2 nautical miles left, which should take about 5 minutes at our current speed of 1 knot. Our range is 2 nautical miles, so no need to refuel just yet. The skies are clear today, with a high of 29 degrees Celsius. The wind is barely blowing from the north at 4kph, and our current course is 330 degrees, taking us due west."
},
{
    "input": "##USER: Hey there, what's the status for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey there, what's the status for today? ##COMMAND: GOOD MORNING ##SYSTEM: 08:30 15 May Key Largo 55 NM left 2h15min 70 NM range; sunny 28C wind E 15kph; 340 degrees 14 knots",
    "output": "##RESPONSE: Hey there, ready for the day's journey? It's the 15th of May, and the time is 08:30. Our destination is Key Largo, and there are 55 nautical miles left, which should take about 2 hours and 15 minutes at our current speed of 14 knots. Our range is 70 nautical miles, so no need to refuel just yet. Today is sunny with a high of 28 degrees Celsius, and the wind is blowing from the east at 15kph. Our current course is 340 degrees, taking us due northwest."
},
{
    "input": "##USER: Captain, what's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 09:15 20 November Cannes 20 NM left 45min 30 NM range; clear skies 25C wind NE 12kph; 350 degrees 10 knots",
    "output": "##RESPONSE: Good morning, captain. Ready to set sail? It's the 20th of November, and the time is 09:15. Our ultimate destination is Cannes, and we've got just 20 nautical miles left, which should take about 45 minutes at our current speed of 10 knots. Our range is 30 nautical miles, so no need to refuel just yet. The weather is sunny today, with a high of 25 degrees Celsius. The wind is blowing from the northeast at 12kph, and our current course is 350 degrees, steering us due north."
},
{
    "input": "##USER: Navigator, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 10:00 10 July Ibiza 25 NM left 1 hour 40min 40 NM range; partly cloudy 22C wind NW 18kph; 0 degrees 16 knots",
    "output": "##RESPONSE: Good morning, navigator. Ready to chart our course? It's the 10th of July, and the time is 10:00. We're making our way to Ibiza, and we've got just 25 nautical miles left, which should take about 1 hour and 40 minutes at our current speed of 16 knots. Our range is 40 nautical miles, so no need to refuel just yet. The skies are partly cloudy today, with a high of 22 degrees Celsius. The wind is blowing from the northwest at 18kph, and our current course is due north."
},
{
    "input": "##USER: Hey there, what's the status for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey there, what's the status for today? ##COMMAND: GOOD MORNING ##SYSTEM: 11:30 5 January Santorini 30 NM left 1h10min 50 NM range; clear skies 18C wind S 14kph; 10 degrees 12 knots",
    "output": "##RESPONSE: Hey there, ready for the day's journey? It's the 5th of January, and the time is 11:30. Our destination is Santorini, and there are 30 nautical miles left, which should take about 1 hour and 10 minutes at our current speed of 12 knots. Our range is 50 nautical miles, so no need to refuel just yet. The skies are clear today, with a high of 18 degrees Celsius. The wind is blowing from the south at 14kph, and our current course is 10 degrees, taking us due north."
},
{
    "input": "##USER: Captain, what's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 12:15 20 March Bali 15 NM left 30min 20 NM range; scattered clouds 30C wind SW 10kph; 20 degrees 8 knots",
    "output": "##RESPONSE: Good morning, captain. Ready to set sail? It's the 20th of March, and the time is 12:15. Our ultimate destination is Bali, and we've got just 15 nautical miles left, which should take about 30 minutes at our current speed of 8 knots. Our range is 20 nautical miles, so no need to refuel just yet. The skies have scattered clouds today, with a high of 30 degrees Celsius. The wind is blowing from the southwest at 10kph, and our current course is 20 degrees, taking us due north."
},
{
    "input": "##USER: Navigator, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 13:00 15 September Mykonos 10 NM left 15min 15 NM range; clear skies 28C wind SE 6kph; 30 degrees 4 knots",
    "output": "##RESPONSE: Good morning, navigator. Ready to chart our course? It's the 15th of September, and the time is 13:00. We're making our way to Mykonos, and we've got just 10 nautical miles left, which should take about 15 minutes at our current speed of 4 knots. Our range is 15 nautical miles, so no need to refuel just yet. The skies are clear today, with a high of 28 degrees Celsius. The wind is blowing from the southeast at 6kph, and our current course is 30 degrees, taking us due north."
},
{
    "input": "##USER: Hey there, what's the status for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey there, what's the status for today? ##COMMAND: GOOD MORNING ##SYSTEM: 14:30 10 May Key West 5 NM left 10min 5 NM range; clear skies 27C wind S 8kph; 40 degrees 2 knots",
    "output": "##RESPONSE: Hey there, ready for the day's journey? It's the 10th of May, and the time is 14:30. Our destination is Key West, and we're down to just 5 nautical miles left, which should take about 10 minutes at our current speed of 2 knots. Our range is 5 nautical miles, so we're good on fuel. The skies are clear today, with a high of 27 degrees Celsius. The wind is blowing from the south at 8kph, and our current course is 40 degrees, taking us due north."
},
{
    "input": "##USER: Captain, what's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 15:15 5 June Venice 2 NM left 5min 3 NM range; sunny 26C wind E 4kph; 50 degrees 2 knots",
    "output": "##RESPONSE: Good afternoon, captain. Ready to set sail? It's the 5th of June, and the time is 15:15. Our ultimate destination is Venice, and we've got just 2 nautical miles left, which should take about 5 minutes at our current speed of 2 knots. Our range is 3 nautical miles, so no need to refuel just yet. The weather is sunny today, with a high of 26 degrees Celsius. The wind is blowing from the east at 4kph, and our current course is 50 degrees, taking us due north."
},
{
    "input": "##USER: Navigator, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 16:00 20 August Seychelles 1 NM left 2min 2 NM range; clear skies 30C wind SE 2kph; 60 degrees 1 knot",
    "output": "##RESPONSE: Good afternoon, navigator. Ready to chart our course? It's the 20th of August, and the time is 16:00. We're making our way to Seychelles, and we've got just 1 nautical mile left, which should take about 2 minutes at our current speed of 1 knot. Our range is 2 nautical miles, so no need to refuel just yet. The skies are clear today, with a high of 30 degrees Celsius. The wind is barely blowing from the southeast at 2kph, and our current course is 60 degrees, taking us due north."
},
{
    "input": "##USER: Hey there, what's the status for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey there, what's the status for today? ##COMMAND: GOOD MORNING ##SYSTEM: 17:30 10 November Cannes 4 NM left 8min 6 NM range; clear skies 22C wind NW 6kph; 70 degrees 3 knots",
    "output": "##RESPONSE: Hey there, ready for the day's journey? It's the 10th of November, and the time is 17:30. Our destination is Cannes, and there are 4 nautical miles left, which should take about 8 minutes at our current speed of 3 knots. Our range is 6 nautical miles, so we're good on fuel. The skies are clear today, with a high of 22 degrees Celsius. The wind is blowing from the northwest at 6kph, and our current course is 70 degrees, taking us due north."
},
{
    "input": "##USER: Captain, what's the plan for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Captain, what's the plan for today? ##COMMAND: GOOD MORNING ##SYSTEM: 18:15 5 April Ibiza 8 NM left 16min 10 NM range; partly cloudy 20C wind N 8kph; 80 degrees 4 knots",
    "output": "##RESPONSE: Good evening, captain. Ready to set sail? It's the 5th of April, and the time is 18:15. Our ultimate destination is Ibiza, and we've got just 8 nautical miles left, which should take about 16 minutes at our current speed of 4 knots. Our range is 10 nautical miles, so no need to refuel just yet. The skies are partly cloudy today, with a high of 20 degrees Celsius. The wind is blowing from the north at 8kph, and our current course is 80 degrees, taking us due east."
},
{
    "input": "##USER: Navigator, what's the scoop for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Navigator, what's the scoop for today? ##COMMAND: GOOD MORNING ##SYSTEM: 19:00 15 June Mykonos 3 NM left 6min 5 NM range; clear skies 28C wind NE 4kph; 90 degrees 2 knots",
    "output": "##RESPONSE: Good evening, navigator. Ready to chart our course? It's the 15th of June, and the time is 19:00. We're making our way to Mykonos, and we've got just 3 nautical miles left, which should take about 6 minutes at our current speed of 2 knots. Our range is 5 nautical miles, so no need to refuel just yet. The skies are clear today, with a high of 28 degrees Celsius. The wind is blowing gently from the northeast at 4kph, and our current course is 90 degrees, taking us due east."
},
{
    "input": "##USER: Hey there, what's the status for today?",
    "output": "##COMMAND: GOOD MORNING"
},
{
    "input": "##USER: Hey there, what's the status for today? ##COMMAND: GOOD MORNING ##SYSTEM: 20:30 10 October Key West 6 NM left 12min 8 NM range; clear skies 24C wind S 6kph; 100 degrees 3 knots",
    "output": "##RESPONSE: Hey there, ready for the day's journey? It's the 10th of October, and the time is 20:30. Our destination is Key West, and there are 6 nautical miles left, which should take about 12 minutes at our current speed of 3 knots. Our range is 8 nautical miles, so we're good on fuel. The skies are clear today, with a high of 24 degrees Celsius. The wind is blowing from the south at 6kph, and our current course is 100 degrees, taking us due east."
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All systems go. Fuel 975/1000L, destination Bali, ETA 9h15m,",
    "output": "##RESPONSE: Aye, aye, captain! All systems are functioning perfectly, and our fuel tank is at 975 liters out of 1000. Our destination is Bali, and we should arrive there in approximately 9 hours and 15 minutes."
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Navigation system error. Fuel 650/800L, destination Venice, ETA 7h30m,",
    "output": "##RESPONSE: Aye, aye, navigator! The navigation system is currently experiencing an error, and it should be addressed before we depart. Our fuel tank is at 650 liters out of 800, and our destination is Venice. We should arrive there in approximately 7 hours and 30 minutes once the issue is resolved."
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Engine temperature warning. Fuel 1100/1200L, destination Tenerife, ETA 10h20m,",
    "output": "##RESPONSE: Aye, aye, captain! There's an engine temperature warning, so it's vital to investigate and address this before we set sail. Our fuel tank is at 1100 liters out of 1200, and our destination is Tenerife. We should reach there in approximately 10 hours and 20 minutes once the engine issue is resolved."
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Weather radar malfunction. Fuel 600/750L, destination Santorini, ETA 6h45m,",
    "output": "##RESPONSE: Aye, aye, navigator! The weather radar is currently malfunctioning, and it should be fixed before we depart. Our fuel tank is at 600 liters out of 750, and our destination is Santorini. We should reach there in approximately 6 hours and 45 minutes once the radar is operational."
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail?",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail? ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All clear. Fuel 850/900L, destination Mykonos, ETA 7h10m,",
    "output": "##RESPONSE: Aye, aye, captain! Everything is in order. Our fuel tank is at 850 liters out of 900, and our destination is Mykonos. We should reach there in approximately 7 hours and 10 minutes."
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: GPS signal lost. Fuel 700/800L, destination Fiji, ETA 8h35m,",
    "output": "##RESPONSE: Aye, aye, navigator! The GPS signal is currently lost, and it should be restored before we depart. Our fuel tank is at 700 liters out of 800, and our destination is Fiji. We should reach there in approximately 8 hours and 35 minutes once the GPS is operational."
},
{
    "input": "##USER: Captain, are we ready to set sail? Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, are we ready to set sail? Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Sonar system malfunction. Fuel 950/1000L, destination Cape Town, ETA 9h55m,",
    "output": "##RESPONSE: Aye, aye, captain! The sonar system is currently experiencing a malfunction, and it should be repaired before we depart. Our fuel tank is at 950 liters out of 1000, and our destination is Cape Town. We should reach there in approximately 9 hours and 55 minutes once the sonar is functioning correctly."
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything thoroughly.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything thoroughly. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Radar system failure. Fuel 550/600L, destination Monaco, ETA 5h40m,",
    "output": "##RESPONSE: Aye, aye, navigator! The radar system has failed, and it should be repaired before we set sail. Our fuel tank is at 550 liters out of 600, and our destination is Monaco. We should reach there in approximately 5 hours and 40 minutes once the radar is operational."
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All systems go. Fuel 800/850L, destination Cannes, ETA 7h25m,",
    "output": "##RESPONSE: Aye, aye, captain! All systems are functioning perfectly, and our fuel tank is at 800 liters out of 850. Our destination is Cannes, and we should arrive there in approximately 7 hours and 25 minutes."
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Navigation system error. Fuel 480/600L, destination Ibiza, ETA 4h55m,",
    "output": "##RESPONSE: Aye, aye, navigator! The navigation system is currently experiencing an error, and it should be addressed before we depart. Our fuel tank is at 480 liters out of 600, and our destination is Ibiza. We should arrive there in approximately 4 hours and 55 minutes once the issue is resolved."
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Engine temperature warning. Fuel 900/950L, destination Key West, ETA 8h05m,",
    "output": "##RESPONSE: Aye, aye, captain! There's an engine temperature warning, so it's vital to investigate and address this before we set sail. Our fuel tank is at 900 liters out of 950, and our destination is Key West. We should reach there in approximately 8 hours and 5 minutes once the engine issue is resolved."
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Weather radar malfunction. Fuel 420/500L, destination Seychelles, ETA 4h40m,",
    "output": "##RESPONSE: Aye, aye, navigator! The weather radar is currently malfunctioning, and it should be fixed before we depart. Our fuel tank is at 420 liters out of 500, and our destination is Seychelles. We should arrive there in approximately 4 hours and 40 minutes once the radar is operational."
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail?",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail? ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All clear. Fuel 720/750L, destination Phuket, ETA 6h30m,",
    "output": "##RESPONSE: Aye, aye, captain! Everything is in order. Our fuel tank is at 720 liters out of 750, and our destination is Phuket. We should reach there in approximately 6 hours and 30 minutes."
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: GPS signal lost. Fuel 380/450L, destination Venice, ETA 3h50m,",
    "output": "##RESPONSE: Aye, aye, navigator! The GPS signal is currently lost, and it should be restored before we depart. Our fuel tank is at 380 liters out of 450, and our destination is Venice. We should arrive there in approximately 3 hours and 50 minutes once the GPS is operational."
},
{
    "input": "##USER: Captain, are we ready to set sail? Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, are we ready to set sail? Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Sonar system malfunction. Fuel 650/700L, destination Tenerife, ETA 5h10m,",
    "output": "##RESPONSE: Aye, aye, captain! The sonar system is currently experiencing a malfunction, and it should be repaired before we depart. Our fuel tank is at 650 liters out of 700, and our destination is Tenerife. We should reach there in approximately 5 hours and 10 minutes once the sonar is functioning correctly."
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything thoroughly.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything thoroughly. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Radar system failure. Fuel 330/400L, destination Santorini, ETA 3h25m,",
    "output": "##RESPONSE: Aye, aye, navigator! The radar system has failed, and it should be repaired before we set sail. Our fuel tank is at 330 liters out of 400, and our destination is Santorini. We should arrive there in approximately 3 hours and 25 minutes once the radar is operational."
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All systems go. Fuel 760/800L, destination Mykonos, ETA 6h45m,",
    "output": "##RESPONSE: Aye, aye, captain! All systems are functioning perfectly, and our fuel tank is at 760 liters out of 800. Our destination is Mykonos, and we should arrive there in approximately 6 hours and 45 minutes."
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Navigation system error. Fuel 420/500L, destination Fiji, ETA 4h30m,",
    "output": "##RESPONSE: Aye, aye, navigator! The navigation system is currently experiencing an error, and it should be addressed before we depart. Our fuel tank is at 420 liters out of 500, and our destination is Fiji. We should arrive there in approximately 4 hours and 30 minutes once the issue is resolved."
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Engine temperature warning. Fuel 890/900L, destination Cape Town, ETA 7h15m,",
    "output": "##RESPONSE: Aye, aye, captain! There's an engine temperature warning, so it's vital to investigate and address this before we set sail. Our fuel tank is at 890 liters out of 900, and our destination is Cape Town. We should reach there in approximately 7 hours and 15 minutes once the engine issue is resolved."
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Weather radar malfunction. Fuel 480/550L, destination Monaco, ETA 5h10m,",
    "output": "##RESPONSE: Aye, aye, navigator! The weather radar is currently malfunctioning, and it should be fixed before we depart. Our fuel tank is at 480 liters out of 550, and our destination is Monaco. We should arrive there in approximately 5 hours and 10 minutes once the radar is operational."
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail?",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail? ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All clear. Fuel 660/700L, destination Cannes, ETA 6h30m,",
    "output": "##RESPONSE: Aye, aye, captain! Everything is in order. Our fuel tank is at 660 liters out of 700, and our destination is Cannes. We should reach there in approximately 6 hours and 30 minutes."
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: GPS signal lost. Fuel 360/400L, destination Ibiza, ETA 3h55m,",
    "output": "##RESPONSE: Aye, aye, navigator! The GPS signal is currently lost, and it should be restored before we depart. Our fuel tank is at 360 liters out of 400, and our destination is Ibiza. We should arrive there in approximately 3 hours and 55 minutes once the GPS is operational."
},
{
    "input": "##USER: Captain, are we ready to set sail? Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, are we ready to set sail? Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Sonar system malfunction. Fuel 620/650L, destination Key West, ETA 5h25m,",
    "output": "##RESPONSE: Aye, aye, captain! The sonar system is currently experiencing a malfunction, and it should be repaired before we depart. Our fuel tank is at 620 liters out of 650, and our destination is Key West. We should reach there in approximately 5 hours and 25 minutes once the sonar is functioning correctly."
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything thoroughly.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything thoroughly. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Radar system failure. Fuel 300/350L, destination Seychelles, ETA 3h15m,",
    "output": "##RESPONSE: Aye, aye, navigator! The radar system has failed, and it should be repaired before we set sail. Our fuel tank is at 300 liters out of 350, and our destination is Seychelles. We should arrive there in approximately 3 hours and 15 minutes once the radar is operational."
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to set sail. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All systems go. Fuel 720/750L, destination Phuket, ETA 6h10m,",
    "output": "##RESPONSE: Aye, aye, captain! All systems are functioning perfectly, and our fuel tank is at 720 liters out of 750. Our destination is Phuket, and we should arrive there in approximately 6 hours and 10 minutes."
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, it's time to prepare for departure. Check everything. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Navigation system error. Fuel 380/450L, destination Venice, ETA 3h45m,",
    "output": "##RESPONSE: Aye, aye, navigator! The navigation system is currently experiencing an error, and it should be addressed before we depart. Our fuel tank is at 380 liters out of 450, and our destination is Venice. We should arrive there in approximately 3 hours and 45 minutes once the issue is resolved."
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, we're ready to embark on our journey. Prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Engine temperature warning. Fuel 870/900L, destination Tenerife, ETA 7h05m,",
    "output": "##RESPONSE: Aye, aye, captain! There's an engine temperature warning, so it's vital to investigate and address this before we set sail. Our fuel tank is at 870 liters out of 900, and our destination is Tenerife. We should reach there in approximately 7 hours and 5 minutes once the engine issue is resolved."
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, prepare for departure. We're ready to head out. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: Weather radar malfunction. Fuel 450/500L, destination Santorini, ETA 4h40m,",
    "output": "##RESPONSE: Aye, aye, navigator! The weather radar is currently malfunctioning, and it should be fixed before we depart. Our fuel tank is at 450 liters out of 500, and our destination is Santorini. We should arrive there in approximately 4 hours and 40 minutes once the radar is operational."
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail?",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Captain, it's time to prepare for departure. Are we ready to set sail? ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: All clear. Fuel 650/700L, destination Mykonos, ETA 6h25m,",
    "output": "##RESPONSE: Aye, aye, captain! Everything is in order. Our fuel tank is at 650 liters out of 700, and our destination is Mykonos. We should reach there in approximately 6 hours and 25 minutes."
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure.",
    "output": "##COMMAND: PREPARE FOR DEPARTURE"
},
{
    "input": "##USER: Navigator, get everything ready. It's time to prepare for departure. ##COMMAND: PREPARE FOR DEPARTURE ##SYSTEM: GPS signal lost. Fuel 350/400L, destination Fiji, ETA 3h45m,",
    "output": "##RESPONSE: Aye, aye, navigator! The GPS signal is currently lost, and it should be restored before we depart. Our fuel tank is at 350 liters out of 400, and our destination is Fiji. We should arrive there in approximately 3 hours and 45 minutes once the GPS is operational."
},
]

# Calculate the number of values to select (0.15 of the total)
num_to_select = int(len(data) * 0.15)

# Randomly shuffle the data
random.shuffle(data)

# Select the first 'num_to_select' values
selected_data = data[:num_to_select]

# Save the selected data to a JSON file
with open('output_valid.json', 'w') as selected_file:
    json.dump(selected_data, selected_file, indent=4)

# Save the remaining data to a JSON file
remaining_data = data[num_to_select:]
with open('output_train.json', 'w') as remaining_file:
    json.dump(remaining_data, remaining_file, indent=4)
