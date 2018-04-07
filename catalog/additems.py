from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///catalogueitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Dummy user

user1 = User(name="Nana Nemo",
             email="nana.nemo@gmail.com",
             picture="https://cdn.pixabay.com/photo/2015/04/18/11/03/profile-728591_1280.jpg")
session.add(user1)
session.commit()

# Insert categories
session.query(Category).delete()
session.query(Item).delete()

category1 = Category(name='Action & Adventure', user=user1)
session.add(category1)
session.commit()

category2 = Category(name='Animation', user=user1)
session.add(category2)
session.commit()

category3 = Category(name='Classics', user=user1)
session.add(category3)
session.commit()

category4 = Category(name='Comedy', user=user1)
session.add(category4)
session.commit()

category5 = Category(name='Horror', user=user1)
session.add(category5)
session.commit()

category6 = Category(name='Musical', user=user1)
session.add(category6)
session.commit()

category7 = Category(name='Science Fiction & Fantasy', user=user1)
session.add(category7)
session.commit()


item1 = Item(name="Mad Max: Fury Road",
             description="Filmmaker George Miller gears up for another post-apocalyptic action adventure with Fury Road, the fourth outing in the Mad Max film series. Charlize Theron stars alongside Tom Hardy (Bronson), with Zoe Kravitz, Adelaide Clemens, and Rosie Huntington Whiteley heading up the supporting cast. ~ Jeremy Wheeler, Rovi",
             category=category1,
             user=user1)
session.add(item1)
session.commit()

# Dummy items

item2 = Item(name="Inside Out",
             description="Growing up can be a bumpy road, and it's no exception for Riley, who is uprooted from her Midwest life when her father starts a new job in San Francisco. Like all of us, Riley is guided by her emotions - Joy (Amy Poehler), Fear (Bill Hader), Anger (Lewis Black), Disgust (Mindy Kaling) and Sadness (Phyllis Smith). The emotions live in Headquarters, the control center inside Riley's mind, where they help advise her through everyday life. As Riley and her emotions struggle to adjust to a new life in San Francisco, turmoil ensues in Headquarters. Although Joy, Riley's main and most important emotion, tries to keep things positive, the emotions conflict on how best to navigate a new city, house and school. -- (C) Pixar",
             category=category2,
             user=user1)
session.add(item2)
session.commit()

item3 = Item(name="Up",
             description="A feisty septuagenarian teams with a fearless wilderness ranger to do battle with a vicious band of beasts and villains in this computer-animated adventure scripted by Pixar veteran Bob Peterson and co-directed by Peterson and Monsters, Inc. director Peter Docter. Carl Fredricksen is a 78-year-old balloon salesman. His entire life, Carl has longed to wander the wilds of South America. Then, one day, the irascible senior citizen shocks his neighbors by tying thousands of balloons to his home and finally taking flight. But Carl isn't alone on his once-in-a-lifetime journey, because stowed away on his front porch is an excitable eight-year-old wilderness explorer named Russell. Later, as the house touches down on the world's second largest continent, Carl and his unlikely traveling companion step outside to discover that not only is their new front lawn considerably larger, but that the predators therein are much more ferocious than anything they ever faced back home.",
             category=category2,
             user=user1)
session.add(item3)
session.commit()

item4 = Item(name="Citizen Kane",
             description="This is the labyrinthine study of the life of a newspaper tycoon.",
             category=category3,
             user=user1)
session.add(item4)
session.commit()

item5 = Item(name="The Hangover",
             description="A blowout Las Vegas bachelor party turns into a race against time when three hung-over groomsmen awaken after a night of drunken debauchery to find that the groom has gone missing, and attempt to get him to the alter in time for his wedding. In 48 hours, Doug is scheduled to walk down the aisle, effectively ending his reign as a rowdy bachelor. Realizing that this is their last blowout with their best friend, Doug's groomsmen organize a Sin City bachelor bash he'll never forget. The next morning, the groomsmen come to in their Caesar's Palace suite to find a tiger in the bathroom and a six-month-old baby tucked away in the closet. Unfortunately, Doug is nowhere to be found. With no memory of the previous night's transgressions and precious little time to spare, the trio sets out in a hazy attempt to retrace their steps and discover exactly where things went wrong. Will they find Doug in time to get him to the wedding back in Los Angeles, or will his bride experience the sharp sting of disappointment when she walks down the aisle to discover that her future husband is nowhere to be found? Bradley Cooper, Ed Helms, Zach Galifianakis, and Heather Graham star in a rambunctious comedy from Old School director Todd Phillips. ~ Jason Buchanan, Rovi",
             category=category4,
             user=user1)
session.add(item5)
session.commit()

item6 = Item(name="Get Out",
             description="Now that Chris and his girlfriend, Rose, have reached the meet-the-parents milestone of dating, she invites him for a weekend getaway upstate with Missy and Dean. At first, Chris reads the family's overly accommodating behavior as nervous attempts to deal with their daughter's interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he could have never imagined.",
             category=category5,
             user=user1)
session.add(item6)
session.commit()

item7 = Item(name="La La Land",
             description="Written and directed by Academy Award (R) nominee Damien Chazelle, LA LA LAND tells the story of Mia [Emma Stone], an aspiring actress, and Sebastian [Ryan Gosling], a dedicated jazz musician, who are struggling to make ends meet in a city known for crushing hopes and breaking hearts. Set in modern day Los Angeles, this original musical about everyday life explores the joy and pain of pursuing your dreams.",
             category=category6,
             user=user1)
session.add(item7)
session.commit()

item8 = Item(name="Hairspray",
             description="Sixteen years after the release of the original film, New Line Cinema brings a feature film adaptation of the Tony award-winning Broadway production 'Hairspray' to life. Based on John Waters' 1988 cult classic about star-struck teenagers on a local Baltimore dance show, the comedy features new and original material.",
             category=category6,
             user=user1)
session.add(item8)
session.commit()

item9 = Item(name="Star Wars: Episode VII - The Force Awakens",
             description="The Star Wars saga continues with this seventh entry -- the first under the Walt Disney Co. umbrella. The film will act as the start of a new trilogy set after the events of Return of the Jedi. J.J. Abrams directs from a script by Michael Arndt. ~ Jeremy Wheeler, Rovi",
             category=category7,
             user=user1)
session.add(item9)
session.commit()

item10 = Item(name="Gravity",
              description="Gravity stars Sandra Bullock and George Clooney in a heart-pounding thriller that pulls you into the infinite and unforgiving realm of deep space. Bullock plays Dr. Ryan Stone, a brilliant medical engineer on her first shuttle mission, with veteran astronaut Matt Kowalsky (Clooney). But on a seemingly routine spacewalk, disaster strikes. The shuttle is destroyed, leaving Stone and Kowalsky completely alone - tethered to nothing but each other and spiraling out into the blackness. The deafening silence tells them they have lost any link to Earth and any chance for rescue. As fear turns to panic, every gulp of air eats away at what little oxygen is left. But the only way home may be to go further out into the terrifying expanse of space. -- (C) Warner Bros.",
              category=category7,
              user=user1)
session.add(item10)
session.commit()

print('added categories and items')
